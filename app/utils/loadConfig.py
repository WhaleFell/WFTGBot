from app.models import Config
from app.utils.log import logger
import yaml
from pathlib import Path

def makeConfig(y:Path)->Config:
    # y = Path(ROOTPATH, "config.yaml")
    if not y.exists():
        logger.critical(f"{y} file not found! generate default config!")
        with open(str(y), "w", encoding="utf8") as f:
            yaml.dump(
                Config().model_dump(), f,
                default_flow_style=False, encoding='utf-8', allow_unicode=True, sort_keys=False
            )
        raise Exception(f"{y} file not found!")
    try:
        with open(str(y), "r", encoding="utf8") as r:
            conf = yaml.safe_load(r)
            c = Config(**conf)
            logger.info(f"load {y} Success!")
            logger.debug(f"load config:{c.model_dump()}")
            return c
    except Exception as e:
        logger.critical(f"load {y} error:{e}")
        logger.exception(f"详细错误！")
        raise Exception("load config.yaml error!")


