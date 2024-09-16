import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class SliderPage(BasePage):
    PAGE_URL = Links.SLIDER_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Slider"]')
    SLIDER = ("xpath", '//input[@type="range"]')
    DATA_SLIDER = ("xpath", '//div[@class="range-slider__tooltip__label"]')
    DATA_FIELD = ("xpath", '//input[@id="sliderValue"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Slider')), "Текст не совпадает"

    def use_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable(self.SLIDER))
        value_before = self.wait.until(EC.visibility_of_element_located(self.DATA_FIELD)).get_attribute('value')
        self.action_drag_and_drop_by_offset(slider, random.randint(0, 10), 0)
        value_after = self.wait.until(EC.visibility_of_element_located(self.DATA_SLIDER)).text
        data_slider = self.wait.until(EC.visibility_of_element_located(self.DATA_SLIDER)).text
        data_field = self.wait.until(EC.visibility_of_element_located(self.DATA_FIELD)).get_attribute('value')
        print(data_slider, data_field)
        assert data_slider == data_field

        print(value_before, value_after)
        assert value_before != value_after, "Ошибка"

