from selenium.webdriver import Remote

from src.mobile.abstract.abstract_ui_object import AbstractUIObject

import abc

from src.mobile.mobileTesting.GoogleFit.enums.nav_container_buttons import NavContainerButton


class BottomNavContainerBase(AbstractUIObject):
    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def is_nav_container_button_selected(self, nav_container_button: NavContainerButton):
        return
