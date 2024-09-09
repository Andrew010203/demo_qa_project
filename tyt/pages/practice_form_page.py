import os

from selenium.webdriver import Keys
import random
from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage(BasePage):
    PAGE_URL = Links.PRACTICE_FORM_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Practice Form"]')
    FIRST_NAME_FIELD = ("xpath", '//input[@id="firstName"]')
    LAST_NAME_FIELD = ("xpath", '//input[@id="lastName"]')
    EMAIL_FIELD = ("xpath", '//input[@id="userEmail"]')
    GENDER_RADIO_BUTTON = ("xpath", f'//*[@for="gender-radio-{random.randint(1, 3)}"]')
    MOBILE_NUMBER_FIELD = ("xpath", '//input[@id="userNumber"]')
    DATE_OF_BIRTH_FIELD = ("xpath", '//input[@id="dateOfBirthInput"]')
    CHOOSE_MONTH = ("xpath", f'//select[@class="react-datepicker__month-select"]/option[@value="{random.randint(0, 11)}"]')
    CHOOSE_YEAR = ("xpath", f'//*[@id="dateOfBirth"]//select/option[@value="{random.randint(1900, 2024)}"]')
    day = random.randint(1, 31)
    formatted_day = f'{day:02}'
    CHOOSE_DAY = ("xpath", f'(//*[contains(@class,"react-datepicker__day react-datepicker__day--0{formatted_day}")])[1]')
    SUBJECTS_FIELD = ("xpath", '//input[@id="subjectsInput"]')
    SUBJECTS = ("xpath", f'//*[@id="react-select-2-option-{random.randint(0, 3)}"]')
    HOBBIES_CHECK_BOXES = ("xpath", f'//*[@for="hobbies-checkbox-{random.randint(1, 3)}"]')
    SELECT_FILE_BUTTON = ("xpath", '//input[@id="uploadPicture"]')
    CURRENT_ADDRESS_FIELD = ("xpath", '//textarea[@id="currentAddress"]')
    SELECT_STATE_FIELD = ("xpath", '//div[@id="state"]')
    CHOOSE_STATE = ("xpath", f'//*[@id="react-select-3-option-{random.randint(1, 3)}"]')
    SELECT_CITY = ("xpath", '//div[@id="city"]')
    CHOOSE_CITY = ("xpath", f'//*[@id="react-select-4-option-{random.randint(0, 1)}"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')
    CLOSE_BUTTON = ("xpath", '//button[@id="closeLargeModal"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Practice Form')), "Текст не совпадает"

    def input_first_name(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys(first_name)

    def input_last_name(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(last_name)

    def input_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)
        
    def choose_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.GENDER_RADIO_BUTTON)).click()

    def input_mobile_number(self, mobile_number):
        if len(mobile_number) == 10 and mobile_number.isdigit():
            self.wait.until(EC.element_to_be_clickable(self.MOBILE_NUMBER_FIELD)).send_keys(mobile_number)
        else:
            raise ValueError("Номер мобильного телефона должен содержать ровно 10 цифр.")

    def input_date_of_birth(self):
        date_of_birth = self.wait.until(EC.element_to_be_clickable(self.DATE_OF_BIRTH_FIELD))
        date_of_birth.click()

    def choose_month(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_MONTH)).click()

    def choose_year(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_YEAR)).click()

    def choose_day(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_DAY)).click()

    def input_subjects_field(self, subjects):
        subject_field = self.wait.until(EC.element_to_be_clickable(self.SUBJECTS_FIELD))
        subject_field.click()
        subject_field.send_keys(subjects)


    def choose_subjects(self):
        subject = self.wait.until(EC.element_to_be_clickable(self.SUBJECTS))
        subject.click()

    def choose_hobbies(self):
        self.wait.until(EC.element_to_be_clickable(self.HOBBIES_CHECK_BOXES)).click()

    def click_select_file_button(self):
        choose_file_btn = self.wait.until(EC.element_to_be_clickable(self.SELECT_FILE_BUTTON))
        choose_file_btn.send_keys(f"{os.getcwd()}\download\pic.jpg")

    def input_current_address(self, address):
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_ADDRESS_FIELD)).send_keys(address)

    def select_state(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_STATE_FIELD)).click()

    def choose_state(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_STATE)).click()

    def select_city(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_CITY)).click()

    def choose_city(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_CITY)).click()

    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def click_close_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_BUTTON)).click()





