from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class ToolTipsPage(BasePage):
    PAGE_URL = Links.TOOL_TIPS_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Tool Tips"]')
    TOOL_TIP_BUTTON = ("xpath", '//button[@id="toolTipButton"]')
    TOOL_TIP_BUTTON_HOVERED = ("xpath", '//div[text()="You hovered over the Button"]')
    TOOL_TIP_FIELD = ("xpath", '//input[@placeholder="Hover me to see"]')
    TOOL_TIP_FIELD_HOVERED = ("xpath", '//div[text()="You hovered over the text field"]')
    LINK_CONTRARY = ("xpath", '//a[text()="Contrary"]')
    CONTRARY_HOVERED = ("xpath", '//div[text()="You hovered over the Contrary"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Tool Tips')), "Текст не совпадает"

    def hover_tool_tip_button(self):
        value_hover_button = self.wait.until(EC.visibility_of_element_located(self.TOOL_TIP_BUTTON))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_hover_button).perform()
        value_hover_button = self.wait.until(EC.visibility_of_element_located(self.TOOL_TIP_BUTTON)).text
        print(value_hover_button)
        assert value_hover_button == "Hover me to see", "Название не совпадает"
        self.wait.until(EC.text_to_be_present_in_element(self.TOOL_TIP_BUTTON_HOVERED, 'You hovered over the Button')), "Текст не совпадает"

    def hover_tool_tip_field(self):
        value_hover_field = self.wait.until(EC.visibility_of_element_located(self.TOOL_TIP_FIELD))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_hover_field).perform()
        value_hover_field = self.wait.until(EC.visibility_of_element_located(self.TOOL_TIP_FIELD)).get_attribute("placeholder")
        print(value_hover_field)
        assert value_hover_field == "Hover me to see", "Название не совпадает"
        self.wait.until(EC.text_to_be_present_in_element(self.TOOL_TIP_FIELD_HOVERED, 'You hovered over the text field')), "Текст не совпадает"

    def hover_tool_tip_contrary(self):
        value_hover_contrary = self.wait.until(EC.visibility_of_element_located(self.LINK_CONTRARY))
        actions = ActionChains(self.driver)
        actions.move_to_element(value_hover_contrary).perform()
        value_hover_contrary = self.wait.until(EC.visibility_of_element_located(self.LINK_CONTRARY)).text
        print(value_hover_contrary)
        assert value_hover_contrary == "Contrary", "Название не совпадает"
        self.wait.until(EC.text_to_be_present_in_element(self.CONTRARY_HOVERED, 'You hovered over the Contrary')), "Текст не совпадает"
