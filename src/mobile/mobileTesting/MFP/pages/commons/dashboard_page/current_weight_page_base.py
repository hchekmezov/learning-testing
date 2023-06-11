import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class CurrentWeightPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def set_weight(self, weight: int):
        return