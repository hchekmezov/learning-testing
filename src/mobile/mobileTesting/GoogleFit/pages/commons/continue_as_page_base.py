import abc

from selenium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage

class ContinueAsPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_continue_as_button(self):
        return