from aiogram.dispatcher.filters.state import StatesGroup, State



class StateBot(StatesGroup):
    Gend_parser = State()
    WP_parser = State()
    Kino_inp = State()
    Kino_ans = State()