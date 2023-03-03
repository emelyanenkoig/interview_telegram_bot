from aiogram.dispatcher.filters import CommandStart, CommandHelp, CommandPrivacy
from aiogram import types

from main.local_settings import dp, Dispatcher


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f'Здравствуйте {message.from_user.full_name} это бот, который соберет ваши данные '
                              f' для дальнейшего оказания услуг!\n'
                              f'/privacy - информация о политике конфиденциальности\n '
                              f'/interview - для начала опроса\n')


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(text='Для того чтобы воспользоваться ботом введите следующие команды:\n '
                              '/privacy - информация о политике конфиденциальности\n '
                              '/interview - для начала опроса'
                              '\nЕсли у вас имеются какие-либо вопросы - напишите нашему представителю напрямую @id_admin')


@dp.message_handler(CommandPrivacy())
async def bot_privacy(message: types.Message):
    await message.answer(text='Политика конфиденциальности')
