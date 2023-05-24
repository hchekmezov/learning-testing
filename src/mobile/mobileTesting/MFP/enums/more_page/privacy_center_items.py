from enum import Enum

from src.mobile.mobileTesting.MFP.pages.commons.more_page.sharing_privacy_sett_page_base import \
    SharingPrivacySettingsPageBase


class PrivacyCenterItem(Enum):
    TERMS_OF_SERVICE = ('com.myfitnesspal.android:id/tos', None)
    PRIVACY_POLICY = ('com.myfitnesspal.android:id/privacy_policy', None)
    PERSONALIZATION = ('com.myfitnesspal.android:id/personalization', None)
    SHARING_AND_PRIVACY_SETTINGS = ('com.myfitnesspal.android:id/sharing_and_privacy', SharingPrivacySettingsPageBase)
    DO_NOT_SELL_MY_PERSONAL_INFO = ('com.myfitnesspal.android:id/do_not_sell', None)
    CONTACT_SUPPORT = ('com.myfitnesspal.android:id/contact_support', None)

    def get_id(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]