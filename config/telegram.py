from os import getenv
from aiogram import Bot, Dispatcher
from config.env import TELEGRAM_TOKEN_KEY

token = getenv(TELEGRAM_TOKEN_KEY)

bot = Bot(str(token))
dp = Dispatcher(bot=bot)