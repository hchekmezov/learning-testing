import abc

from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver import Remote


class AbstractPage():
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver:  Remote):
        # super().__init__()
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 30)

    @abc.abstractmethod
    def is_page_opened(self) -> bool:
        return

