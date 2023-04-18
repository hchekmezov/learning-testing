from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy


class FirstTitles(Enum):
    ZERO_SEVEN = (AppiumBy.ID, 'com.google.android.apps.fitness:id/card_custom_chart_title')
    ZERO_HUNDRED_FIFTY = (AppiumBy.ID, 'com.google.android.apps.fitness:id/weekly_heart_points_card_progress_text')