import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from app import database as db
from app.interaction_logging import setup_interaction_logging
from router import r


logging.basicConfig(
    format="%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])", datefmt="%d/%m/%Y %I:%M:%S %p",
    level=logging.INFO,
    stream=sys.stdout,
)
bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(r)
interaction_log = setup_interaction_logging(dp)
logging.info("Interaction log: %s", interaction_log.path)


"""async def on_startup() -> None:
    await db.db_start()
    logging.info("Database started")"""


async def on_shutdown() -> None:
    await bot.session.close()
    #await script.bot.session.close()
    logging.info("Bot session closed")


async def set_bot_commands() -> None:
    commands = [
        BotCommand(command="start", description="Start creating your DnD character's form"),
    ]
    await bot.set_my_commands(commands)


async def main() -> None:
    #dp.startup.register(on_startup)
    await set_bot_commands()
    # Middleware alone does not add event types to aiogram's automatic
    # subscription. Receive all supported types so unmatched events are logged.
    allowed_updates = [name for name in dp.observers if name not in {"update", "error"}]
    await dp.start_polling(bot, on_shutdown=on_shutdown, allowed_updates=allowed_updates)


if __name__ == "__main__":
    logging.info("Bot launched")
    asyncio.run(main())
    logging.info("Bot shut down")
