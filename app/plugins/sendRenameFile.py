# send rename file
from app import CONF, logger, tg
from pyrogram import Client, filters
from pyrogram.types import Message
from typing import BinaryIO
import io
from pathlib import Path
import os
import datetime
import asyncio

user = None


async def get_bot_info():
    global user
    user = await tg.get_me()

# 获取当前运行中的事件循环
loop = asyncio.get_running_loop()
# 指派到当前运行的事件循环中
asyncio.ensure_future(get_bot_info(), loop=loop)


def is_empty_string(string, specified_variable):
    if string == "":
        return True
    if string.isspace():
        return True
    if string == specified_variable:
        return True

    return False


async def filtersNoRule(app: Client, message: Message):
    file_name = message.text.split(
        f"/gm")[1].strip()
    if is_empty_string(file_name, f"@{user.username}"):
        await message.reply(
            text="请以 /gm+空格+要改的毒包名字的格式发给我"
        )
        return False
    return file_name


def read_file() -> BinaryIO:
    filePath = Path(CONF.RenameFile.file_path).absolute()

    with open(str(filePath), "rb") as f:
        return io.BytesIO(f.read())


def get_file_modified_time(file_path):
    timestamp = os.path.getmtime(file_path)
    modified_time = datetime.datetime.fromtimestamp(timestamp)
    # Subtracting 8 hours to convert to UTC+8
    utc_time = modified_time + datetime.timedelta(hours=8)
    formatted_time = utc_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


@tg.on_message(filters.text & filters.command("gm"))
async def handle_private_message(client: Client, message: Message):
    logger.info("sendRenameFile:", message.chat.username, message.text)
    file_name = await filtersNoRule(tg, message)
    if not file_name:
        return

    file_content = read_file()

    await client.send_document(
        chat_id=message.chat.id,
        document=file_content,
        file_name="%s.zip" % file_name,
        caption=CONF.RenameFile.file_desc.format(
            update_time=get_file_modified_time(CONF.RenameFile.file_path)),
        reply_to_message_id=message.id
    )
