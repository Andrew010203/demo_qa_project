import time
import allure
from tyt.base.base_test import BaseTest


@allure.feature("Login")
class TestLogin(BaseTest):

    @allure.title("Check Login")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.check_main_word()
        self.login_page.enter_user_name(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
