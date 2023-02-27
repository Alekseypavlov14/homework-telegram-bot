from entities.course import Course
from aiogram.types import InlineKeyboardMarkup
from ui.courses.course_button import create_course_button

def create_course_buttons(courses: list[Course]):
  buttons = InlineKeyboardMarkup()

  for course in courses:
    button = create_course_button(course)
    buttons.add(button)
  
  return buttons