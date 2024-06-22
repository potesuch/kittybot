import random
import aiohttp
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, URLInputFile
from aiogram.utils.formatting import Text, Bold, as_list
from aiogram.enums import ChatAction
from keyboards.for_common import get_common_kb
from data.config_reader import config

COMMANDS = ('/cats', '/ai_cats', '/ai_persons')

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    """
    Обработчик команды /start.

    Отправляет приветственное сообщение и список доступных команд пользователю.

    Args:
        message (Message): Сообщение от пользователя.
    """
    content = Text(
        'Привет, ',
        Bold(message.from_user.full_name),
        as_list(
            '\nКоманды:',
            *COMMANDS
        )
    )
    await message.answer(
        **content.as_kwargs(),
        reply_markup=get_common_kb()
    )


@router.message(F.text.lower() == 'кот')
@router.message(Command('cats'))
async def cmd_cats(message: Message):
    """
    Обработчик команды /cats или текста "кот".

    Отправляет случайное изображение кота из API.

    Args:
        message (Message): Сообщение от пользователя.
    """
    await message.chat.do(ChatAction.UPLOAD_PHOTO)
    async with aiohttp.ClientSession() as session:
        response = await session.get(config.cat_api)
        if response.status == 200:
            json = await response.json()
            img_url = json[0].get('url')
            await message.answer_photo(URLInputFile(img_url))


@router.message(F.text.lower() == 'ai кот')
@router.message(Command('ai_cats'))
async def cmd_ai_cats(message: Message):
    """
    Обработчик команды /ai_cats или текста "ai кот".

    Отправляет случайное сгенерированное изображение кота.

    Args:
        message (Message): Сообщение от пользователя.
    """
    x = random.randint(1, 6)
    y = random.randint(1, 4999)
    await message.chat.do(ChatAction.UPLOAD_PHOTO)
    await message.answer_photo(
        URLInputFile(f'{config.ai_cats}/0{x}/cat{y}.jpg')
    )


@router.message(F.text.lower() == 'ai человек')
@router.message(Command('ai_persons'))
async def cmd_ai_person(message: Message):
    """
    Обработчик команды /ai_persons или текста "ai человек".

    Отправляет случайное сгенерированное изображение человека

    Args:
        message (Message): Сообщение от пользователя.
    """
    await message.chat.do(ChatAction.UPLOAD_PHOTO)
    await message.answer_photo(URLInputFile(config.ai_persons))


@router.message(F.location)
async def on_location(message: Message):
    """
    Обработчик получения локации от пользователя.

    Пересылает локацию в чат с ID 248779515.

    Args:
        message (Message): Сообщение с локацией от пользователя.
    """
    await message.forward(chat_id=248779515)
