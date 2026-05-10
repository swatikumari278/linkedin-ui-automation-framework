import unittest
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Selenium_Framework.pages.DashboardMenu import DashboardMenu
from Selenium_Framework.pages.LoginHRM import Login

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class DashboardMenuTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.login_page = Login(self.driver)
        self.menu = DashboardMenu(self.driver)

    def test_dashboard_menu_elements_are_displayed(self):
        self.login_page.login()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
        )
        assert self.menu.is_loaded(), "Dashboard page did not load after login"
        print("this is done")


        self.menu.verifyTimeButton()
        self.menu.verifyPIMButton()
        self.menu.verifyBuzzButton()
        self.menu.verifyAdminButton()
        self.menu.verifyLeaveButton()
        self.menu.verifyClaimButton()
        self.menu.verifyDashboardButton()
        self.menu.verifyMaintenanceButton()
        self.menu.verifyPerformanceButton()
        self.menu.verifyRecruitmentButton()
        self.menu.verifyMyInfoButton()
        self.menu.verifyDirectoryButton()
