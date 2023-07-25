'''KOMANDALARNI ILADIGAN HANDLERLAR'''
import os

from telebot.types import Message, ReplyKeyboardRemove
from data.loader import bot, db
from keyboards.default import send_contact
from keyboards.inline import barber_name_inline, clear_db, check_admin, barber_experience, bron_day
from states.state import BarberSaveStates
import pandas as pd
import xlsxwriter


@bot.message_handler(commands=['start'], chat_types='private')
def start(message: Message):
    chat_id = message.chat.id
    db.insert_user_telegram_id(chat_id)
    first_name = message.from_user.first_name
    check = db.check_user_date(chat_id)
    if None in check:
        bot.send_message(chat_id,
                         f"Assalomu alaykum <b>{first_name}</b>\n Siz botdan to'liq foydalanish uchun ro'yxatdan o'tishingiz kerak")
        msg = bot.send_message(chat_id, "To'liq ism familiyangizni kiriting: ")
        bot.register_next_step_handler(msg, save_name)
    else:
        bot.send_message(chat_id, f"Assalomu alaykum <b>{first_name}</b>", reply_markup=barber_name_inline())
        bot.send_location(chat_id, latitude=41.33268927764987, longitude=69.26393800002455)


data = {}


def save_name(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    full_name = message.text.title()
    data[from_user_id] = {"full_name": full_name}
    msg = bot.send_message(chat_id, "Telfon raqamingizni kiriting: ", reply_markup=send_contact())
    bot.register_next_step_handler(msg, save_phone)


def save_phone(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    phone_number = message.contact.phone_number

    data[from_user_id]['contact'] = phone_number
    full_name = data[from_user_id]['full_name']
    db.update_user_save(full_name=full_name, phone_number=phone_number, chat_id=chat_id)
    bot.send_message(chat_id, "Tabriklayman siz to'yxatdan o'ttingiz.", reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, "Sartaroshlardan birini tanlang", reply_markup=barber_name_inline())


def only_for_barber(chat_id):
    a = db.only_for_barber(chat_id)
    c = []
    for i in a:
        c.append({
            'customer_name': i[0],
            'customer_phone_number': i[1],
            'customer_telegram_id': i[2],
            'visiting_day': i[4],
            'visiting_time': i[5],
            'barber_name': i[3]
        })

    return c


def only_for_admin():
    a = db.only_for_admin()
    c = []
    for i in a:
        c.append({
            'customer_name': i[0],
            'customer_phone_number': i[1],
            'customer_telegram_id': i[2],
            'visiting_day': i[4],
            'visiting_time': i[5],
            'barber_name': i[3]
        })
    return c


@bot.message_handler(commands=['count'])
def count_barber(message: Message):
    chat_id = str(message.chat.id)
    if message.from_user.username in ["husenkomilov", "@navruz_web"]:
        if message.from_user.username == "husenkomilov":
            a = only_for_admin()
            workbook = xlsxwriter.Workbook('barber_bot.xlsx')
            worksheet = workbook.add_worksheet('firstShett')
            worksheet.write(0, 0, "#")
            worksheet.write(0, 1, "Mijoz ismi")
            worksheet.write(0, 2, "Mijoz Telefon raqami")
            worksheet.write(0, 3, "Mijoz chat id")
            worksheet.write(0, 4, "Tashrif sanasi")
            worksheet.write(0, 5, "Tashrif vaqti")
            worksheet.write(0, 6, "Barber ismi")
            for index, entry in enumerate(a):
                worksheet.write(index + 1, 0, str(index))
                worksheet.write(index + 1, 1, entry['customer_name'])
                worksheet.write(index + 1, 2, entry['customer_phone_number'])
                worksheet.write(index + 1, 3, entry['customer_telegram_id'])
                worksheet.write(index + 1, 4, entry['visiting_day'])
                worksheet.write(index + 1, 5, entry['visiting_time'])
                worksheet.write(index + 1, 6, entry['barber_name'])
            workbook.close()
            import os.path

            file1 = 'barber_bot.xlsx'
            path = "D:\\python_ls\\All_project\\TelegramBot\\barberBot\\barber_bot.xlsx"
            with open(path, mode='rb') as data:
                file = data.read()

            bot.send_document(chat_id, file, visible_file_name=path)
            bot.send_message(chat_id, "Bazani tozalashni xolaysizmi?", reply_markup=clear_db())
        else:
            a = only_for_barber(chat_id)
            workbook = xlsxwriter.Workbook('barber_bot.xlsx')
            worksheet = workbook.add_worksheet('firstShett')
            worksheet.write(0, 0, "#")
            worksheet.write(0, 1, "Mijoz ismi")
            worksheet.write(0, 2, "Mijoz Telefon raqami")
            worksheet.write(0, 3, "Mijoz chat id")
            worksheet.write(0, 4, "Tashrif sanasi")
            worksheet.write(0, 5, "Tashrif vaqti")
            worksheet.write(0, 6, "Barber ismi")
            for index, entry in enumerate(a):
                worksheet.write(index + 1, 0, str(index))
                worksheet.write(index + 1, 1, entry['customer_name'])
                worksheet.write(index + 1, 2, entry['customer_phone_number'])
                worksheet.write(index + 1, 3, entry['customer_telegram_id'])
                worksheet.write(index + 1, 4, entry['visiting_day'])
                worksheet.write(index + 1, 5, entry['visiting_time'])
                worksheet.write(index + 1, 6, entry['barber_name'])
            workbook.close()
            import os.path
            path = "D:\\python_ls\\All_project\\TelegramBot\\barberBot\\barber_bot.xlsx"
            with open(path, mode='rb') as data:
                file = data.read()

            bot.send_document(chat_id, file, visible_file_name=path)
            bot.send_message(chat_id)

    else:
        bot.send_message(chat_id, "Kechirasi siz bot admini emassiz shunig uchun ushbu bo'limga kira olmaysiz")


# date = {}


def save_chat_id(message: Message):
    barber_chat_id = message.text
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    bot.set_state(from_user_id, BarberSaveStates.save_barber, chat_id)

    with bot.retrieve_data(from_user_id, chat_id) as date:
        if date.get('card'):
            date['card'][from_user_id] = {
                'barber_chat_id': barber_chat_id
            }
        else:
            date['card'] = {
                from_user_id: {
                    'barber_chat_id': barber_chat_id
                }
            }
        msg = bot.send_message(chat_id, "Barber ismini kiriting: ")
        bot.register_next_step_handler(msg, save_barber_name)


def save_barber_name(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    barber_name = message.text.title()
    with bot.retrieve_data(from_user_id, chat_id) as date:
        if date.get('card'):
            for i in date['card'].values():
                i['barber_name'] = barber_name
        msg = bot.send_message(chat_id, "Barber yoshini kiriting: ")
        bot.register_next_step_handler(msg, save_barber_age)


def save_barber_age(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    barber_age = message.text
    with bot.retrieve_data(from_user_id, chat_id) as date:
        if date.get('card'):
            for i in date['card'].values():
                i['barber_age'] = barber_age
        bot.send_message(chat_id, "Barber Tajribasini kiriting: ", reply_markup=barber_experience())


def save_barber_experience(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    barber_experience = message.text
    with bot.retrieve_data(from_user_id, chat_id) as date:
        if date.get('card'):
            for i in date['card'].values():
                i['barber_experience'] = barber_experience
        msg = bot.send_message(chat_id, "Barber rasmini kiriting: ")
        bot.register_next_step_handler(msg, save_barber_photo)


def save_barber_photo(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    if message.content_type == 'photo':
        bot.send_message(chat_id, "Rasm qabul qilindi")
        raw = message.photo[2].file_id
        name = raw + ".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name, 'wb') as new_file:
            new_file.write(downloaded_file)
        with bot.retrieve_data(from_user_id, chat_id) as date:
            if date.get('card'):
                for i in date['card'].values():
                    barber_chat_id = i['barber_chat_id']
                    barber_name = i['barber_name']
                    barber_age = i['barber_age']
                    barber_experience = i['barber_experience']
                text = f"Barber chatID: {barber_chat_id}\n" \
                       f"Barber ismi: {barber_name}\n " \
                       f"Barber yoshi: {barber_age}\n " \
                       f"Barber tajribasi: {barber_experience}"
                file = open(name, mode='rb')
                photo = file.read()
                bot.send_photo(chat_id, photo=photo, caption=text, reply_markup=check_admin())
                file.close()
            os.remove(name)


@bot.message_handler(commands=['maps'])
def maps(message: Message):
    chat_id = message.chat.id
    bot.send_location(chat_id, latitude=41.33268927764987, longitude=69.26393800002455)
