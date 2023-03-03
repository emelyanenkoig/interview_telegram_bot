import sqlite3 as sq


def sql_start():
    global base, cur

    base = sq.connect('interview.db')
    cur = base.cursor()

    if base:
        print('База данных успешно подключена!')
    base.execute(
        "CREATE TABLE IF NOT EXISTS interview(user_id TEXT PRIMARY KEY, name TEXT, phone TEXT, category TEXT, "
        "text TEXT)")
    base.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM interview WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO interview VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
    base.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute('UPDATE interview SET name == "{}", phone == "{}", category == "{}", text == "{}" WHERE user_id == "{}"'.format(data['name'], data['phone'], data['category_of_problem'], data['text_of_problem'], user_id))
        base.commit()
