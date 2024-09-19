import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ResizablePage(BasePage):
    PAGE_URL = Links.RESIZABLE_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Resizable"]')
    RESIZABLE_BOX = ("xpath", '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE_BOX_HANDLE = ("xpath", '(//span[@class="react-resizable-handle react-resizable-handle-se"])[1]')
    RESIZABLE = ("xpath", '//div[@id="resizable"]')
    RESIZABLE_HANDLE = ("xpath", '(//span[@class="react-resizable-handle react-resizable-handle-se"])[2]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Resizable')), "Текст не совпадает"

    def interaction_with_resizable_box(self):
        x_offset = random.randint(150, 300)
        y_offset = random.randint(150, 500)
        value_size = self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.RESIZABLE_BOX_HANDLE)), x_offset, y_offset)
        print(value_size)

    def interaction_with_resizable(self):
        x_offset = random.randint(20, 500)
        y_offset = random.randint(20, 200)
        value_size = self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.RESIZABLE_HANDLE)), x_offset, y_offset)
        print(value_size)


