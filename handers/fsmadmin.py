from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup
from data_base import  bot_db
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from bot_instance import db,bot

class FSMADMIN(StatesGroup):
    photo = State()
    title = State()
    discription = State()

async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'admin, what do u need')
async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMADMIN.photo.set()
        await bot.send_message(message.from_user.id,'admin , send photo')



async def load_photo(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMADMIN.next()
        await message.reply('send me title of photo')

async def load_title(messeage: types.Message,
                     state: FSMContext):
    if messeage.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['title'] = messeage.text
        await  FSMADMIN.next()
        await messeage.reply('admin , send me discription')


async def load_discription(message: types.Message,
                           state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['description'] = message.text
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await bot_db.sql_command_insert(state)

        await state.finish()



def register_handler(db:Dispatcher):
    db.register_message_handler(is_admin_func,commands=['admin'], is_chat_admin= True)
    db.register_message_handler(fsm_start,commands=['download'], state = None)
    db.register_message_handler(load_photo,content_types=['photo'], state= FSMADMIN.photo)
    db.register_message_handler(load_title, state= FSMADMIN.title)
    db.register_message_handler(load_discription, state = FSMADMIN.discription)