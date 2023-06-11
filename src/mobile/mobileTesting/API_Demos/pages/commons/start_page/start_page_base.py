import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.API_Demos.enums.start_page_items import StartPageItem


class StartPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def open_page(self, item: StartPageItem) -> AbstractPage:
        return