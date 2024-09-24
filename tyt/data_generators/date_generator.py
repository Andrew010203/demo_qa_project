import random

from tyt.base.base_page import BasePage


class DateGenerator(BasePage):

    @classmethod
    def generate_random_date(cls):
        day = random.randint(1, 31)
        month = random.randint(1, 12)
        year = random.randint(1900, 2024)
        return f'{day:02}/{month:02}/{year}'

