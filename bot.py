python
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = "8686110571:AAGl1Fy9Nw4-_ESpzP_dxWqHGWqOKzarS-E"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("✅ EhmedliBot işləyir! Salam!")

@dp.message(Command("phone"))
async def phone(message: Message):
    await message.answer("📞 Telefon axtarışı test üçün hazırdır")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())