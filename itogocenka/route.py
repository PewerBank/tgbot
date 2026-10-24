from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from keyboard import get_main_reply_keyboard, main_menu, menu_streams, subj_menu, parts_menu
from formulas import get_subject, get_formula, calculate_subject_score
from sessiondays import get_session_status
from states import StatesBot 
import json
import os

DB_FILE = "users.json"

def get_user_stream(user_id: int) -> str:
    if not os.path.exists(DB_FILE): return None
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try: data = json.load(f)
        except Exception: return None
    return data.get(str(user_id), {}).get("stream")

def set_user_stream(user_id: int, stream_id: str):
    data = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try: data = json.load(f)
            except Exception: data = {}
    if str(user_id) not in data: data[str(user_id)] = {}
    data[str(user_id)]["stream"] = stream_id
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

router = Router()


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

@router.callback_query(F.data == "menu_mark", StateFilter("*"))
async def f_menu_mark(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    saved_stream = get_user_stream(callback.from_user.id)
    
    if saved_stream:
        await state.update_data(stream_id=saved_stream)
        await state.set_state(StatesBot.choose_subject)
        await callback.message.edit_text(f"📚 Ваш поток: {saved_stream}. Выберите предмет:", reply_markup=subj_menu(saved_stream))
    else:
        await callback.message.edit_text("🎓 Выберите ваш поток:", reply_markup=menu_streams())
    await callback.answer()

@router.callback_query(F.data.startswith("stream_"), StateFilter("*"))
async def f_select_stream(callback: CallbackQuery, state: FSMContext):
    stream_id = callback.data.split("_")[1] # Получим "1", "2" или "3"
    set_user_stream(callback.from_user.id, stream_id) # Запоминаем в JSON
    
    await state.update_data(stream_id=stream_id)
    await state.set_state(StatesBot.choose_subject)
    await callback.message.edit_text(f"📚 Поток успешно сохранен! Выберите предмет:", reply_markup=subj_menu(stream_id))
    await callback.answer()

@router.callback_query(F.data == "reset_stream", StateFilter("*"))
async def f_reset_stream(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    set_user_stream(callback.from_user.id, None) # Удаляем из JSON
    await callback.message.edit_text("🎓 Поток сброшен. Выберите поток заново:", reply_markup=menu_streams())
    await callback.answer()    

@router.callback_query(F.data == "menu_days")
async def f_menu_days(callback: CallbackQuery):
    text_response = get_session_status()
    user_id = callback.from_user.id
    
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔔 Включить напоминания каждый день", callback_data="enable_notify")],
        [InlineKeyboardButton(text="🔕 Выключить", callback_data="disable_notify")]
    ])
    
    await callback.message.answer(text_response, reply_markup=kb)
    await callback.answer()

@router.callback_query(F.data == "enable_notify")
async def f_enable_notify(callback: CallbackQuery):
    await callback.message.answer("🔔 Вы подписались на ежедневный отсчет до сессии! Бот будет писать вам в 9:25.")
    await callback.answer()

@router.callback_query(F.data == "disable_notify")
async def f_disable_notify(callback: CallbackQuery):
    # вызываем функцию из db.py и ставим False
    await callback.message.answer("🔕 Ежедневные уведомления отключены.")
    await callback.answer()


@router.callback_query(F.data.startswith("stream_"), StatesBot.choose_stream)
async def f_stream_chosen(callback: CallbackQuery, state: FSMContext):
    id_stream = callback.data.split("_")[1]
    if id_stream=="1":
        stream_name = "I поток"
    elif id_stream=="2":
        stream_name = "II поток"
    elif id_stream=="3":
        stream_name = "III поток"
    await state.update_data(stream_id=id_stream)

    await callback.message.answer(
        f"Поток: {stream_name}\n\nВыбери предмет:", reply_markup=subj_menu(id_stream)
    )
    await state.set_state(StatesBot.choose_subject)
    await callback.answer()


@router.callback_query(F.data.startswith("subj_"), StateFilter("*"))
async def f_subj_chosen(callback: CallbackQuery, state: FSMContext):
    konkretnoe_name = callback.data.replace("subj_", "")
    
    data = await state.get_data()
    stream_id = data.get("stream_id")
    if not stream_id:
        stream_id = get_user_stream(callback.from_user.id)

    formulka = get_formula(stream_id, konkretnoe_name)
    
    await state.update_data(
        stream_id=stream_id,
        subject=konkretnoe_name,
        components=formulka.get("components", []),
        formula=formulka.get("formula", ""),
        grades={}
    )
    
    await state.set_state(StatesBot.view_subject)
    await subj_card(callback.message, state)
    await callback.answer()


async def subj_card(message: Message, state: FSMContext):
    data = await state.get_data()
    subj = data["subject"]
    formula = data["formula"]
    parts = data["components"]
    grades = data.get("grades", {})

    l = []
    for p in parts:
        name = p["name"]
        if name in grades:
            l.append(f"✅ {name}: {grades[name]}")
        else:
            l.append(f"⏳ {name}: —")

    text = f"📚 {subj}\n🧮 Формула: {formula}\n━━━━━━━━━━\n"
    for line in l:
        text += line + "\n"
    text += '━━━━━━━━━━'

    try:
        await message.edit_text(text=text, reply_markup=parts_menu(parts, grades))
    except Exception:
        await message.answer(text=text, reply_markup=parts_menu(parts, grades))


