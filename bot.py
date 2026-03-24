import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8686110571:AAGl1Fy9Nw4-_ESpzP_dxWqHGWqOKzarS-E"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("✅ EhmedliBot işləyir! Salam!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)