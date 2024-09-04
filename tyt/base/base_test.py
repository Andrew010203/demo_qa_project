import pytest

from tyt.pages.broken_links_images_page import BrokenLinksImagesPage
from tyt.pages.buttons_page import ButtonsPage
from tyt.pages.check_box_page import CheckBoxPage
from tyt.pages.dynamic_properties_page import DynamicPropertiesPage
from tyt.pages.links_page import LinksPage
from tyt.pages.radio_button_page import RadioButtonPage
# from config.data import Data
from tyt.pages.text_box_page import TextBoxPage
from tyt.pages.upload_and_download_page import UploadAndDownloadPage
from tyt.pages.web_tables_page import WebTablesPage




class BaseTest:

    # data: Data

    text_box_page: TextBoxPage
    check_box_page: CheckBoxPage
    radio_button_page: RadioButtonPage
    web_tables_page: WebTablesPage
    buttons_page: ButtonsPage
    links_page: LinksPage
    broken_links_images_page: BrokenLinksImagesPage
    upload_and_download_page: UploadAndDownloadPage
    dynamic_properties_page: DynamicPropertiesPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        # request.cls.data = Data()

        request.cls.text_box_page = TextBoxPage(driver)
        request.cls.check_box_page = CheckBoxPage(driver)
        request.cls.radio_button_page = RadioButtonPage(driver)
        request.cls.web_tables_page = WebTablesPage(driver)
        request.cls.buttons_page = ButtonsPage(driver)
        request.cls.links_page = LinksPage(driver)
        request.cls.broken_links_images_page = BrokenLinksImagesPage(driver)
        request.cls.upload_and_download_page = UploadAndDownloadPage(driver)
        request.cls.dynamic_properties_page = DynamicPropertiesPage(driver)