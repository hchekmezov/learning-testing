import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class HomePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def get_plus_button(self):
        return

    @abc.abstractmethod
    def is_plus_button_static(self):
        return

    @abc.abstractmethod
    def is_plus_button_present(self):
        return

    @abc.abstractmethod
    def is_plus_button_below_container(self):
        return


