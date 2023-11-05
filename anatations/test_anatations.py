import pytest
from base.base_page import BasePage

class BaseAnatations:
    """Создание связи методов с разных страниц"""
    base_page: BasePage


    @pytest.fixture(autouse=True)
    def setup_anatations(self, request, driver):

        request.cls.driver = driver
        request.cls.base_page = BasePage(driver)


