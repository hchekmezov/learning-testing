import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class AddNutrientInfoPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_no_thanks_button(self):
        return
