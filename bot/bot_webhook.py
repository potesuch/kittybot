import logging
from aiohttp import web
from aiohttp import ClientSession
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from handlers import common, support
from data.config_reader import config


async def on_startup(bot: Bot):
    """
    Функция, вызываемая при старте бота.

    Настраивает вебхук для бота Telegram.

    Args:
        bot (Bot): Экземпляр бота Telegram.
    """
    if config.webhook_base_url is not None:
        await bot.set_webhook(f'{config.webhook_base_url}{config.webhook_path}')
    else:
        async with ClientSession() as session:
            r = await session.get(f'http://{config.ngrok_host}:{config.ngrok_port}/api/tunnels')
            data = await r.json()
            ngrok_url = data.get('tunnels')[0].get('public_url')
        await bot.set_webhook(f'{ngrok_url}{config.webhook_path}')


async def on_shutdown(bot: Bot):
    """
    Функция, вызываемая при выключении бота.

    Удаляет вебхук у бота Telegram.

    Args:
        bot (Bot): Экземпляр бота Telegram.
    """
    await bot.delete_webhook()


def main():
    """
    Основная функция для запуска бота в режиме вебхук.

    Инициализирует диспетчер бота, устанавливает вебхук или запускает локальный туннель ngrok для вебхука.
    Запускает веб-сервер с использованием aiohttp.

    Raises:
        RuntimeError: Ошибка запуска веб-сервера.
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s | %(levelname)s : %(message)s')
    storage = RedisStorage.from_url(f'redis://{config.redis_host}:'
                                    f'{config.redis_port}/{config.redis_db}')
    dp = Dispatcher(storage=storage)
    dp.include_routers(common.router, support.router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    bot = Bot(token=config.bot_token.get_secret_value())
    app = web.Application()
    webhook_request_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    webhook_request_handler.register(app, path=config.webhook_path)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=config.web_server_host, port=int(config.web_server_port))


if __name__ == '__main__':
    main()
