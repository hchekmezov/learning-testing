from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.colors import Color
from src.mobile.mobileTesting.GoogleFit.pages.android.bottom_nav_container import BottomNavContainer
from src.mobile.mobileTesting.GoogleFit.pages.commons.gf_common_page_base import GFCommonPageBase
from src.mobile.utils.mobile_utils import *
from PIL import Image
import io
import webcolors


class GFCommonPage(GFCommonPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def get_bottom_nav_container(self):
        return BottomNavContainer(self.driver)

    def get_color_of_element(self, locator) -> str:
        """**locator** need to use like: (AppiumBy.ID, 'just_an_id')"""
        self.wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        screenshot = self.driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot))
        elementLeftUpper = Point(element.location['x'], element.location['y'])
        elementDimension = Dimension(element.size['width'], element.size['height'])

        # for i in range(elementLeftUpper.getX(), elementLeftUpper.getX() + elementDimension.getWidth()):
        #     for j in range(elementLeftUpper.getY(), elementLeftUpper.getY() + elementDimension.getHeight()):
        #         pixel_color = image.getpixel((i, j))
        #         # color_name = webcolors.rgb_to_name((pixel_color[0], pixel_color[1], pixel_color[2]))
        #         string_rgb = "({}, {}, {})".format(pixel_color[0], pixel_color[1], pixel_color[2])
        #         if string_rgb not in dictionary.keys():
        #             dictionary[string_rgb] = 1
        #         else:
        #             dictionary[string_rgb] = dictionary.get(string_rgb) + 1
        #
        # logger.info(sorted(dictionary.values()))

        red = 0
        green = 0
        blue = 0

        dictionary = dict()

        for y in range(elementLeftUpper.getY(), elementLeftUpper.getY() + elementDimension.getHeight()):
            for x in range(elementLeftUpper.getX(), elementLeftUpper.getX() + elementDimension.getWidth()):
                pixel_color = image.getpixel((x, y))
                red = red + pixel_color[0]
                green = green + pixel_color[1]
                blue = blue + pixel_color[2]

        dictionary['RED'] = red
        dictionary['GREEN'] = green
        dictionary['BLUE'] = blue

        key_list = list(dictionary.keys())
        val_list = list(dictionary.values())

        position = val_list.index(max(red, max(green, blue)))

        # divider
        divider = elementDimension.getWidth() * elementDimension.getHeight()

        logger.info("Result sum RGB of element <<{}>>: ({}, {}, {})".format(locator, red, green, blue))
        logger.info("Result RGB average of element <<{}>>: ({}, {}, {})".format(locator,
                                                                                int(red / divider),
                                                                                int(green / divider),
                                                                                int(blue / divider)))

        if self.__percent_difference(red, green) < 1.5 \
            and self.__percent_difference(red, blue) < 1.5 \
                and self.__percent_difference(green, blue) < 1.5:
                    return Color.WHITE.value
        else:
            return key_list[position]


    def __percent_difference(self, num1, num2):
        """this method needs only for **get_color_of_element**"""
        abs_diff = abs(num1 - num2)
        average = (num1 + num2) / 2
        percent_diff = abs_diff / average * 100
        # logger.info(percent_diff)
        return percent_diff
