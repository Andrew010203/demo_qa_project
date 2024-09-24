import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Register")
class TestRegister(BaseTest):

    @allure.title("Check Register")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_register(self):
        self.register_page.open()
        self.register_page.is_opened()
        self.register_page.check_main_word()
        self.register_page.enter_first_name()
        self.register_page.enter_last_name()
        self.register_page.enter_user_name(self.data.LOGIN)
        self.register_page.enter_password(self.data.PASSWORD)
        self.register_page.click_register_button()
