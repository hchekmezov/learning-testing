from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.newsfeed_page.comments_page_base import CommentsPageBase
from src.mobile.utils.mobile_utils import *

class CommentsPage(CommentsPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']//*[@text='Comments']")
        self.__input_comment_field = (AppiumBy.ID, "com.myfitnesspal.android:id/inputComment")
        self.__post_button = (AppiumBy.ACCESSIBILITY_ID, "Post")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__input_comment_field))

    def send_comment(self, comment: str):
        self.driver.find_element(*self.__input_comment_field).send_keys(comment)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__post_button))
        self.driver.find_element(*self.__post_button).click()

    def is_comment_sent_by_username(self, comment: str, username: str) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((AppiumBy.XPATH,
                             "//*[@resource-id='com.myfitnesspal.android:id/layoutCommentContainer']"
                             "//*[@resource-id='com.myfitnesspal.android:id/textUsername' and @text='{}']"
                             "/..//*[@resource-id='com.myfitnesspal.android:id/textStatusText' and @text='{}']"
                             .format(username, comment))))
