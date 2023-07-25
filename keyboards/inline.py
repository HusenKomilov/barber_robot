'''
SIZ BU YERDA INLINE KNOPKALAR YARATA OLASIZ
'''
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.loader import db
import datetime
import calendar
import pandas as pd


def barber_name_inline():
    markup = InlineKeyboardMarkup(row_width=1)

    user_name = db.select_barber_users_name()
    for i in user_name:
        markup.add(InlineKeyboardButton(f"{i[0]}", callback_data=f"barber|{i[1]}"))
    return markup


def bron_day():
    markup = InlineKeyboardMarkup(row_width=2)
    import datetime as dt

    x = dt.datetime.now()

    year = int(x.strftime('%Y'))
    month = int(x.strftime('%m'))
    day = int(x.strftime('%d'))
    month_name = x.strftime('%B')
    b = calendar.Calendar().monthdayscalendar(year, month)

    oylar = [1, 3, 5, 7, 8, 10, 12]  # 31 kun
    if month in oylar:
        for j in b:
            for i in j:
                if i >= day:
                    d = pd.Timestamp(f'{year}-{month}-{i}')
                    day_name = d.day_name()
                    if i < day + 7:
                        if day_name == "Monday":
                            if month_name == "Junuary":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Yanvar Dushanba", callback_data=f"day|{i}-Yanvar"))
                            elif month_name == "March":
                                markup.add(InlineKeyboardButton(f"{i}-Mart Dushanba", callback_data=f"day|{i}-Mart"))
                            elif month_name == "May":
                                markup.add(InlineKeyboardButton(f"{i}-May Dushanba", callback_data=f"day|{i}-May"))
                            elif month_name == "July":
                                markup.add(InlineKeyboardButton(f"{i}-Iyul Dushanba", callback_data=f"day|{i}-Iyul"))
                            elif month_name == "August":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Avgust Dushanba", callback_data=f"day|{i}-Avgust"))
                            elif month_name == "October":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Oktabr Dushanba", callback_data=f"day|{i}-Oktabr"))
                            elif month_name == "December":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Dekaber Dushanba", callback_data=f"day|{i}-Dekaber"))
                        elif day_name == "Tuesday":
                            if month_name == "Junuary":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Yanvar Seshanba", callback_data=f"day|{i}-Yanvar"))
                            elif month_name == "March":
                                markup.add(InlineKeyboardButton(f"{i}-Mart Seshanba", callback_data=f"day|{i}-Mart"))
                            elif month_name == "May":
                                markup.add(InlineKeyboardButton(f"{i}-May Seshanba", callback_data=f"day|{i}-May"))
                            elif month_name == "July":
                                markup.add(InlineKeyboardButton(f"{i}-Iyul Seshanba", callback_data=f"day|{i}-Iyul"))
                            elif month_name == "August":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Avgust Seshanba", callback_data=f"day|{i}-Avgust"))
                            elif month_name == "October":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Oktabr Seshanba", callback_data=f"day|{i}-Oktabr"))
                            elif month_name == "December":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Dekaber Seshanba", callback_data=f"day|{i}-Dekaber"))
                        elif day_name == "Wednesday":
                            if month_name == "Junuary":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Yanvar Chorshanba", callback_data=f"day|{i}-Yanvar"))
                            elif month_name == "March":
                                markup.add(InlineKeyboardButton(f"{i}-Mart Chorshanba", callback_data=f"day|{i}-Mart"))
                            elif month_name == "May":
                                markup.add(InlineKeyboardButton(f"{i}-May Chorshanba", callback_data=f"day|{i}-May"))
                            elif month_name == "July":
                                markup.add(InlineKeyboardButton(f"{i}-Iyul Chorshanba", callback_data=f"day|{i}-Iyul"))
                            elif month_name == "August":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Avgust Chorshanba", callback_data=f"day|{i}-Avgust"))
                            elif month_name == "October":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Oktabr Chorshanba", callback_data=f"day|{i}-Oktabr"))
                            elif month_name == "December":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Dekaber Chorshanba", callback_data=f"day|{i}-Dekaber"))
                        elif day_name == "Thursday":
                            if month_name == "Junuary":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Yanvar Payshanba", callback_data=f"day|{i}-Yanvar"))
                            elif month_name == "March":
                                markup.add(InlineKeyboardButton(f"{i}-Mart Payshanba", callback_data=f"day|{i}-Mart"))
                            elif month_name == "May":
                                markup.add(InlineKeyboardButton(f"{i}-May Payshanba", callback_data=f"day|{i}-May"))
                            elif month_name == "July":
                                markup.add(InlineKeyboardButton(f"{i}-Iyul Payshanba", callback_data=f"day|{i}-Iyul"))
                            elif month_name == "August":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Avgust Payshanba", callback_data=f"day|{i}-Avgust"))
                            elif month_name == "October":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Oktabr Payshanba", callback_data=f"day|{i}-Oktabr"))
                            elif month_name == "December":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Dekaber Payshanba", callback_data=f"day|{i}-Dekaber"))
                        elif day_name == "Friday":
                            if month_name == "Junuary":
                                markup.add(InlineKeyboardButton(f"{i}-Yanvar Juma", callback_data=f"day|{i}-Yanvar"))
                            elif month_name == "March":
                                markup.add(InlineKeyboardButton(f"{i}-Mart Juma", callback_data=f"day|{i}-Mart"))
                            elif month_name == "May":
                                markup.add(InlineKeyboardButton(f"{i}-May Juma", callback_data=f"day|{i}-May"))
                            elif month_name == "July":
                                markup.add(InlineKeyboardButton(f"{i}-Iyul Juma", callback_data=f"day|{i}-Iyul"))
                            elif month_name == "August":
                                markup.add(InlineKeyboardButton(f"{i}-Avgust Juma", callback_data=f"day|{i}-Avgust"))
                            elif month_name == "October":
                                markup.add(InlineKeyboardButton(f"{i}-Oktabr Juma", callback_data=f"day|{i}-Oktabr"))
                            elif month_name == "December":
                                markup.add(InlineKeyboardButton(f"{i}-Dekaber Juma", callback_data=f"day|{i}-Dekaber"))
                        elif day_name == "Saturday":
                            if month_name == "Junuary":
                                markup.add(InlineKeyboardButton(f"{i}-Yanvar Shanba", callback_data=f"day|{i}-Yanvar"))
                            elif month_name == "March":
                                markup.add(InlineKeyboardButton(f"{i}-Mart Shanba", callback_data=f"day|{i}-Mart"))
                            elif month_name == "May":
                                markup.add(InlineKeyboardButton(f"{i}-May Shanba", callback_data=f"day|{i}-May"))
                            elif month_name == "July":
                                markup.add(InlineKeyboardButton(f"{i}-Iyul Shanba", callback_data=f"day|{i}-Iyul"))
                            elif month_name == "August":
                                markup.add(InlineKeyboardButton(f"{i}-Avgust Shanba", callback_data=f"day|{i}-Avgust"))
                            elif month_name == "October":
                                markup.add(InlineKeyboardButton(f"{i}-Oktabr Shanba", callback_data=f"day|{i}-Oktabr"))
                            elif month_name == "December":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Dekaber Shanba", callback_data=f"day|{i}-Dekaber"))
                        elif day_name == "Sunday":
                            if month_name == "Junuary":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Yanvar Yakshanba", callback_data=f"day|{i}-Yanvar"))
                            elif month_name == "March":
                                markup.add(InlineKeyboardButton(f"{i}-Mart Yakshanba", callback_data=f"day|{i}-Mart"))
                            elif month_name == "May":
                                markup.add(InlineKeyboardButton(f"{i}-May Yakshanba", callback_data=f"day|{i}-May"))
                            elif month_name == "July":
                                markup.add(InlineKeyboardButton(f"{i}-Iyul Yakshanba", callback_data=f"day|{i}-Iyul"))
                            elif month_name == "August":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Avgust Yakshanba", callback_data=f"day|{i}-Avgust"))
                            elif month_name == "October":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Oktabr Yakshanba", callback_data=f"day|{i}-Oktabr"))
                            elif month_name == "December":
                                markup.add(
                                    InlineKeyboardButton(f"{i}-Dekaber Yakshanba", callback_data=f"day|{i}-Dekaber"))

    elif month == 2:
        for j in b:
            for i in j:
                if i >= day:
                    d = pd.Timestamp(f'{year}-{month}-{i}')
                    day_name = d.day_name()
                    if day_name == "Monday":
                        markup.add(InlineKeyboardButton(f"{i}-Fevral Dushanba", callback_data=f"day|{i}-Fevral"))
                    elif day_name == "Tuesday":
                        markup.add(InlineKeyboardButton(f"{i}-Fevral Seshanba", callback_data=f"day|{i}-Fevral"))
                    elif day_name == "Wednesday":
                        markup.add(InlineKeyboardButton(f"{i}-Fevral Chorshanba", callback_data=f"day|{i}-Fevral"))
                    elif day_name == "Thursday":
                        markup.add(InlineKeyboardButton(f"{i}-Fevral Payshanba", callback_data=f"day|{i}-Fevral"))
                    elif day_name == "Friday":
                        markup.add(InlineKeyboardButton(f"{i}-Fevral Juma", callback_data=f"day|{i}-Fevral"))
                    elif day_name == "Saturday":
                        markup.add(InlineKeyboardButton(f"{i}-Fevral Shanba", callback_data=f"day|{i}-Fevral"))
                    elif day_name == "Sunday":
                        markup.add(InlineKeyboardButton(f"{i}-Fevral Yakshanba", callback_data=f"day|{i}-Fevral"))

    else:
        for j in b:
            for i in j:
                if i >= day:
                    d = pd.Timestamp(f'{year}-{month}-{i}')
                    day_name = d.day_name()
                    if day_name == 'Monday':
                        if month_name == "April":
                            markup.row(InlineKeyboardButton(f"{i}-Aprel Dushanba", callback_data=f"day|{i}-Aprel"))
                        elif month_name == "June":
                            markup.row(InlineKeyboardButton(f"{i}-Iyun Dushanba", callback_data=f"day|{i}-Iyun"))
                        elif month_name == "September":
                            markup.row(InlineKeyboardButton(f"{i}-Sentabr Dushanba", callback_data=f"day|{i}-Sentabr"))
                        elif month_name == "November":
                            markup.row(InlineKeyboardButton(f"{i}-Noyabr Dushanba", callback_data=f"day|{i}-Noyabr"))
                    elif day_name == "Tuesday":
                        if month_name == "April":
                            markup.row(InlineKeyboardButton(f"{i}-Aprel Seshanba", callback_data=f"day|{i}-Aprel"))
                        elif month_name == "June":
                            markup.row(InlineKeyboardButton(f"{i}-Iyun Seshanba", callback_data=f"day|{i}-Iyun"))
                        elif month_name == "September":
                            markup.row(InlineKeyboardButton(f"{i}-Sentabr Seshanba", callback_data=f"day|{i}-Sentabr"))
                        elif month_name == "November":
                            markup.row(InlineKeyboardButton(f"{i}-Noyabr Seshanba", callback_data=f"day|{i}-Noyabr"))
                    elif day_name == "Wednesday":
                        if month_name == "April":
                            markup.row(InlineKeyboardButton(f"{i}-Aprel Chorshanba", callback_data=f"day|{i}-Aprel"))
                        elif month_name == "June":
                            markup.row(InlineKeyboardButton(f"{i}-Iyun Chorshanba", callback_data=f"day|{i}-Iyun"))
                        elif month_name == "September":
                            markup.row(
                                InlineKeyboardButton(f"{i}-Sentabr Chorshanba", callback_data=f"day|{i}-Sentabr"))
                        elif month_name == "November":
                            markup.row(InlineKeyboardButton(f"{i}-Noyabr Chorshanba", callback_data=f"day|{i}-Noyabr"))
                    elif day_name == "Thursday":
                        if month_name == "April":
                            markup.row(InlineKeyboardButton(f"{i}-Aprel Payshanba", callback_data=f"day|{i}-Aprel"))
                        elif month_name == "June":
                            markup.row(InlineKeyboardButton(f"{i}-Iyun Payshanba", callback_data=f"day|{i}-Iyun"))
                        elif month_name == "September":
                            markup.row(InlineKeyboardButton(f"{i}-Sentabr Payshanba", callback_data=f"day|{i}-Sentabr"))
                        elif month_name == "November":
                            markup.row(InlineKeyboardButton(f"{i}-Noyabr Payshanba", callback_data=f"day|{i}-Noyabr"))
                    elif day_name == "Friday":
                        if month_name == "April":
                            markup.row(InlineKeyboardButton(f"{i}-Aprel Juma", callback_data=f"day|{i}-Aprel"))
                        elif month_name == "June":
                            markup.row(InlineKeyboardButton(f"{i}-Iyun Juma", callback_data=f"day|{i}-Iyun"))
                        elif month_name == "September":
                            markup.row(InlineKeyboardButton(f"{i}-Sentabr Juma", callback_data=f"day|{i}-Sentabr"))
                        elif month_name == "November":
                            markup.row(InlineKeyboardButton(f"{i}-Noyabr Juma", callback_data=f"day|{i}-Noyabr"))
                    elif day_name == "Saturday":
                        if month_name == "April":
                            markup.row(InlineKeyboardButton(f"{i}-Aprel Shanba", callback_data=f"day|{i}-Aprel"))
                        elif month_name == "June":
                            markup.row(InlineKeyboardButton(f"{i}-Iyun Shanba", callback_data=f"day|{i}-Iyun"))
                        elif month_name == "September":
                            markup.row(InlineKeyboardButton(f"{i}-Sentabr Shanba", callback_data=f"day|{i}-Sentabr"))
                        elif month_name == "November":
                            markup.row(InlineKeyboardButton(f"{i}-Noyabr Shanba", callback_data=f"day|{i}-Noyabr"))
                    elif day_name == "Sunday":
                        if month_name == "April":
                            markup.row(InlineKeyboardButton(f"{i}-Aprel Yakshanba", callback_data=f"day|{i}-Aprel"))
                        elif month_name == "June":
                            markup.row(InlineKeyboardButton(f"{i}-Iyun Yakshanba", callback_data=f"day|{i}-Iyun"))
                        elif month_name == "September":
                            markup.row(InlineKeyboardButton(f"{i}-Sentabr Yakshanba", callback_data=f"day|{i}-Sentabr"))
                        elif month_name == "November":
                            markup.row(InlineKeyboardButton(f"{i}-Noyabr Yakshanba", callback_data=f"day|{i}-Noyabr"))
    return markup


