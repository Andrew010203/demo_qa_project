import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Selectable")
class TestSortable(BaseTest):

    @allure.title("Check selectable")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_sortable(self):
        self.selectable_page.open()
        self.selectable_page.is_opened()
        self.selectable_page.check_main_word()
        self.selectable_page.selectable_list_random_element()
        self.selectable_page.selectable_grid_random_element()
        time.sleep(10)