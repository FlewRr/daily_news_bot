import time
st = time.time()
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import app.data_generator
from app.ml.database.db import News, add_news_to_storage
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

st = time.time()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_TOKEN = os.environ.get("API_TOKEN")
engine = create_engine("sqlite:///news.db")
News.metadata.create_all(bind=engine)
db = Session(autoflush=False, bind=engine)
fn = time.time()
print(f"DB created in {fn-st}")
topics_ = app.data_generator.generate_dataset(db, 10, API_TOKEN)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
fn = time.time()
print(f"EVERYTHING SUCCESSFULLY BUILDED IN {fn-st}")
