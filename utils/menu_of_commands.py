from aiogram import types
from main.local_settings import dp


async def set_default_commands():
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("interview", "Пройти опрос"),
        ]
    )