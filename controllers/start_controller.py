from messages.start_message import get_start_message
from ui.buttons import keyboard
from entities.user import User
from aiogram import types
from store import store

async def start_controller(message: types.Message):
  user_name = message.from_user.first_name
  user_id = message.from_user.id

  user = store.find_user_by_id(user_id)

  if (not(user)):
    user = User(user_name, user_id)
    store.add_user(user)

  start_message = get_start_message(user_name)
  return await message.answer(start_message, reply_markup=keyboard, parse_mode='HTML')