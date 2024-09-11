from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class AccordianPage(BasePage):
    PAGE_URL = Links.ACCORDIAN_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Accordian"]')
    WHAT_CARD = ("xpath", '//*[@id="section1Heading"]')
    WHERE_CARD = ("xpath", '//*[@id="section2Heading"]')
    WHY_CARD = ("xpath", '//*[@id="section3Heading"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Accordian')), "Текст не совпадает"

    def click_what_card(self):
        self.wait.until(EC.element_to_be_clickable(self.WHAT_CARD))
        value_title = self.driver.find_element("xpath", '//*[text()="What is Lorem Ipsum?"]').text
        assert value_title == "What is Lorem Ipsum?", "Заголовок не совпадает"
        value_body_title = self.driver.find_element("xpath", '//*[@id="section1Content"]/p').text
        print(value_body_title)
        assert "Lorem Ipsum is simply dummy text of the printing and typ" in value_body_title, "Содержимое не совпадает"

    def click_where_card(self):
        self.wait.until(EC.element_to_be_clickable(self.WHERE_CARD)).click()
        value_title = self.driver.find_element("xpath", '//*[text()="Where does it come from?"]').text
        assert value_title == "Where does it come from?", "Заголовок не совпадает"
        value_body_title = self.driver.find_element("xpath", '//*[@id="section2Content"]/p').text
        print(value_body_title)
        assert "Contrary to popular belief, Lorem Ipsum is not simply ra" in value_body_title, "Содержимое не совпадает"

    def click_why_card(self):
        self.wait.until(EC.element_to_be_clickable(self.WHY_CARD)).click()
        value_title = self.driver.find_element("xpath", '//*[text()="Why do we use it?"]').text
        assert value_title == "Why do we use it?", "Заголовок не совпадает"
        value_body_title = self.driver.find_element("xpath", '//*[@id="section3Content"]/p').text
        print(value_body_title)
        assert "It is a long established fact that a reader will be dist" in value_body_title, "Содержимое не совпадает"