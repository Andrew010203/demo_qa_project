import allure
from tyt.base.base_test import BaseTest


@allure.feature("Input text box")
class TestTextBox(BaseTest):

    @allure.title("Add user data")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_text_box(self):
        self.text_box_page.open()
        self.text_box_page.is_opened()
        self.text_box_page.check_main_word()
        self.text_box_page.input_full_name()
        self.text_box_page.input_email()
        self.text_box_page.input_address()
        self.text_box_page.input_permanent_address()
        self.text_box_page.click_submit()







