import random
import time

from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class TabsPage(BasePage):
    PAGE_URL = Links.TABS_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Tabs"]')
    WHAT_TAB = ("xpath", '//a[@id="demo-tab-what"]')
    VALUE_WHAT_TAB = ("xpath", '//div[@id="demo-tabpane-what"]/p')
    ORIGIN_TAB = ("xpath", '//a[@id="demo-tab-origin"]')
    VALUE_ORIGIN_TAB = ("xpath", '(//div[@id="demo-tabpane-origin"]/p)[1]')
    USE_TAB = ("xpath", '//a[@id="demo-tab-use"]')
    VALUE_USE_TAB = ("xpath", '//div[@id="demo-tabpane-use"]/p')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Tabs')), "Текст не совпадает"

    def click_what_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.WHAT_TAB)).click()
        value_what_tab = self.driver.find_element("xpath", '//div[@id="demo-tabpane-what"]/p').text
        print(value_what_tab)
        print(len(value_what_tab))
        assert "Lorem Ipsum is simply dummy text of the printing and typesetting" in value_what_tab, "ошибка"
        assert len(value_what_tab) != 0, "Вкладка what не была нажата или текст отсутствует"

    def click_origin_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.ORIGIN_TAB)).click()
        value_origin_tab = self.driver.find_element("xpath", '(//div[@id="demo-tabpane-origin"]/p)[1]').text
        print(value_origin_tab)
        print(len(value_origin_tab))
        assert "Contrary to popular belief, Lorem Ipsum is not simply random text" in value_origin_tab, "ошибка"
        assert len(value_origin_tab) != 0, "Вкладка origin не была нажата или текст отсутствует"

    def click_use_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.USE_TAB)).click()
        value_use_tab = self.driver.find_element("xpath", '//div[@id="demo-tabpane-use"]/p').text
        print(value_use_tab)
        print(len(value_use_tab))
        assert "It is a long established fact that a reader will be distracted by" in value_use_tab, "ошибка"
        assert len(value_use_tab) != 0, "Вкладка use не была нажата или текст отсутствует"


