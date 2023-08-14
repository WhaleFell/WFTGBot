import sys
import os
import asyncio
from pathlib import Path
from app.utils.loadConfig import makeConfig
from app.utils.log import logger, getLogger
from pyrogram import Client, idle

ROOTPATH = Path(os.getcwd()).absolute()
# load config
CONF = makeConfig(Path(ROOTPATH, "config.yaml"))
# set log level
getLogger(CONF.log)
loop = asyncio.get_event_loop()

# Only preform check if your code will run on non-windows environments.
if sys.platform == 'win32':
    # Set the policy to prevent "Event loop is closed" error on Windows - https://github.com/encode/httpx/issues/914
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def mkAPP():
    if Path(ROOTPATH, "%s.session" % CONF.name).exists():
        logger.info("session exists!use session to login")
        return Client(
            name=CONF.name,
            api_id=CONF.api_id,
            api_hash=CONF.api_hash,
        )

    if CONF.session_str:
        logger.info("login by session string!")
        return Client(
            name=CONF.name,
            api_id=CONF.api_id,
            api_hash=CONF.api_hash,
            session_string=CONF.session_str,
            in_memory=True
        )

    if CONF.isUser:
        logger.info("use tg user login...requise login")
        return Client(
            name=CONF.name,
            api_id=CONF.api_id,
            api_hash=CONF.api_hash,
            in_memory=True
        )
    elif CONF.bot_token:
        logger.info("use tg bot login with bot_token..")
        return Client(
            name=CONF.name,
            bot_token=CONF.bot_token,
            api_id=CONF.api_id,
            api_hash=CONF.api_hash,
            in_memory=True
        )

    raise Exception("error to mk client!")


tg = mkAPP()
