from tyt.data_generators.date_generator import DateGenerator
from tyt.data_generators.time_generator import TimeGenerator
from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC


class DatePickerPage(BasePage):
    PAGE_URL = Links.DATE_PICKER_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Date Picker"]')
    SELECT_DATE_FIELD = ("xpath", '//input[@id="datePickerMonthYearInput"]')
    SELECT_DATE_AND_TIME_FIELD = ("xpath", '//input[@id="dateAndTimePickerInput"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Date Picker')), "Текст не совпадает"

    def select_date(self):
        random_date = DateGenerator.generate_random_date()
        select_date = self.wait.until(EC.element_to_be_clickable(self.SELECT_DATE_FIELD))
        select_date.send_keys(Keys.CONTROL + "A")
        select_date.send_keys(Keys.BACK_SPACE)
        select_date.send_keys(random_date)

    def select_date_and_time(self):
        random_date = DateGenerator.generate_random_date()
        random_time = TimeGenerator.generate_random_time()
        select_date = self.wait.until(EC.element_to_be_clickable(self.SELECT_DATE_AND_TIME_FIELD))
        select_date.send_keys(Keys.CONTROL + "A")
        select_date.send_keys(Keys.BACK_SPACE)
        select_date.send_keys(random_date + ' ' + random_time)