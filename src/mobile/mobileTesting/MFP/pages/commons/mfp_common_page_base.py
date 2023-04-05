from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage
import abc

class MFPCommonPageBase(AbstractPage):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def wait_until_spinner_rounding(self):
        return

    @abc.abstractmethod
    def get_bottom_nav_bar(self):
        return