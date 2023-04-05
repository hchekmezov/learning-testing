import abc

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Remote
from src.mobile.abstract.abstract_ui_object import AbstractUIObject
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem


class BottomNavBarBase(AbstractUIObject):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_on_nav_bar_item(self, nav_bar_item: BottomNavBarItem):
        return

    @abc.abstractmethod
    def is_nav_bar_item_clickable(self, nav_bar_item: BottomNavBarItem):
        return