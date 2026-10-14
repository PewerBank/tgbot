from aiogram import Router, F
from aiogram.types import CallbackQuery
from datetime import datetime

router = Router()

def get_days_until_session() -> int:
    # Укажите точную дату начала вашей зимней сессии (Год, Месяц, День)
    session_date = datetime(2026, 12, 15) 
    today = datetime.now()
    delta = session_date - today
    return max(0, delta.days) # Если сессия прошла, вернет 0

@router.callback_query(F.data == "menu_days")
async def f_menu_days(callback: CallbackQuery):
    days = get_days_until_session()
    
    if days > 0:
        await callback.message.answer(f"⏳ До начала сессии осталось **{days}** дней. Время ботать!")
    else:
        await callback.message.answer("🎉 Сессия уже идет или успешно завершена!")
        
    await callback.answer()
