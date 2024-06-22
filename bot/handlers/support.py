from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Support
from keyboards.for_support import get_for_support_kb
from keyboards.for_common import get_common_kb

router = Router()


@router.message((F.text.lower() == 'поддержка') & (F.chat.id == 248779515))
async def support_admin(message: Message, state: FSMContext):
    """
    Обработчик для администратора поддержки.

    Отправляет сообщение о входе в чат поддержки и устанавливает состояние FSM.

    Args:
        message (Message): Сообщение от пользователя.
        state (FSMContext): Контекст FSM для установки состояния.
    """
    await message.answer('Вы вошли в чат поддержки',
                         reply_markup=get_for_support_kb())
    await state.set_state(Support.in_conv)


@router.message(F.text.lower() == 'поддержка')
async def support(message: Message, state: FSMContext):
    """
    Обработчик для обычного пользователя поддержки.

    Отправляет сообщение с приглашением написать вопрос и устанавливает состояние FSM.

    Args:
        message (Message): Сообщение от пользователя.
        state (FSMContext): Контекст FSM для установки состояния.
    """
    await message.answer(
        'Напишите ваш вопрос:',
        reply_markup=get_for_support_kb()
    )
    await state.set_state(Support.in_conv)

@router.message(Support.in_conv, (F.chat.id == 248779515) & F.reply_to_message)
async def support_answer(message: Message):
    """
    Отправляет ответ пользователю в чат поддержки.

    Args:
        message (Message): Сообщение с ответом от поддержки.
    """
    await message.bot.send_message(
        chat_id=message.reply_to_message.forward_origin.sender_user.id,
        text=message.text
    )


@router.message(Support.in_conv, F.text.lower() == 'выход')
async def support_exit(message: Message, state: FSMContext):
    """
    Завершает чат поддержки для пользователя.

    Очищает состояние FSM и отправляет сообщение о выходе.

    Args:
        message (Message): Сообщение от пользователя.
        state (FSMContext): Контекст FSM для очистки состояния.
    """
    await state.clear()
    await message.answer(
        'Вы вышли из чата поддержки',
        reply_markup=get_common_kb()
    )


@router.message(Support.in_conv)
async def question(message: Message):
    """
    Пересылает вопрос пользователя в чат поддержки админа.

    Args:
        message (Message): Сообщение от пользователя с вопросом.
    """
    await message.forward(chat_id=248779515)
