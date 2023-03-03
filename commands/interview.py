from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from data_base.sqlite_db import create_profile
from main.keyboards import keyboard
from main.local_settings import dp
from aiogram import types
from data_base import sqlite_db
from states.states_of_interview import User


# Start Interview
@dp.message_handler(Command('interview'))
async def on_start_interview(message: types.Message):
    user_id = message.from_user.id
    print(user_id)
    await create_profile(user_id=user_id)
    await message.answer('Доброго времени суток!')
    await message.answer('Введите пожалуйста ваше Ф.И.О:')
    await User.name.set()


# User name
@dp.message_handler(state=User.name)
async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    try:
        if (data['name']).replace(' ', '').isalpha():
            print(data['name'])
            await User.next()
            await message.answer('Введите пожалуйста ваш номер телефона:')
            await User.phone.set()
        else:
            await message.answer(f'Прошу прощения, но "{data["name"]}" не является корректной информацией.')
            await message.answer(f'Попробуйте использовать <b>буквенный</b> формат ввода данных', parse_mode='html')
    except Exception:
        await message.answer(f'{data["name"]} является корректной информацией?')


# User Phone
@dp.message_handler(state=User.phone)
async def phone_number(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    try:
        if (data['phone']).replace('+', '').isnumeric():
            await User.next()
            await message.answer('К какой категории из предложенных вы могли бы отнести свой вопрос:',
                                 reply_markup=keyboard(), )
            await User.category_of_problem.set()
        else:
            await message.answer('Нам нужен ваш <b>корректный</b> номер телефона для обратной связи', parse_mode='html')
    except Exception:
        await message.answer('Введите корректный номер телефона')


# User Category
@dp.message_handler(state=User.category_of_problem)
async def category_of_problem(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category_of_problem'] = message.text
    await User.next()
    await message.answer(f'Опишите пожалуйста вашу проблему как можно подробнее:')
    await User.text_of_problem.set()


# User Description of Problem
@dp.message_handler(state=User.text_of_problem)
async def description(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['text_of_problem'] = message.text
    await sqlite_db.edit_profile(state, user_id=user_id)
    await message.answer('Ваша анкета успешно создана!\n'
                         'В ближайшее время с вами свяжется наш специалист!')
    await state.finish()

    # User data for staff
    name_of_user = message.from_user.full_name
    user_login = message.from_user.username

    await message.bot.send_message(398928816, text=f'Здравствуйте, появился новый пользователь:\n\n'
                                                   f'<b>Логин пользователя:</b>\n'
                                                   f'{user_login}\n\n'
                                                   f'<b>Пользователь:</b>\n'
                                                   f'{data["name"]}\n\n'
                                                   f'<b>Номер:</b>\n'
                                                   f'{data["phone"]}\n\n'
                                                   f'<b>Категория:</b>\n'
                                                   f'{data["category_of_problem"]}\n\n'
                                                   f'<b>Проблема:</b>\n'
                                                   f'{data["text_of_problem"]}', parse_mode='html')
