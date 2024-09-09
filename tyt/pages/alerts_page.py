from tyt.base.base_page import BasePage
from tyt.config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class AlertsPage(BasePage):
    PAGE_URL = Links.ALERTS_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Alerts"]')
    CLICK_BUTTON_TO_SEE_ALERT = ("xpath", '//button[@id="alertButton"]')
    CLICK_BUTTON_TO_SEE_ALERT_AFTER_5_SECONDS = ("xpath", '//button[@id="timerAlertButton"]')
    CLICK_BUTTON_CONFIRM_BOX_WILL_APPEAR = ("xpath", '//button[@id="confirmButton"]')
    CLICK_BUTTON_PROMPT_BOX_WILL_APPEAR = ("xpath", '//button[@id="promtButton"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Alerts')), "Текст не совпадает"

    def click_button_to_see_alert(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_BUTTON_TO_SEE_ALERT)).click()
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        alert.accept()

    def click_button_to_see_alert_after_5_seconds(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_BUTTON_TO_SEE_ALERT_AFTER_5_SECONDS)).click()
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        alert.accept()

    def click_button_confirm_box_will_appear(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_BUTTON_CONFIRM_BOX_WILL_APPEAR)).click()
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        alert.dismiss()

    def click_button_prompt_box_will_appear(self, text):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_BUTTON_PROMPT_BOX_WILL_APPEAR)).click()
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()