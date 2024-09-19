import random

from tyt.base.base_page import BasePage
from tyt.config.links import Links
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class SortablePage(BasePage):
    PAGE_URL = Links.SORTABLE_PAGE

    MAIN_WORD = ("xpath", '//h1[text()="Sortable"]')
    TAB_LIST = ("xpath", '//a[text()="List"]')
    LIST_ITEM = ("xpath", '//div[@id="demo-tabpane-list"]/div')
    TAB_GRID = ("xpath", '//a[@id="demo-tab-grid"]')
    # GRID_ITEM = ("xpath", '//div[@class="create-grid"]')
    # GRID_ITEM = ("xpath", '//div[@id="demo-tabpane-grid"]//*[@class="list-group-item list-group-item-action"]')
    # GRID_ITEM = ("xpath", f'(//div[@id="demo-tabpane-grid"]//div)[{random.randint(3, 11)}]')
    GRID_ITEM = ("xpath", f'(//div[@id="demo-tabpane-grid"]//*[@class="list-group-item list-group-item-action"])[2]')

    list_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
    list_grit = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Sortable')), "Текст не совпадает"

    # def get_sortable_items(self, elements):
    #     item_list = self.wait.until(EC.presence_of_all_elements_located(*elements))
    #     return [item.text for item in item_list]

    def drag_and_drop_random_list(self):
        # Выбираем случайный элемент из списка
        random_item_text = random.choice(self.list_list)

        # Находим элемент по тексту
        source_element = self.wait.until(
            EC.visibility_of_element_located((self.LIST_ITEM[0], f'//div[text()="{random_item_text}"]')))

        # Находим целевой элемент (например, первый элемент в списке)
        target_element = self.wait.until(
            EC.visibility_of_element_located((self.LIST_ITEM[0], f'//div[text()="{random_item_text}"]')))

        # Выполняем действие перетаскивания
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

    def drag_and_drop_random_grit(self):
        self.wait.until(EC.element_to_be_clickable(self.TAB_GRID)).click()

        # Выбираем случайный элемент из списка
        random_item_text = random.choice(self.list_grit)
        print(f"Выбранный элемент: {random_item_text}")

        # Находим элемент по тексту
        source_element = self.wait.until(
            EC.visibility_of_element_located(
                ('xpath', f'//div[@id="demo-tabpane-grid"]//div[text()="{random_item_text}"]')))

        print(f"Найден исходный элемент: {source_element.text}")

        # Находим целевой элемент (например, элемент с текстом "Two")
        target_element = self.wait.until(
        EC.visibility_of_element_located(('xpath', '//div[@id="demo-tabpane-grid"]//div[text()="Seven"]')))

        print(f"Найден целевой элемент: {target_element.text}")

        # Выполняем действие перетаскивания
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()
