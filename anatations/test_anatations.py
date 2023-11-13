import pytest
from base.base_page import BasePage
from pages.wildberries_app import Wildberries

class BaseAnatations:
    """Создание связи методов с разных страниц"""
    base_page: BasePage
    wildberries_app: Wildberries



    @pytest.fixture(autouse=True)
    def setup_anatations(self, request, driver):

        request.cls.driver = driver
        request.cls.base_page = BasePage(driver)
        request.cls.wildberries_app = Wildberries(driver)

