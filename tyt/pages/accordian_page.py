from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class AccordianPage(BasePage):
    PAGE_URL = Links.ACCORDIAN_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Accordian"]')
    WHAT_CARD = ("xpath", '//*[@id="section1Heading"]')
    WHAT_CARD_CONTENT = ("xpath", '//*[@id="section1Content"]/p')
    WHERE_CARD = ("xpath", '//div[@id="section2Heading"]')
    WHERE_CARD_CONTENT = ("xpath", '//div[@id="section2Content"]/p')
    WHY_CARD = ("xpath", '//*[@id="section3Heading"]')
    WHY_CARD_CONTENT = ("xpath", '//*[@id="section3Content"]/p')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Accordian')), "Текст не совпадает"

    def click_what_card(self):
        self.wait.until(EC.element_to_be_clickable(self.WHAT_CARD))
        value_title = self.wait.until(EC.visibility_of_element_located(self.WHAT_CARD)).text
        assert "What is Lorem Ipsum?" in value_title, "Заголовок не совпадает"
        value_body_title = self.wait.until(EC.visibility_of_element_located(self.WHAT_CARD_CONTENT)).text
        print(value_body_title)
        assert value_body_title is not None, "Контент отсутствует"

    def click_where_card(self):
        self.wait.until(EC.element_to_be_clickable(self.WHERE_CARD)).click()
        value_title = self.wait.until(EC.visibility_of_element_located(self.WHERE_CARD)).text
        assert "Where does it come from?" in value_title, "Заголовок не совпадает"
        value_body_title = self.wait.until(EC.visibility_of_element_located(self.WHERE_CARD_CONTENT)).text
        print(value_body_title)
        assert value_body_title is not None, "Контент отсутствует"

    def click_why_card(self):
        self.wait.until(EC.element_to_be_clickable(self.WHY_CARD)).click()
        value_title = self.wait.until(EC.visibility_of_element_located(self.WHY_CARD)).text
        assert "Why do we use it?" in value_title, "Заголовок не совпадает"
        value_body_title = self.wait.until(EC.visibility_of_element_located(self.WHY_CARD_CONTENT)).text
        print(value_body_title)
        assert value_body_title is not None, "Контент отсутствует"