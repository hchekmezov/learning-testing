import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class DragAndDropPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def make_drag_and_drop_dot1_and_dot2(self):
        return

    @abc.abstractmethod
    def is_drag_and_dropped_dot1_and_dot2(self) -> bool:
        return