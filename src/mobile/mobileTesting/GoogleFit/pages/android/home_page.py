from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.nav_container_buttons import NavContainerButton
from src.mobile.mobileTesting.GoogleFit.pages.android.gf_common_page import GFCommonPage
from src.mobile.mobileTesting.GoogleFit.pages.android.plus_button_modal import PlusButtonModal
from src.mobile.mobileTesting.GoogleFit.pages.commons.home_page_base import HomePageBase
from selenium.webdriver.support import expected_conditions as EC
from src.mobile.utils.mobile_utils import *
from src.mobile.utils.operating_system import OS
from src.mobile.utils.direction import Direction

class HomePage(HomePageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__lotie_celebration = (AppiumBy.ID, "com.google.android.apps.fitness:id/lottie_celebration")
        self.__plus_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/add_entry_fab")
        self.__cards_frame_container = (AppiumBy.ID, "com.google.android.apps.fitness:id/cards_frame")
        self.__learn_more = (AppiumBy.XPATH, "//android.widget.Button[@text='Learn more']")


    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__lotie_celebration))\
            and GFCommonPage(self.driver)\
                .get_bottom_nav_container()\
                .is_nav_container_button_selected(NavContainerButton.HOME)

    def get_plus_button(self):
        return PlusButtonModal(self.driver)

    def is_plus_button_static(self):
        return self.get_plus_button()\
            .is_plus_button_static_on_page(self.__learn_more, self.driver.find_element(*self.__cards_frame_container))

    def is_plus_button_present(self):
        return self.get_plus_button().is_present()

    def is_plus_button_below_container(self):
        return self.get_plus_button()\
            .is_plus_button_below_container_on_page(self.driver.find_element(*self.__cards_frame_container))











