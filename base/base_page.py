from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement, Remote
from time import sleep

class BasePage:
    CHROME = ('xpath', '//android.widget.TextView[@content-desc="Chrome"]')


    def __init__(self, driver:Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, 200, 1)


    def open_chrome(self):
        element = self.CHROME
        el: WebElement = self.wait.until(EC.element_to_be_clickable(element))
        el.click()
        sleep(2)
        a = self.driver.window_handles
        print(a)



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











    # wite = WebDriverWait(driver, 20, 1)
    # el = wite.until(EC.element_to_be_clickable(('xpath', '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]')))
    # el.click()
    # driver.press_keycode(4) # Домой


    # def test_find_battery(driver):
    #     el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    #     el.click()