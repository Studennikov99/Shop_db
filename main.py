import asyncio
import os
import aiogram
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from aiogram.types import BotCommand

from handlers.buy_reg import register_handlers_buy
from handlers.buyer_reg import register_handlers_buyer
from handlers.shirts_reg import register_handlers_shirts
from handlers.sneakers_reg import register_handlers_sneakers
from handlers.start_menu import register_handlers_start
from handlers.pants_reg import register_handlers_pants


from db.main import get_db

db_generator = get_db()
db_session = next(db_generator)

load_dotenv(os.getenv("TOKEN"))
TOKEN = os.environ.get("TOKEN")


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начало работы"),
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_start(dp)
    register_handlers_shirts(dp)
    register_handlers_pants(dp)
    register_handlers_sneakers(dp)
    register_handlers_buyer(dp)
    register_handlers_buy(dp)

    await set_commands(bot)
    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
