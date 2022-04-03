import asyncio

from aiogram import executor
from bot_instance import db,bot,URL
from handers import client,callback, extra ,hw_notification,inline
from data_base import bot_db
from handers.notification import schedukler
from handers.hw_notification import remind
from decouple import config






async def on_startup(_):
    await bot.set_webhook(URL)
    bot_db.sql_create()
    asyncio.create_task(schedukler())
    asyncio.create_task(remind())

async def om_shutdown(db):
    await bot.delete_webhook()


client.register_handlers_client(db)
callback.register_handler_callback(db)
inline.register_handlers_inline(db)
extra.register_handlers_extra(db)
hw_notification.register_notification(db)



if __name__ == '__main__':
    # executor.start_polling(db,skip_updates=False,on_startup=on_startup)
    executor.set_webhook(
        dispatcher=db,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=om_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=int(config('PORT',default=5000))
    )