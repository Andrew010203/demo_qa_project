from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class WebTablesPage(BasePage):

    PAGE_URL = Links.WEB_TABLES_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Web Tables"]')
    ADD_BUTTON = ("xpath", '//button[@id="addNewRecordButton"]')
    FIRST_NAME_FIELD = ("xpath", '//input[@id="firstName"]')
    LAST_NAME_FIELD = ("xpath", '//input[@id="lastName"]')
    EMAIL_FIELD = ("xpath", '//input[@id="userEmail"]')
    AGE_FIELD = ("xpath", '//input[@id="age"]')
    SALARY_FIELD = ("xpath", '//input[@id="salary"]')
    DEPARTMENT_FIELD = ("xpath", '//input[@id="department"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')
    PEN_BUTTON = ("xpath", '//span[@id="edit-record-4"]')
    TYPE_TO_SEARCH_FIELD = ("xpath", '//input[@id="searchBox"]')
    SEARCH_BUTTON = ("xpath", '//span[@id="basic-addon2"]')
    DELETE_BUTTON = ("xpath", '//span[@title="Delete"]')
    TEST_WORD = ("xpath", '//div[text()="No rows found"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Web Tables')), "Текст не совпадает"

    def click_button_add(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def input_first_name(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys(first_name)

    def input_last_name(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(last_name)

    def input_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def input_age(self, age):
        self.wait.until(EC.element_to_be_clickable(self.AGE_FIELD)).send_keys(age)

    def input_salary(self, salary):
        self.wait.until(EC.element_to_be_clickable(self.SALARY_FIELD)).send_keys(salary)

    def input_department(self, department):
        self.wait.until(EC.element_to_be_clickable(self.DEPARTMENT_FIELD)).send_keys(department)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def click_button_pen(self):
        self.wait.until(EC.element_to_be_clickable(self.PEN_BUTTON)).click()

    def input_edit_salary(self):
        edit_salary = self.wait.until(EC.element_to_be_clickable(self.SALARY_FIELD))
        edit_salary.clear()
        edit_salary.send_keys("220000")

    def click_edit_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def input_search_field(self):
        self.wait.until(EC.element_to_be_clickable(self.TYPE_TO_SEARCH_FIELD)).click()
        self.wait.until(EC.element_to_be_clickable(self.TYPE_TO_SEARCH_FIELD)).send_keys("33")

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def click_delete_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.TEST_WORD)).is_displayed(), "текст отсутствует"






