'''TEXTLARNI ILADIGAN HANDLERLAR'''
from telebot.types import Message
from data.loader import bot
from keyboards.inline import bron_day


@bot.message_handler(func=lambda message: message.text == "📅 Sanani belgilash ✅")
def timer_check(message: Message):
    chat_id = message.chat.id
    bot.delete_message(chat_id, message.message_id)
    bot.send_message(chat_id, "Tashrif buyurmoqchi bo'lgan kuningiz belgilang", reply_markup=bron_day())
