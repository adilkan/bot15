from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from data_base import bot_db
from bot_instance import db,bot

class FSMADMIN(StatesGroup):
    user_id = State()
    user_name = State()
    first_name = State()
    last_name = State()



async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'admin, what11 do u need')


async def fsm_start(message: types.Message):
    await FSMADMIN.user_id.set()
    await bot.send_message(message.from_user.id,'admin , send user id ')



async def load_user_id(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text
    await FSMADMIN.next()
    await bot.send_message(message.chat.id,'send me user name')

async def load_user_name(messeage: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['user name'] = messeage.from_user.username
    await  FSMADMIN.next()
    await bot.send_message(messeage.chat.id,'admin , send me first name')


async def load_first_name(messeage: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:

        data['first_name'] = messeage.from_user.first_name
    await  FSMADMIN.next()
    await bot.send_message(messeage.chat.id,'admin , send me last name')


async def load_last_name(message: types.Message,
                           state: FSMContext):

    async with state.proxy() as data:
        data['last_name'] = message.from_user.last_name
        # async with state.proxy() as data:
        #     await message.reply(str(data))
    await bot_db.sql_command_insert(state)
    await state.finish()



def register_handler(db:Dispatcher):
    db.register_message_handler(is_admin_func,commands=['admin1'], is_chat_admin= True)
    db.register_message_handler(fsm_start,commands=['data'], state = None)
    db.register_message_handler(load_user_id, state= FSMADMIN.user_id)
    db.register_message_handler(load_user_name, state= FSMADMIN.user_name)

    db.register_message_handler(load_first_name, state=FSMADMIN.first_name)

    db.register_message_handler(load_last_name, state = FSMADMIN.last_name)