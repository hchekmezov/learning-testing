from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.profile_page.weight_page.weight_measures import WeightMeasure
from src.mobile.mobileTesting.GoogleFit.pages.commons.profile_pages.weight_page_base import WeightPageBase
from selenium.webdriver.support import expected_conditions as EC
from src.mobile.utils.mobile_utils import *


class WeightPage(WeightPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.google.android.apps.fitness:id/alertTitle")
        self.__ok_button = (AppiumBy.ID, "android:id/button1")
        self.__number_pickers_input = (AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']")
        self.__number_pickers_containers = (AppiumBy.XPATH, "//android.widget.NumberPicker")

        self.__unit_spinner = (AppiumBy.ID, "com.google.android.apps.fitness:id/unit_spinner")
        self.__variant_from_spinner = None

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) and \
            self.wait.until(EC.visibility_of_element_located(self.__ok_button))

    def change_weight(self, left_needed: int, right_needed: int, measure: WeightMeasure):
        self.driver.find_element(*self.__unit_spinner).click()
        self.__variant_from_spinner = (AppiumBy.XPATH, "//android.widget.CheckedTextView[@text='{}']"
                                       .format(measure.value))
        self.wait.until(EC.visibility_of_element_located(self.__variant_from_spinner))
        self.driver.find_element(*self.__variant_from_spinner).click()

        if measure.value == 'Pounds' or measure.value == 'Kilograms':
            expected = True

            if right_needed > 9 or right_needed < 0:
                logger.info("right_needed should be less or equals 9 and more or equals 0. 0 will be used as default!")
                right_needed = 0

            tmp = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.EditText")
            left_value = int(tmp[0].text)
            right_value = int(tmp[1].text)

            corners = self.driver.find_elements(*self.__number_pickers_containers)
            left_corner = corners[0]
            right_corner = corners[1]


            # left
            while expected:
                try:
                    self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='{}']".format(left_needed)).click()
                    expected = False
                except NoSuchElementException:
                    if (left_needed > left_value):
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
                    self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='{}']".format(right_needed)).click()
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
        else:
            logger.info("For measure <<{}>> this method is not implemented yet!".format(measure.value))
            raise Exception("Is not implemented!")

        self.driver.find_element(*self.__ok_button).click()

        if measure.value == 'Pounds':
            return str(left_needed) + "." + str(right_needed) + " lb"
        elif measure.value == 'Kilograms':
            return str(left_needed) + "." + str(right_needed) + " kg"
        else:
            logger.info("For measure <<{}>> this method is not implemented yet!".format(measure.value))
            raise Exception("Is not implemented!")


