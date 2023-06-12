import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.API_Demos.enums.popup_menu_button_items import PopupMenuButtonItem


class PopupMenuPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def make_a_toast_for(self, item: PopupMenuButtonItem):
        return

    @abc.abstractmethod
    def is_toast_shown_for(self, item: PopupMenuButtonItem):
        return