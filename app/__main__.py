import asyncio
from app import CONF, logger, tg, plugins
from pyrogram import idle
from app.plugins import ALL_MODULES
import importlib
from contextlib import closing, suppress
from pyrogram import filters
from pyrogram.handlers.message_handler import MessageHandler

HELPABLE = {}


@logger.catch()
async def start_bot():

    # 动态 import
    # for module in ALL_MODULES:
    #     imported_module = importlib.import_module("app.plugins." + module)
    #     if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
    #         imported_module.__MODULE__ = imported_module.__MODULE__
    #         if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
    #             HELPABLE[
    #                 imported_module.__MODULE__.replace(" ", "_").lower()
    #             ] = imported_module

    logger.success(f"found plugins...{ALL_MODULES}")

    await tg.start()
    logger.info(f"BOT STARTED AS {CONF.name}!")

    # ===== loading pluging ========
    from app.plugins import start
    from app.plugins import customCommand

    if CONF.KeyMonitor.enable:
        from app.plugins import forwardKeywordMsg
        logger.info("forwardKeywordMsg load")
    if CONF.RenameFile.enable:
        from app.plugins import sendRenameFile
        logger.info("sendRenameFile load")

    # ===== loading pluging ending ========

    global user
    user = await tg.get_me()

    logger.success(
        f"login Account Success user:{user.first_name} phone_number:{user.phone_number}"
    )

    await idle()  # 堵塞

    await tg.stop()


def main():
    # 一定要在当前文件获取事件循环
    # must get the event loop in the file
    loop = asyncio.get_event_loop()
    with closing(loop):
        with suppress(asyncio.exceptions.CancelledError):
            loop.run_until_complete(start_bot())
        loop.run_until_complete(asyncio.sleep(3.0))  # task cancel wait 等待任务结束


if __name__ == "__main__":
    main()
