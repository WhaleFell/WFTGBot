from loguru import logger
import sys


def getLogger(loglevel):
    logger.remove()
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:HH:mm:ss}</green> | {name}:{function} {level} | <level>{message}</level>",
        level=loglevel,
        backtrace=True,
        diagnose=True
    )


# default level
getLogger("DEBUG")
