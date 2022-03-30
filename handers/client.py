from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ParseMode
from bot_instance import db,bot
from keyboard import keyboard
from data_base import bot_db
from parser import tv_show



async def hello(message: types.Message):
    await bot.send_message(message.chat.id,f' hi : {message.from_user.full_name}',
                           reply_markup=keyboard.keyboard_start)



async def choice(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton('решение',
                                       callback_data='button_call')
    markup.add(button_call)



    question = 'Output:'
    answer = ['for i in range(0,len(list1)):\n'
    'list1.append(list1[i])','impossible','23']
    photo = open('media/Безымянный123.png','rb')
    await bot.send_photo(message.chat.id,photo=photo)

    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        correct_option_id=0,
                        open_period=10,
                        type='quiz',
                        reply_markup=markup
                        )




async def asa(message: types.Message):
    markup=InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('next',
                                       callback_data='button_call_1')
    markup.add(button_call_1)
    question='последняя верся пайтона '
    answer= ['3.9','3.10','3.8']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        correct_option_id=1,
                        open_period=10,
                        reply_markup=markup,
                        type='quiz')

async def hw2 (message: types.Message):
    question='4+3'
    answer = ['5','1','7']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        correct_option_id=2,
                        type='quiz')


async def hw2_1(message: types.Message):
    question='33+4?'
    answer = ['53', '37', '73']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        correct_option_id=1,
                        type='quiz')



async def vetki(message: types.Message):

    markup = InlineKeyboardMarkup()
    button_call_hw2 = InlineKeyboardButton('Хорошо',callback_data='button_call_hw2')




    markup2 = InlineKeyboardMarkup()
    button_call_hw2_2 = InlineKeyboardButton('Плохо', callback_data='button_call_hw2_2')
    markup2.add(button_call_hw2)
    a=markup2.add(button_call_hw2_2)

    await bot.send_message(message.chat.id,'как настроение ?',
                           reply_markup=a)

async def show_all(messege: types.Message):
    await bot_db.sql_command_select(messege)


async def parser_xxx(message: types.Message):
    data= tv_show.parser()
    for i in data:
        await bot.send_message(message.chat.id, i)





def register_handlers_client(db: Dispatcher):
    db.register_message_handler(hello, commands=['start'])
    db.register_message_handler(asa, commands=['quiz'])
    db.register_message_handler(hw2, commands=['hw2'])
    db.register_message_handler(hw2_1, commands=['hw2.1'])
    db.register_message_handler(vetki,commands=['vetki'])
    db.register_message_handler(show_all,commands=['all'])
    db.register_message_handler(parser_xxx,commands=['parser'])