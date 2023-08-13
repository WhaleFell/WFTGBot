from app import CONF, logger, tg
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers.message_handler import MessageHandler
import asyncio


def mk_custom_command_handle(customText: str) -> asyncio.coroutines:
    async def customHandle(client: Client, message: Message):
        logger.info("custom_command:", message.chat.username, message.text)
        await client.send_message(
            chat_id=message.chat.id,
            text=customText,
            reply_to_message_id=message.id
        )

    return customHandle


for cc in CONF.CustomCommands:
    tg.add_handler(
        MessageHandler(
            mk_custom_command_handle(cc.text),
            filters=filters.command(cc.command)
        )
    )
    logger.debug(f"add custom AQ: /{cc.command} -> {cc.text}  desc: {cc.desc}")
