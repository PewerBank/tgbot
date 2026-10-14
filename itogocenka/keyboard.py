from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#from formulas import FORMULAS  # Импортируем базу данных

def get_main_reply_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Старт")],
            [KeyboardButton(text="О боте"), KeyboardButton(text="Помощь")]
        ],
        resize_keyboard=True
    )

def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сколько дней до сессии?", callback_data="menu_days")],
            [InlineKeyboardButton(text="Рассчитать оценку", callback_data="menu_mark")]
        ]
    )

def get_potoks_keyboard():
    from formulas import FORMULAS
    """Генерирует кнопки потоков автоматически из нашей БД"""
    inline_keyboard = []
    '''for potok_id, data in FORMULAS.items():
        # callback_data будет вида "potok_potok_1"
        inline_keyboard.append([InlineKeyboardButton(text=data["name"], callback_data=f"potok_{potok_id}")])'''
    
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