def timer(day_today):
    markup = InlineKeyboardMarkup(row_width=2)
    x = datetime.datetime.now()
    h = int(x.strftime("%H"))
    day = int(x.strftime('%d'))
    if day != day_today:
        for i in range(9, 23):
            markup.row(InlineKeyboardButton(f"⏰{i}:00 dan ⏰{i + 1}:00 gacha", callback_data=f"timer|{i}"))
    elif day == day_today:
        if h < 8:
            for i in range(9, 23):
                markup.row(InlineKeyboardButton(f"⏰{i}:00 dan ⏰{i + 1}:00 gacha", callback_data=f"timer|{i}"))
        else:
            for i in range(h, 23):
                markup.row(InlineKeyboardButton(f"⏰{i}:00 dan ⏰{i + 1}:00 gacha", callback_data=f"timer|{i}"))
    return markup


def confirm_success():
    markup = InlineKeyboardMarkup(row_width=1)
    confirm = InlineKeyboardButton("Tasdiqlandi", callback_data="confirm_success")
    return markup.add(confirm)


def confirm_break():
    markup = InlineKeyboardMarkup(row_width=1)
    confirm = InlineKeyboardButton("Bekor qilingan", callback_data="confirm_break")
    return markup.add(confirm)


def check():
    markup = InlineKeyboardMarkup(row_width=2, )
    confirmation = InlineKeyboardButton("✅", callback_data="confirmation")
    cancellation = InlineKeyboardButton("❌", callback_data="cancellation")
    return markup.add(confirmation, cancellation)


