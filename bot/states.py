from aiogram.fsm.state import StatesGroup, State


class Support(StatesGroup):
    """
    Класс состояний для поддержки чата.

    Состояния:
        in_conv: Состояние общения в чате поддержки.
    """
    in_conv = State()
