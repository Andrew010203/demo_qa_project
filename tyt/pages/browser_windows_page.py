from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class BrowserWindowsPage(BasePage):
    PAGE_URL = Links.BROWSER_WINDOWS_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Browser Windows"]')
    NEW_TAB_BUTTON = ("xpath", '//button[@id="tabButton"]')
    NEW_WINDOW_BUTTON = ("xpath", '//button[@id="windowButton"]')
    NEW_WINDOW_MESSAGE = ("xpath", '//button[@id="messageWindowButton"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Browser Windows')), "Текст не совпадает"

    def click_new_tab_button(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_TAB_BUTTON)).click()

    def switch_new_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def click_new_window_button(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_WINDOW_BUTTON)).click()

    def click_new_window_message_button(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_WINDOW_MESSAGE)).click()