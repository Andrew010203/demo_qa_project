import allure
from tyt.base.base_test import BaseTest


@allure.feature("Test dynamic properties")
class TestDynamicProperties(BaseTest):

    @allure.title("Check dynamic properties buttons")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_dynamic_properties(self):
        self.dynamic_properties_page.open()
        self.dynamic_properties_page.is_opened()
        self.dynamic_properties_page.check_main_word()
        self.dynamic_properties_page.click_will_enable_5_seconds_button()
        self.dynamic_properties_page.click_color_change_button()
        self.dynamic_properties_page.click_visible_after_5_seconds_button()