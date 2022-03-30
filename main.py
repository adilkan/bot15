import asyncio

from aiogram import executor
from bot_instance import db
from handers import client, callback, extra, fsmadmin, notification, inline
from data_base import bot_db
from handers.notification import schedukler




async def on_startup(_):
    bot_db.sql_create()
    asyncio.create_task(schedukler())
    print("Bot is online")


fsmadmin.register_handler(db)
client.register_handlers_client(db)
callback.register_handler_callback(db)
inline.register_handlers_inline(db)
extra.register_handlers_extra(db)
notification.register_notification(db)


if __name__ == "__main__":
    executor.start_polling(db, skip_updates=False, on_startup=on_startup)