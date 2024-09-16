import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Date picker")
class TestDatePicker(BaseTest):

    @allure.title("Input date")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_date_picker(self):
        self.date_picker_page.open()
        self.date_picker_page.is_opened()
        self.date_picker_page.check_main_word()
        self.date_picker_page.select_date()
        self.date_picker_page.select_date_and_time()
        time.sleep(3)