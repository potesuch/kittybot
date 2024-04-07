from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_common_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text='Кот'),
        KeyboardButton(text='AI Кот'),
    )
    kb.row(
        KeyboardButton(text='AI Человек'),
        KeyboardButton(
            text='Отправить локацию',
            request_location=True
        ),
    )
    kb.row(
        KeyboardButton(text='Поддержка')
    )
    return kb.as_markup(resize_keyboard=True)
