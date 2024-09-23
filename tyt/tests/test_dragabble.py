import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Dragabble")
class TestDragabble(BaseTest):

    @allure.title("Check dragabble")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_dragabble(self):
        self.dragabble_page.open()
        self.dragabble_page.is_opened()
        self.dragabble_page.check_main_word()
        self.dragabble_page.drag_me_in_another_place()
        self.dragabble_page.drag_only_x_only_y()
        self.dragabble_page.drag_cont_restricted()
