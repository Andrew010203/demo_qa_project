import allure
from tyt.base.base_test import BaseTest


@allure.feature("Input text box")
class TestTextBox(BaseTest):

    @allure.title("Add user data")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_text_box(self):
        self.text_box_page.open()
        self.text_box_page.is_opened()
        self.text_box_page.check_main_word()
        self.text_box_page.input_full_name()
        self.text_box_page.input_email()
        self.text_box_page.input_address()
        self.text_box_page.input_permanent_address()
        self.text_box_page.click_submit()

        # self.check_box_page.open()
        # self.check_box_page.is_opened()
        # self.check_box_page.click_togle_home()
        # self.check_box_page.click_check_box_desktop()

        # self.radio_button_page.open()
        # self.radio_button_page.is_opened()
        # self.radio_button_page.click_radio_button_yes()
        # self.radio_button_page.click_radio_button_impressive()

        # self.web_tables_page.open()
        # self.web_tables_page.is_opened()
        # self.web_tables_page.click_button_add()
        # self.web_tables_page.input_first_name()
        # self.web_tables_page.input_last_name()
        # self.web_tables_page.input_email()
        # self.web_tables_page.input_age()
        # self.web_tables_page.input_salary()
        # self.web_tables_page.input_department()
        # self.web_tables_page.click_submit()
        # self.web_tables_page.click_button_pen()
        # self.web_tables_page.input_edit_salary()
        # self.web_tables_page.click_edit_submit()
        # self.web_tables_page.input_search_field()
        # self.web_tables_page.click_search_button()
        # self.web_tables_page.click_delete_button()

        # self.buttons_page.open()
        # self.buttons_page.is_opened()
        # self.buttons_page.double_click_button()
        # self.buttons_page.right_click_button()
        # self.buttons_page.click_me_button()

        # self.links_page.open()
        # self.links_page.is_opened()
        # self.links_page.click_home_link()
        # self.links_page.click_homebt_ott_link()
        # self.links_page.click_created_link()
        # self.links_page.click_no_content_link()
        # self.links_page.click_moved_link()
        # self.links_page.click_bad_request_link()
        # self.links_page.click_unauthorized_link()
        # self.links_page.click_forbidden_link()
        # self.links_page.click_not_found_link()

        # self.broken_links_images_page.open()
        # self.broken_links_images_page.is_opened()
        # self.broken_links_images_page.click_valid_link()
        # self.broken_links_images_page.click_broken_link()

        # self.upload_and_download_page.open()
        # self.upload_and_download_page.is_opened()
        # self.upload_and_download_page.click_download_button()
        # self.upload_and_download_page.click_select_file_button()

        # self.dynamic_properties_page.open()
        # self.dynamic_properties_page.is_opened()
        # self.dynamic_properties_page.click_will_enable_5_seconds_button()
        # self.dynamic_properties_page.click_color_change_button()
        # self.dynamic_properties_page.click_visible_after_5_seconds_button()
        # time.sleep(10)
        #
        # time.sleep(6)






