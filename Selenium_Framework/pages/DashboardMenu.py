from Selenium_Framework.base.BasePage import BasePage
import Selenium_Framework.utilities.CustomLogger as cl

class DashboardMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators  values in Contact form page

    _menuOpen = "//button[@fdprocessedid='qqvdy9']" #xpath
    _searchButton = "//input[@placeholder='Search']" #xpath
    _adminButton = "//span[text()='Admin']" #xpath
    _pimButton = "//span[text()='PIM']"
    _leaveButton = "//span[text()='Leave']"
    _timeButton = "//span[text()='Time']"
    _recruitmentButton = "//span[text()='Recruitment']"
    _myInfoButton ="//span[text()='My Info']"
    _performanceButton ="//span[text()='Performance']"
    _dashboardButton = "//span[text()='Dashboard']"
    _directoryButton = "//span[text()='Directory']"
    _maintenanceButton = "//span[text()='Maintenance']"
    _claimButton = "//span[text()='Claim']"
    _buzzButton = "//span[text()='Buzz']"


    def clickOnMenu(self):
        self.clickOnElement(self._menuOpen, "xpath")

    def verifySearchButton(self):
        element = self.isElementDisplayed(self._searchButton, "xpath")
        assert element == True

    def verifyAdminButton(self):
        element = self.isElementDisplayed(self._adminButton, "xpath")
        assert element == True

    def verifyPIMButton(self):
        element = self.isElementDisplayed(self._pimButton, "xpath")
        assert element == True

    def verifyLeaveButton(self):
        element = self.isElementDisplayed(self._leaveButton, "xpath")
        assert element == True

    def verifyTimeButton(self):
        element = self.isElementDisplayed(self._timeButton, "xpath")
        assert element == True

    def verifyRecruitmentButton(self):
        element = self.isElementDisplayed(self._recruitmentButton, "xpath")
        assert element == True

    def verifyMyInfoButton(self):
        element = self.isElementDisplayed(self._myInfoButton, "xpath")
        assert element == True

    def verifyPerformanceButton(self):
        element = self.isElementDisplayed(self._performanceButton, "xpath")
        assert element == True

    def verifyDashboardButton(self):
        element = self.isElementDisplayed(self._dashboardButton, "xpath")
        assert element == True

    def verifyDirectoryButton(self):
        element = self.isElementDisplayed(self._directoryButton, "xpath")
        assert element == True

    def verifyMaintenanceButton(self):
        element = self.isElementDisplayed(self._maintenanceButton, "xpath")
        assert element == True

    def verifyClaimButton(self):
        element = self.isElementDisplayed(self._claimButton, "xpath")
        assert element == True

    def verifyBuzzButton(self):
        element = self.isElementDisplayed(self._buzzButton, "xpath")
        assert element == True

    def is_loaded(self):
        # Check if the Dashboard page is loaded by verifying a unique dashboard element is visible
        return self.isElementDisplayed(self._dashboardButton, "xpath")







