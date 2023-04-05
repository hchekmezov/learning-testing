from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.Carina.enums.navigate_up_menu_item import NavigateUpMenuItem
import abc


class NavigateUpMenuBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver):
        super().__init__(driver)

    @abc.abstractmethod
    def click_navigate_up_menu_item(self, nav_up_item: NavigateUpMenuItem):
        return