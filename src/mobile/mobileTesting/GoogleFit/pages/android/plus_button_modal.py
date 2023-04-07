from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.pages.commons.plus_button_modal_base import PlusButtonModalBase
from src.mobile.utils.mobile_utils import *
from src.mobile.utils.direction import Direction
from src.mobile.utils.operating_system import OS


class PlusButtonModal(PlusButtonModalBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__plus_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/add_entry_fab")

    def is_present(self) -> bool:
        if self.driver.find_element(*self.__plus_button).get_attribute("enabled") == 'true':
            return True
        else:
            return False

    def is_plus_button_static_on_page(self, locator, container):
        element = self.driver.find_element(*self.__plus_button)
        oldLocation = Point(element.location['x'], element.location['y'])
        oldDimension = Dimension(element.size['width'], element.size['height'])

        swipe(locator, container, Direction.UP, 5, 200, self.driver, OS.ANDROID)

        # swipeUp(200, 5, self.driver, OS.ANDROID)

        # logger.info('oldLocation = {}, oldDimension = {}'.format(oldLocation, oldDimension))

        element = self.driver.find_element(*self.__plus_button)
        newLocation = Point(element.location['x'], element.location['y'])
        newDimension = Dimension(element.size['width'], element.size['height'])

        # logger.info('newLocation = {}, newDimension = {}'.format(newLocation, newDimension))
        return oldDimension.__eq__(newDimension) and oldLocation.__eq__(newLocation)

    def is_plus_button_below_container_on_page(self, container):
        swipeUp(100, 1, self.driver, OS.ANDROID)
        # containerLocation = Point(container.location['x'], container.location['y'])
        containerDimension = Dimension(container.size['width'], container.size['height'])
        # logger.info("Container Location: %s ---- Container Dimension: %s" % (containerLocation, containerDimension))

        element = self.driver.find_element(*self.__plus_button)
        plusLocation = Point(element.location['x'], element.location['y'])
        # plusDimension = Dimension(element.size['width'], element.size['height'])
        # logger.info("Plus Location: %s ---- Plus Dimension: %s" % (plusLocation, plusDimension))
        return plusLocation.getY() > containerDimension.getHeight()






