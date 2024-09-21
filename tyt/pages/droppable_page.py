import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DroppablePage(BasePage):
    PAGE_URL = Links.DROPPABLE_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Droppable"]')
    # simple
    DRAG_ME = ("xpath", '//div[@id="draggable"]')
    DROP_HERE = ("xpath", '(//div[@id="droppable"])[1]')
    # accept
    ACCEPT_TAB = ("xpath", '//a[@id="droppableExample-tab-accept"]')
    ACCEPTABLE = ("xpath", '//div[@id="acceptable"]')
    NOT_ACCEPTABLE = ("xpath", '//div[@id="notAcceptable"]')
    ACCEPT_DROP_HERE = ("xpath", '(//div[@id="droppable"])[2]')
    # Prevent Propogation
    PREVENT_PROPOGATION_TAB = ("xpath", '//a[@id="droppableExample-tab-preventPropogation"]')
    PREVENT_DRAG_ME = ("xpath", '//div[@id="dragBox"]')
    OUTER_DROPPABLE_NG = ("xpath", '//div[@id="notGreedyDropBox"]/p')
    INNER_DROPPABLE_NG = ("xpath", '//div[@id="notGreedyInnerDropBox"]')
    OUTER_DROPPABLE_G = ("xpath", '//div[@id="greedyDropBox"]')
    INNER_DROPPABLE_G = ("xpath", '//div[@id="greedyDropBoxInner"]')
    # Prevent Draggable
    REVERT_DRAGGABLE_TAB = ("xpath", '//a[@id="droppableExample-tab-revertable"]')
    DROP_HERE_REVERT_DRAGGABLE = ("xpath", '(//div[@id="droppable"])[3]')
    WILL_REVERT = ("xpath", '//div[@id="revertable"]')
    NOT_REVERT = ("xpath", '//div[@id="notRevertable"]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Droppable')), "Текст не совпадает"

    def drag_me_in_drop_here(self):
        drag_me = self.wait.until(EC.element_to_be_clickable(self.DRAG_ME)).text
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE)).text
        assert "Drag me" in drag_me
        assert "Drop here" in drop_here
        drag_me = self.wait.until(EC.element_to_be_clickable(self.DRAG_ME))
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE))
        self.drag_and_drop(drag_me, drop_here)
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE)).text
        assert "Dropped!" in drop_here

    def drag_not_acceptable_in_drop_here(self):
        # Переключаемся на вкладку Accept
        self.wait.until(EC.element_to_be_clickable(self.ACCEPT_TAB)).click()
        # Проверяем текст элемента
        not_acceptable = self.wait.until(EC.element_to_be_clickable(self.NOT_ACCEPTABLE)).text
        assert "Not Acceptable" in not_acceptable
        not_acceptable = self.wait.until(EC.element_to_be_clickable(self.NOT_ACCEPTABLE))
        drop_here = self.wait.until(EC.element_to_be_clickable(self.ACCEPT_DROP_HERE))
        # Передвигаем элемент Not acceptable в Drop here и проверяем, что текстовое значение Drop here не изменилось
        self.drag_and_drop(not_acceptable, drop_here)
        drop_here = self.wait.until(EC.element_to_be_clickable(self.ACCEPT_DROP_HERE)).text
        assert "Drop here" in drop_here

    def drag_acceptable_in_drop_here(self):
        # Проверяем текст элемента
        acceptable = self.wait.until(EC.element_to_be_clickable(self.ACCEPTABLE)).text
        assert "Acceptable" in acceptable
        acceptable = self.wait.until(EC.element_to_be_clickable(self.ACCEPTABLE))
        drop_here = self.wait.until(EC.element_to_be_clickable(self.ACCEPT_DROP_HERE))
        # Передвигаем элемент Acceptable в Drop here и проверяем, что текстовое значение Drop here изменилось "Dropped!"
        self.drag_and_drop(acceptable, drop_here)
        drop_here = self.wait.until(EC.element_to_be_clickable(self.ACCEPT_DROP_HERE)).text
        assert "Dropped!" in drop_here

    def drag_me_in_outer_droppable_ng(self):
        # Переключаемся на вкладку Prevent Propogation
        self.wait.until(EC.element_to_be_clickable(self.PREVENT_PROPOGATION_TAB)).click()
        drag_me = self.wait.until(EC.element_to_be_clickable(self.PREVENT_DRAG_ME)).text
        assert "Drag Me" in drag_me
        outer_droppable = self.wait.until(EC.element_to_be_clickable(self.OUTER_DROPPABLE_NG)).text
        assert "Outer droppable" in outer_droppable
        # Передвигаем элемент Drag Me в Outer droppable и проверяем,
                                                          # что текстовое значение Outer droppable изменилось "Dropped!"
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.PREVENT_DRAG_ME)), 320, 0)
        outer_droppable = self.wait.until(EC.element_to_be_clickable(self.OUTER_DROPPABLE_NG)).text
        assert "Dropped!" in outer_droppable

    def drag_me_in_inner_droppable_not_greedy(self):
        # Переключаемся на вкладку Prevent Propogation
        self.wait.until(EC.element_to_be_clickable(self.PREVENT_PROPOGATION_TAB)).click()
        drag_me = self.wait.until(EC.element_to_be_clickable(self.PREVENT_DRAG_ME)).text
        assert "Drag Me" in drag_me
        inner_droppable = self.wait.until(EC.element_to_be_clickable(self.INNER_DROPPABLE_NG)).text
        assert "Inner droppable (not greedy)" in inner_droppable
        # Передвигаем элемент Drag Me в Inner droppable (not reedy) и проверяем,
                                                          # что текстовое значение Inner droppable изменилось "Dropped!"
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.PREVENT_DRAG_ME)), 0, 120)
        inner_droppable = self.wait.until(EC.element_to_be_clickable(self.INNER_DROPPABLE_NG)).text
        assert "Dropped!" in inner_droppable

    def drag_me_in_outer_droppable_g(self):
        # Переключаемся на вкладку Prevent Propogation
        self.wait.until(EC.element_to_be_clickable(self.PREVENT_PROPOGATION_TAB)).click()
        drag_me = self.wait.until(EC.element_to_be_clickable(self.PREVENT_DRAG_ME)).text
        assert "Drag Me" in drag_me
        outer_droppable = self.wait.until(EC.element_to_be_clickable(self.OUTER_DROPPABLE_G)).text
        assert "Outer droppable" in outer_droppable
        # Передвигаем элемент Drag Me в Outer droppable и проверяем,
                                                          # что текстовое значение Outer droppable изменилось "Dropped!"
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.PREVENT_DRAG_ME)), 0, 170)
        outer_droppable = self.wait.until(EC.element_to_be_clickable(self.OUTER_DROPPABLE_G)).text
        assert "Dropped!" in outer_droppable

    def drag_me_in_inner_droppable_g(self):
        # Переключаемся на вкладку Prevent Propogation
        self.wait.until(EC.element_to_be_clickable(self.PREVENT_PROPOGATION_TAB)).click()
        drag_me = self.wait.until(EC.element_to_be_clickable(self.PREVENT_DRAG_ME)).text
        assert drag_me == "Drag Me"
        inner_droppable = self.wait.until(EC.element_to_be_clickable(self.INNER_DROPPABLE_G)).text
        assert "Inner droppable (greedy)" in inner_droppable
        # Передвигаем элемент Drag Me в Inner droppable и проверяем,
                                                          # что текстовое значение Inner droppable изменилось "Dropped!"
        self.action_drag_and_drop_by_offset(self.wait.until
                                            (EC.element_to_be_clickable(self.PREVENT_DRAG_ME)), 0, 65)
        inner_droppable = self.wait.until(EC.element_to_be_clickable(self.INNER_DROPPABLE_G)).text
        assert "Dropped!" in inner_droppable

    def not_revert_in_drop_here(self):
        # Переключаемся на вкладку Prevent Draggable
        self.wait.until(EC.element_to_be_clickable(self.REVERT_DRAGGABLE_TAB)).click()
        not_revert = self.wait.until(EC.element_to_be_clickable(self.NOT_REVERT)).text
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE_REVERT_DRAGGABLE)).text
        assert "Not Revert" in not_revert
        assert "Drop here" in drop_here
        not_revert = self.wait.until(EC.element_to_be_clickable(self.NOT_REVERT))
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE_REVERT_DRAGGABLE))
        self.drag_and_drop(not_revert, drop_here)
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE_REVERT_DRAGGABLE)).text
        assert "Dropped!" in drop_here

    def will_revert_in_drop_here(self):
        # Переключаемся на вкладку Prevent Draggable
        self.wait.until(EC.element_to_be_clickable(self.REVERT_DRAGGABLE_TAB)).click()
        will_revert = self.wait.until(EC.element_to_be_clickable(self.WILL_REVERT)).text
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE_REVERT_DRAGGABLE)).text
        assert "Will Revert" in will_revert
        assert "Dropped!" in drop_here
        will_revert = self.wait.until(EC.element_to_be_clickable(self.WILL_REVERT))
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE_REVERT_DRAGGABLE))
        self.drag_and_drop(will_revert, drop_here)
        drop_here = self.wait.until(EC.element_to_be_clickable(self.DROP_HERE_REVERT_DRAGGABLE)).text
        assert "Dropped!" in drop_here





