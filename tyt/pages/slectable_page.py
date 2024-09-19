import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SelectablePage(BasePage):
    PAGE_URL = Links.SELECTABLE_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Selectable"]')
    TAB_LIST = ("xpath", '//a[text()="List"]')
    LIST_ITEM = ("xpath", f'(//ul[@id="verticalListContainer"]/li)[{random.randint(1, 4)}]')
    TAB_GRID = ("xpath", '//a[@id="demo-tab-grid"]')
    GRID_ITEM = ("xpath", f'(//div[@id="gridContainer"]/'
                          f'/li[@class="list-group-item list-group-item-action"])[{random.randint(1, 8)}]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Selectable')), "Текст не совпадает"

    def selectable_list_random_element(self):
        self.wait.until(EC.element_to_be_clickable(self.LIST_ITEM)).click()
        class_attribute = self.wait.until(EC.element_to_be_clickable(self.LIST_ITEM)).get_attribute("class")
        print(class_attribute)
        assert "active" in class_attribute, "Элемент не активен"

    def selectable_grid_random_element(self):
        self.wait.until(EC.element_to_be_clickable(self.TAB_GRID)).click()
        self.wait.until(EC.element_to_be_clickable(self.GRID_ITEM)).click()
        element_active = self.wait.until(EC.element_to_be_clickable(self.GRID_ITEM)).text
        print(element_active)
        return element_active


