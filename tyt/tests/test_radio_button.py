import allure
from tyt.base.base_test import BaseTest


@allure.feature("Check radio button")
class TestRadioButton(BaseTest):

    @allure.title("Check radio button")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_radio_button(self):
        self.radio_button_page.open()
        self.radio_button_page.is_opened()
        self.radio_button_page.check_main_word()
        self.radio_button_page.click_radio_button_yes()
        self.radio_button_page.click_radio_button_impressive()