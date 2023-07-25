'''
BOTNI ISHGA TUSHIRISH
'''
from middlewares import SimpleMiddleware
from data.loader import bot, db
from telebot.types import BotCommand
import handlers


# bot.remove_webhook()

# bot.setup_middleware(SimpleMiddleware(1))  # bu botga qayta qayta yozmaslik uchun limit(sekundda) kiritiladi

bot.set_my_commands(
    commands=[
        BotCommand('/start', "Bu botnni qayta ishga tushirish uchun"),
        BotCommand('/count', "Hisobot olish uchun"),
        BotCommand('/maps', "Manzilni aniqlash uchun")
    ]
)

if __name__ == '__main__':
    db.create_user_table()
    db.create_barber_users()
    # db.()
    db.create_barber_booking()
    bot.polling(none_stop=True)
