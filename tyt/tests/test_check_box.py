import allure
from tyt.base.base_test import BaseTest


@allure.feature("Input check box")
class TestCheckBox(BaseTest):

    @allure.title("Check box test")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_check_box(self):
        self.check_box_page.open()
        self.check_box_page.is_opened()
        self.check_box_page.check_main_word()
        self.check_box_page.click_togle_home()
        self.check_box_page.click_check_box_desktop()
