from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.create_food_page_base import CreateFoodPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.user_page_base import UserPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC

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

    def open_dashboard_page(self):
        self.driver.find_element(*self.__back_button).click()
