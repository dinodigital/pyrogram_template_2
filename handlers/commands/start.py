from pyrogram import Client, filters
from pyrogram.types import Message

from helpers import markup
from data.models import User


@Client.on_message(~filters.bot & filters.command("start") & ~filters.channel & ~filters.group)
def start(cli: Client, message: Message):
    chat_id = message.chat.id
    tg_id = message.from_user.id

    user, is_created = User.get_or_create(tg_id=tg_id)

    if is_created:
        txt = "Привет, новенький"
    else:
        txt = "Привет. А я тебя знаю!"

    msg_1: Message = cli.send_message(chat_id, txt, reply_markup=markup.with_close_btn())

