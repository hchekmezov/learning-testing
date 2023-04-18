import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.colors import Color


# from src.mobile.mobileTesting.GoogleFit.enums.profile_page.settings_page.settings_titles import SettingsTitle


class SettingsPageBase(AbstractPage):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def color_of_title(self, settings_title):
        return