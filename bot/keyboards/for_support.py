from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def get_for_support_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Выход')
    return kb.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
