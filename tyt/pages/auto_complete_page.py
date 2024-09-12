import random

from data_generators.color_generator import ColorGenerator
from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC


class AutoCompletePage(BasePage):
    PAGE_URL = Links.AUTOCOMPLETE_PAGE_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Auto Complete"]')
    MULTIPLE_FIELD = ("xpath", '//*[@id="autoCompleteMultipleInput"]')
    SINGLE_FIELD = ("xpath", '//*[@id="autoCompleteSingleInput"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Auto Complete')), "Текст не совпадает"

    def input_multiple_field(self):
        number_of_colors = random.randint(1, 5)
        for _ in range(number_of_colors):
            random_color = ColorGenerator.random_color()
            self.wait.until(EC.element_to_be_clickable(self.MULTIPLE_FIELD)).send_keys(random_color)
            self.wait.until(EC.element_to_be_clickable(self.MULTIPLE_FIELD)).send_keys(Keys.ENTER)

    def input_single_field(self):
        random_color = ColorGenerator.random_color()
        self.wait.until(EC.element_to_be_clickable(self.SINGLE_FIELD)).send_keys(random_color)
        self.wait.until(EC.element_to_be_clickable(self.SINGLE_FIELD)).send_keys(Keys.ENTER)
