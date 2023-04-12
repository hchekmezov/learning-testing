import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.gender import Gender


class GenderPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def check_gender(self, gender: Gender):
        return

    @abc.abstractmethod
    def click_back_button(self):
        return