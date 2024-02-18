from aiogram import types
from aiogram.dispatcher import FSMContext
from app.utils import States, start_keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import numpy as np
from app.ml.database.db import get_news_by_topics
import json 
from app.loader import db, dp, topics_

@dp.message_handler(commands=["start"], state="*")
async def welcome(message: types.Message, state: FSMContext):
    await States.work.set()
    await message.answer("Hello!", reply_markup=start_keyboard)
    

@dp.message_handler(commands=["about"], state="*")
async def about(message: types.Message, state: FSMContext):
    await message.answer("I am news bot")
    await welcome(message, state)

@dp.message_handler(state=States.work)
async def start(message: types.Message, state: FSMContext):
    if message.text == 'Get news':
        await States.choose_topic.set()
        topics = [f"{x} : {y}" for x, y in topics_.items()]
        topics_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        if len(topics) % 2 == 0:
            for i in range(1, len(topics)+1, 2):
                topics_keyboard.row(KeyboardButton(str(i)), KeyboardButton(str(i+1)))
        else:
            for i in range(1, len(topics), 2):
                topics_keyboard.row(KeyboardButton(str(i)), KeyboardButton(str(i+1)))
            topics_keyboard.row(KeyboardButton(str(len(topics))))

        s = "\n".join([element for element in topics])
        await message.answer(f"Choose one of the topics: {s}", reply_markup=topics_keyboard)
    else:
        return
    
@dp.message_handler(state=States.choose_topic)
async def choose_topic(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) > len(topics_) or int(message.text) < 1:
        await message.answer("Sorry, I need the number, not what you've just said")
        return
    else:
        news_text = get_news_by_topics(db, int(message.text))
        await message.answer(news_text)
        await welcome(message, state)
