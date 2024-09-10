from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class FramesPage(BasePage):
    PAGE_URL = Links.FRAMES_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Frames"]')
    FRAME_1 = ("xpath", '//iframe[@id="frame1"]')
    FRAME_2 = ("xpath", '//iframe[@id="frame2"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Frames')), "Текст не совпадает"

    def switch_to_iframe_1(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.FRAME_1))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_iframe_2(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.FRAME_2))
