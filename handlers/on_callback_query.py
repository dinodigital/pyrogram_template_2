import pyrogram
from loguru import logger
from pyrogram import Client
from pyrogram.types import CallbackQuery, Message

from config import const


@pyrogram.Client.on_callback_query()
def callback_handler(cli: Client, q: CallbackQuery):
    chat_id = q.from_user.id
    msg_id = q.message.id

    if q.data == const.DELETE_MSG:
        q.message.delete()
