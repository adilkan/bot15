from aiogram import Bot,Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = config('Token')
bot = Bot(token)
db = Dispatcher(bot=bot,storage=storage)
URL ='https://botqwerty123456.herokuapp.com/'
URI = 'postgres://bqjtyoaoffzjsz:800100e76312661fc5a57ffee9bc6d9855622b8248d6f39575429492c948b8ad@ec2-18-214-134-226.compute-1.amazonaws.com:5432/d94pergv2dfu0d'
