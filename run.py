from loguru import logger
from pyrogram import Client

from config import config
from jobs.scheduler import scheduler
from data.models import create_db_if_not_exists

plugins = dict(root="handlers")
app = Client(config.TELEGRAM_BOT_SESSION_NAME,
             api_id=config.TG_API_ID,
             api_hash=config.TG_API_HASH,
             bot_token=config.TELEGRAM_BOT_TOKEN,
             plugins=plugins)

# Запуск приложения
if __name__ == "__main__":
    create_db_if_not_exists()


    logger.info("Запускаю бота")

    scheduler.start()
    app.run()

    scheduler.shutdown()
