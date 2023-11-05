import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os

capabilities = dict(
    # app=os.path.abspath('apk_files/wildberries-5-3-4000.apk'),
    # appPackage='com.android.settings',
    #appActivity='.Settings',
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'

@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app_driver
    app_driver.quit()

def test_find_battery(driver):
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()


