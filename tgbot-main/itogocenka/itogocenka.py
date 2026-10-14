import os 
import asyncio 
from dotenv import load_dotenv 
from aiogram import Bot, Dispatcher, types 
from aiogram.filters import CommandStart, Command

load_dotenv() 
TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=TOKEN) 
dp = Dispatcher()

@dp.message(CommandStart()) 
async def cmd_start(message: types.Message): 
    await message.answer(
         f"Привет, {message.from_user.full_name}! 👋\n"
          "Я бот-помощник для студентов.\n"
          "Скоро я научусь считать твои оценки, а пока ты можешь проверить команду /help" 
    )


@dp.message(Command("help")) 
async def cmd_help(message: types.Message): 
    await message.answer("В будущем здесь будет меню выбора предметов и расчет сессии! 🚀")


async def main(): 
    print("Бот успешно запущен и слушает команды...") 
    await dp.start_polling(bot)

if __name__ == "__main__": 
    asyncio.run(main())