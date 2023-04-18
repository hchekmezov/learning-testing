from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy


class Switcher(Enum):
    SLEEP_SWITCH = (AppiumBy.ID, "com.google.android.apps.fitness:id/profile_sleep_switch")