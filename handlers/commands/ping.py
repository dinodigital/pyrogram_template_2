import pyrogram
from loguru import logger
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(~filters.bot & filters.command("ping") & ~filters.channel & ~filters.group)
def ping(cli: Client, message: Message):
    logger.info(f"tg_id: '{message.from_user.id}'  msg: '{message.text}'")
    message.reply("pong")

    raise pyrogram.StopPropagation
