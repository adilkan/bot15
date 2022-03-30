from aiogram import types, Dispatcher
from aiogram.types import ParseMode,InlineKeyboardButton,InlineKeyboardMarkup
from bot_instance import bot


async def resh1(call: types.CallbackQuery):
    question='когда вышла пайтон'
    answer=['1999','2001','1991']
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        correct_option_id=2,
                        type='quiz'
                        )

async def hw2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()

    button_call_hw2_3 = InlineKeyboardButton('просто',callback_data='button_call_hw2_3')
    button_call_hw2_4 = InlineKeyboardButton('погода хорошая', callback_data='button_call_hw2_4')
    button_call_hw2_5 = InlineKeyboardButton('я выспался ', callback_data='button_call_hw2_5')

    markup.add(button_call_hw2_5)
    markup.add(button_call_hw2_3)
    markup.add(button_call_hw2_4)




    await bot.send_message(call.message.chat.id,'почему ?',reply_markup=markup)



async def hw2_3(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'понял')


async def hw2_4(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'понял_1')

async def hw2_5(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'понял_2')

















async def hw2_2(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'почему плохо?')
    markup = InlineKeyboardMarkup()

    button_call_hw2_6 = InlineKeyboardButton('просто', callback_data='button_call_hw2_6')
    button_call_hw2_7 = InlineKeyboardButton('погода bad', callback_data='button_call_hw2_7')
    button_call_hw2_8 = InlineKeyboardButton('я not выспался ', callback_data='button_call_hw2_8')

    markup.add(button_call_hw2_6)
    markup.add(button_call_hw2_7)
    markup.add(button_call_hw2_8)

    await bot.send_message(call.message.chat.id, 'почему ?', reply_markup=markup)


async def hw2_6(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'понял_3')


async def hw2_7(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'понял_4')

async def hw2_8(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'понял_5')





def register_handler_callback(db :Dispatcher):
    db.register_callback_query_handler(resh1,lambda func: func.data == 'button_call_1')
    db.register_callback_query_handler(hw2,lambda func1: func1.data == 'button_call_hw2')
    db.register_callback_query_handler(hw2_2, lambda func2: func2.data == 'button_call_hw2_2')
    db.register_callback_query_handler(hw2_3, lambda func3: func3.data == 'button_call_hw2_3')
    db.register_callback_query_handler(hw2_4, lambda funс4: funс4.data == 'button_call_hw2_4')
    db.register_callback_query_handler(hw2_5, lambda func5: func5.data == 'button_call_hw2_5')
    db.register_callback_query_handler(hw2_6, lambda func6: func6.data == 'button_call_hw2_6')
    db.register_callback_query_handler(hw2_7, lambda func7: func7.data == 'button_call_hw2_7')
    db.register_callback_query_handler(hw2_8, lambda func8: func8.data == 'button_call_hw2_8')