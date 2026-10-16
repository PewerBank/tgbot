from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from sessiondays import get_session_status
from states import StatesBot
from aiogram.fsm.context import FSMContext

router = Router()

from keyboard import get_main_reply_keyboard, main_menu


def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сколько дней до сессии?", callback_data="menu_days")],
            [InlineKeyboardButton(text="Рассчитать оценку", callback_data="menu_mark")]
        ]
    )
    return keyboard

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Я - оценка-бот. \nПомогу рассчитать итоговую оценку для студентов ВШЭ НН 1 курса КНТ. \n\n"
                         "Нажми 'старт', чтобы начать работу.",
                         reply_markup=get_main_reply_keyboard())
    await state.set_state(StatesBot.wait_for_start)

@router.message(F.text.lower() == 'старт', StatesBot.wait_for_start)
async def start_branch1(message: Message, state: FSMContext): 
    await message.answer("Выбери действие:", reply_markup=main_menu()) 
    await state.set_state(StatesBot.main_menu)

@router.message(F.text.lower() == 'помощь', StateFilter("*"))
async def help(message: Message):
    await message.answer("Помощь\nЧто я умею?\n"
                         "•Показывать, сколько дней до сессии\n"
                         "•Рассчитывать итоговую оценку\n"
                         "Нажми 'Старт', чтобы начать.",
                         reply_markup=get_main_reply_keyboard())

@router.message(F.text.lower() == 'о боте', StateFilter("*"))
async def about(message: Message):
    await message.answer("Это проект группы студетов из 26КНТ-4 по Технологиям Программирования в 1 модуле.")

   
# Не забудьте импортировать get_potoks_keyboard из файла с клавиатурами в самом верху route.py
from keyboard import get_potoks_keyboard 
@router.callback_query(F.data == "menu_days")
async def f_menu_days(callback: CallbackQuery):
    # Эта функция берёт текст из sessiondays.py и кладёт его в переменную
    text_response = get_session_status()
    
    # Бот отправляет пользователю этот готовый текст
    await callback.message.answer(text_response)
    await callback.answer()


@router.callback_query(F.data == "menu_mark")
async def f_menu_mark(callback):
    await callback.message.answer("Выбери поток:")
    await callback.answer()