import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, Message

from app import database as db
from router import r


class UserLoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            user = event.from_user
            logging.info(f"User login: {user.username} (ID: {user.id})")
        return await handler(event, data)


logging.basicConfig(
    format="%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])", datefmt="%d/%m/%Y %I:%M:%S %p",
    level=logging.INFO,
    filename="bot_logs.log",
    filemode="w",
)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(r)
dp.message.middleware(UserLoggingMiddleware())


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
    await dp.start_polling(bot, on_shutdown=on_shutdown)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.info("Bot launched")
    asyncio.run(main())
    logging.info("Bot shut down")
