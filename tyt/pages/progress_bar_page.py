import random
import time

from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class ProgressBarPage(BasePage):
    PAGE_URL = Links.PROGRESS_BAR_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Progress Bar"]')
    START_STOP_BUTTON = ("xpath", '//button[@id="startStopButton"]')
    PROGRESS_BAR = ("xpath", '//div[@id="progressBar"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Progress Bar')), "Текст не совпадает"

    def choose_progress_bar_value(self):
        value_before = self.wait.until(EC.visibility_of_element_located(self.PROGRESS_BAR)).text
        self.wait.until(EC.element_to_be_clickable(self.START_STOP_BUTTON)).click()
        time.sleep(random.randint(1, 5))
        self.wait.until(EC.element_to_be_clickable(self.START_STOP_BUTTON)).click()
        value_after = self.wait.until(EC.visibility_of_element_located(self.PROGRESS_BAR)).text
        print(value_before, value_after)
        assert value_before != value_after, "Ошибка"
