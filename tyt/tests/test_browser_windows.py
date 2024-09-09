import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Switching between windows and tabs")
class TestBrowserWindows(BaseTest):

    @allure.title("Test switching")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_input_data(self):
        self.browser_windows_page.open()
        self.browser_windows_page.is_opened()
        self.browser_windows_page.check_main_word()
        self.browser_windows_page.click_new_tab_button()
        self.browser_windows_page.switch_new_tab(1)
        self.browser_windows_page.switch_new_tab(0)
        self.browser_windows_page.click_new_window_button()
        self.browser_windows_page.switch_new_tab(2)
        self.browser_windows_page.switch_new_tab(0)
        self.browser_windows_page.click_new_window_message_button()
        self.browser_windows_page.switch_new_tab(3)
        self.browser_windows_page.switch_new_tab(0)

