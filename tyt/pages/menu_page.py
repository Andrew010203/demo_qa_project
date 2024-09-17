from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MenuPage(BasePage):
    PAGE_URL = Links.MENU_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Menu"]')
    MAIN_ITEM_1 = ("xpath", '//a[text()="Main Item 1"]')
    MAIN_ITEM_2 = ("xpath", '//a[text()="Main Item 2"]')
    SUB_ITEM_1 = ("xpath", '(//a[text()="Sub Item"])[1]')
    SUB_ITEM_2 = ("xpath", '(//a[text()="Sub Item"])[2]')
    SUB_SUB_LIST = ("xpath", '//a[text()="SUB SUB LIST »"]')
    SUB_SUB_ITEM_1 = ("xpath", '//a[text()="Sub Sub Item 1"]')
    SUB_SUB_ITEM_2 = ("xpath", '//a[text()="Sub Sub Item 2"]')
    MAIN_ITEM_3 = ("xpath", '//a[text()="Main Item 3"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Menu')), "Текст не совпадает"

    def hover_main_item_1(self):
        value_hover_item_1 = self.wait.until(EC.visibility_of_element_located(self.MAIN_ITEM_1))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_hover_item_1).perform()
        value_hover_item_1 = self.wait.until(EC.visibility_of_element_located(self.MAIN_ITEM_1)).text
        print(value_hover_item_1)
        assert value_hover_item_1 == "Main Item 1", "Название не совпадает"

    def hover_main_item_2(self):
        value_hover_item_2 = self.wait.until(EC.visibility_of_element_located(self.MAIN_ITEM_2))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_hover_item_2).perform()
        value_hover_item_2 = self.wait.until(EC.visibility_of_element_located(self.MAIN_ITEM_2)).text
        print(value_hover_item_2)
        assert value_hover_item_2 == "Main Item 2", "Название не совпадает"

    def hover_sub_item_1(self):
        value_sub_item_1 = self.wait.until(EC.visibility_of_element_located(self.SUB_ITEM_1))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_sub_item_1).perform()
        value_sub_item_1 = self.wait.until(EC.visibility_of_element_located(self.SUB_ITEM_1)).text
        print(value_sub_item_1)
        assert value_sub_item_1 == "Sub Item", "Название не совпадает"

    def hover_sub_item_2(self):
        value_sub_item_2 = self.wait.until(EC.visibility_of_element_located(self.SUB_ITEM_2))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_sub_item_2).perform()
        value_sub_item_2 = self.wait.until(EC.visibility_of_element_located(self.SUB_ITEM_2)).text
        print(value_sub_item_2)
        assert value_sub_item_2 == "Sub Item", "Название не совпадает"

    def hover_sub_sub_list(self):
        value_sub_sub_list = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_LIST))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_sub_sub_list).perform()
        value_sub_sub_list = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_LIST)).text
        print(value_sub_sub_list)
        assert value_sub_sub_list == "SUB SUB LIST »", "Название не совпадает"

    def hover_sub_sub_item_1(self):
        value_sub_sub_item_1 = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_ITEM_1))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_sub_sub_item_1).perform()
        value_sub_sub_item_1 = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_ITEM_1)).text
        print(value_sub_sub_item_1)
        assert value_sub_sub_item_1 == "Sub Sub Item 1", "Название не совпадает"

    def hover_sub_sub_item_2(self):
        value_sub_sub_item_2 = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_ITEM_2))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_sub_sub_item_2).perform()
        value_sub_sub_item_2 = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_ITEM_2)).text
        print(value_sub_sub_item_2)
        assert value_sub_sub_item_2 == "Sub Sub Item 2", "Название не совпадает"

    def hover_main_item_3(self):
        value_hover_item_3 = self.wait.until(EC.visibility_of_element_located(self.MAIN_ITEM_3))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_hover_item_3).perform()
        value_hover_item_3 = self.wait.until(EC.visibility_of_element_located(self.MAIN_ITEM_3)).text
        print(value_hover_item_3)
        assert value_hover_item_3 == "Main Item 3", "Название не совпадает"