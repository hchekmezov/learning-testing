from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy


class Labels(Enum):
    HOME_LABEL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Home']/android.view.ViewGroup")
    JOURNAL_LABEL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Journal']/android.view.ViewGroup")
    BROWSE_LABEL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Browse']/android.view.ViewGroup")
    PROFILE_LABEL = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Profile']/android.view.ViewGroup")