from appium.webdriver import Remote
import abc

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.meals_names import MealName


class AddFoodPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_needed_page_opened_by_meal_name(self, meal_name: MealName) -> bool:
        return

    @abc.abstractmethod
    def get_title(self) -> str:
        return

    @abc.abstractmethod
    def click_back_button(self):
        return

    @abc.abstractmethod
    def find_and_add_meal(self, meal: str):
        return