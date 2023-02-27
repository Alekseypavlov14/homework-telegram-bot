from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ui.courses import courses_button

tasks_button = InlineKeyboardButton(text='Tasks', callback_data='tasks')

keyboard = InlineKeyboardMarkup().add(courses_button, tasks_button)