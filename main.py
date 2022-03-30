import asyncio
from aiogram import executor
from bot_instance import db
from handers import client,callback, extra,hw3_fsmadmin,notification,hw_notification,inline
from data_base import bot_db
from handers.notification import schedukler
from handers.hw_notification import remind







async def on_startup(_):
    bot_db.sql_create()
    asyncio.create_task(schedukler())
    asyncio.create_task(remind())

client.register_handlers_client(db)
callback.register_handler_callback(db)
inline.reqister()
extra.register_handlers_extra(db)
hw_notification.register_notification(db)




if __name__ == '__main__':
    executor.start_polling(db,skip_updates=False,on_startup=on_startup)
