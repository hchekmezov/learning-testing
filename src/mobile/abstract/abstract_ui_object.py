import abc

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory
from appium.webdriver import Remote

from src.mobile.utils.constants import Constants


class AbstractUIObject():
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver:  Remote):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 300)

    @abc.abstractmethod
    def is_present(self) -> bool: # is_ui_object_present
        return