import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class GFCommonPageBase(AbstractPage):

    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def get_bottom_nav_container(self):
        return