from enum import Enum

from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.api_demos_page_base import ApiDemosPageBase


class StartPageItem(Enum):
    APP_INVITE_DEMO = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='App Invite Demo']", None)
    API_DEMOS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='API Demos']", ApiDemosPageBase)
    SUPPORT_V4_DEMOS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support v4 Demos']", None)
    SUPPORT_V7_DEMOS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support v7 Demos']", None)
    SUPPORT_V13_DEMOS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support v13 Demos']", None)
    SUPPORT_DESIGN_DEMOS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support Design Demos']"
                            , None)
    SUPPORT_PERCENT_DEMOS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support Percent Demos"
                             "']", None)
    SUPPORT_APP_NAVIGATION = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support App "
                              "Navigation']", None)
    SUPPORT_DESIGN_DEMO = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support Design Demo: "
                           "Cheesesquare']", None)
    MOBILE_VISION_DEMOS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Mobile Vision Demos']",
                           None)
    SUPPORT_LEANBACK_SHOWCASE = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Support Leanback "
                                 "Showcase (Android TV)']", None)












    def get_xpath(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]