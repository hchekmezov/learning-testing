from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Remote
from src.mobile.mobileTesting.MFP.pages.commons.existing_user_tutor_page_base import ExistingUserTutorPageBase
from selenium.webdriver.support import expected_conditions as EC


class ExistingUserTutorPage(ExistingUserTutorPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__close_button = (AppiumBy.XPATH, "//android.view.View [@resource-id='buttonExistingUserTutorial']/android.widget.Button")
        self.__see_tutorial_button = (AppiumBy.XPATH, "//android.view.View[@resource-id='buttonSeeTutorial']")

    def click_close_button(self):
        self.driver.find_element(self.__close_button[0], self.__close_button[1]).click()

    def is_page_opened(self) -> bool:
        return self.wait.until(
            EC.presence_of_element_located((self.__close_button[0], self.__close_button[1]))) \
            and self.driver.find_element(self.__see_tutorial_button[0], self.__see_tutorial_button[1]).is_displayed()