import abc
from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class GFCommonPageBase(AbstractPage):

    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def get_bottom_nav_container(self):
        return

    @abc.abstractmethod
    def get_color_of_element(self, locator):
        return