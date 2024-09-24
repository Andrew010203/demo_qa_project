import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Login"]')
    USER_NAME_FIELD = ("xpath", '//input[@id="userName"]')
    PASSWORD_FIELD = ("xpath", '//input[@id="password"]')
    LOGIN_BUTTON = ("xpath", '//button[@id="login"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Login')), "Текст не совпадает"

    def enter_user_name(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USER_NAME_FIELD)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()