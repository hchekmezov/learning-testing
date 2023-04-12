import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class TimePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    # @abc.abstractmethod
    # def send_keys_to_hours(self, hours: int):
    #     return
    #
    # @abc.abstractmethod
    # def send_keys_to_minutes(self, minutes: int):
    #     return

    @abc.abstractmethod
    def set_hours_and_minutes(self, hours: int, minutes: int):
        return

    @abc.abstractmethod
    def click_ok_button(self):
        return