import logging
import asyncio
from aiogram import Bot, Dispatcher
from handlers import common, support
from aiogram.fsm.storage.memory import MemoryStorage
from data.config_reader import config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s : %(message)s'
)

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(storage=MemoryStorage())


async def main():
    """
    Основная функция для запуска бота в режиме поллинга.

    Инициализирует диспетчер бота, включает роутеры и запускает поллинг для получения сообщений.

    Raises:
        AiogramConnectionError: Ошибка соединения с ботом.
    """
    dp.include_routers(common.router, support.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
