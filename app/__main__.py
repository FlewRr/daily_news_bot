from aiogram.utils import executor
from app.loader import dp     
from app.handlers import *


if __name__ == "__main__":
    print("Ready for work")
    executor.start_polling(dp) 
