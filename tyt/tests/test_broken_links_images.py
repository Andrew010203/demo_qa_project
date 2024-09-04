import allure
from tyt.base.base_test import BaseTest



@allure.feature("Check links")
class TestBrokenLinksImages(BaseTest):

    @allure.title("Click links")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_broken_links(self):
        self.broken_links_images_page.open()
        self.broken_links_images_page.is_opened()
        self.broken_links_images_page.check_main_word()
        self.broken_links_images_page.click_valid_link()
        self.broken_links_images_page.click_broken_link()