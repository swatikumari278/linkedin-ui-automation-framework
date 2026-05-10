"""
config_reader.py
----------------
Central access point for all configuration values read from config.ini.
No hard-coded values anywhere in the framework — everything goes through here.
"""

import configparser
import os

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.ini")


def _get_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(_CONFIG_PATH)
    return config


def get_linkedin_credentials() -> tuple[str, str]:
    """Return (email, password) for LinkedIn from config.ini."""
    config = _get_config()
    return (
        config["credentials"]["linkedin_email"],
        config["credentials"]["linkedin_password"],
    )


def get_base_url() -> str:
    """Return the base URL for the active environment."""
    config = _get_config()
    active_env = config["env"]["active_env"]
    return config["env"][f"base_url_{active_env}"]


def get_timeouts() -> dict:
    """Return timeout values as a dict with keys: implicit, explicit, page_load."""
    config = _get_config()
    return {
        "implicit":  int(config["timeouts"]["implicit_wait"]),
        "explicit":  int(config["timeouts"]["explicit_wait"]),
        "page_load": int(config["timeouts"]["page_load_timeout"]),
    }
