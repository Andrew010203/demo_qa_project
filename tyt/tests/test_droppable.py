import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Droppable")
class TestDroppable(BaseTest):

    @allure.title("Check droppable")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_droppable(self):
        self.droppable_page.open()
        self.droppable_page.is_opened()
        self.droppable_page.check_main_word()
        self.droppable_page.drag_me_in_drop_here()
        self.droppable_page.drag_not_acceptable_in_drop_here()
        self.droppable_page.drag_acceptable_in_drop_here()
        self.droppable_page.drag_me_in_outer_droppable_ng()
        self.droppable_page.drag_me_in_inner_droppable_not_greedy()
        self.droppable_page.drag_me_in_outer_droppable_g()
        self.droppable_page.drag_me_in_inner_droppable_g()
        self.droppable_page.not_revert_in_drop_here()
        self.droppable_page.will_revert_in_drop_here()
