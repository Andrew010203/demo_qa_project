import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Work with modal dialogs")
class TestModalDialogs(BaseTest):

    @allure.title("Test select modal dialogs")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_modal_dialogs(self):
        self.modal_dialogs_page.open()
        self.modal_dialogs_page.is_opened()
        self.modal_dialogs_page.check_main_word()
        self.modal_dialogs_page.click_small_modal_button()
        self.modal_dialogs_page.click_close_small_modal_button()
        self.modal_dialogs_page.click_large_modal_button()
