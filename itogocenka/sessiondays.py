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
        "start": datetime(2026, 12, 21).date(),
        "end": datetime(2026, 12, 30).date(),
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

SEMESTER_2_START = datetime(2027, 1, 1).date()

def get_current_semester() -> int:
    today = datetime.now().date()
    if today >= SEMESTER_2_START:
        return 2
    return 1

def get_session_status() -> str:
    today = datetime.now().date()
    
    for name, dates in SESSIONS.items():
        if dates["start"] <= today <= dates["end"]:
            days_left = (dates["end"] - today).days
            return f"Сейчас идёт {name}!**\nДо её окончания осталось дней: {days_left}."

    upcoming_sessions = []
    for name, dates in SESSIONS.items():
        if dates["start"] > today:
            upcoming_sessions.append((name, dates["start"]))

    if upcoming_sessions:
        upcoming_sessions.sort(key=lambda x: x[1])
        next_session_name, next_session_start = upcoming_sessions[0]
        days_delta = (next_session_start - today).days
        if days_delta > 1:
            return f"📅 До начала следующей ({next_session_name}) осталось дней: {days_delta}."
        if days_delta == 1:
            return f"Остался один день до сессии. Удачи на экзаменах!"
    
    return "🎉 Все сессии в этом учебном году успешно завершены!"
