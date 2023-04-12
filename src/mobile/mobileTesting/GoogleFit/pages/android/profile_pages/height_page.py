from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.profile_page.height_page.height_measures import HeightMeasure
from src.mobile.mobileTesting.GoogleFit.pages.commons.profile_pages.height_page_base import HeightPageBase
from src.mobile.utils.mobile_utils import *

class HeightPage(HeightPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__ok_button = (AppiumBy.ID, "android:id/button1")
        self.__title = (AppiumBy.ID, "com.google.android.apps.fitness:id/alertTitle")
        self.__number_pickers_containers = (AppiumBy.XPATH, "//android.widget.NumberPicker")
        self.__number_pickers_input = (AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']")

        self.__unit_spinner = (AppiumBy.ID, "com.google.android.apps.fitness:id/unit_picker")
        self.__variant_from_spinner = None

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) and \
            self.wait.until(EC.visibility_of_element_located(self.__ok_button))

    def change_height(self, needed: int, measure: HeightMeasure, right_needed=0):
        """If measure is '**Feet & inches**' then we need to get right_needed corner, because we have tho containers!"""
        self.driver.find_element(*self.__unit_spinner).click()
        self.__variant_from_spinner = (AppiumBy.XPATH,
                                       "//android.widget.CheckedTextView[@text='{}']".format(measure.value))

        self.wait.until(EC.visibility_of_element_located(self.__variant_from_spinner))
        self.driver.find_element(*self.__variant_from_spinner).click()


        if measure.value == 'Centimeters':
            expected = True

            # we have only one corner
            corner = self.driver.find_element(*self.__number_pickers_containers)
            tmp = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.EditText")
            value = int(tmp[0].text.split(' ')[0])

            while expected:
                try:
                    self.driver.find_element(AppiumBy.XPATH,
                                             "//android.widget.Button[@text='{} cm']".format(needed)).click()
                    expected = False
                except NoSuchElementException:
                    if (needed > value):
                        needed_direction = Direction.UP
                    else:
                        needed_direction = Direction.DOWN
                    # left

                    swipeInContainerOneCount(corner,
                                             needed_direction,
                                             600,
                                             self.driver,
                                             OS.ANDROID)
        else:
            expected = True

            if needed > 8 or needed < 1:
                logger.info("needed should be less or equals 8 and more or equals 1. 1 will be used as default!")
                needed = 1

            if right_needed > 11 or right_needed < 0:
                logger.info("right_needed should be less or equals 11 and more or equals 0. 0 will be used as default!")
                right_needed = 0

            tmp = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.EditText")
            left_value = int(tmp[0].text.split(' ')[0])
            right_value = int(tmp[1].text.split(' ')[0])

            corners = self.driver.find_elements(*self.__number_pickers_containers)
            left_corner = corners[0]
            right_corner = corners[1]

            # left
            while expected:
                try:
                    self.driver.find_element(AppiumBy.XPATH,
                                             "//android.widget.Button[@text='{} ft']".format(needed)).click()
                    expected = False
                except NoSuchElementException:
                    if (needed > left_value):
                        needed_direction = Direction.UP
                    else:
                        needed_direction = Direction.DOWN
                    # left

                    swipeInContainerOneCount(left_corner,
                                             needed_direction,
                                             600,
                                             self.driver,
                                             OS.ANDROID)

            # right
            expected = True
            while expected:
                try:
                    self.driver.find_element(AppiumBy.XPATH,
                                             "//android.widget.Button[@text='{} in']".format(right_needed)).click()
                    expected = False
                except NoSuchElementException:
                    if (right_needed > right_value):
                        needed_direction = Direction.UP
                    else:
                        needed_direction = Direction.DOWN
                    # left

                    swipeInContainerOneCount(right_corner,
                                             needed_direction,
                                             600,
                                             self.driver,
                                             OS.ANDROID)

        self.driver.find_element(*self.__ok_button).click()

        if measure.value == 'Centimeters':
            return str(needed) + " cm"
        else:
            # 5′0″, Expected: 5'0"
            return str(needed) + "′" + str(right_needed) + "″"

