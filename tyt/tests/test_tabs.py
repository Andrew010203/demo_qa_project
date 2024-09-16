import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Tabs")
class TestTabs(BaseTest):

    @allure.title("Check tabs")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_tabs(self):
        self.tabs_page.open()
        self.tabs_page.is_opened()
        self.tabs_page.check_main_word()
        self.tabs_page.click_what_tab()
        self.tabs_page.click_origin_tab()
        self.tabs_page.click_use_tab()
