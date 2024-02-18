from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup

class States(StatesGroup):
    work = State()
    choose_topic = State()

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_keyboard.row(KeyboardButton('Get news'), KeyboardButton('Get news [ru] (beta)'))
start_keyboard.row(KeyboardButton('Exit'))