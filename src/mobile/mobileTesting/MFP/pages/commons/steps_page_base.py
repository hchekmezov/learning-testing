import abc

from appium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage

class StepsPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_progress_spinner_rounding_present(self):
        return

    @abc.abstractmethod
    def click_enable_checkbox(self):
        return
