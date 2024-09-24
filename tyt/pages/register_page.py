import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(BasePage):
    PAGE_URL = Links.REGISTER_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Register"]')
    FIRST_NAME_FIELD = ("xpath", '//input[@id="firstname"]')
    LAST_NAME_FIELD = ("xpath", '//input[@id="lastname"]')
    USER_NAME_FIELD = ("xpath", '//input[@id="userName"]')
    PASSWORD_FIELD = ("xpath", '//input[@id="password"]')
    REGISTER_BUTTON = ("xpath", '//button[@id="register"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Register')), "Текст не совпадает"

    def enter_first_name(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys("f_name")

    def enter_last_name(self):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys("l_name")

    def enter_user_name(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USER_NAME_FIELD)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()