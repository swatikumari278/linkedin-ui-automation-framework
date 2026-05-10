from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium_Framework.utilities.config_reader import get_timeouts

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, get_timeouts()["explicit"])

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

    def clickOnElement(self, locator, locator_type):
        by_type = self.get_by_type(locator_type)
        element = self.wait.until(EC.element_to_be_clickable((by_type, locator)))
        element.click()

    def sendText(self, text, locator, locator_type):
        by_type = self.get_by_type(locator_type)
        element = self.wait.until(EC.visibility_of_element_located((by_type, locator)))
        element.clear()
        element.send_keys(text)

    def isElementDisplayed(self, locator, locator_type):
        by_type = self.get_by_type(locator_type)
        try:
            self.wait.until(EC.visibility_of_element_located((by_type, locator)))
            return True
        except:
            return False
