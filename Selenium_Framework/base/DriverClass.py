from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
class WebDriveClass:
    def getWebDriver(self, browserName):
        if browserName.lower() == "chrome":
            service = Service(r"C:\Users\Admin\Desktop\Selenium_Framework_Python\Selenium_Framework\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
            options = Options()
            driver = webdriver.Chrome(service=service, options=options)
            return driver


