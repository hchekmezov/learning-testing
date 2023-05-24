import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class QuickAddPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def quick_add_fat_carbs_protein(self, fat: int, carbs: int, protein: int):
        return

    @abc.abstractmethod
    def is_calories_equals_value(self, value: int) -> bool:
        return
