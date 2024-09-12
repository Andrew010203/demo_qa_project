import random

from tyt.base.base_page import BasePage


class ColorGenerator(BasePage):
    COLORS = ["Red", "Green", "Blue", "Yellow", "Purple", "White", "Voilet", "Indigo", "Magenta", "Aqua"]

    @classmethod
    def random_color(cls):
        return random.choice(cls.COLORS)