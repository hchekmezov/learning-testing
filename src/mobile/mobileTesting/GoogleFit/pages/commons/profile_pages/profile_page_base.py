import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.pages_from_about_you import PageFromAboutYou
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.switchers import Switcher


class ProfilePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def open_page_from_about_you(self, page: PageFromAboutYou):
        return

    @abc.abstractmethod
    def open_settings_page(self):
        return

    @abc.abstractmethod
    def check_all_changed_info(self, gender, birthday, weight, height) -> bool:
        return

    @abc.abstractmethod
    def is_switcher_checked(self, switcher: Switcher):
        return

    @abc.abstractmethod
    def switcher_check(self, switcher: Switcher):
        return

    @abc.abstractmethod
    def switcher_uncheck(self, switcher: Switcher):
        return

    @abc.abstractmethod
    def get_color_of_switcher(self, switcher: Switcher):
        return

    @abc.abstractmethod
    def get_color_of_account_image(self):
        return