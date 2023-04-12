from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.profile_page.birthday_page.monthes import Month
from src.mobile.mobileTesting.GoogleFit.pages.commons.profile_pages.birthday_page_base import BirthdayPageBase
from selenium.webdriver.support import expected_conditions as EC
from src.mobile.utils.mobile_utils import *


class BirthdayPage(BirthdayPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@text='Birthday']")
        self.__month_spinner = (AppiumBy.XPATH, "//android.widget.Spinner")
        self.__day_field = (AppiumBy.XPATH, "//android.widget.TextView[@text='Day']"
                                            "//following-sibling::android.widget.EditText")
        self.__year_field = (AppiumBy.XPATH, "//android.widget.TextView[@text='Year']"
                                             "//following-sibling::android.widget.EditText")
        self.__save_button = (AppiumBy.XPATH, "//android.widget.Button[@text='Save']")
        self.__back_button = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) and \
            self.wait.until(EC.visibility_of_element_located(self.__month_spinner))

    def change_month_day_year(self, month: Month, day: int, year: int):
        # month changing
        self.driver.find_element(*self.__month_spinner).click()
        container = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Menu for selecting month of birth']")
        locator = (AppiumBy.XPATH, "//android.view.View[@text='{}']".format(month.value))
        swipe(locator, container, Direction.VERTICAL, 10, 200, self.driver, OS.ANDROID)
        self.driver.find_element(*locator).click()
        # day changing
        self.driver.find_element(*self.__day_field).send_keys(day)
        # year changing
        self.driver.find_element(*self.__year_field).send_keys(year)
        return (month.value[:3] + " " + str(day) + ", " + str(year))

    def confirm_changes(self):
        self.driver.hide_keyboard()
        if self.driver.find_element(*self.__save_button).get_attribute("enabled") == 'true':
            self.driver.find_element(*self.__save_button).click()
            self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Confirm']")))
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Confirm']").click()
        self.wait.until(EC.visibility_of_element_located(self.__back_button))
        self.driver.find_element(*self.__back_button).click()



