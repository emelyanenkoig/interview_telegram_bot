from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard():
    practice_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb1 = KeyboardButton('Долги')
    kb2 = KeyboardButton('Кредит')
    kb3 = KeyboardButton('Финансовый управляющий')
    kb4 = KeyboardButton('Конфискация имущества')
    kb5 = KeyboardButton('Суд')
    kb6 = KeyboardButton('Банкротство')
    practice_keyboard.add(kb1).add(kb2).add(kb3).add(kb4).add(kb5).add(kb6)
    return practice_keyboard


def phone_number():
    number = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb1 = KeyboardButton('Поделиться номером телефона', request_contact=True)
    number.add(kb1)
    return number