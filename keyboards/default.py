'''
SIZ BU YERDA ODDIY KNOPKALAR YARATA OLASIZ
'''

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import datetime as dt


def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    contact = KeyboardButton("Kontactni ulashish", request_contact=True)

    markup.add(contact)
    return markup


def time_barber():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    time = KeyboardButton("📅 Sanani belgilash ✅")
    return markup.add(time)
