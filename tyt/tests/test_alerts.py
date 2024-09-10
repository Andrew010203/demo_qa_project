import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Work with alerts")
class TestAlerts(BaseTest):

    @allure.title("Test alerts")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_alerts(self):
        self.alerts_page.open()
        self.alerts_page.is_opened()
        self.alerts_page.click_button_to_see_alert()
        self.alerts_page.click_button_to_see_alert_after_5_seconds()
        self.alerts_page.click_button_confirm_box_will_appear()
        self.alerts_page.click_button_prompt_box_will_appear("hello world")
