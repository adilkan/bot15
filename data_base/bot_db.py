import sqlite3
from bot_instance import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()
    if db:
        print('Databasr connrcted successfully')
    db.execute('CREATE TABLE IF NOT EXISTS user '
               '(user_id TEXT PRIMARY KEY, user_name , first_name TEXT, last_name TEXT'')')
    db.commit()
async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO user VALUES (?,?,?,?)' , tuple(data.values()))
        db.commit()

async def sql_command_select(message):
    for result in cursor.execute('SELECT * FROM user').fetchall():

        await bot.send_message(message.from_user.id,f'user_id: {result[0]}\n'
                               f'user_name: {result[1]}\n'
                               f'first_name: {result[2]}\n'
                               f'last_name: {result[3]}\n')

