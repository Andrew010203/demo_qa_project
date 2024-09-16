import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Tool tips")
class TestToolTips(BaseTest):

    @allure.title("Check tool tips")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_tool_tips(self):
        self.tool_tips_page.open()
        self.tool_tips_page.is_opened()
        self.tool_tips_page.check_main_word()
        self.tool_tips_page.hover_tool_tip_button()
        self.tool_tips_page.hover_tool_tip_field()
        self.tool_tips_page.hover_tool_tip_contrary()
