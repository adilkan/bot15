# -*- coding: cp1251 -*-
from bot_instance import bot,db,Dispatcher
import asyncio
import aioschedule
from aiogram import types

async def comfirm_notification(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    if message.text == 'wake me up':
        await message.reply('ok')

async def wake_up():
    await bot.send_message(chat_id=chat_id,text='проснис братик')


async def schedukler():
    aioschedule.every().day.at('23:01').do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_notification(db: Dispatcher):
    db.register_message_handler(comfirm_notification,content_types=['text'] )