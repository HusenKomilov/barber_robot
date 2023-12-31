'''
BOTNI ISHGA TUSHIRISH UCHUN KERAK BO'LADIGAN NARSALARNI KIRG'IZING
'''
from telebot import TeleBot
from config import TOKEN
from database.database import DataBase
from telebot import custom_filters
from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()
db = DataBase()

bot = TeleBot(TOKEN, parse_mode="html", state_storage=state_storage)

bot.add_custom_filter(custom_filter=custom_filters.StateFilter(bot))

