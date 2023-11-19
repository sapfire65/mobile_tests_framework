import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from time import sleep


capabilities = dict(
    # app=os.path.abspath('apps/wildberries-5-3-4000.apk'),
    # appPackage='com.android.settings',
    # appActivity='.Settings',
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'

@pytest.fixture()
def driver(request):
    app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    request.cls.driver = app_driver
    # app_driver.press_keycode(3)  # Домой
    sleep(1)
    yield app_driver
    # app_driver.press_keycode(3)  # Домой
    app_driver.quit()


