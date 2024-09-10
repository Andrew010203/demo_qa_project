import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Work with iframes")
class TestNestedFrames(BaseTest):

    @allure.title("Test select frames")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_nested_frames(self):
        self.nested_frames_page.open()
        self.nested_frames_page.is_opened()
        self.nested_frames_page.check_main_word()
        self.nested_frames_page.switch_to_parent_iframe()
        self.nested_frames_page.switch_to_child_iframe()
        self.nested_frames_page.switch_to_default_content()
