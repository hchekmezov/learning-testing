import abc

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage

class DashboardPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_track_steps_button(self):
        return