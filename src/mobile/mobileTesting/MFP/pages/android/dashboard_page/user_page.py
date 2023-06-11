from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.create_food_page_base import CreateFoodPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.goals_page_base import GoalsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.user_page_base import UserPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC, swipeToElementVerticalWithCountAndDuration
from src.mobile.utils.operating_system import OS


class UserPage(UserPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__user_image = (AppiumBy.ID, "com.myfitnesspal.android:id/image")
        self.__back_button = (AppiumBy.ID, "com.myfitnesspal.android:id/profileBackArrow")

        self.__my_items_tab = (AppiumBy.ACCESSIBILITY_ID, "My Items")
        self.__food_text_elem = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/foods']"
                                                 "//*[@resource-id='com.myfitnesspal.android:id/text']")
        self.__food_create_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/foods']"
                                                     "//*[@resource-id='com.myfitnesspal.android:id/create']")
        self.__username = (AppiumBy.ID, "com.myfitnesspal.android:id/toolbarUsername")
        self.__update_goals_button = (AppiumBy.XPATH, "//android.widget.Button[@text='UPDATE GOALS']")

        self.__daily_goal = (AppiumBy.ID, "com.myfitnesspal.android:id/dailyGoalEnergy")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__user_image)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__back_button))

    def click_my_items_tab(self):
        self.driver.find_element(*self.__my_items_tab).click()

    def click_create_food_button(self) -> CreateFoodPageBase:
        self.driver.find_element(*self.__food_create_button).click()
        return init_page_or_uiobject(self.driver, CreateFoodPageBase)

    def get_current_food_count(self) -> int:
        return int(self.driver.find_element(*self.__food_text_elem).text.split(' ')[0])

    def get_username(self) -> str:
        return self.driver.find_element(*self.__username).text

    def click_back_button(self):
        self.driver.find_element(*self.__back_button).click()

    def click_update_goals_button(self) -> GoalsPageBase:
        swipeToElementVerticalWithCountAndDuration(self.__update_goals_button, 5, 600, self.driver, OS.ANDROID)
        self.driver.find_element(*self.__update_goals_button).click()
        return init_page_or_uiobject(self.driver, GoalsPageBase)

    def get_number_of_daily_goal(self):
        txt = self.driver.find_element(*self.__daily_goal).text
        return int(txt.split()[0].replace(',', ''))




