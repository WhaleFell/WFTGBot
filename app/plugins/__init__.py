import glob
from app.utils.log import logger
from os.path import basename, dirname, isfile
import importlib


def __list_all_modules():
    # This generates a list of modules in this
    # folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
        and not f.endswith("__main__.py")
    ]

    return all_modules


logger.info("IMPORTING MODULES")

ALL_MODULES = sorted(__list_all_modules())
importlib.import_module("app.plugins.__main__")
__all__ = ALL_MODULES + ["ALL_MODULES"]
