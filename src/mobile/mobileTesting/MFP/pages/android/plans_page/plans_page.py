from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from src.common_utils.soft_assert import SoftAssert
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.enums.plans_page.filter_by_buttons import FilterByButton
from src.mobile.mobileTesting.MFP.enums.plans_page.plans_page_items import PlansPageItem, get_list_of_texts_by_button
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_page_base import DiaryPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.end_plan_page_base import EndPlanPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.log_workout_page_base import LogWorkoutPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plan_details_page_base import PlanDetailsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plans_page_base import PlansPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plus_plans_page_base import PlusPlansPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *
from src.mobile.utils.operating_system import OS


class PlansPage(PlansPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//android.widget.LinearLayout"
                                        "[@resource-id='com.myfitnesspal.android:id/toolbar_container']"
                                        "//android.widget.TextView")

        self.__take_the_survey = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/take_the_survey")
        self.__text_filter_by = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/textFilterBy")
        self.__buttons_container = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/chipGroupFilterTags")
        self.__button_web = None

        self.__plan_title = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/planTitle")
        self.__plus_button = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/action_show_plans_hub")
        self.__more_menu_button = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/task_day_more_menu")
        self.__end_plan_button = (AppiumBy.XPATH, "//*[@text='End Plan']")
        self.__log_workout_button = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/logWorkout")
        self.__workout_logged_confirmation = (AppiumBy.XPATH,
                                              "//*[@resource-id='com.myfitnesspal.android:id/snackbar_text' "
                                              "and @text='Workout logged.']")
        self.__view_button = (AppiumBy.ID, "com.myfitnesspal.android:id/snackbar_action")

    def get_all_filterby_buttons(self) -> list[WebElement]:
        path = (AppiumBy.XPATH, "//android.widget.RadioButton")
        tmp = []
        elements = self.driver.find_elements(*path)
        result_arr = []

        while tmp != elements:
            tmp = []
            for elem in elements:
                if elem not in result_arr:
                    result_arr.append(elem)
                tmp.append(elem)
            swipeLeftInContainer(self.driver.find_element(*self.__buttons_container), 700, self.driver, OS.ANDROID)
            elements = self.driver.find_elements(*path)

        return result_arr

    def get_all_texts_on_page(self) -> list[str]:
        item_plan_name = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/plan_name")
        texts_from_page = []
        elements = []
        flag = True
        while flag:
            try:
                self.driver.find_element(*self.__take_the_survey)
                elements = self.driver.find_elements(*item_plan_name)
                for elem in elements:
                    if elem.text not in texts_from_page:
                        texts_from_page.append(elem.text)
                flag = False
            except NoSuchElementException:
                tmp = []
                for elem in elements:
                    tmp.append(elem)
                elements = self.driver.find_elements(*item_plan_name)

                if tmp == elements:
                    raise AssertionError('[Plans Page] Take The Survey link is not present!')

                for elem in elements:
                    if not elem.text in texts_from_page:
                        texts_from_page.append(elem.text)
                swipeUp(600, 1, self.driver, OS.ANDROID)

        return texts_from_page

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.__title)) \
            and not init_page_or_uiobject(self.driver, MFPCommonPageBase) \
                .get_bottom_nav_bar().is_nav_bar_item_clickable(BottomNavBarItem.PLANS)

    def is_text_filter_by_present(self) -> bool:
        return self.driver.find_element(*self.__text_filter_by).is_displayed()

    def is_all_filter_by_buttons_present(self) -> bool:
        result_arr = self.get_all_filterby_buttons()

        for i in range(len(result_arr)):
            result_arr[i] = result_arr[i].text

        enum_values = [e.value for e in FilterByButton]

        if len(enum_values) != len(result_arr):
            raise AssertionError(
                '[Plans Page] Not all buttons present on page (difference by count)! Should be {}, but found only {}'
                .format(enum_values, result_arr))

        soft_assert = SoftAssert()
        for txt in result_arr:
            soft_assert.assert_expression(txt in enum_values, '[Plans Page] {} is not in FilterByButton Enum! It means '
                                                              'that not all buttons present!'.format(txt))
        soft_assert.assert_all()

        return True

    def is_all_texts_and_survey_link_present(self) -> bool:
        texts_from_page = self.get_all_texts_on_page()

        enum_values = [e.value[0] for e in PlansPageItem]

        if len(enum_values) != len(texts_from_page):
            raise AssertionError(
                '[Plans Page] Not all texts present on page (difference by count)! Should be {}, but found only {}'
                .format(enum_values, texts_from_page))

        soft_assert = SoftAssert()
        for txt in texts_from_page:
            soft_assert.assert_expression(txt in enum_values, '[Plans Page] {} is not in PlansPageItem Enum! It means '
                                                              'that not all texts present!'.format(txt))
        soft_assert.assert_all()

        return True

    def is_plan_shows(self, plan: PlansPageItem) -> bool:
        return self.driver.find_element(*self.__plan_title).text == plan.value[0]

    def check_filter_work_as_expected(self, button: FilterByButton) -> bool:
        self.click_filterby_button(button)

        texts_on_page = self.get_all_texts_on_page()
        list_of_needed_texts = get_list_of_texts_by_button(button)

        soft_assert = SoftAssert()
        for txt in texts_on_page:
            soft_assert.assert_expression(txt in list_of_needed_texts,
                                          '[Plans Page] {} is redundant on the page on button {}!'.format(txt, button))
        for txt in list_of_needed_texts:
            soft_assert.assert_expression(txt in texts_on_page,
                                          '[Plans Page] {} is missing from the page on button {}!'.format(txt, button))
        soft_assert.assert_all()

        return True

    def click_filterby_button(self, button: FilterByButton):
        swipeToElementVerticalDownFirstWithCountAndDuration(self.__text_filter_by, 10, 700, self.driver, OS.ANDROID)
        self.__button_web = (AppiumBy.XPATH, "//android.widget.RadioButton[@text='{}']".format(button.value))
        try:
            self.driver.find_element(*self.__button_web).click()
        except NoSuchElementException:
            swipeLeftInContainerWithCount(self.driver.find_element(*self.__buttons_container),
                                          700, 1, self.driver, OS.ANDROID)

    def click_on_plan(self, plan: PlansPageItem) -> PlanDetailsPageBase:
        elem = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android.plans:id/plan_name' and @text='{}']"
                .format(plan.value[0]))
        swipeToElementUpWithDuration(elem, 700, self.driver, OS.ANDROID)
        self.driver.find_element(*elem).click()
        return init_page_or_uiobject(self.driver, PlanDetailsPageBase)

    def click_plus_button(self) -> PlusPlansPageBase:
        self.driver.find_element(*self.__plus_button).click()
        return init_page_or_uiobject(self.driver, PlusPlansPageBase)

    def open_end_plan_page(self) -> EndPlanPageBase:
        self.driver.find_element(*self.__more_menu_button).click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.__end_plan_button))
        self.driver.find_element(*self.__end_plan_button).click()
        return init_page_or_uiobject(self.driver, EndPlanPageBase)

    def click_log_workout_button(self) -> LogWorkoutPageBase:
        self.driver.find_element(*self.__log_workout_button).click()
        return init_page_or_uiobject(self.driver, LogWorkoutPageBase)

    def is_workout_logged_confirmation_message_present(self) -> bool:
        return WebDriverWait(self.driver, 15)\
            .until(EC.visibility_of_element_located(self.__workout_logged_confirmation))

    def click_view_button(self) -> DiaryPageBase:
        self.driver.find_element(*self.__view_button).click()
        return init_page_or_uiobject(self.driver, DiaryPageBase)
