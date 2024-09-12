from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckBoxPage(BasePage):
    PAGE_URL = Links.CHECK_BOX_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Check Box"]')
    HOME_TOGLE = ("xpath", '//button[@title="Toggle"]')
    CHECK_BOX_DESKTOP = ("xpath", '(//span[@class="rct-title"])[2]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Check Box')), "Текст не совпадает"

    def click_togle_home(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME_TOGLE)).click()

    def click_check_box_desktop(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX_DESKTOP)).click()