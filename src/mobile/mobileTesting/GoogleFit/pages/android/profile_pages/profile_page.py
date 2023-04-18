from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.profile_page.pages_from_about_you import PageFromAboutYou
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.switchers import Switcher
from src.mobile.mobileTesting.GoogleFit.pages.android.gf_common_page import GFCommonPage
from src.mobile.mobileTesting.GoogleFit.pages.commons.profile_pages.profile_page_base import ProfilePageBase
from src.mobile.utils.mobile_utils import *
from appium.webdriver.common.touch_action import TouchAction


class ProfilePage(ProfilePageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__about_you_placeholder = (AppiumBy.ID, "com.google.android.apps.fitness:id/about_you_placeholder")
        self.__goals_heading = (AppiumBy.ID, "com.google.android.apps.fitness:id/goals_heading")
        self.__page_from_about_you = None
        self.__settings_button = (AppiumBy.ACCESSIBILITY_ID, "Settings")
        self.__account_image = (AppiumBy.ID, "com.google.android.apps.fitness:id/og_apd_internal_image_view")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__about_you_placeholder)) \
            and self.wait.until(EC.visibility_of_element_located(self.__goals_heading))

    def open_page_from_about_you(self, page: PageFromAboutYou):
        self.__page_from_about_you = (AppiumBy.ID,
                                      "com.google.android.apps.fitness:id/{}_field".format(page.value.lower()))
        self.driver.find_element(*self.__page_from_about_you).click()

    def open_settings_page(self):
        self.driver.find_element(*self.__settings_button).click()

    def check_all_changed_info(self, gender: str, birthday: str, weight: str, height: str) -> bool:
        gender_info = self.driver.find_element(AppiumBy.ID, "com.google.android.apps.fitness:id/gender_field")
        birthday_info = self.driver.find_element(AppiumBy.ID, "com.google.android.apps.fitness:id/birthday_field")
        weight_info = self.driver.find_element(AppiumBy.ID, "com.google.android.apps.fitness:id/weight_field")
        height_info = self.driver.find_element(AppiumBy.ID, "com.google.android.apps.fitness:id/height_field")
        if gender_info.text != gender:
            logger.info("Gender info is not the same! Actual: {}, Expected: {}".format(gender_info.text, gender))
            return False
        elif birthday_info.text != birthday:
            logger.info("Birthday info is not the same! Actual: {}, Expected: {}".format(birthday_info.text, birthday))
            return False
        elif weight_info.text != weight:
            logger.info("Weight info is not the same! Actual: {}, Expected: {}".format(weight_info.text, weight))
            return False
        elif height_info.text != height:
            logger.info("Height info is not the same! Actual: {}, Expected: {}".format(height_info.text, height))
            return False

        return True

    def is_switcher_checked(self, switcher: Switcher) -> bool:
        # if self.driver.find_element(*switcher.value).get_attribute("checked") == 'true':
        #     return True
        # else:
        #     return False

        return True if self.driver.find_element(*switcher.value).get_attribute("checked") == 'true' else False

    def switcher_check(self, switcher: Switcher):
        if self.is_switcher_checked(switcher):
            return
        else:
            actions = TouchAction(self.driver)
            actions.tap(self.driver.find_element(*switcher.value))
            actions.perform()
            # self.driver.find_element(*switcher.value).click()

    def switcher_uncheck(self, switcher: Switcher):
        if not self.is_switcher_checked(switcher):
            return
        else:
            actions = TouchAction(self.driver)
            actions.tap(self.driver.find_element(*switcher.value))
            actions.perform()
            # self.driver.find_element(*switcher.value).click()

    def get_color_of_switcher(self, switcher: Switcher):
        return GFCommonPage(self.driver).get_color_of_element(switcher.value)

    def get_color_of_account_image(self):
        return GFCommonPage(self.driver).get_color_of_element(self.__account_image)



