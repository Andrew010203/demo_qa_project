import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Slider")
class TestSlider(BaseTest):

    @allure.title("Check slider")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_slider(self):
        self.slider_page.open()
        self.slider_page.is_opened()
        self.slider_page.check_main_word()
        self.slider_page.use_slider()
