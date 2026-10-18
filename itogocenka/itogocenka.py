import sys
import os
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import logging
logging.basicConfig(level=logging.INFO)
import asyncio 
from os import getenv 
from aiogram import Bot, Dispatcher 
from dotenv import load_dotenv

from route import router as main_router 
from sessiondays import router as session_router

from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv() 
TOKEN = getenv("BOT_TOKEN")

from sessiondays import get_session_status

async def send_daily_countdown(bot):
    if not os.path.exists("users.json"):
        return
    with open("users.json", "r", encoding="utf-8") as f:
        try:
            users = json.load(f)
        except Exception:
            return
        
    text = get_session_status()
    
    for user_id, settings in users.items():
        if settings.get("notify") is True:
            try:
                from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
                kb = InlineKeyboardMarkup(inline_keyboard=[[
                    InlineKeyboardButton(text="🔕 Отключить уведомления", callback_data="disable_notify")
                ]])
                await bot.send_message(chat_id=int(user_id), text=f"⏰ Ежедневное напоминание!\n\n{text}", reply_markup=kb)
            except Exception:
                pass


async def main(): 
    print("Start..")

    bot = Bot(token=TOKEN) 
    dp = Dispatcher()
    dp.include_routers(main_router, session_router)
    print("Роутеры подключены")
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_daily_countdown, "cron", hour=9, minute=25, args=[bot])
    scheduler.start()
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__": 
    asyncio.run(main())

