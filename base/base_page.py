import subprocess
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement, Remote
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

class BasePage:

    ACTIVITY = 'com.wildberries.ru/ru.wildberries.SplashActivity'
    APP_NAME = 'com.wildberries.ru'

    CHROME = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Chrome"]')
    LOGO_GOOGLE = (AppiumBy.CLASS_NAME, 'android.widget.FrameLayout')
    SEARSH_INPUT = (AppiumBy.ID, 'com.android.chrome:id/search_box_text')


    def __init__(self, driver:Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 1)


    def open_activity(self, main_activity):
        """Открывает установленное приложение.
        Вывод текущего activity: adb shell am stack list
        Params: пример:
            main_activity: (str) - 'com.wildberries.ru/ru.wildberries.SplashActivity'

        """
        command = f"adb shell am start -n {main_activity}"
        subprocess.run(command, shell=True)

    def delet_cash(self, app_name):
        """Clear cash"""
        command = f"adb shell pm clear {app_name}"
        print(command)
        subprocess.run(command, shell=True)

    def open_wildberries(self):
        self.open_activity(self.ACTIVITY)


    def click_obj(self, locator):
        """Нажать по кликабельному объекту"""
        el: WebElement = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def check_element_located(self, locator: str):
        """
        Проверка видимости элемента

        Params:
            locator (str)
        """
        self.wait.until(EC.visibility_of_element_located(locator))


    def send(self, locator: str, text: str):
        """
        Ввод текста

        Params:
            locator (str)
            text (str) - yuor masage
        """
        el: WebElement = self.wait.until(EC.element_to_be_clickable(locator))
        el.send_keys(text)

    def press_enter(self):
        # self.driver.is_keyboard_shown()
        self.driver.press_keycode(66)
        sleep(2)


    def swipe_too(self, target_direction: str = 'MOVE_UP', repeat: int = 1):
        """
        Params:
            target_direction - (str) 'MOVE_UP'
            target_direction - (str) 'MOVE_DOWN'
            target_direction - (str) 'MOVE_LEFT'
            target_direction - (str) 'MOVE_RIGHT'
            repeat: (int) - number of swipes
        """
        for i in range(repeat):
            if target_direction == 'MOVE_UP':
                self.driver.swipe(750, 2000, 750, 700, duration=1000) # swaip_up
            elif target_direction == 'MOVE_DOWN':
                self.driver.swipe(750, 750, 750, 2000, duration=1000) # swaip_down
            elif target_direction == 'MOVE_LEFT':
                self.driver.swipe(1200, 1000, 200, 1000, duration=1000) # swaip_down
            elif target_direction == 'MOVE_RIGHT':
                self.driver.swipe(200, 1000, 1200, 1000, duration=1000) # swaip_down


    def open_chrome(self):
        self.click_obj(self.CHROME)
        self.check_element_located(self.LOGO_GOOGLE)
        self.send(locator=self.SEARSH_INPUT, text='Hoo Hoo Hoo')
        self.press_enter()
        sleep(5)

    def wildberries(self):
        self.open_wildberries()











    # wite = WebDriverWait(driver, 20, 1)
    # el = wite.until(EC.element_to_be_clickable(('xpath', '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]')))
    # el.click()
    # driver.press_keycode(4) # Домой


    # def test_find_battery(driver):
    #     el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    #     el.click()