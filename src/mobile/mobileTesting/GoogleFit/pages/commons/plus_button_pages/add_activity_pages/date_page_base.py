import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class DatePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_needed_date(self, index: int):
        return

    @abc.abstractmethod
    def click_ok_button(self):
        return