from src.mobile.abstract.abstract_page import AbstractPage
from appium.webdriver import Remote

import abc

class PreviewPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_login_button(self):
        return