import pathlib
from datetime import datetime

import peewee
from loguru import logger

from config.config import USER_DB_NAME, USER_DB_PATH

user_db = peewee.SqliteDatabase(USER_DB_PATH)


class BaseModel(peewee.Model):
    class Meta:
        database = user_db


class User(BaseModel):
    created = peewee.DateTimeField(default=datetime.now)
    tg_id = peewee.IntegerField(default=None, null=True)


def create_db_if_not_exists():
    """
    Создает новую базу данных SQLite, если такой нет
    """
    logger.info(f"Проверяю наличие базы данных: {USER_DB_NAME}")

    # Проверка на наличие файла БД
    if pathlib.Path(USER_DB_PATH).exists():
        logger.info(f"База данных найдена")
        return False

    # Создание БД
    logger.info(f"База данных не найдена. Создаю новую.")
    my_db = peewee.SqliteDatabase(USER_DB_PATH)
    my_db.connect()
    my_db.create_tables([User, ])  # Тут таблицы, которые создаем
    my_db.close()
    return True
