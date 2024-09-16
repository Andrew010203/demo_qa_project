import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Progress bar")
class TestSlider(BaseTest):

    @allure.title("Check progress bar")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_progress_bar(self):
        self.progress_bar_page.open()
        self.progress_bar_page.is_opened()
        self.progress_bar_page.check_main_word()
        self.progress_bar_page.choose_progress_bar_value()
