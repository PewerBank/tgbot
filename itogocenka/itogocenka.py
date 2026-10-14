import logging
logging.basicConfig(level=logging.INFO)
import os 
import asyncio 
from os import getenv 
from aiogram import Bot, Dispatcher 
from dotenv import load_dotenv

from route import router as main_router 
from sessiondays import router as session_router

load_dotenv() 
TOKEN = getenv("BOT_TOKEN")

async def main(): 
    print("Start..")

    bot = Bot(token=TOKEN) 
    dp = Dispatcher()

    dp.include_routers(main_router, session_router)

    print("Роутеры подключены")
    await dp.start_polling(bot)

if __name__ == "__main__": 
    asyncio.run(main())