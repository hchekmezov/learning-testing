import abc

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver import Remote

from src.mobile.utils.constants import Constants


class AbstractPage():
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver:  Remote):
        # super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 300)

    @abc.abstractmethod
    def is_page_opened(self) -> bool:
        return

