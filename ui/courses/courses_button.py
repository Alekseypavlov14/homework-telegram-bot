from aiogram.types import InlineKeyboardButton, CallbackQuery
from services.get_user_courses import get_user_courses
from ui.courses.course_buttons import create_course_buttons
from config.telegram import dp

callback_data = 'courses'

courses_button = InlineKeyboardButton(text='Courses', callback_data=callback_data)

@dp.callback_query_handler(text=[callback_data])
async def click_handler(call: CallbackQuery):
  user_id = call.from_user.id
  courses = get_user_courses(user_id)

  if (len(courses) == 0):
    return await call.message.answer('You do not have any courses')

  course_buttons = create_course_buttons(courses)

  return await call.message.answer('Your courses are:', reply_markup=course_buttons)