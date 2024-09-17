import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Menu")
class TestMenu(BaseTest):

    @allure.title("Check menu")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_menu(self):
        self.menu_page.open()
        self.menu_page.is_opened()
        self.menu_page.check_main_word()
        self.menu_page.hover_main_item_1()
        self.menu_page.hover_main_item_2()
        self.menu_page.hover_sub_item_1()
        self.menu_page.hover_sub_item_2()
        self.menu_page.hover_sub_sub_list()
        self.menu_page.hover_sub_sub_item_1()
        self.menu_page.hover_sub_sub_item_2()
        self.menu_page.hover_main_item_3()
