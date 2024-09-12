import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Check autocomplete")
class TestAutoComplete(BaseTest):

    @allure.title("Input auto complete")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_autocomplete(self):
        self.auto_complete_page.open()
        self.auto_complete_page.is_opened()
        self.auto_complete_page.check_main_word()
        self.auto_complete_page.input_multiple_field()
        self.auto_complete_page.input_single_field()
