import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class SurePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_yes_button(self):
        return

    @abc.abstractmethod
    def click_no_button(self):
        return