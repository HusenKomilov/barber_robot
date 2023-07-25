'''CALLBACKLARNI ILADIGAN HANDLERLAR'''
import os

from telebot.types import CallbackQuery, ReplyKeyboardRemove
from data.loader import bot, db
from keyboards.default import time_barber
from keyboards.inline import check, check_barber, barber_name_inline, timer, confirm_success, confirm_break
from states.state import BarberStates
from .commands import save_chat_id, save_barber_photo


@bot.callback_query_handler(func=lambda call: "barber|" in call.data)
def barber_bron(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    barber_id = call.data.split('|')[1]
    barber_bio = db.select_barber_bio(barber_id)
    users_bio = db.check_user_date(chat_id)
    name = barber_bio[2]
    age = barber_bio[3]
    experience = barber_bio[4]
    bot.set_state(from_user_id, BarberStates.barber_card, chat_id)

    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            data['card'][users_bio[0]] = {
                'barber_name': name,
                'barber_id': barber_id,
                'barber_telegram_id': barber_bio[1],
                'users_chat_id': chat_id,
                'users_phone_number': users_bio[1]
            }

        else:
            data['card'] = {
                users_bio[0]: {
                    'barber_name': name,
                    'barber_id': barber_id,
                    'barber_telegram_id': barber_bio[1],
                    'users_chat_id': chat_id,
                    'users_phone_number': users_bio[1]
                }
            }

    text = f"🙎🏻‍♂️Ism: {name}\n" \
           f"Yosh {age}\n" \
           f"Tajriba: {experience}"
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_photo(chat_id, photo=barber_bio[-1], caption=text, reply_markup=time_barber())


@bot.callback_query_handler(func=lambda call: "day|" in call.data)
def day_call(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    visiting_day = call.data.split('|')[1]
    day_today = int(visiting_day.split('-')[0])
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['visiting_day'] = visiting_day
                bot.send_message(chat_id, "Tashrif buyurish sanasi belgilandi", reply_markup=ReplyKeyboardRemove())
                bot.send_message(chat_id, "Tashrif buyurish vaqtini belgilang", reply_markup=timer(day_today))
                bot.delete_message(chat_id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: "timer|" in call.data)
def timer_call(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    time_id = call.data.split('|')[1]
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['visiting_time'] = f"{time_id}:00"
                for j in data['card'].keys():
                    bot.delete_message(chat_id, call.message.message_id)

                    bot.send_message(chat_id, "Ma'lumolar to'g'ri bo'lsa ✅ bosing,\n"
                                              "Aks holatda ❌ bosing")
                    text = f"Sartarosh: <b>{i['barber_name']}</b>\n" \
                           f"Ismingiz: {j}\n" \
                           f"Telefoningiz: {i['users_phone_number']}\n" \
                           f"Tashrif buyurish kuni: {i['visiting_day']}\n" \
                           f"Tashrif buyurish vaqti: {i['visiting_time']}\n"
                    bot.send_message(chat_id, text, reply_markup=check())


@bot.callback_query_handler(func=lambda call: call.data == "confirmation")
def confirmation(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    bot.edit_message_reply_markup(chat_id, message_id=call.message.message_id, reply_markup=confirm_success())
    bot.send_message(chat_id,
                     "Sizning so'rovingiz Barberga yuborildi iltimos javobni kuting.",
                     reply_to_message_id=call.message.message_id)
    text = call.message.text
    msg = [chat_id, from_user_id]
    with bot.retrieve_data(from_user_id, chat_id) as data:
        for i in data['card'].values():
            barber_chat_id = int(i['barber_telegram_id'])
            a = i['users_chat_id']
            try:
                text += f"\nchat_id {a} \nuser_id {from_user_id}"
                bot.send_message(barber_chat_id, text, reply_markup=check_barber())
            except Exception as e:
                pass


@bot.callback_query_handler(func=lambda call: call.data == "cancellation")
def cancellation(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, "Tashrif vaqtini bekor qildingiz\n"
                              "Boshqa vaqtni belgilash uchun /start komandasini boshing va qaytadan boshlang")


@bot.callback_query_handler(func=lambda call: call.data == "barber_confirmation")
def barber_confirmation(call: CallbackQuery):
    a = call.message.text.split(' ')[-3::2]
    chat_id = int(a[0])
    from_user_id = int(a[1])
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                for j in data['card'].keys():
                    barber_name = i['barber_name']
                    customer_phone_number = i['users_phone_number']
                    customer_chat_id = int(i['users_chat_id'])
                    visiting_day = i['visiting_day']
                    visiting_time = i['visiting_time']
                    barber_id = i['barber_id']
                    barber_telegram_id = int(i['barber_telegram_id'])
                    customer_name = j
                    db.insert_barber_booking(customer_name, customer_phone_number, customer_chat_id, visiting_day,
                                             visiting_time, barber_id, barber_telegram_id, barber_name)
                    bot.edit_message_reply_markup(barber_telegram_id, message_id=call.message.message_id,
                                                  reply_markup=confirm_success())
                    bot.send_message(barber_telegram_id, "Tashrifni qabul qildingiz",
                                     reply_to_message_id=call.message.message_id)
                    bot.send_message(customer_chat_id, "Tashrifingiz qabul qilindi")
    bot.delete_state(from_user_id, chat_id)


@bot.callback_query_handler(func=lambda call: call.data == "barber_cancellation")
def barber_cancellation(call: CallbackQuery):
    a = call.message.text.split(' ')[-3::2]
    chat_id = int(a[0])
    from_user_id = int(a[1])
    with bot.retrieve_data(from_user_id, chat_id) as data:
        for i in data['card'].values():
            users_chat_id = int(i['users_chat_id'])
            barber_chat_id = int(i['barber_telegram_id'])
            bot.edit_message_reply_markup(barber_chat_id, message_id=call.message.message_id,
                                          reply_markup=confirm_break())
            bot.send_message(users_chat_id, "Tashrif bekor qilindi, Barber tomonidan.")
    bot.delete_state(from_user_id, chat_id)


@bot.callback_query_handler(func=lambda call: call.data == "clear")
def clear(call: CallbackQuery):
    chat_id = call.message.chat.id
    db.drop_table_barber_booking()
    bot.send_message(chat_id, "Baza tozalandi")
    db.create_barber_booking()


@bot.callback_query_handler(func=lambda call: call.data == "no_clear")
def no_clear(call: CallbackQuery):
    chat_id = call.message.chat.id
    first_name = call.message.chat.first_name
    bot.delete_message(chat_id, message_id=call.message.message_id)
    bot.send_message(chat_id, f"Assalomu alaykum <b>{first_name}</b>", reply_markup=barber_name_inline())


@bot.callback_query_handler(func=lambda call: call.data == "add_barber")
def add_barber(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    msg = bot.send_message(chat_id, "Barber chat idsini kiriting")
    bot.register_next_step_handler(msg, save_chat_id)


@bot.callback_query_handler(func=lambda call: call.data == "no_experience")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "Tajriba yo'q"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "six_month")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "6 oy"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "one_year")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "1 yil"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "one_year_plus")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "1.5 yil"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "two_year")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "2-3 yil"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "four_year")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "4-5 yil"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "six_year")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "6-7 yil"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "eight_year")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "8-9 yil"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "ten_year")
def six_mont(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    with bot.retrieve_data(from_user_id, chat_id) as data:
        if data.get('card'):
            for i in data['card'].values():
                i['barber_experience'] = "10+ yil"
            msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
            bot.register_next_step_handler(msg, save_barber_photo)


@bot.callback_query_handler(func=lambda call: call.data == "admin_confirmation")
def admin_confirmation(call: CallbackQuery):
    chat_id = call.message.chat.id
    a = call.message.caption.split(':')
    barber_chat_id = int(a[1][1:-12])
    barber_name = a[2][1:-13]
    barber_age = int(a[3][1:3])
    barber_experience = a[4]
    raw = call.message.photo[2].file_id
    name = raw + ".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)
    file = open(name, mode='rb')
    photo = file.read()
    # print(a)
    try:
        db.insert_barber_users(barber_chat_id, barber_name, barber_age, barber_experience, photo)
        file.close()
        bot.send_message(chat_id, "Ma'lumotlar saqlandi")

        os.remove(name)
    except Exception as e:
        bot.send_message(chat_id, "Ma'lumotlarda xatolik bor")

    bot.delete_state(call.message.from_user.id, chat_id)


@bot.callback_query_handler(func=lambda call: call.data == "admin_cancellation")
def admin_cancellation(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, f"Assalomu alaykum <b>{call.message.from_user.first_name}</b>",
                     reply_markup=barber_name_inline())
