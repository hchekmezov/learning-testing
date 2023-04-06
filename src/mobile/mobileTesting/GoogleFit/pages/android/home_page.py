from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.nav_container_buttons import NavContainerButton
from src.mobile.mobileTesting.GoogleFit.pages.android.gf_common_page import GFCommonPage
from src.mobile.mobileTesting.GoogleFit.pages.commons.home_page_base import HomePageBase
from selenium.webdriver.support import expected_conditions as EC

class HomePage(HomePageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__lotie_celebration = (AppiumBy.ID, "com.google.android.apps.fitness:id/lottie_celebration")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__lotie_celebration))\
            and GFCommonPage(self.driver)\
                .get_bottom_nav_container()\
                .is_nav_container_button_selected(NavContainerButton.HOME)