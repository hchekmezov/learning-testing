import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.create_food_page_base import CreateFoodPageBase


class UserPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_my_items_tab(self):
        return

    @abc.abstractmethod
    def click_create_food_button(self) -> CreateFoodPageBase:
        return

    @abc.abstractmethod
    def get_current_food_count(self) -> int:
        return

    @abc.abstractmethod
    def get_username(self) -> str:
        return

    @abc.abstractmethod
    def open_dashboard_page(self):
        return
