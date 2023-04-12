import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class ActivityPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def delete_activity(self):
        return

