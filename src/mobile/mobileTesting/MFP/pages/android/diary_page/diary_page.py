from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.enums.diary_activity_items import DiaryActivityItem
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.custom_dashboard_page_base import CustomDashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_action_bar_page_base import DiaryActionBarPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.edit_diary_page_base import EditDiaryPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.more_button_page_base import MoreButtonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.nutrition_page_base import NutritionPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *

from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_page_base import DiaryPageBase


class DiaryPage(DiaryPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat"
                                        "//preceding-sibling::android.widget.TextView")
        self.__more_options_button = (AppiumBy.ACCESSIBILITY_ID, "More options")
        self.__nutrition_button = (AppiumBy.ID, "com.myfitnesspal.android:id/btn_nutrition")
        self.__calories_remaining_title = (AppiumBy.ID, "com.myfitnesspal.android:id/title")
        self.__edit_diary_button = (AppiumBy.ACCESSIBILITY_ID, "Edit Diary")
        self.__calories_goal_value = (AppiumBy.ID, "com.myfitnesspal.android:id/goal")
        self.__calories_remaining_value = (AppiumBy.ID, "com.myfitnesspal.android:id/remaining_diary")
        self.__summary_more_button = (
            AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/daily_summary_container']"
                            "//*[@resource-id='com.myfitnesspal.android:id/more']")
        self.__add_button = None
        self.__more_button = None

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and not init_page_or_uiobject(self.driver, MFPCommonPageBase) \
                .get_bottom_nav_bar().is_nav_bar_item_clickable(BottomNavBarItem.DIARY)

    def open_nutrition_page(self) -> NutritionPageBase:
        swipeToElementUp(self.__nutrition_button, self.driver, OS.ANDROID)
        self.driver.find_element(*self.__nutrition_button).click()
        return init_page_or_uiobject(self.driver, NutritionPageBase)

    def click_add_button_on_activity(self, item: DiaryActivityItem):
        self.__add_button = (AppiumBy.XPATH, "(//*[@text='{}']/../..//"
                                             "following-sibling::android.widget.LinearLayout"
                                             "//android.widget.Button[1])[1]".format(item.value))
        swipeToElementVertical(self.__add_button, self.driver, OS.ANDROID)
        # swipeUp(7000, 1, self.driver, OS.ANDROID)
        self.driver.find_element(*self.__add_button).click()

    def click_more_button_on_activity(self, item: DiaryActivityItem) -> MoreButtonPageBase:
        self.__more_button = (AppiumBy.XPATH, "(//*[@text='{}']/../..//following-sibling::android.widget.LinearLayout"
                                             "//android.widget.Button[2])[1]".format(item.value))
        swipeToElementVertical(self.__more_button, self.driver, OS.ANDROID)
        # swipeUp(7000, 1, self.driver, OS.ANDROID)
        self.driver.find_element(*self.__more_button).click()
        return init_page_or_uiobject(self.driver, MoreButtonPageBase)

    def is_meal_added(self) -> bool:
        return self.driver.find_element(AppiumBy.ID,
                                        "com.myfitnesspal.android:id/foodSearchViewFoodItem").is_displayed()

    def delete_all_added_meals_in_activity(self, item: DiaryActivityItem):

        if not swipeWithCountAndDirection((AppiumBy.XPATH, "//*[@text='{}']".format(item.value)),
                                          self.driver.find_element(AppiumBy.ID,
                                                                   "com.myfitnesspal.android:id/diary_recycler_view"),
                                          Direction.VERTICAL_DOWN_FIRST, 10, self.driver, OS.ANDROID):
            raise Exception("Page does not have needed element!")

        tmp_items = (AppiumBy.XPATH, "//*[@text='{}']/../..//following-sibling::android.widget.LinearLayout"
                                     "[@resource-id='com.myfitnesspal.android:id/foodSearchViewFoodItem']".format(
            item.value))
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(tmp_items))

        elements_for_deleting: list[WebElement] = self.driver.find_elements(*tmp_items)
        # logger.info(elements_for_deleting)

        for element in elements_for_deleting:
            long_press_on_element(element, self.driver)
            diary_action_bar_page_base = init_page_or_uiobject(self.driver, DiaryActionBarPageBase)
            assert diary_action_bar_page_base.is_page_opened(), "[Diary Action Bar Page] Page is not opened!"
            diary_action_bar_page_base.click_delete_entry()

    def is_all_meals_deleted_in_activity(self, item: DiaryActivityItem) -> bool:
        tmp_items = (AppiumBy.XPATH, "//*[@text='{}']/../..//following-sibling::android.widget.LinearLayout"
                                     "[@resource-id='com.myfitnesspal.android:id/foodSearchViewFoodItem']".format(
            item.value))

        elements_for_deleting: list[WebElement] = self.driver.find_elements(*tmp_items)

        if len(elements_for_deleting) == 0:
            return True
        else:
            return False

    def is_calories_remaining_chosen(self) -> bool:
        return self.driver.find_element(*self.__calories_remaining_title).text == 'Calories Remaining'

    def clear_user_diary(self):
        lst = self.driver.find_elements(*self.__edit_diary_button)
        if len(lst) > 0:
            lst[0].click()
            edit_diary_page_base = init_page_or_uiobject(self.driver, EditDiaryPageBase)
            assert edit_diary_page_base.is_page_opened(), \
                "[Edit Diary Page] Edit Diary Page is not opened after clicking on edit diary button!"
            edit_diary_page_base.delete_all_items()
        else:
            logger.info("Diary Page already cleared, so no need to clean it!")

    def get_calories_goal_int_value(self) -> int:
        calories = self.driver.find_element(*self.__calories_goal_value).text
        calories = calories.replace(',', '')
        return int(calories)

    def get_calories_remaining_int_value(self) -> int:
        calories = self.driver.find_element(*self.__calories_remaining_value).text
        calories = calories.replace(',', '')
        return int(calories)

    def click_summary_more_button(self) -> CustomDashboardPageBase:
        self.driver.find_element(*self.__summary_more_button).click()
        return init_page_or_uiobject(self.driver, CustomDashboardPageBase)











