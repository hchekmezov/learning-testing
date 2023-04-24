import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class NewsfeedPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)