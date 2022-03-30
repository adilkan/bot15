from aiogram import types,Dispatcher
from bot_instance import bot

async def secret_word (message: types.Message):

    await message.reply('yes , my master')



async def exo_and_ban(messege: types.Message):
    ban_words=['java', 'bitch','python is bad','манда',]
    for i in ban_words:
        if i in messege.text.lower().replace(' ', ''):
            await messege.delete()
            await bot.send_message(messege.chat.id,'bot deleted bad words')
    if messege.text.lower() == 'dice':
        await bot.send_dice(messege.chat.id, )

    elif messege.text.startswith('pin'):
        await bot.pin_chat_message(messege.chat.id, messege.message_id)





def register_handlers_extra(db: Dispatcher):
    db.register_message_handler(secret_word, lambda word: 'saliery' in word.text)
    db.register_message_handler(exo_and_ban,content_types=['text'])