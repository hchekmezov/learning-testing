from enum import Enum

from src.mobile.mobileTesting.MFP.pages.commons.more_page.edit_profile_page_base import EditProfilePageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.privacy_center_page_base import PrivacyCenterPageBase


class SettingsItem(Enum):
    EDIT_PROFILE = ('com.myfitnesspal.android:id/textEditProfile', EditProfilePageBase)
    MY_GOALS = ('com.myfitnesspal.android:id/textMyGoals', None)
    PREMIUM_SUBSCRIPTION = ('com.myfitnesspal.android:id/textPremiumSubscription', None)
    MY_APPS_AND_DEVICES = ('com.myfitnesspal.android:id/textAppsDevices', None)
    DELETE_ACCOUNT = ('com.myfitnesspal.android:id/textDeleteAccount', None)
    CHANGE_PASSWORD = ('com.myfitnesspal.android:id/textChangePassword', None)
    LOG_OUT = ('com.myfitnesspal.android:id/textLogOut', None)
    APPEARANCE = ('com.myfitnesspal.android:id/textAppearanceSettings', None)
    DIARY_SETTINGS = ('com.myfitnesspal.android:id/textDiarySettings', None)
    REMINDERS = ('com.myfitnesspal.android:id/textReminders', None)
    PRIVACY_CENTER = ('com.myfitnesspal.android:id/textPrivacyCenter', PrivacyCenterPageBase)
    WEEKLY_NUTRITION_SETTINGS = ('com.myfitnesspal.android:id/textWeeklyNutrition', None)
    STEPS = ('com.myfitnesspal.android:id/textSteps', None)
    PUSH_NOTIFICATIONS = ('com.myfitnesspal.android:id/textPushNotifications', None)
    ABOUT_US = ('com.myfitnesspal.android:id/textAboutUs', None)
    CONTACT_SUPPORT = ('com.myfitnesspal.android:id/textContactSupport', None)
    JOIN_OUR_BETA_PROGRAM = ('com.myfitnesspal.android:id/textBetaJoin', None)
    FAQS_FEEDBACK = ('com.myfitnesspal.android:id/textFaq', None)
    TROUBLESHOOTING = ('com.myfitnesspal.android:id/textTroubleshooting', None)
    DEBUG_LOGS = ('com.myfitnesspal.android:id/textDebugLogs', None)

    def get_id(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]


