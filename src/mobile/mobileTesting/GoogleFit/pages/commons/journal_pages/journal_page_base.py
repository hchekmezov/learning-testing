import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class JournalPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_activity_right(self, activity: str, time: str, date: str) -> bool:
        return

    @abc.abstractmethod
    def click_activity_view_group(self):
        return