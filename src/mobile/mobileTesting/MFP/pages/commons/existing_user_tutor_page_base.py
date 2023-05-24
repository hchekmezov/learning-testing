from appium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage
import abc

class ExistingUserTutorPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_close_button(self):
        return
