from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class BrokenLinksImagesPage(BasePage):

    PAGE_URL = Links.BROKEN_LINKS_IMAGES_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Broken Links - Images"]')
    VALID_LINK = ("xpath", '//a[@href="http://demoqa.com"]')
    BROKEN_LINK = ("xpath", '//a[@href="http://the-internet.herokuapp.com/status_codes/500"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Broken Links - Images')), "Текст не совпадает"

    def click_valid_link(self):
        self.wait.until(EC.element_to_be_clickable(self.VALID_LINK)).click()
        self.driver.back()

        # Возврат назад return

    def click_broken_link(self):
        self.wait.until(EC.element_to_be_clickable(self.BROKEN_LINK)).click()
        self.driver.back()