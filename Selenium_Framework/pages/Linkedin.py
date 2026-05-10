from Selenium_Framework.base.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import Selenium_Framework.utilities.CustomLogger as cl
import time

class LinkedinPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _signInButton="//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']" #xpath
    _email = "username" #id
    _password = "password" #id
    _linkedinSignIn="//button[@data-litms-control-urn='login-submit']" #xpath
    _startAPost="//strong[text()='Start a post']" #xpath
    _insidePost="//div[@data-placeholder='What do you want to talk about?']"
    _imgPost="//button[@aria-label='Add a photo']" #xpath
    _postButton="//span[contains(., 'Post')]" #xpath



    def clickOnLinkedinSignIn(self):
        self.clickOnElement(self._signInButton, "xpath")

    def clickOnUserName(self):
        self.clickOnElement(self._email, "id")

    def enterUserName(self, username):
        self.sendText(username, self._email, "id")

    def clickOnPassword(self):
        self.clickOnElement(self._password, "id")

    def enterPassword(self, password):
        self.sendText(password, self._password, "id")

    def clickOnSignIn(self):
        self.clickOnElement(self._linkedinSignIn, "xpath")

    def clickOnStartAPost(self):
        self.clickOnElement(self._startAPost, "xpath")

    def clickOnPost(self):
        self.clickOnElement(self._insidePost, "xpath")

    def enterContentOnLinkedIn(self,content):
        self.sendText(content,self._insidePost,locator_type="xpath")

    def clickOnPostButton(self):
        self.clickOnElement(self._postButton, "xpath")







