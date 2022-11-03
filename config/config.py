from dotenv import load_dotenv, find_dotenv
import os

from pathlib import Path

load_dotenv(find_dotenv())

USER_DB_NAME = "user.db"

ROOT_DIR = Path(__file__).resolve().parent.parent
USER_DB_PATH = os.path.join(ROOT_DIR, f"data/{USER_DB_NAME}")


TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TG_API_ID = int(os.environ.get('TG_API_ID'))
TG_API_HASH = os.environ.get('TG_API_HASH')

