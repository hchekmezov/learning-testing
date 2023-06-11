import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class DatePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def switch_to_text_mode(self):
        return

    @abc.abstractmethod
    def set_date_by_years_ago(self, years: int):
        return
