from aiogram.utils import executor
from app.loader import dp     
from app.handlers import *


if __name__ == "__main__":
    executor.start_polling(dp) 
