from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class ModalDialogsPage(BasePage):
    PAGE_URL = Links.MODAL_DIALOGS_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Modal Dialogs"]')
    SMALL_MODAL_BUTTON = ("xpath", '//button[@id="showSmallModal"]')
    CLOSE_SMALL_MODAL_BUTTON = ("xpath", '//button[@id="closeSmallModal"]')
    LARGE_MODAL_BUTTON = ("xpath", '//*[@id="showLargeModal"]')
    CLOSE_LARGE_MODAL_BUTTON = ("xpath", '//*[@id="closeLargeModal"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Modal Dialogs')), "Текст не совпадает"

    def click_small_modal_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SMALL_MODAL_BUTTON)).click()
        value_title = self.driver.find_element("xpath", '//*[text()="Small Modal"]').text
        assert value_title == "Small Modal", "Заголовок не совпадает"
        value_body_title = self.driver.find_element("xpath", '//*[@class="modal-body"]').text
        assert "This is a small modal. It has very less content" in value_body_title, "Содержимое не совпадает"

    def click_close_small_modal_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_SMALL_MODAL_BUTTON)).click()

    def click_large_modal_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LARGE_MODAL_BUTTON)).click()
        value_title = self.driver.find_element("xpath", '//*[text()="Large Modal"]').text
        assert value_title == "Large Modal", "Заголовок не совпадает"
        value_body_title = self.driver.find_element("xpath", '//*[@class="modal-body"]/p').text
        assert "Lorem Ipsum is simply dummy text of the printing and typ" in value_body_title, "Содержимое не совпадает"

    def click_close_large_modal_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_LARGE_MODAL_BUTTON)).click()