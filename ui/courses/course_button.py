from aiogram.types import InlineKeyboardButton, CallbackQuery
from entities.course import Course
from config.telegram import dp

def create_course_button(course: Course):
  callback_data = f'course:{course.id}'

  button = InlineKeyboardButton(text=course.name, callback_data=callback_data)

  @dp.callback_query_handler(text=[callback_data])
  async def click_handler(call: CallbackQuery):
    return await call.message.answer(course.name)
  
  return button



