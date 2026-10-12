"""A bounded, persistent audit log for incoming Telegram interactions."""

import asyncio
import json
import logging
import os
import shutil
import stat
import tempfile
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Update


LOG_PATH = Path(__file__).resolve().parent.parent / "interactions.txt"
MAX_LOG_BYTES = 250 * 1024 * 1024
_CONTEXT_KEY = "_interaction_log_entry"
logger = logging.getLogger(__name__)


class InteractionLog:
    """Append JSON lines; keep the newest complete lines when the file fills up.

    One instance is shared by all updates in the bot process. Disk operations
    are serialized, including copying the retained tail during cleanup.
    """

    def __init__(self, path: Path = LOG_PATH, max_bytes: int = MAX_LOG_BYTES):
        if max_bytes <= 0:
            raise ValueError("max_bytes must be positive")
        self.path = Path(path).resolve()
        self.max_bytes = max_bytes
        self._lock = threading.Lock()
        # Check writability at startup, without truncating the existing log.
        with self.path.open("ab"):
            pass
        size = self.path.stat().st_size
        if size > self.max_bytes:
            self._replace_with_tail(size, self.max_bytes * 9 // 10)

    def append(self, record: dict) -> None:
        line = (json.dumps(record, ensure_ascii=False) + "\n").encode("utf-8")
        if len(line) > self.max_bytes:
            raise ValueError("Interaction record exceeds the log size limit")
        with self._lock:
            size = self.path.stat().st_size
            if size + len(line) > self.max_bytes:
                # Free 10% at a time so a busy bot doesn't copy 250 MiB for
                # every new interaction once the limit is reached.
                keep_bytes = max(0, self.max_bytes * 9 // 10 - len(line))
                self._replace_with_tail(size, keep_bytes, line)
            else:
                # Closing the file flushes each entry immediately.
                with self.path.open("ab") as stream:
                    stream.write(line)

    def _replace_with_tail(self, size: int, keep_bytes: int, line: bytes = b"") -> None:
        temp_path = None
        try:
            with self.path.open("rb") as source:
                offset = max(0, size - keep_bytes)
                if offset:
                    source.seek(offset - 1)
                    if source.read(1) != b"\n":
                        # Discard a partial first line, with bounded memory
                        # even if the previous file contains a very long line.
                        while fragment := source.readline(64 * 1024):
                            if fragment.endswith(b"\n"):
                                break
                with tempfile.NamedTemporaryFile(
                    mode="wb", dir=self.path.parent,
                    prefix=f".{self.path.name}.", suffix=".tmp", delete=False,
                ) as target:
                    temp_path = Path(target.name)
                    os.fchmod(target.fileno(), stat.S_IMODE(os.fstat(source.fileno()).st_mode))
                    shutil.copyfileobj(source, target, length=1024 * 1024)
                    target.write(line)
                    target.flush()
                    os.fsync(target.fileno())
            # Replacing only after the complete tail is written keeps the old
            # log intact if copying fails. The containing directory must be
            # mounted in Docker, rather than the individual log file.
            os.replace(temp_path, self.path)
        finally:
            if temp_path is not None:
                temp_path.unlink(missing_ok=True)


@dataclass
class _PendingEntry:
    record: dict
    written: bool = False


class InteractionLoggingMiddleware(BaseMiddleware):
    """Capture every incoming update, including events with no matching handler."""

    def __init__(self, log: InteractionLog):
        self.log = log

    async def write(self, entry: _PendingEntry) -> None:
        if entry.written:
            return
        entry.written = True
        try:
            # In particular, trimming a large log must not block the event loop.
            await asyncio.to_thread(self.log.append, entry.record)
        except OSError:
            # Surface disk/permission failures in stderr without disabling the
            # bot's handlers. Startup errors, however, fail fast in InteractionLog.
            logger.exception("Cannot write interaction log: %s", self.log.path)

    async def __call__(self, handler, event: Update, data):
        telegram_event = event.event
        user = data.get("event_from_user")
        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "username": user.username if user else None,
            "user_id": user.id if user else None,
            "event": event.event_type,
            "handler": "unhandled",
            "update_id": event.update_id,
        }
        text = getattr(telegram_event, "text", None)
        if text and text.startswith("/"):
            record["command"] = text.split(maxsplit=1)[0][:256]
        if event.event_type == "callback_query":
            record["callback_data"] = telegram_event.data
        entry = _PendingEntry(record)
        data[_CONTEXT_KEY] = entry
        try:
            return await handler(event, data)
        finally:
            # Inner middleware normally writes before the business handler.
            # This fallback also covers rejected/unmatched updates.
            await self.write(entry)


class HandlerLoggingMiddleware(BaseMiddleware):
    def __init__(self, update_logger: InteractionLoggingMiddleware):
        self.update_logger = update_logger

    async def __call__(self, handler, event, data):
        entry = data[_CONTEXT_KEY]
        callback = data["handler"].callback
        entry.record["handler"] = f"{callback.__module__}.{callback.__qualname__}"
        await self.update_logger.write(entry)
        return await handler(event, data)


def setup_interaction_logging(
    dispatcher: Dispatcher, log: InteractionLog = None,
) -> InteractionLog:
    if log is None:
        log = InteractionLog()
    update_logger = InteractionLoggingMiddleware(log)
    dispatcher.update.outer_middleware(update_logger)
    handler_logger = HandlerLoggingMiddleware(update_logger)
    for name, observer in dispatcher.observers.items():
        if name not in {"update", "error"}:
            observer.middleware(handler_logger)
    return log
