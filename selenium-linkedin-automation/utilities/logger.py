"""
logger.py
---------
Provides a reusable logger factory for the entire framework.
Logs are written to reports/automation.log relative to the project root.
"""

import logging
import os

_LOG_DIR  = os.path.join(os.path.dirname(__file__), "..", "reports")
_LOG_FILE = os.path.join(_LOG_DIR, "automation.log")

os.makedirs(_LOG_DIR, exist_ok=True)

_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATE_FMT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG,
    format=_FORMAT,
    datefmt=_DATE_FMT,
    handlers=[
        logging.FileHandler(_LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def get_logger(name: str) -> logging.Logger:
    """
    Return a named logger. Call this at the top of each module:
        from utilities.logger import get_logger
        log = get_logger(__name__)
    """
    return logging.getLogger(name)
