from telebot.handler_backends import State, StatesGroup


class BarberStates(StatesGroup):
    barber_card = State()


class BarberSaveStates(StatesGroup):
    save_barber = State()
