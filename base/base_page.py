import subprocess
from base.key_cods import KeyCodeForDevices, KeyKodeForApps
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement, Remote
from appium.webdriver.common.appiumby import AppiumBy
from colorama import Fore, Style
from time import sleep

class BasePage:

    FOLDER_AND_APP = "apps/wildberries-5-3-4000.apk"


    def __init__(self, driver:Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60, 1)


    def color_message_in_consol(self, name_function: str, text: str) -> None:
        print(f'\n{Fore.CYAN}Function: {name_function}{Style.RESET_ALL} (request) >>> {Fore.GREEN}{text}{Style.RESET_ALL}')


    def setup_app(self, preferences: str = None, permissions: str = None, checking_version: str = None):
        """Установка приложения с возможными дополнительными опциями

        Params:
            preferences: str = "-r" — сохранить данные приложения
            permissions: str = "-d" — выдать все запрашиваемые разрешения
            checking_version: str = "-g" — отключает проверку версии приложения

        """
        if preferences is None: preferences = ''
        if permissions is None: permissions =''
        if checking_version is None: checking_version = ''
        setup_comand = f'adb install {preferences} {permissions} {checking_version} {self.FOLDER_AND_APP}'
        print(setup_comand)
        self.start_adb_comand_and_check_request_status('setup_app', setup_comand)


    def start_adb_comand_and_check_request_status(self, name_func, adb_request: str) -> bool:
        """Проверка статуса применения adb команды"""
        try:
            obj = subprocess.check_output(adb_request, shell=True, stderr=subprocess.STDOUT, text=True)
            self.color_message_in_consol(name_func, obj)
            return True
        except subprocess.CalledProcessError as e:
            obj = e.output
            self.color_message_in_consol(name_func, obj)
            return False


    def delete_cache_and_application_data(self, app_name: str, preferences = None, permissions = None, checking_version = None) -> None:
        """Clear cash or installation app / очистит кеш или установит приложение из папки apps
        Params:
            app_name: str - 'com.wildberries.ru'
            preferences: str = "-r" — сохранить данные приложения
            permissions: str = "-d" — выдать все запрашиваемые разрешения
            checking_version: str = "-g" — отключает проверку версии приложения
        """
        command = f"adb shell pm clear {app_name}"
        if not self.start_adb_comand_and_check_request_status('delet_cash', command):
            self.setup_app(preferences=preferences, permissions=permissions, checking_version=checking_version)


    def open_activity(self, main_activity: str) -> None:
        """Открывает установленное приложение.
        Вывод текущего activity: adb shell am stack list
        Params: пример:
            main_activity: (str) - 'com.wildberries.ru/ru.wildberries.SplashActivity'

        """

        command = f"adb shell am start -n {main_activity}"
        obj = subprocess.run(command, shell=True, text=True)
        self.color_message_in_consol('open_activity', obj.args)




    def click_obj(self, locator: str) -> None:
        """Нажать по кликабельному объекту"""
        el: WebElement = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def check_element_located(self, locator: str) -> None:
        """
        Проверка видимости элемента

        Params:
            locator (str)
        """
        self.wait.until(EC.visibility_of_element_located(locator))


    def send(self, locator: str, text: str) -> None:
        """
        Ввод текста

        Params:
            locator (str)
            text (str) - yuor masage
        """
        el: WebElement = self.wait.until(EC.element_to_be_clickable(locator))
        el.send_keys(text)


    def swipe_too(self, target_direction: str = 'MOVE_UP', repeat: int = 1) -> None:
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


    def press_enter(self) -> None:
        # self.driver.is_keyboard_shown()
        ADB_ENTER = KeyKodeForApps.ADB_ENTER
        self.driver.press_keycode(ADB_ENTER)

    def press_home(self) -> None:
        ADB_HOME = KeyCodeForDevices.ADB_HOME
        self.driver.press_keycode(ADB_HOME)

    def press_back(self) -> None:
        ADB_BACK = KeyCodeForDevices.ADB_HOME
        self.driver.press_keycode(ADB_BACK)

