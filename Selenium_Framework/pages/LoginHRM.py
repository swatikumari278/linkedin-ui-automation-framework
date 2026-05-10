from Selenium_Framework.base.BasePage import BasePage
from Selenium_Framework.utilities.config_reader import get_valid_credentials
from Selenium_Framework.utilities.config_reader import get_linkedin_credentials
import Selenium_Framework.utilities.CustomLogger as cl

class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _userNamePageLocator = "username"  # name
    _passwordPageLocator = "password"  # name
    _loginPagelocator = "//button[@type='submit']"  # xpath
    _dashboardTitleLocator = "//h6[text()='Dashboard']"

    def clickOnUserName(self):
        self.clickOnElement(self._userNamePageLocator, "name")

    def enterUserName(self, username):
        self.sendText(username, self._userNamePageLocator, "name")

    def clickOnPassword(self):
        self.clickOnElement(self._passwordPageLocator, "name")

    def enterPassword(self, password):
        self.sendText(password, self._passwordPageLocator, "name")

    def clickOnLoginButton(self):
        self.clickOnElement(self._loginPagelocator, "xpath")

    def verifyDashboard(self):
        element = self.isElementDisplayed(self._dashboardTitleLocator, "xpath")
        assert element is True

    def login(self):
        username, password = get_valid_credentials()  # read from config
        self.clickOnUserName()
        self.enterUserName(username)
        self.clickOnPassword()
        self.enterPassword(password)
        self.clickOnLoginButton()



