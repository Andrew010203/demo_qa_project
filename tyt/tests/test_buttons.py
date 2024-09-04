import allure
from tyt.base.base_test import BaseTest


@allure.feature("Check buttons")
class TestButtons(BaseTest):

    @allure.title("Click buttons")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_buttons(self):
        self.buttons_page.open()
        self.buttons_page.is_opened()
        self.buttons_page.check_main_word()
        self.buttons_page.double_click_button()
        self.buttons_page.right_click_button()
        self.buttons_page.click_me_button()