"""Telegram bot entry point scaffold. Set BOT_TOKEN before running."""
import asyncio, os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://your-webapp.example")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⚔ Open Animeverse", web_app=WebAppInfo(url=WEBAPP_URL))]])
    await message.answer("✦ <b>Welcome to ANIMEVERSE</b>\n\nThe rift is calling, Walker. Open the game to summon characters, build your formation and enter the arena.", reply_markup=keyboard, parse_mode="HTML")

async def main():
    if not TOKEN:
        raise RuntimeError("Set BOT_TOKEN in your environment")
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
