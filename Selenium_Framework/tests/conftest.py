import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Selenium_Framework.utilities.config_reader import get_base_url, get_timeouts
from Selenium_Framework.pages.LoginHRM import Login

@pytest.fixture(scope="session")
def setup():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.page_load_strategy = 'normal'

    driver = webdriver.Chrome(options=options)

    timeouts = get_timeouts()
    driver.maximize_window()
    driver.set_page_load_timeout(timeouts["page_load"])
    driver.implicitly_wait(timeouts["implicit"])

    #driver.get(get_base_url())
    driver.get(get_base_url())
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def beforeClass(request, setup):
    request.cls.driver = setup  # Assign driver instance to test class
    yield
    # any class-level teardown here

@pytest.fixture(scope="function")
def beforeMethod(request):
    def beforeMethod(request):
        # Runs before each test method
        yield
        # Runs after each test method
