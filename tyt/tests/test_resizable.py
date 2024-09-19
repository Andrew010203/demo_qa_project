import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Resizable")
class TestResizable(BaseTest):

    @allure.title("Check resizable")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_resizable(self):
        self.resizable_page.open()
        self.resizable_page.is_opened()
        self.resizable_page.check_main_word()
        self.resizable_page.scroll_page(0, 200)
        self.resizable_page.interaction_with_resizable_box()
        self.resizable_page.interaction_with_resizable()
