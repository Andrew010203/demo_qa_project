from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class TextBoxPage(BasePage):

    PAGE_URL = Links.TEXT_BOX_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Text Box"]')
    FULL_NAME_FIELD = ("xpath", '//input[@id="userName"]')
    EMAIL_FIELD = ("xpath", '//input[@id="userEmail"]')
    CURRENT_ADDRESS_FIELD = ("xpath", '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS_FIELD = ("xpath", '//textarea[@id="permanentAddress"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Text Box')), "Текст не совпадает"

    def input_full_name(self):
        self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD)).send_keys("Ivanov Ivan")

    def input_email(self):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys("IvanIvanov@Example.com")

    def input_address(self):
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_ADDRESS_FIELD)).send_keys("Russia, Moscow")

    def input_permanent_address(self):
        self.wait.until(EC.element_to_be_clickable(self.PERMANENT_ADDRESS_FIELD)).send_keys("Lenina, 100")

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

