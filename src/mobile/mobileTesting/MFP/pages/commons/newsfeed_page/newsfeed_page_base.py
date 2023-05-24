import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.pages.commons.newsfeed_page.comments_page_base import CommentsPageBase


class NewsfeedPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_user_can_like_default_post(self) -> bool:
        return

    @abc.abstractmethod
    def is_user_can_unlike_default_post(self) -> bool:
        return

    @abc.abstractmethod
    def click_comment_button(self) -> CommentsPageBase:
        return

    @abc.abstractmethod
    def is_articles_myfitnesspal_present(self) -> bool:
        return
