import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DragabblePage(BasePage):
    PAGE_URL = Links.DRAGABBLE_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Dragabble"]')
    # simple
    DRAG_ME = ("xpath", '//div[@id="dragBox"]')
    # Axis Restricted
    AXIS_RESTRICTED_TAB = ("xpath", '//a[text()="Axis Restricted"]')
    ONLY_X = ("xpath", '//div[@id="restrictedX"]')
    ONLY_Y = ("xpath", '//div[@id="restrictedY"]')
    # Container Restricted
    CONTAINER_RESTRICTED_TAB = ("xpath", '//a[text()="Container Restricted"]')
    CONT_W_BOX = ("xpath", '//div[@class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    CONT_W_PARENT = ("xpath", '//span[@class="ui-widget-header ui-draggable ui-draggable-handle"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Dragabble')), "Текст не совпадает"

    def drag_me_in_another_place(self):
        # Проверяем, что текстовое значение элемента совпадает
        drag_me = self.wait.until(EC.element_to_be_clickable(self.DRAG_ME)).text
        assert "Drag me" in drag_me
        # Передвигаем элемент по координатам
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.DRAG_ME)), 300, 150)

    def drag_only_x_only_y(self):
        # Переключаемся на вкладку Axis Restricted
        self.wait.until(EC.element_to_be_clickable(self.AXIS_RESTRICTED_TAB)).click()
        # Проверяем, что текстовое значение элемента совпадает
        only_x = self.wait.until(EC.element_to_be_clickable(self.ONLY_X)).text
        assert "Only X" in only_x
        # Передвигаем елемент по горизонтали
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.ONLY_Y)), 200, 0)
        # Проверяем, что текстовое значение элемента совпадает
        only_y = self.wait.until(EC.element_to_be_clickable(self.ONLY_Y)).text
        assert "Only Y" in only_y
        # Передвигаем елемент по вертикали
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.ONLY_Y)), 0, 150)

    def drag_cont_restricted(self):
        # Переключаемся на вкладку Container Restricted
        self.wait.until(EC.element_to_be_clickable(self.CONTAINER_RESTRICTED_TAB)).click()
        # Проверяем, что текстовое значение элемента совпадает
        cont_w_box = self.wait.until(EC.element_to_be_clickable(self.CONT_W_BOX)).text
        assert "I'm contained within the box" in cont_w_box
        # Передвигаем елемент по координатам
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.CONT_W_BOX)), 200, 50)
        # Проверяем, что текстовое значение элемента совпадает
        cont_w_parent = self.wait.until(EC.element_to_be_clickable(self.CONT_W_PARENT)).text
        assert "I'm contained within my parent" in cont_w_parent
        # Передвигаем елемент по координатам
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.CONT_W_PARENT)), 15, 25)
