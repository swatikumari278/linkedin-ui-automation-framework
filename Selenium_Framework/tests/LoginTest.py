import pytest

from Selenium_Framework.pages.LoginHRM import Login
from Selenium_Framework.pages.DashboardMenu import DashboardMenu
from Selenium_Framework.utilities.config_reader import get_invalid_credentials

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestLogin:

    def test_valid_login_redirects_to_dashboard(self):
        login = Login(self.driver)
        login.login()  # reads valid credentials from config.ini

        dashboard = DashboardMenu(self.driver)
        assert dashboard.is_loaded(), "Dashboard page did not load after login"

    @pytest.mark.parametrize("username,password", [
        get_invalid_credentials(),  # from config.ini
        ("", ""),                   # blank both
        ("Admin", ""),              # blank password
        ("", "admin123")            # blank username
    ])
    def test_invalid_login_should_not_redirect(self, username, password):

        login = Login(self.driver)

        login.clickOnUserName()
        login.enterUserName(username)
        login.clickOnPassword()
        login.enterPassword(password)
        login.clickOnLoginButton()

        # Make sure we're not redirected to dashboard
        assert "dashboard" not in self.driver.current_url.lower(), "Unexpectedly redirected to dashboard"
