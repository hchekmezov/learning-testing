from enum import Enum
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.add_nutrient_info_page_base import \
    AddNutrientInfoPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.create_food_page_base import CreateFoodPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC


class CreateFoodPage(CreateFoodPageBase):

    class Defaults(Enum):
        BRAND_NAME = 'name'
        DESCRIPTION = 'description'
        SERVING_SIZE = '1'
        SERVING_MEASURE = 'gram'
        SERVINGS_PER_CONTAINER = '1'
        CALORIES = '100'

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__brand_name = (AppiumBy.ID, "com.myfitnesspal.android:id/editTxtBrandName")
        self.__description = (AppiumBy.ID, "com.myfitnesspal.android:id/editTxtDescription")
        self.__serving_size = (AppiumBy.ID, "com.myfitnesspal.android:id/editTxtServingSizeQuantity")
        self.__serving_measure = (AppiumBy.ID, "com.myfitnesspal.android:id/servingSizeAutoTxt")
        self.__servings_per_container = (AppiumBy.ID, "com.myfitnesspal.android:id/editTxtServingsPerContainer")
        self.__next_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                              "/androidx.appcompat.widget.LinearLayoutCompat/android.widget.Button")
        self.__calories_field = (AppiumBy.ID, "com.myfitnesspal.android:id/editTxtCalories")
        self.__save_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                              "/androidx.appcompat.widget.LinearLayoutCompat/android.widget.Button")

        self.__back_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                              "/android.widget.ImageButton")
        self.__title = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                        "/android.widget.TextView")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__back_button))

    def fill_all_fields_by_default_values(self) -> AddNutrientInfoPageBase:
        self.driver.hide_keyboard()
        self.driver.find_element(*self.__brand_name).send_keys(self.Defaults.BRAND_NAME.value)
        self.driver.find_element(*self.__description).send_keys(self.Defaults.DESCRIPTION.value)
        self.driver.find_element(*self.__serving_size).send_keys(self.Defaults.SERVING_SIZE.value)
        self.driver.find_element(*self.__serving_measure).send_keys(self.Defaults.SERVING_MEASURE.value)
        self.driver.find_element(*self.__servings_per_container).send_keys(self.Defaults.SERVINGS_PER_CONTAINER.value)
        self.driver.find_element(*self.__next_button).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__calories_field))
        self.driver.find_element(*self.__calories_field).send_keys(self.Defaults.CALORIES.value)
        save_btn_elen = self.driver.find_element(*self.__save_button)
        save_btn_elen.click()
        save_btn_elen.click()
        return init_page_or_uiobject(self.driver, AddNutrientInfoPageBase)

