from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ButtonsPage(BasePage):

    PAGE_URL = Links.BUTTONS_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Buttons"]')
    DOUBLE_CLICK_ME_BUTTON = ("xpath", '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK_ME_BUTTON = ("xpath", '//button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = ("xpath", '//button[text()="Click Me"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Buttons')), "Текст не совпадает"

    def double_click_button(self):
        dbl_btn = self.wait.until(EC.element_to_be_clickable(self.DOUBLE_CLICK_ME_BUTTON))
        actions = ActionChains(self.driver)
        actions.double_click(dbl_btn).perform()

    def right_click_button(self):
        rgt_btn = self.wait.until(EC.element_to_be_clickable(self.RIGHT_CLICK_ME_BUTTON))
        actions = ActionChains(self.driver)
        actions.context_click(rgt_btn).perform()

    def click_me_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_ME_BUTTON)).click()