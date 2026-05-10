"""
base_page.py
------------
Base class for all Page Objects. Provides reusable Selenium interactions
with explicit waits and a unified locator resolution strategy.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config_reader import get_timeouts


class BasePage:
    """Reusable base class inherited by all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, get_timeouts()["explicit"])

    # ── Locator resolution ─────────────────────────────────────────────────
    def _get_by(self, locator_type: str) -> By:
        """Map a locator type string to a Selenium By strategy."""
        mapping = {
            "id":    By.ID,
            "name":  By.NAME,
            "xpath": By.XPATH,
            "css":   By.CSS_SELECTOR,
            "tag":   By.TAG_NAME,
            "class": By.CLASS_NAME,
        }
        by = mapping.get(locator_type.lower())
        if not by:
            raise ValueError(f"Unsupported locator type: '{locator_type}'. "
                             f"Valid options: {list(mapping.keys())}")
        return by

    # ── Core interactions ──────────────────────────────────────────────────
    # All methods follow the same argument order as Selenium's own API:
    #   find_element(By.XPATH, "//value")  →  (locator_type, locator)
    # Locator tuples in page objects are therefore defined as ("type", "value")
    # and unpacked with * so the order always stays consistent.

    def click(self, locator_type: str, locator: str) -> None:
        """Wait for element to be clickable, then click it.

        Args:
            locator_type: Selector strategy — one of: id, name, xpath, css, tag, class
            locator:      The selector value, e.g. "//button[@type='submit']"
        """
        element = self.wait.until(
            EC.element_to_be_clickable((self._get_by(locator_type), locator))
        )
        element.click()

    def type_text(self, text: str, locator_type: str, locator: str) -> None:
        """Clear the field and type text into a visible element.

        Args:
            text:         The string to type into the element
            locator_type: Selector strategy — one of: id, name, xpath, css, tag, class
            locator:      The selector value
        """
        element = self.wait.until(
            EC.visibility_of_element_located((self._get_by(locator_type), locator))
        )
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator_type: str, locator: str) -> bool:
        """Return True if element is visible within the explicit wait timeout.

        Args:
            locator_type: Selector strategy — one of: id, name, xpath, css, tag, class
            locator:      The selector value
        """
        try:
            self.wait.until(
                EC.visibility_of_element_located((self._get_by(locator_type), locator))
            )
            return True
        except Exception:
            return False

    def get_text(self, locator_type: str, locator: str) -> str:
        """Return visible text of an element.

        Args:
            locator_type: Selector strategy — one of: id, name, xpath, css, tag, class
            locator:      The selector value
        """
        element = self.wait.until(
            EC.visibility_of_element_located((self._get_by(locator_type), locator))
        )
        return element.text
