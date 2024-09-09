import time

import allure
from tyt.base.base_test import BaseTest


@allure.feature("Input user data")
class TestPracticeForm(BaseTest):

    @allure.title("Add user data")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_input_data(self):
        self.practice_form_page.open()
        self.practice_form_page.is_opened()
        self.practice_form_page.scroll_page(0, 200)
        self.practice_form_page.check_main_word()
        self.practice_form_page.input_first_name("Ivan")
        self.practice_form_page.input_last_name("Ivanov")
        self.practice_form_page.input_email("IvanIvanov@Example.com")
        self.practice_form_page.choose_gender()
        self.practice_form_page.input_mobile_number("1234567890")
        self.practice_form_page.input_date_of_birth()
        self.practice_form_page.choose_month()
        self.practice_form_page.choose_year()
        self.practice_form_page.choose_day()
        self.practice_form_page.input_subjects_field("e")
        self.practice_form_page.choose_subjects()
        self.practice_form_page.choose_hobbies()
        self.practice_form_page.click_select_file_button()
        self.practice_form_page.input_current_address("Lenina 25")
        self.practice_form_page.select_state()
        self.practice_form_page.choose_state()
        self.practice_form_page.select_city()
        self.practice_form_page.choose_city()
        self.practice_form_page.click_submit_button()
        self.practice_form_page.click_close_button()
