from aiogram.fsm.state import State, StatesGroup

class StatesBot(StatesGroup):
    wait_for_start = State()
    main_menu = State()
    choose_stream = State()
    choose_subject = State()
    view_subject = State()
    enter_grade = State()
    wait_for_input = State()