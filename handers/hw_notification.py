# -*- coding: cp1251 -*-
from bot_instance import bot,db,Dispatcher
import asyncio
import aioschedule
from aiogram import types

async def comfirm_notification(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    if message.text == 'напомни про дантиста':
        await message.reply('хорошо братик')

async def dantist():
    await bot.send_message(chat_id=chat_id,text='тебе надо к дантисту братик')


async def remind():
    aioschedule.every().wednesday.at('23:12').do(remind)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_notification(db: Dispatcher):
    db.register_message_handler(comfirm_notification,content_types=['text'] )