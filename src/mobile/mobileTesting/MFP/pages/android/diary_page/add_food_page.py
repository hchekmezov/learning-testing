from appium.webdriver import Remote, WebElement
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.enums.meals_names import MealName
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.add_food_page_base import AddFoodPageBase
from src.mobile.utils.mobile_utils import EC


class AddFoodPage(AddFoodPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/selectMealText")
        self.__search_bar = (AppiumBy.ID, "com.myfitnesspal.android:id/searchBar")
        self.__selected_meal = (AppiumBy.ID, "com.myfitnesspal.android:id/selectMeal")
        self.__search_edit_text_field = (AppiumBy.ID, "com.myfitnesspal.android:id/searchEditText")
        self.__back_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/selectMeal']"
                                              "//preceding-sibling::android.widget.ImageButton")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__selected_meal)) and \
            self.wait.until(EC.visibility_of_element_located(self.__search_bar))

    def is_needed_page_opened_by_meal_name(self, meal_name: MealName) -> bool:
        return meal_name.value == self.driver.find_element(*self.__title).text

    def click_back_button(self):
        self.driver.find_element(*self.__back_button).click()

    def get_title(self) -> str:
        return self.driver.find_element(*self.__title).text

    def find_and_add_meal(self, meal: str):
        search_edit: WebElement = self.driver.find_element(*self.__search_edit_text_field)
        search_edit.send_keys(meal)
        self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/recyclerSearchFoodList']"
                                                 "/android.view.ViewGroup[2]")))

        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/recyclerSearchFoodList']"
                                                 "/android.view.ViewGroup[2]").click()
        self.driver.hide_keyboard()
        self.wait.until(EC.visibility_of_all_elements_located((AppiumBy.ID,
                                                               "com.myfitnesspal.android:id/onlineSearchStatus")))
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/itemWithHeaderContainer']"
                                                 "[1]//android.widget.ImageView").click()










