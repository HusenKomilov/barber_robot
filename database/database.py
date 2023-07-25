import psycopg2
from config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST  # AGARDA PORT BO'LSA PORTNI QO'SHING
        )

    '''MANAGER ORQALI SQL SAVOLLARNI ISHLATING!'''

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                fetchmany: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result

    def create_user_table(self):
        sql = """CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY,
            full_name VARCHAR(150),
            phone_number VARCHAR(13)
        )"""
        self.manager(sql, commit=True)

    def insert_user_telegram_id(self, chat_id):
        sql = """INSERT INTO users(telegram_id) VALUES (%s) ON CONFLICT DO NOTHING"""
        self.manager(sql, (chat_id,), commit=True)

    def check_user_date(self, chat_id):
        sql = """SELECT full_name, phone_number FROM users WHERE telegram_id = %s"""
        return self.manager(sql, chat_id, fetchone=True)

    def update_user_save(self, full_name, phone_number, chat_id):
        sql = """UPDATE users SET full_name = %s, phone_number = %s WHERE telegram_id = %s"""
        self.manager(sql, full_name, phone_number, chat_id, commit=True)

    def create_barber_users(self):
        sql = """CREATE TABLE IF NOT EXISTS barber(
            id INTEGER GENERATED ALWAYS AS IDENTITY,
            chat_id BIGINT PRIMARY KEY,
            full_name VARCHAR(200) UNIQUE,
            age INTEGER,
            experience TEXT,
            image BYTEA
        )"""
        self.manager(sql, commit=True)

    def insert_barber_users(self, chat_id, full_name, age, experience, image):
        sql = """INSERT INTO barber(chat_id, full_name, age, experience, image)
        VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING"""
        self.manager(sql, chat_id, full_name, age, experience, image, commit=True)

    def select_barber_users_name(self):
        sql = """SELECT full_name, id FROM barber"""
        return self.manager(sql, fetchall=True)

    def select_barber_bio(self, id):
        sql = """SELECT * FROM barber WHERE id = %s"""
        return self.manager(sql, id, fetchone=True)

    def create_barber_booking(self):
        sql = """CREATE TABLE IF NOT EXISTS barber_booking(
            customer_name TEXT,
            customer_phone_number VARCHAR(13),
            customer_telegram_id TEXT,
            visiting_day VARCHAR(15),
            visiting_time VARCHAR(5) UNIQUE,
            barber_id TEXT,
            barber_telegram_id TEXT,
            barber_name TEXT
        )"""
        self.manager(sql, commit=True)

    def drop_table_barber_booking(self):
        sql = """DROP TABLE IF EXISTS barber_booking"""
        self.manager(sql, commit=True)

    def insert_barber_booking(self, customer_name, customer_phone_number, customers_telegram_id, visiting_day,
                              visiting_time,
                              barber_id, barber_telegram_id, barber_name):
        sql = """INSERT INTO barber_booking(customer_name, customer_phone_number,  customer_telegram_id, visiting_day, 
        visiting_time, barber_id, barber_telegram_id, barber_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
        ON CONFLICT DO NOTHING"""
        self.manager(sql, customer_name, customer_phone_number, customers_telegram_id, visiting_day,
                     visiting_time, barber_id,
                     barber_telegram_id, barber_name, commit=True)

    def only_for_barber(self, barber_telegram_id):
        sql = """SELECT customer_name, customer_phone_number, customer_telegram_id, barber_name, 
        visiting_day, visiting_time FROM barber_booking WHERE barber_telegram_id = %s"""
        return self.manager(sql, barber_telegram_id, fetchall=True)

    def only_for_admin(self):
        sql = """SELECT customer_name, customer_phone_number, customer_telegram_id, barber_name,
        visiting_day, visiting_time FROM barber_booking"""
        return self.manager(sql, fetchall=True)

    def clear_db_barber_booking(self):
        sql = """DROP TABLE IF EXISTS barber_booking"""
        self.manager(sql, commit=True)
