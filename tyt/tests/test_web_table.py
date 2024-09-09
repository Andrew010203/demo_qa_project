import allure
from tyt.base.base_test import BaseTest


@allure.feature("Input data")
class TestWebTable(BaseTest):

    @allure.title("Check web table")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_web_table(self):
        self.web_tables_page.open()
        self.web_tables_page.is_opened()
        self.web_tables_page.check_main_word()
        self.web_tables_page.click_button_add()
        self.web_tables_page.input_first_name("Ivan")
        self.web_tables_page.input_last_name("Ivanov")
        self.web_tables_page.input_email("IvanIvanov@Example.com")
        self.web_tables_page.input_age("33")
        self.web_tables_page.input_salary("200000")
        self.web_tables_page.input_department("AQA")
        self.web_tables_page.click_submit()
        self.web_tables_page.click_button_pen()
        self.web_tables_page.input_edit_salary()
        self.web_tables_page.click_edit_submit()
        self.web_tables_page.input_search_field()
        self.web_tables_page.click_search_button()
        self.web_tables_page.click_delete_button()