import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class HeightPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def set_height(self, height: int):
        return