def check_barber():
    markup = InlineKeyboardMarkup(row_width=2)
    confirmation = InlineKeyboardButton("✅", callback_data="barber_confirmation")
    cancellation = InlineKeyboardButton("❌", callback_data="barber_cancellation")
    return markup.add(confirmation, cancellation)


def clear_db():
    markup = InlineKeyboardMarkup(row_width=1)
    add_barber = InlineKeyboardButton("Yangi barber qo'shish", callback_data="add_barber")
    clear = InlineKeyboardButton("Bazani tozalsh", callback_data="clear")
    no_clear = InlineKeyboardButton("Bekor qilish", callback_data="no_clear")
    return markup.add(add_barber, clear, no_clear)


def check_admin():
    markup = InlineKeyboardMarkup(row_width=2)
    confirmation = InlineKeyboardButton("✅", callback_data="admin_confirmation")
    cancellation = InlineKeyboardButton("❌", callback_data="admin_cancellation")
    return markup.add(confirmation, cancellation)


def barber_experience():
    markup = InlineKeyboardMarkup(row_width=2)
    no_experience = InlineKeyboardButton("Tajriba yo'q", callback_data="no_experience")
    six_month = InlineKeyboardButton("6 oy", callback_data="six_month")
    one_year = InlineKeyboardButton("1 yil", callback_data="one_year")
    one_year_plus = InlineKeyboardButton("1.5 yil", callback_data="one_year_plus")
    two_year = InlineKeyboardButton("2-3 yil", callback_data="two_year")
    four_year = InlineKeyboardButton("4-5 yil", callback_data="four_year")
    six_year = InlineKeyboardButton("6-7 yil", callback_data="six_year")
    eight_year = InlineKeyboardButton("8-9 yil", callback_data="eight_year")
    ten_year = InlineKeyboardButton("10+ yil", callback_data="ten_year")
    markup.add(no_experience, six_month, one_year, one_year_plus, two_year, four_year, six_year, eight_year, ten_year)
    return markup
