import random

from tyt.base.base_page import BasePage


class TimeGenerator(BasePage):

    @classmethod
    def generate_random_time(cls):
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        # seconds = random.randint(0, 59)
        return f'{hours:02}:{minutes:02}'