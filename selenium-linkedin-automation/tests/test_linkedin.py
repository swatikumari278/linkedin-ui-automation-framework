"""
test_linkedin.py
----------------
Test suite covering LinkedIn sign-in and post creation flows.
Uses Page Object Model — no raw Selenium calls inside test methods.

Test order:
    1. test_sign_in_navigates_to_feed  — authenticates and verifies the feed loads
    2. test_create_text_post           — creates a text post using the active session
"""

import os
import unittest
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.linkedin_page import LinkedInPage
from utilities.config_reader import get_linkedin_credentials


POST_CONTENT_FILE = os.path.join(os.path.dirname(__file__), "post_content", "input_text.txt")


@pytest.mark.usefixtures("before_class")
class TestLinkedIn(unittest.TestCase):
    """End-to-end test suite for LinkedIn sign-in and post creation."""

    @pytest.fixture(autouse=True)
    def init_page(self):
        self.linkedin = LinkedInPage(self.driver)

    # ── Helpers ────────────────────────────────────────────────────────────
    def _ensure_logged_in(self) -> None:
        """Log in if the current session is not already on the feed page."""
        if "feed" not in self.driver.current_url:
            email, password = get_linkedin_credentials()
            self.linkedin.login(email, password)
            WebDriverWait(self.driver, 20).until(EC.url_contains("feed"))

    def _read_post_content(self) -> str:
        """Read post text from the external content file."""
        assert os.path.isfile(POST_CONTENT_FILE), \
            f"Post content file not found: {POST_CONTENT_FILE}"
        with open(POST_CONTENT_FILE, "r", encoding="utf-8") as f:
            return f.read()

    # ── Tests ──────────────────────────────────────────────────────────────
    def test_sign_in_navigates_to_feed(self):
        """
        GIVEN a user with valid LinkedIn credentials
        WHEN they complete the sign-in flow
        THEN the LinkedIn feed should load and the post prompt should be visible
        """
        email, password = get_linkedin_credentials()
        self.linkedin.login(email, password)

        WebDriverWait(self.driver, 20).until(EC.url_contains("feed"))
        assert self.linkedin.is_logged_in(), \
            "Login succeeded but feed indicator was not found on the page."

    def test_create_text_post(self):
        """
        GIVEN a logged-in LinkedIn user
        WHEN they create a post with text read from post_content/input_text.txt
        THEN the post should be submitted successfully
        """
        self._ensure_logged_in()
        content = self._read_post_content()
        self.linkedin.create_post(content)
