from aiogram import executor
from main.local_settings import dp
from data_base.sqlite_db import sql_start
from commands import default_commands, interview
from utils.menu_of_commands import set_default_commands


def on_startup():
    print('Бот работает в онлайн режиме')
    sql_start()
    # /set_default_commands()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
