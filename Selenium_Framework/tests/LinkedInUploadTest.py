import unittest
import pytest
from Selenium_Framework.pages.Linkedin import LinkedinPage
from Selenium_Framework.utilities.config_reader import get_linkedin_credentials
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestLinkedIn(unittest.TestCase):  # Optional: prefix class name with Test

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.link = LinkedinPage(self.driver)

    def test_linkedin_sign_in(self):
        linkedin_username, linkedin_password = get_linkedin_credentials()
        self.link.clickOnLinkedinSignIn()
        self.link.clickOnUserName()
        self.link.enterUserName(linkedin_username)
        self.link.clickOnPassword()
        self.link.enterPassword(linkedin_password)
        self.link.clickOnSignIn()

    def test_Post_Text_Content(self):
        self.test_linkedin_sign_in()
        WebDriverWait(self.driver, 10).until(EC.url_contains("feed/?trk=guest_homepage-basic_nav-header-signin"))
        self.link.clickOnStartAPost()
        self.link.clickOnPost()
        with open("Post_Content/input_text.txt", "r", encoding="utf-8") as file:
            notepad_text = file.read()
        self.link.enterContentOnLinkedIn(notepad_text)
        self.driver.implicitly_wait(20)  # Wait up to 10 seconds for elements to appear
        self.link.clickOnPostButton()





