import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import Message

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(API_TOKEN)
dp = Dispatcher()


@dp.message()
async def process_message(message: Message):
    await message.answer(message.text)


async def start():
    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f'There is an exception - {_ex}')
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())

