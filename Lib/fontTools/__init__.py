import logging
from fontTools.misc.loggingTools import configLogger

log = logging.getLogger(__name__)

version = __version__ = "4.25.1.dev0"

__all__ = ["version", "log", "configLogger"]
