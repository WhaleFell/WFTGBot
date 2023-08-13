from app import CONF, logger, tg
from pyrogram import Client, filters
from pyrogram.types import Message


@tg.on_message(filters=filters.command("start"))
async def start(client: Client, message: Message):
    await tg.send_message(
        chat_id=message.chat.id,
        text=CONF.bot_desc,
        reply_to_message_id=message.id
    )