@router.callback_query(F.data.startswith("fill_"), StatesBot.view_subject)
async def f_fill(callback: CallbackQuery, state: FSMContext):
    # Используем безопасное удаление префикса
    name = callback.data.replace("fill_", "") 
    await state.update_data(filling=name)
    
    await callback.message.answer(
        f"Введи {name}.\n"
        f"📝 Если вводишь накопленную оценку, то вводи все полученные оценки через пробел.\n"
        f"🎯 Пример ввода: 7 8 9"
    )
    await state.set_state(StatesBot.enter_grade)
    await callback.answer()


@router.message(StatesBot.enter_grade)
async def f_grade(message: Message, state: FSMContext):
    data = await state.get_data()
    filling = data["filling"]
    components = data["components"]
    
    comp = None
    for c in components:
        if c["name"] == filling:
            comp = c
            break
            
    if not comp:
        await message.answer("❌ Компонент не найден. Вернитесь к выбору предмета.")
        await state.set_state(StatesBot.view_subject)
        return

    text = message.text.strip()
    value = 0.0
    if comp["type"] == "grade":
        try:
            value = float(text.replace(",", "."))
        except ValueError:
            await message.answer("⚠️ Введи число от 0 до 10")
            return
            
        if not (0 <= value <= 10):
            await message.answer("⚠️ Оценка должна быть от 0 до 10")
            return

    elif comp["type"] == "list":
        input_grades = text.replace(",", " ").split()
        if not input_grades:
            await message.answer("⚠️ Введи хотя бы одну оценку")
            return
            
        try:
            numbers = [float(p) for p in input_grades]
        except ValueError:
            await message.answer("⚠️ Введи числа через пробел. Например: 7 8 9")
            return
            
        for n in numbers:
            if not (0 <= n <= 10):
                await message.answer("⚠️ Все оценки должны быть от 0 до 10")
                return
        value = sum(numbers) / len(numbers)

    await message.answer(f"✅ {filling} = {value:.2f}")
    
    grades = data.get("grades", {})
    grades[filling] = value
    await state.update_data(grades=grades)
    
    await state.set_state(StatesBot.view_subject)
    await subj_card(message, state)


@router.callback_query(F.data == "calculate_final_score", StateFilter("*"))
async def process_final_calculation(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    subj = data.get("subject", "Предмет")
    formula = data.get("formula", "")
    grades = data.get("grades", {})
    
    final_grade = calculate_subject_score(formula, grades)
    
    if final_grade >= 7.5:
        rec = "🎉 Отличный результат! Вы идете на Отлично (8-10 баллов)."
    elif final_grade >= 5.5:
        rec = "👍 Хороший средний балл (6-7 баллов). Можно поднажать до отличной!"
    elif final_grade >= 3.5:
        rec = "⚠️ Вы близки к порогу (4-5 баллов). Будьте аккуратнее на экзаменах."
    else:
        rec = "🚨 Прогноз неудовлетворительный (меньше 4). Срочно закрывайте долги!"

    subj_lower = subj.lower()
    if final_grade >= 8.0 and ("орг" in subj_lower or "истори" in subj_lower):
        rec = "🎉 Отличный результат! Если хочешь получить 9-10 баллов, тебе стоит обратиться к преподавателю и попросить дополнительное задание."

    response_text = (
        f"📊 **Итоговый расчет по предмету {subj}**\n"
        f"📝 Применяемая формула: `{formula}`\n\n"
        f"📈 **Ваш прогнозируемый итоговый балл: {final_grade}**\n\n"
        f"ℹ️ *Рекомендация:* {rec}"
    )
    
    await callback.message.answer(response_text, parse_mode="Markdown")
    await callback.answer()
    await state.clear()


@router.callback_query(F.data.startswith("fill_"), StateFilter("*"))
async def f_fill_component(callback: CallbackQuery, state: FSMContext):
    component_name = callback.data.replace("fill_", "")

    await state.update_data(current_component=component_name)
    await state.set_state(StatesBot.wait_for_input)
    
    await callback.message.answer(f"📥 Введи {component_name}:")
    await callback.answer()


@router.message(StatesBot.wait_for_input)
async def f_save_component_grade(message: Message, state: FSMContext):
    try:
        grade_val = float(message.text.replace(",", "."))
    except ValueError:
        await message.answer("❌ Ошибка! Введите оценку числом (например: `8` или `7.5`). Попробуйте еще раз:")
        return

    data = await state.get_data()
    grades = data.get("grades", {})
    component_name = data.get("current_component")

    grades[component_name] = grade_val
    await state.update_data(grades=grades)
    await state.set_state(StatesBot.view_subject)
    await subj_card(message, state)