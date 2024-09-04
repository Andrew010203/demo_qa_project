from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LinksPage(BasePage):

    PAGE_URL = Links.LINKS_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Links"]')
    HOME_LINK = ("xpath", '//a[@id="simpleLink"]')
    HOMEBT_OTT_LINK = ("xpath", '//a[@id="dynamicLink"]')
    CREATED_LINK = ("xpath", '//a[@id="created"]')
    NO_CONTENT_LINK = ("xpath", '//a[@id="no-content"]')
    MOVED_LINK = ("xpath", '//a[@id="moved"]')
    BAD_REQUEST_LINK = ("xpath", '//a[@id="bad-request"]')
    UNAUTHORIZED_LINK = ("xpath", '//a[@id="unauthorized"]')
    FORBIDDEN_LINK = ("xpath", '//a[@id="forbidden"]')
    NOT_FOUND_LINK = ("xpath", '//a[@id="invalid-url"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Links')), "Текст не совпадает"

    def click_home_link(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME_LINK)).click()
        # возврат на главную вкладку
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])

    def click_homebt_ott_link(self):
        self.wait.until(EC.element_to_be_clickable(self.HOMEBT_OTT_LINK)).click()
        # возврат на первую вкладку
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])

    def click_created_link(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATED_LINK)).click()

    def click_no_content_link(self):
        self.wait.until(EC.element_to_be_clickable(self.NO_CONTENT_LINK)).click()

    def click_moved_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MOVED_LINK)).click()

    def click_bad_request_link(self):
        self.wait.until(EC.element_to_be_clickable(self.BAD_REQUEST_LINK)).click()

    def click_unauthorized_link(self):
        self.wait.until(EC.element_to_be_clickable(self.UNAUTHORIZED_LINK)).click()

    def click_forbidden_link(self):
        self.wait.until(EC.element_to_be_clickable(self.FORBIDDEN_LINK)).click()

    def click_not_found_link(self):
        self.wait.until(EC.element_to_be_clickable(self.NOT_FOUND_LINK)).click()

