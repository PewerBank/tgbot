from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()
import datetime
from datetime import datetime

SESSIONS = {
    "осенняя сессия": {
        "start": datetime(2026, 10, 26).date(),
        "end": datetime(2026, 10, 31).date(),
    },
    "зимняя сессия": {
        "start": datetime(2026, 1, 21).date(),
        "end": datetime(2026, 1, 30).date(),
    },
    "весенняя модульная сессия": {
        "start": datetime(2027, 3, 25).date(),
        "end": datetime(2027, 3, 31).date(),
    },
    "летняя сессия": {
        "start": datetime(2027, 6, 21).date(),
        "end": datetime(2027, 6, 30).date(),
    }
}

# Дата автоматической смены формул оценки
SEMESTER_2_START = datetime(2027, 1, 1).date()

def get_current_semester() -> int:
    """Автоматически определяет текущий семестр на основе даты"""
    today = datetime.now().date()
    if today >= SEMESTER_2_START:
        return 2
    return 1

def get_session_status() -> str:
    """
    Проверяет статус сессий: пишет, если сессия идет сейчас,
    или считает дни до начала ближайшей будущей сессии.
    """
    today = datetime.now().date()
    
    # 1. Сначала проверяем, идет ли какая-то сессия прямо сейчас
    for name, dates in SESSIONS.items():
        if dates["start"] <= today <= dates["end"]:
            days_left = (dates["end"] - today).days
            return f"Сейчас идёт {name}!**\nДо её окончания осталось дней: {days_left}."

    # 2. Если ни одна сессия не идет, ищем самую ближайшую будущую
    upcoming_sessions = []
    for name, dates in SESSIONS.items():
        if dates["start"] > today:
            upcoming_sessions.append((name, dates["start"]))
            
    # Сортируем будущие сессии по дате начала, чтобы найти самую первую
    if upcoming_sessions:
        upcoming_sessions.sort(key=lambda x: x[1])
        next_session_name, next_session_start = upcoming_sessions[0]
        days_delta = (next_session_start - today).days
        if days_delta > 1:
            return f"📅 До начала следующей ({next_session_name}) осталось дней: {days_delta}."
        if days_delta == 1:
            return f"Остался один день до сессии. Удачи на экзаменах!"
    
    
    # Если все сессии из словаря на этот учебный год уже завершились
    return "🎉 Все сессии в этом учебном году успешно завершены!"
