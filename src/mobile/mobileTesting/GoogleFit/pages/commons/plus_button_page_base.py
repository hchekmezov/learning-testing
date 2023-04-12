import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.plus_button_page_item import PlusButtonPageItem


class PlusButtonPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_item_on_page(self, item: PlusButtonPageItem):
        return

    @abc.abstractmethod
    def close_page(self):
        return