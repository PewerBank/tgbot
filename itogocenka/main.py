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
    bot = Bot(token=TOKEN) 
    dp = Dispatcher()
    dp.include_routers(main_router, session_router)

    print("Start..")
    await dp.start_polling(bot)

if name == "main": 
    asyncio.run(main())

"""import os 
import asyncio 
from dotenv import load_dotenv 
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

# Импортируем наши модули
from states import StatesBot
import keyboards as kb
import session  # Импортируем файл с сессией

load_dotenv() 
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN) 
dp = Dispatcher()

# --- ХЭНДЛЕРЫ ГЛАВНОГО МЕНЮ ---

@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(
        "Привет! Я — оценка-бот. \nПомогу рассчитать итоговую оценку для студентов ВШЭ НН 1 курса КНТ. \n\n"
        "Нажми 'Старт', чтобы начать работу.",
        reply_markup=kb.get_main_reply_keyboard()
    )
    await state.set_state(StatesBot.wait_for_start)

@dp.message(F.text.lower() == 'старт')
async def start_branch1(message: Message, state: FSMContext):
    await message.answer("Выбери действие", reply_markup=kb.main_menu())
    await state.set_state(StatesBot.main_menu)

@dp.message(F.text.lower() == 'помощь')
async def help_cmd(message: Message):
    await message.answer(
        "Помощь\nЧто я умею?\n"
        "• Показывать, сколько дней до сессии\n"
        "• Рассчитывать итоговую оценку\n"
        "Нажми 'Старт', чтобы начать.",
        reply_markup=kb.get_main_reply_keyboard()
    )

@dp.message(F.text.lower() == 'о боте')
async def about(message: Message):
    await message.answer("Это проект группы студентов из 26-КНТ4 по ТП в 1 модуле.")

@dp.callback_query(F.data == "menu_mark")
async def f_menu_mark(callback: CallbackQuery):
    # Берем клавиатуру потоков из файла keyboards.py
    await callback.message.answer("Выбери свой поток:", reply_markup=kb.get_potoks_keyboard())
    await callback.answer()

# --- ЗАПУСК ---

async def main(): 
    # ВАЖНО: Подключаем роутер из файла session.py
    dp.include_router(session.router)
    
    print("Бот успешно запущен в модульной структуре!") 
    await dp.start_polling(bot)

if __name__ == "__main__": 
    asyncio.run(main())
"""