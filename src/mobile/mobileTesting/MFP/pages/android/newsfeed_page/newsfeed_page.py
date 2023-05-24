from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.newsfeed_page.comments_page_base import CommentsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.newsfeed_page.newsfeed_page_base import NewsfeedPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *


class NewsfeedPage(NewsfeedPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//android.widget.LinearLayout"
                                        "[@resource-id='com.myfitnesspal.android:id/toolbar_container']"
                                        "//android.widget.TextView")
        self.__like_button = (AppiumBy.XPATH, "(//*[@resource-id='com.myfitnesspal.android:id/buttonLike']/../../..)"
                                              "[1]//*[@resource-id='com.myfitnesspal.android:id/buttonLike']")
        self.__comment_button = (AppiumBy.XPATH, "(//*[@resource-id='com.myfitnesspal.android:id/buttonLike']/../.."
                                            "/..)[1]//*[@resource-id='com.myfitnesspal.android:id/textButtonComment']")
        self.__text_number_of_likes = (AppiumBy.XPATH,
                                       "(//*[@resource-id='com.myfitnesspal.android:id/buttonLike']/../../..)[1]"
                                       "//*[@resource-id='com.myfitnesspal.android:id/textNumberOfLikes']")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and not init_page_or_uiobject(self.driver, MFPCommonPageBase) \
            .get_bottom_nav_bar().is_nav_bar_item_clickable(BottomNavBarItem.NEWSFEED)

    def is_user_can_like_default_post(self) -> bool:
        swipeToElementUpWithDuration(self.__like_button, 200, self.driver, OS.ANDROID)
        number_of_likes = self.driver.find_elements(*self.__text_number_of_likes)
        if len(number_of_likes) > 0:
            number = int(number_of_likes[0].text.split(' ')[0])
        else:
            number = 0

        self.driver.find_element(*self.__like_button).click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.__text_number_of_likes))
        return int(self.driver.find_element(*self.__text_number_of_likes).text.split(' ')[0]) == number + 1

    def is_user_can_unlike_default_post(self) -> bool:
        swipeToElementUpWithDuration(self.__like_button, 200, self.driver, OS.ANDROID)
        number_of_likes = self.driver.find_element(*self.__text_number_of_likes)

        number = int(number_of_likes.text.split(' ')[0])
        self.driver.find_element(*self.__like_button).click()

        if number > 1:
            return int(self.driver.find_element(*self.__text_number_of_likes).text.split(' ')[0]) == number - 1
        else:
            return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(self.__text_number_of_likes))

    def click_comment_button(self) -> CommentsPageBase:
        swipeToElementUpWithDuration(self.__comment_button, 200, self.driver, OS.ANDROID)
        self.driver.find_element(*self.__comment_button).click()
        return init_page_or_uiobject(self.driver, CommentsPageBase)

    def is_articles_myfitnesspal_present(self) -> bool:
        return swipeToElementVerticalWithCountAndDuration(
            (AppiumBy.XPATH,"//*[@resource-id='com.myfitnesspal.android:id/textBlogLink' "
                            "and @text='MyFitnessPal Blog']"),
        13, 600, self.driver, OS.ANDROID)
