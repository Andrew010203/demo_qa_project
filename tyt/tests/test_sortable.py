import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Sortable")
class TestSortable(BaseTest):

    @allure.title("Check sortable")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_sortable(self):
        self.sortable_page.open()
        self.sortable_page.is_opened()
        self.sortable_page.check_main_word()
        self.sortable_page.drag_and_drop_random_list()
        self.sortable_page.drag_and_drop_random_grit()
