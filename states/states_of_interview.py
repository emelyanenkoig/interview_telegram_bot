from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):
    name = State()   # Last name of User
    phone = State()  # Phone Number
    category_of_problem = State()   # Category of Problem
    text_of_problem = State()   # Full text of Problem
    send_admin_info = State()   # Send a contact to Admin for usage
