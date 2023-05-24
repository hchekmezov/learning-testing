from appium.webdriver.common.touch_action import TouchAction
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.mobile.utils.operating_system import OS
from selenium.webdriver import Remote

from pytest_zebrunner import attach_test_screenshot

from src.mobile.utils.direction import Direction

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class Dimension():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Dimension):
            return self.__width == o.__width and self.__height == o.__height
        else:
            return False

    def __str__(self) -> str:
        return "(width = {width}, height = {height})".format(width=self.__width, height=self.__height)

    def __hash__(self) -> int:
        return super().__hash__()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def moveBy(self, xOffset, yOffset):
        return Point(self.x + xOffset, self.y + yOffset)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"(x = {self.x}, y = {self.y})"


def attach_screenshot(driver: Remote):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")


def isVisibleMethod(timeout, locator, driver) -> bool:
    res = False
    try:
        res = WebDriverWait(driver=driver, timeout=timeout).until(EC.visibility_of_element_located(locator=locator))
    except Exception as e:
        logger.debug(f"wait.until: {e}")
    return bool(res)


def swipeInContainer(container, direction, count, duration, driver, os: OS) -> bool:
        """**container** should be transferred like: *driver.find_element(container[0], container[1])*
        or
        *driver.find_element(\*container)*"""

        elementLocation = None # Point
        elementDimensions = None # Dimension
        if container == None:
            elementLocation = Point(0, 0)
            deviceSize = driver.get_window_size()
            elementDimensions = Dimension(deviceSize['width'], deviceSize['height'])
        else:
            # isContainerVisible = EC.visibility_of(container)
            # if isinstance(isContainerVisible, WebElement):
            #     isContainerVisible = True
            # else:
            #     isContainerVisible = False

            if not container.is_displayed():
                logger.warning("Cannot swipe! Impossible to find element " + str(container))

            elementLocation = Point(container.location['x'], container.location['y'])
            elementDimensions = Dimension(container.size['width'], container.size['height'])

        minCoefficient = 0.3
        maxCoefficient = 0.6
        if (os.value == "Android"):
            minCoefficient = 0.25
            maxCoefficient = 0.5
        elif os.value == "IOS" or os.value == "MAC" or os.value == "TVOS":
            minCoefficient = 0.25
            maxCoefficient = 0.8

        startx = 0
        starty = 0
        endx = 0
        endy = 0
        if direction.value == "UP":
                startx = endx = elementLocation.getX() + round(float(elementDimensions.getWidth()) / 2.0)
                starty = (int)(elementLocation.getY() + round(maxCoefficient * float(elementDimensions.getHeight())))
                endy = (int)(elementLocation.getY() + round(minCoefficient * float(elementDimensions.getHeight())))
        elif direction.value == "DOWN":
                startx = endx = elementLocation.getX() + round(float(elementDimensions.getWidth()) / 2.0)
                starty = (int)(elementLocation.getY() + round(minCoefficient * float(elementDimensions.getHeight())))
                endy = (int)(elementLocation.getY() + round(maxCoefficient * float(elementDimensions.getHeight())))
        elif direction.value == "LEFT":
                starty = endy = elementLocation.getY() + round(float(elementDimensions.getHeight()) / 2.0)
                startx = (int)(elementLocation.getX() + round(maxCoefficient * float(elementDimensions.getWidth())))
                endx = (int)(elementLocation.getX() + round(minCoefficient * float(elementDimensions.getWidth())))
        elif direction.value == "RIGHT":
                starty = endy = elementLocation.getY() + round(float(elementDimensions.getHeight()) / 2.0)
                startx = (int)(elementLocation.getX() + round(minCoefficient * float(elementDimensions.getWidth())))
                endx = (int)(elementLocation.getX() + round(maxCoefficient * float(elementDimensions.getWidth())))
        else:
                raise Exception('Unsupported operation')

        logger.debug("Swipe from (X = {startx}; Y = {starty}) to (X = {endx}; Y = {endy})"
                     .format(startx=startx, starty=starty, endx=endx, endy=endy))

        try:
            for i in range (0, count):
                driver.swipe(start_x=startx, start_y=starty, end_x=endx, end_y=endy, duration=duration)
            return True
        except Exception as e:
            logger.error("Error during Swipe from (X = {startx}; Y = {starty}) to (X = {endx}; Y = {endy}): {e}"
                         .format(startx=startx, starty=starty, endx=endx, endy=endy, e=e))
            return False


def swipeInContainerOneCount(container, direction: Direction, duration: int, driver, os: OS) -> bool:
    return swipeInContainer(container, direction, 1, duration, driver, os)


def swipeWithCountAndDirection(locator, container, direction: Direction, count: int, driver, os: OS) -> bool:
    return swipe(locator, container, direction, count, 1000, driver, os)


def swipeWithDirection(locator, container, direction: Direction, driver, os: OS) -> bool:
    return swipe(locator, container, direction, 50, 1000, driver, os)


