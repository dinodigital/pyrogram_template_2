import datetime as dt

from datetime import datetime
import pytz


def msk_now():
    tz = pytz.timezone('Europe/Moscow')  # <- сюда пишем часовой пояс
    return datetime.now(tz).replace(tzinfo=None)  # получаем локальное время


def msk_today_dm():
    now = msk_now()
    return now.strftime("%d.%m")


def msk_yesterday_dm():
    now = msk_now()
    yesterday = now - dt.timedelta(days=1)
    return yesterday.strftime("%d.%m")


def get_msk_time():
    """
    Время в формате 11.04.1989 11:00:00
    """
    tz = pytz.timezone('Europe/Moscow')  # <- сюда пишем часовой пояс
    now = datetime.now(tz)  # получаем локальное время
    msk_time = now.strftime('%H:%M:%S')  # форматируем
    return msk_time


def get_msk_time_lite():
    """
    Время в формате 11.04.1989 11:00:00
    """
    tz = pytz.timezone('Europe/Moscow')  # <- сюда пишем часовой пояс
    now = datetime.now(tz)  # получаем локальное время
    msk_time = now.strftime('%H:%M')  # форматируем
    return msk_time


def get_datetime_now_msk():
    tz = pytz.timezone('Europe/Moscow')  # <- сюда пишем часовой пояс
    return datetime.now(tz)  # получаем локальное время


def get_hm(dt):
    """
    Часы:Минуты (18:45)

    :param dt: datetime object
    """
    return dt.strftime('%H:%M')
