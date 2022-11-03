from loguru import logger
from pyrogram import Client

from config.config import TELEGRAM_BOT_TOKEN, TG_API_ID, TG_API_HASH
from jobs.scheduler import scheduler
from data.models import create_db_if_not_exists

plugins = dict(root="handlers")
app = Client("MyBot",
             api_id=TG_API_ID,
             api_hash=TG_API_HASH,
             bot_token=TELEGRAM_BOT_TOKEN,
             plugins=plugins)

# Запуск приложения
if __name__ == "__main__":
    create_db_if_not_exists()


    logger.info("Запускаю бота")

    scheduler.start()
    app.run()

    scheduler.shutdown()
