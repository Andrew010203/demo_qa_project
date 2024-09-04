from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RadioButtonPage(BasePage):

    PAGE_URL = Links.RADIO_BUTTON_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Radio Button"]')
    RADIO_BUTTON_YES = ("xpath", '(//*[text()="Yes"])[1]')
    RADIO_BUTTON_IMPRESSIVE = ("xpath", '(//*[text()="Impressive"])[1]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Radio Button')), "Текст не совпадает"

    def click_radio_button_yes(self):
        self.wait.until(EC.element_to_be_clickable(self.RADIO_BUTTON_YES)).click()

    def click_radio_button_impressive(self):
        self.wait.until(EC.element_to_be_clickable(self.RADIO_BUTTON_IMPRESSIVE)).click()