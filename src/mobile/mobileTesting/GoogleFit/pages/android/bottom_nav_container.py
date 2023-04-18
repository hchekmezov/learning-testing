from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.icons import Icons
from src.mobile.mobileTesting.GoogleFit.enums.labels import Labels

from src.mobile.mobileTesting.GoogleFit.enums.nav_container_buttons import NavContainerButton
from src.mobile.mobileTesting.GoogleFit.pages.commons.bottom_nav_container_base import BottomNavContainerBase


class BottomNavContainer(BottomNavContainerBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__nav_container_button = (AppiumBy.XPATH, None)

    def is_present(self) -> bool:
        return self.driver.find_element(AppiumBy.ID, "com.google.android.apps.fitness:id/bottom_navigation").is_enabled()

    def is_nav_container_button_selected(self, nav_container_button: NavContainerButton):
        return self.driver.find_element(self.__nav_container_button[0],
                                        "//android.widget.FrameLayout[@resource-id='com.google.android.apps.fitness:id/"
                                        "bottom_navigation']"
                                        "//android.widget.FrameLayout[@content-desc='{}']"
                                        .format(nav_container_button.value)).is_selected()

    def click_nav_container_button(self, nav_container_button: NavContainerButton):
        self.driver.find_element(self.__nav_container_button[0],
                                        "//android.widget.FrameLayout[@resource-id='com.google.android.apps.fitness:id/"
                                        "bottom_navigation']"
                                        "//android.widget.FrameLayout[@content-desc='{}']"
                                        .format(nav_container_button.value)).click()


