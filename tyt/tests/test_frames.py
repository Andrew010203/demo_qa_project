import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Work with iframes")
class TestFrames(BaseTest):

    @allure.title("Test select frames")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_frames(self):
        self.frames_page.open()
        self.frames_page.is_opened()
        self.frames_page.check_main_word()
        self.frames_page.switch_to_iframe_1()
        self.frames_page.switch_to_default_content()
        self.frames_page.switch_to_iframe_2()
        time.sleep(3)