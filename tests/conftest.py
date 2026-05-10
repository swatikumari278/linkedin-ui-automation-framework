"""
conftest.py
-----------
pytest fixtures for the LinkedIn automation suite.
Driver setup and teardown are handled here so every test class
receives a ready-to-use WebDriver instance.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.config_reader import get_base_url, get_timeouts, get_linkedin_credentials


def _build_chrome_options() -> Options:
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.page_load_strategy = "normal"
    return options


@pytest.fixture(scope="session")
def driver():
    """
    Session-scoped Chrome WebDriver.
    Selenium Manager handles chromedriver automatically — no manual path needed.
    """
    options = _build_chrome_options()
    _driver = webdriver.Chrome(options=options)

    timeouts = get_timeouts()
    _driver.maximize_window()
    _driver.set_page_load_timeout(timeouts["page_load"])
    _driver.implicitly_wait(timeouts["implicit"])
    _driver.get(get_base_url())

    yield _driver
    _driver.quit()


@pytest.fixture(scope="class")
def before_class(request, driver):
    """Inject the shared driver instance into each test class."""
    request.cls.driver = driver
    yield


@pytest.fixture(scope="session")
def linkedin_credentials():
    """Provide LinkedIn credentials from config (never hard-coded in tests)."""
    email, password = get_linkedin_credentials()
    return email, password
