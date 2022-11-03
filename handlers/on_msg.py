from loguru import logger
from pyrogram import Client, filters
from pyrogram.types import Message

from helpers import markup


@Client.on_message(~filters.bot & ~filters.channel & ~filters.group)
def on_message_handler(cli: Client, message: Message):
    """
    Когда боту приходит сообщение
    """
    chat_id = message.chat.id
    tg_id = message.from_user.id
    txt = message.text

    cli.send_message(chat_id, tg_id, txt, reply_markup=markup.with_close_btn())
