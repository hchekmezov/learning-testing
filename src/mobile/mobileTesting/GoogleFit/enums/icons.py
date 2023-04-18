from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy


class Icons(Enum):
    HOME_ICON = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Home']/android.widget.FrameLayout")
    JOURNAL_ICON = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Journal']/android.widget.FrameLayout")
    BROWSE_ICON = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Browse']/android.widget.FrameLayout")
    PROFILE_ICON = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Profile']/android.widget.FrameLayout")