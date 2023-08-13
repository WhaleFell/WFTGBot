from app import tg
from pyrogram import filters

__MODULE__ = "复读机模块"
__HELP__ = "私聊任何字符都会复读"


@tg.on_message()
async def echo(client, message):
    print("触发")
    print(message)
    # await message.reply(message.text)
