"""
linkedin_page.py
----------------
Page Object for LinkedIn — covers sign-in flow and post creation.
All locators are centralised at the top of the class.
"""

from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.logger import get_logger

log = get_logger(__name__)


class LinkedInPage(BasePage):
    """Encapsulates all LinkedIn UI interactions."""

    # ── Locators ───────────────────────────────────────────────────────────
    # Sign-in flow
    _SIGN_IN_BTN    = ("xpath", "//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']")
    _EMAIL_FIELD    = ("id",    "username")
    _PASSWORD_FIELD = ("id",    "password")
    _SUBMIT_BTN     = ("xpath", "//button[@data-litms-control-urn='login-submit']")

    # Feed / post creation
    _START_POST_BTN  = ("xpath", "//strong[text()='Start a post']")
    _POST_TEXT_AREA  = ("xpath", "//div[@data-placeholder='What do you want to talk about?']")
    _POST_SUBMIT_BTN = ("xpath", "//span[contains(., 'Post')]")

    # Post-login verification
    _FEED_INDICATOR  = ("xpath", "//span[contains(text(),'Start a post')]")

    def __init__(self, driver):
        super().__init__(driver)

    # ── Authentication ─────────────────────────────────────────────────────
    def click_sign_in(self) -> None:
        """Click the Sign In link on the LinkedIn homepage."""
        log.info("Clicking Sign In button on homepage")
        self.click(*self._SIGN_IN_BTN)

    def enter_email(self, email: str) -> None:
        log.info("Entering email address")
        self.type_text(email, *self._EMAIL_FIELD)

    def enter_password(self, password: str) -> None:
        log.info("Entering password")
        self.type_text(password, *self._PASSWORD_FIELD)

    def submit_login(self) -> None:
        log.info("Submitting login form")
        self.click(*self._SUBMIT_BTN)

    def login(self, email: str, password: str) -> None:
        """Full login flow: navigate to sign-in, enter credentials, submit."""
        self.click_sign_in()
        self.enter_email(email)
        self.enter_password(password)
        self.submit_login()

    def is_logged_in(self) -> bool:
        """Return True if the feed page loaded successfully after login."""
        return self.is_displayed(*self._FEED_INDICATOR)

    # ── Post creation ──────────────────────────────────────────────────────
    def click_start_a_post(self) -> None:
        log.info("Clicking 'Start a post'")
        self.click(*self._START_POST_BTN)

    def enter_post_content(self, content: str) -> None:
        log.info("Typing post content")
        self.click(*self._POST_TEXT_AREA)
        self.type_text(content, *self._POST_TEXT_AREA)

    def submit_post(self) -> None:
        log.info("Submitting post")
        self.click(*self._POST_SUBMIT_BTN)

    def create_post(self, content: str) -> None:
        """Full post creation flow."""
        self.click_start_a_post()
        self.enter_post_content(content)
        self.submit_post()
