from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_quiz = KeyboardButton('/quiz')
button_hw2 = KeyboardButton("/hw2")
button_hw2_1 = KeyboardButton("/hw2.1")
button_vetki = KeyboardButton('/vetki')




button_location= KeyboardButton('share location',request_location=True)
button_info = KeyboardButton('share info', request_contact=True)





keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

keyboard_start.row(button_vetki,button_info,button_location,button_hw2,button_quiz)