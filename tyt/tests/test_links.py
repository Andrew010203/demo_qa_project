import allure
from tyt.base.base_test import BaseTest


@allure.feature("Check links")
class TestLink(BaseTest):

    @allure.title("Click links")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_links(self):
        self.links_page.open()
        self.links_page.is_opened()
        self.links_page.check_main_word()
        self.links_page.click_home_link()
        self.links_page.click_homebt_ott_link()
        self.links_page.click_created_link()
        self.links_page.click_no_content_link()
        self.links_page.click_moved_link()
        self.links_page.click_bad_request_link()
        self.links_page.click_unauthorized_link()
        self.links_page.click_forbidden_link()
        self.links_page.click_not_found_link()