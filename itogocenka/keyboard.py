from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from formulas import FORMULAS, get_subject

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

def menu_streams():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="I поток", callback_data="stream_1")],
            [InlineKeyboardButton(text="II поток", callback_data="stream_2")],
            [InlineKeyboardButton(text="III поток", callback_data="stream_3")]
        ]
    )
    return keyboard

def subj_menu(stream_id):
    subj = get_subject(stream_id)
    butt = []
    # Передаем САМО название предмета текстом
    for i in subj:
        butt.append([InlineKeyboardButton(text=i, callback_data=f'subj_{i}')])
        
    # Добавляем кнопку сброса сохраненного потока
    butt.append([InlineKeyboardButton(text="🔄 Сбросить выбранный поток", callback_data="reset_stream")])
    return InlineKeyboardMarkup(inline_keyboard=butt)

def parts_menu(parts, full):
    buttons = []
    all_filled = True
    
    for p in parts:
        chastichka = p["name"]
        if chastichka in full:
            buttons.append([InlineKeyboardButton(
                text=f"✅ {chastichka} = {full[chastichka]}",
                callback_data=f"fill_{chastichka}" # Разрешаем перезаписать оценку при клике
            )])
        else:
            all_filled = False
            buttons.append([InlineKeyboardButton(
                text=f"➕ {chastichka}",
                callback_data=f"fill_{chastichka}"
            )])
            
    # Если заполнено абсолютно всё, показываем заветную кнопку подсчета
    if all_filled and len(parts) > 0:
        buttons.append([InlineKeyboardButton(
            text="🧮 Посчитать итоговую оценку",
            callback_data="calculate_final_score"
        )])
        
    return InlineKeyboardMarkup(inline_keyboard=buttons)
