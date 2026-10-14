from aiogram.fsm.state import State, StatesGroup

class StatesBot(StatesGroup):
    wait_for_start = State()
    main_menu = State()