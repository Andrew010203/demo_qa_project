import allure
from tyt.base.base_test import BaseTest


@allure.feature("Check upload and down")
class TestUploadAndDownload(BaseTest):

    @allure.title("Test upload/down")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_upload_and_download(self):
        self.upload_and_download_page.open()
        self.upload_and_download_page.is_opened()
        self.upload_and_download_page.check_main_word()
        self.upload_and_download_page.click_download_button()
        self.upload_and_download_page.click_select_file_button()