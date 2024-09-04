import os
from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class UploadAndDownloadPage(BasePage):
    PAGE_URL = Links.UPLOAD_AND_DOWNLOAD_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Upload and Download"]')
    DOWNLOAD_BUTTON = ("xpath", '//a[@id="downloadButton"]')
    SELECT_FILE_BUTTON = ("xpath", '//input[@id="uploadFile"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Upload and Download')), "Текст не совпадает"

    def click_download_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_BUTTON)).click()

    def click_select_file_button(self):
        choose_file_btn = self.wait.until(EC.element_to_be_clickable(self.SELECT_FILE_BUTTON))
        choose_file_btn.send_keys(f"{os.getcwd()}\download\pic.jpg")
