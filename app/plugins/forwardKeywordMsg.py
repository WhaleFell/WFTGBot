from app import CONF, logger, tg
from pyrogram import Client, filters
from pyrogram.types import Message
from app.utils.helper import generate_regex

regex = generate_regex(generate_regex(CONF.KeyMonitor.keywords))


@tg.on_message(filters=filters.text & filters.regex(regex))
async def forwardKeyworkMessageToMe(client: Client, message: Message):
    for fid in CONF.KeyMonitor.forword_id:
        await message.forward(chat_id=fid)
        logger.success(
            "catch key forward: %s to:%s" %
            (message.text[:10].strip(), fid)
        )
