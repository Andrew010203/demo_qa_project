import pytest

from tyt.pages.accordian_page import AccordianPage
from tyt.pages.alerts_page import AlertsPage
from tyt.pages.auto_complete_page import AutoCompletePage
from tyt.pages.broken_links_images_page import BrokenLinksImagesPage
from tyt.pages.browser_windows_page import BrowserWindowsPage
from tyt.pages.buttons_page import ButtonsPage
from tyt.pages.check_box_page import CheckBoxPage
from tyt.pages.date_picker_page import DatePickerPage
from tyt.pages.dragabble_page import DragabblePage
from tyt.pages.droppable_page import DroppablePage
from tyt.pages.dynamic_properties_page import DynamicPropertiesPage
from tyt.pages.frames_page import FramesPage
from tyt.pages.links_page import LinksPage
from tyt.pages.login_page import LoginPage
from tyt.pages.menu_page import MenuPage
from tyt.pages.modal_dialogs_page import ModalDialogsPage
from tyt.pages.nested_frames_page import NestedFramesPage
from tyt.pages.practice_form_page import PracticeFormPage
from tyt.pages.progress_bar_page import ProgressBarPage
from tyt.pages.radio_button_page import RadioButtonPage
from tyt.pages.register_page import RegisterPage
from tyt.pages.resizable_page import ResizablePage
from tyt.pages.slectable_page import SelectablePage
from tyt.pages.slider_page import SliderPage
from tyt.pages.sortable_page import SortablePage
from tyt.pages.tabs_page import TabsPage
from tyt.config.data import Data
from tyt.pages.text_box_page import TextBoxPage
from tyt.pages.tool_tips_page import ToolTipsPage
from tyt.pages.upload_and_download_page import UploadAndDownloadPage
from tyt.pages.web_tables_page import WebTablesPage




class BaseTest:

    data: Data

    text_box_page: TextBoxPage
    check_box_page: CheckBoxPage
    radio_button_page: RadioButtonPage
    web_tables_page: WebTablesPage
    buttons_page: ButtonsPage
    links_page: LinksPage
    broken_links_images_page: BrokenLinksImagesPage
    upload_and_download_page: UploadAndDownloadPage
    dynamic_properties_page: DynamicPropertiesPage
    practice_form_page: PracticeFormPage
    browser_windows_page: BrowserWindowsPage
    alerts_page: AlertsPage
    frames_page: FramesPage
    nested_frames_page: NestedFramesPage
    modal_dialogs_page: ModalDialogsPage
    accordian_page: AccordianPage
    auto_complete_page: AutoCompletePage
    date_picker_page: DatePickerPage
    slider_page: SliderPage
    progress_bar_page: ProgressBarPage
    tabs_page: TabsPage
    tool_tips_page: ToolTipsPage
    menu_page: MenuPage
    sortable_page: SortablePage
    selectable_page: SelectablePage
    resizable_page: ResizablePage
    droppable_page: DroppablePage
    dragabble_page: DragabblePage
    register_page: RegisterPage
    login_page: LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.text_box_page = TextBoxPage(driver)
        request.cls.check_box_page = CheckBoxPage(driver)
        request.cls.radio_button_page = RadioButtonPage(driver)
        request.cls.web_tables_page = WebTablesPage(driver)
        request.cls.buttons_page = ButtonsPage(driver)
        request.cls.links_page = LinksPage(driver)
        request.cls.broken_links_images_page = BrokenLinksImagesPage(driver)
        request.cls.upload_and_download_page = UploadAndDownloadPage(driver)
        request.cls.dynamic_properties_page = DynamicPropertiesPage(driver)
        request.cls.practice_form_page = PracticeFormPage(driver)
        request.cls.browser_windows_page = BrowserWindowsPage(driver)
        request.cls.alerts_page = AlertsPage(driver)
        request.cls.frames_page = FramesPage(driver)
        request.cls.nested_frames_page = NestedFramesPage(driver)
        request.cls.modal_dialogs_page = ModalDialogsPage(driver)
        request.cls.accordian_page = AccordianPage(driver)
        request.cls.auto_complete_page = AutoCompletePage(driver)
        request.cls.date_picker_page = DatePickerPage(driver)
        request.cls.slider_page = SliderPage(driver)
        request.cls.progress_bar_page = ProgressBarPage(driver)
        request.cls.tabs_page = TabsPage(driver)
        request.cls.tool_tips_page = ToolTipsPage(driver)
        request.cls.menu_page = MenuPage(driver)
        request.cls.sortable_page = SortablePage(driver)
        request.cls.selectable_page = SelectablePage(driver)
        request.cls.resizable_page = ResizablePage(driver)
        request.cls.droppable_page = DroppablePage(driver)
        request.cls.dragabble_page = DragabblePage(driver)
        request.cls.register_page = RegisterPage(driver)
        request.cls.login_page = LoginPage(driver)
