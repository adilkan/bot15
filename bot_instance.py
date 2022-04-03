from aiogram import Bot,Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = config('Token')
bot = Bot(token)
db = Dispatcher(bot=bot,storage=storage)
URL = 'https://botqwerty123456.herokuapp.com/'