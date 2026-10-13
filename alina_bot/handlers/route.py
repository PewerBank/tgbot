from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from states import StatesBot
from aiogram.fsm.context import FSMContext

router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Старт")],
            [KeyboardButton(text="О боте"), KeyboardButton(text="Помощь")]
        ],
        resize_keyboard=True
    )
    return keyboard

def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сколько дней до сессии?", callback_data="menu_days")],
            [InlineKeyboardButton(text="Рассчитать оценку", callback_data="menu_mark")]
        ]
    )
    return keyboard

"""@router.callback_query(lambda c: c.data=="info more")
async def process_more_info(callback: CallbackQuery):
    await callback.message.answer("Вот более подробная инфа")
    await callback.answer()"""

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Я - оценка-бот. \nПомогу рассчитать итоговую оценку для студентов ВШЭ НН 1 курса КНТ. \n\n"
                         "Нажми 'старт', чтобы начать работу.",
                         reply_markup=get_main_reply_keyboard())
    await state.set_state(StatesBot.wait_for_start)

@router.message(F.text.lower() == 'старт')
async def start_branch1(message: Message, state: FSMContext):
    await message.answer("Выбери действие",
                         reply_markup=main_menu())
    await state.set_state(StatesBot.main_menu)

@router.message(F.text.lower() == 'помощь')
async def help(message: Message):
    await message.answer("Помощь\nЧто я умею?\n"
                         "•Показывать, сколько дней до сессии\n"
                         "•Рассчитывать итоговую оценку\n"
                         "Нажми 'Старт', чтобы начать.",
                         reply_markup=get_main_reply_keyboard())

@router.message(F.text.lower() == 'о боте')
async def about(message: Message):
    await message.answer("Это проект группы студетов из 26-КНТ4 по ТП в 1 модуле.")

@router.callback_query(F.data == "menu_days")
async def f_menu_days(callback):
    await callback.message.answer("До сессионной недели х дней.")
    await callback.answer()

@router.callback_query(F.data == "menu_mark")
async def f_menu_mark(callback):
    await callback.message.answer("Выбери поток:")
    await callback.answer()