from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DynamicPropertiesPage(BasePage):

    PAGE_URL = Links.DYNAMIC_PROPERTIES_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Dynamic Properties"]')
    WILL_EN_BUTTON = ("xpath", '//button[@id="enableAfter"]')
    COLOR_CHANGE_BUTTON = ("xpath", '//button[@id="colorChange"]')
    VISIBLE_AFTER_BUTTON = ("xpath", '//button[@id="visibleAfter"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Dynamic Properties')), "Текст не совпадает"

    def click_will_enable_5_seconds_button(self):
        self.wait.until(EC.element_to_be_clickable(self.WILL_EN_BUTTON)).click()

    def click_color_change_button(self):
        self.wait.until(EC.element_to_be_clickable(self.COLOR_CHANGE_BUTTON)).click()

    def click_visible_after_5_seconds_button(self):
        self.wait.until(EC.visibility_of_element_located(self.VISIBLE_AFTER_BUTTON)).click()
