import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class ActivityTypePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def select_random_activity(self, activity):
        return