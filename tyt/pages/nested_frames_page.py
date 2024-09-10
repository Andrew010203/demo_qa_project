from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class NestedFramesPage(BasePage):
    PAGE_URL = Links.NESTED_FRAMES_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Nested Frames"]')
    PARENT_FRAME = ("xpath", '//iframe[@id="frame1"]')
    CHILD_FRAME = ("xpath", '//iframe[@srcdoc="<p>Child Iframe</p>"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Nested Frames')), "Текст не совпадает"

    def switch_to_parent_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.PARENT_FRAME))
        value_text = self.driver.find_element("xpath", "//body").text
        assert value_text == "Parent frame", "Название frame не совпадает"

    def switch_to_child_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.CHILD_FRAME))
        value_text = self.driver.find_element("xpath", "//body").text
        assert value_text == "Child Iframe", "Название frame не совпадает"

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

