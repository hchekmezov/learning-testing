import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage


class CommentsPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def send_comment(self, comment: str):
        return

    @abc.abstractmethod
    def is_comment_sent_by_username(self, comment: str, username: str) -> bool:
        return
