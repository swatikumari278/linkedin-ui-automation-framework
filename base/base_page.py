from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _get_by(self, locator_type):
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
            raise ValueError(
                f"Unsupported locator type: '{locator_type}'. "
                "Valid options: ['id', 'name', 'xpath', 'css', 'tag', 'class']"
            )

    def click(self, locator_type, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((self._get_by(locator_type), locator))
        )
        element.click()

    def type_text(self, locator_type, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located((self._get_by(locator_type), locator))
        )
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator_type, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located((self._get_by(locator_type), locator))
            )
            return True
        except Exception:
            return False

    def get_text(self, locator_type, locator):
        element = self.wait.until(
            EC.visibility_of_element_located((self._get_by(locator_type), locator))
        )
        return element.text