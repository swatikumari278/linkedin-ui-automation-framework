import configparser
import os

def get_config():
    config = configparser.ConfigParser()
    path = os.path.join(os.path.dirname(__file__), '../config/config.ini')
    config.read(path)
    return config

def get_valid_credentials():
    config = get_config()
    return config["credentials"]["valid_username"], config["credentials"]["valid_password"]

def get_linkedin_credentials():
    config = get_config()
    return config["credentials"]["linkedin_username"], config["credentials"]["linkedin_password"]

def get_invalid_credentials():
    config = get_config()
    return config["credentials"]["invalid_username"], config["credentials"]["invalid_password"]

def get_base_url():
    config = get_config()
    active_env = config["env"]["active_env"]
    return config["env"][f"base_url_{active_env}"]

def get_timeouts():
    config = get_config()
    return {
        "implicit": int(config["timeouts"]["implicit_wait"]),
        "explicit": int(config["timeouts"]["explicit_wait"]),
        "page_load": int(config["timeouts"]["page_load_timeout"]),
    }

def get_test_data(key):
    config = get_config()
    return config["testdata"].get(key)
