from enum import Enum

from src.mobile.mobileTesting.MFP.pages.commons.more_page.newsfeed_sharing_page_base import NewsfeedSharingPageBase


class SharingPrivacyItem(Enum):
    NEWS_FEED_SHARING = ("//*[@resource-id='com.myfitnesspal.android:id/textSettingName' "
                         "and @text='News Feed Sharing']", NewsfeedSharingPageBase)
    DIARY_SHARING = ("//*[@resource-id='com.myfitnesspal.android:id/textSettingName' "
                         "and @text='Diary Sharing']", None)
    EMAIL_SETTINGS = ("//*[@resource-id='com.myfitnesspal.android:id/textSettingName' "
                         "and @text='Email Settings']", None)
    FACEBOOK_SETTINGS = ("//*[@resource-id='com.myfitnesspal.android:id/textSettingName' "
                         "and @text='Facebook Settings']", None)
    AUTO_PLAY_SETTINGS = ("//*[@resource-id='com.myfitnesspal.android:id/textSettingName' "
                         "and @text='Auto-Play Settings']", None)

    def get_xpath(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]