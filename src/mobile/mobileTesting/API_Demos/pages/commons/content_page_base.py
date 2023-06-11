import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.start_page_base import StartPageBase


class ContentPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_ok_button(self) -> StartPageBase:
        return