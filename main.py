from aiogram import executor, types
from config.telegram import dp
from controllers.start_controller import start_controller

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
  await start_controller(message)

if __name__ == '__main__':
  executor.start_polling(dp)