from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.profile_page.gender_page.gender import Gender
from src.mobile.mobileTesting.GoogleFit.pages.commons.profile_pages.gender_page_base import GenderPageBase
from selenium.webdriver.support import expected_conditions as EC


class GenderPage(GenderPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//android.view.View[@resource-id='yDmH0d']"
                                        "/android.view.View/android.view.View"
                                        "/android.view.View"
                                        "/android.widget.TextView")
        self.__add_custom_gender_button = (AppiumBy.XPATH, "//*[@text='Add custom gender']")
        self.__back_button = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) \
            and self.wait.until(EC.visibility_of_element_located(self.__add_custom_gender_button))

    def check_gender(self, gender: Gender):
        # all_genders = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View/android.widget.RadioButton")
        # checked_gender = ""
        # for gend in all_genders:
        #     if gend.get_attribute("checked") == 'true':
        #         checked_gender = gend.text
        #         break
        #
        # if gender.value == checked_gender:
        #     if gender.value == 'Male':
        #         self.driver.find_element(AppiumBy.XPATH,
        #                                  "//android.view.View/android.widget.RadioButton[@text='Female']").click()
        #     else:
        #         self.driver.find_element(AppiumBy.XPATH,
        #                                  "//android.view.View/android.widget.RadioButton[@text='Male']").click()
        # else:
            self.driver.find_element(AppiumBy.XPATH,
                                     "//android.view.View/android.widget.RadioButton[@text='{}']".format(gender.value))\
                .click()
            return gender.value

    def click_back_button(self):
        self.driver.find_element(*self.__back_button).click()