def swipe(locator, container, direction: Direction, count: int, duration: int, driver, os: OS) -> bool:

        isVisible = isVisibleMethod(timeout=1, locator=locator, driver=driver)

        if isVisible:
            element = driver.find_element(locator[0], locator[1])
            logger.info("Element already present before swipe: " + str(element))
            return True
        else:
            logger.info("Swiping to needed element")
            oppositeDirection = Direction.DOWN
            bothDirections = False
            if direction.value == "UP":
                oppositeDirection = Direction.DOWN
            elif direction.value == "DOWN":
                oppositeDirection = Direction.UP
            elif direction.value == "LEFT":
                oppositeDirection = Direction.RIGHT
            elif direction.value == "RIGHT":
                oppositeDirection = Direction.LEFT
            elif direction.value == "HORIZONTAL":
                direction = Direction.LEFT
                oppositeDirection = Direction.RIGHT
                bothDirections = True
            elif direction.value == "HORIZONTAL_RIGHT_FIRST":
                direction = Direction.RIGHT
                oppositeDirection = Direction.LEFT
                bothDirections = True
            elif direction.value == "VERTICAL":
                direction = Direction.UP
                oppositeDirection = Direction.DOWN
                bothDirections = True
            elif direction.value == "VERTICAL_DOWN_FIRST":
                direction = Direction.DOWN
                oppositeDirection = Direction.UP
                bothDirections = True
            else:
                    raise Exception("Unsupported direction for swipeInContainerTillElement: " + str(direction))

            currentCount = count
            while currentCount > 0 and not isVisible:
                logger.debug(
                    f"Element not present! Swipe {direction} will be executed to element")
                swipeInContainerOneCount(container=container, direction=direction, duration=duration, driver=driver,
                                         os=os)
                logger.info(f"Swipe was executed. Attempts remain: {currentCount}")
                isVisible = isVisibleMethod(timeout=1, locator=locator, driver=driver)
                # try:
                #     element = driver.find_element(locator[0], locator[1])
                #     isVisible = True
                # except:
                #     isVisible = False

                # if isinstance(isVisible, WebElement):
                #     isVisible = True
                # else:
                #     isVisible = False
                currentCount -= 1

            currentCount = count

            while bothDirections and not isVisible and currentCount > 0:
                logger.debug(
                    f"Element not present! Swipe {oppositeDirection} will be executed to element")
                swipeInContainerOneCount(container=container, direction=oppositeDirection,
                                         duration=duration, driver=driver, os=os)
                isVisible = isVisibleMethod(timeout=1, driver=driver, locator=locator)
                # try:
                #     element = driver.find_element(locator[0], locator[1])
                #     isVisible = True
                # except:
                #     isVisible = False
                # if isinstance(isVisible, WebElement):
                #     isVisible = True
                # else:
                #     isVisible = False
                logger.info(f"Swipe was executed. Attempts remain: {currentCount}")
                currentCount -= 1

            logger.info("Result: " + str(isVisible))
            return isVisible


def swipeUpOneCount(duration: int, driver, os: OS):
    swipeInContainerOneCount(None, Direction.UP, duration, driver, os)


def swipeUp(duration: int, times: int, driver, os: OS):
    for i in range(times):
        swipeUpOneCount(duration, driver, os)


def swipeLeftOneCount(duration: int, driver, os: OS):
    swipeLeftInContainer(None, duration, driver, os)


def swipeLeft(duration: int , times: int, driver, os: OS):
    for i in range(times):
        swipeLeftOneCount(duration, driver, os)


def swipeLeftInContainer(container, duration: int, driver, os: OS):
    swipeInContainerOneCount(container, Direction.LEFT, duration, driver, os)


def swipeLeftInContainerWithCount(container, duration: int, count: int, driver, os: OS):
    for i in range(count):
        swipeLeftInContainer(container, duration, driver, os)


def swipeToElementVertical(locator, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.VERTICAL, 50, 1000, driver, os)


def swipeToElementVerticalWithCount(locator, count: int, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.VERTICAL, count, 1000, driver, os)


def swipeToElementVerticalWithCountAndDuration(locator, count: int, duration: int, driver: Remote, os: OS):
    return swipe(locator, None, Direction.VERTICAL, count, duration, driver, os)


def swipeToElementtVerticalDownFirst(locator, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.VERTICAL_DOWN_FIRST, 50, 1000, driver, os)


def swipeToElementVerticalDownFirstWithCount(locator, count: int, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.VERTICAL_DOWN_FIRST, count, 1000, driver, os)


def swipeToElementVerticalDownFirstWithCountAndDuration(locator, count: int, duration: int, driver: Remote, os: OS):
    return swipe(locator, None, Direction.VERTICAL_DOWN_FIRST, count, duration, driver, os)


def swipeToElementUp(locator, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.UP, 50, 1000, driver, os)


def swipeToElementUpWithCount(locator, count: int, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.UP, count, 1000, driver, os)


def swipeToElementUpWithDuration(locator, duration: int, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.UP, 50, duration, driver, os)


def swipeToElementDown(locator, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.DOWN, 50, 1000, driver, os)


def swipeToElementDownWithCount(locator, count: int, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.DOWN, count, 1000, driver, os)


def swipeToElementDownWithDuration(locator, duration: int, driver: Remote, os: OS) -> bool:
    return swipe(locator, None, Direction.DOWN, 50, duration, driver, os)


def long_press_on_element(element, driver: Remote):
    actions = TouchAction(driver)
    actions.long_press(element, duration=2000)
    actions.perform()
