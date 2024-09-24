import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Check accordian")
class TestAccordian(BaseTest):

    @allure.title("Click accordian card and check title, body")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_accordian(self):
        self.accordian_page.open()
        self.accordian_page.is_opened()
        self.accordian_page.check_main_word()
        self.accordian_page.scroll_page(0, 200)
        self.accordian_page.click_what_card()
        time.sleep(1)
        self.accordian_page.click_where_card()
        time.sleep(1)
        self.accordian_page.click_why_card()
