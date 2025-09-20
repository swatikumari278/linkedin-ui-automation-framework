from Selenium_Framework.base.DriverClass import WebDriveClass
import  Selenium_Framework.utilities.CustomLogger as cl
import time

wd = WebDriveClass()
driver = wd.getWebDriver("chrome")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
log = cl.customLogger()
log.info("web page launched")
time.sleep(2)
driver.quit()