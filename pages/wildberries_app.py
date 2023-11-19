import subprocess
from base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement, Remote
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from colorama import Fore, Style

class Wildberries(BasePage):

    ACTIVITY = 'com.wildberries.ru/ru.wildberries.SplashActivity'
    APP_NAME_WILDBERIES = 'com.wildberries.ru'
    RADIO_BUTTON_RUSSIA = (AppiumBy.XPATH, '//android.widget.TextView[@text="Россия"]')
    SEARCH_ICON = (AppiumBy.CLASS_NAME, 'android.widget.Button')
    BUTTON_REMIND_ME_LATER = (AppiumBy.ID, 'com.wildberries.ru:id/remindLaterButton')


    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 60, 1)


    def open_and_add_localisation(self):
        # self.setup_app()
        self.delet_cash(self.APP_NAME_WILDBERIES)
        # self.open_activity(self.ACTIVITY)
        # self.click_obj(self.RADIO_BUTTON_RUSSIA)
        # self.click_obj(self.BUTTON_REMIND_ME_LATER)
        # self.check_element_located(self.SEARCH_ICON)
        # print(f'{Fore.YELLOW}Wildberries app is opened start page{Style.RESET_ALL}')






