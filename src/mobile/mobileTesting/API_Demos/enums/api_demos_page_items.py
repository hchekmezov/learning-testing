from enum import Enum

from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.views_page.views_page_base import ViewsPageBase


class ApiDemosPageItem(Enum):
    ACCESSIBILITY = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Accessibility']", None)
    ANIMATION = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Animation']", None)
    APP = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='App']", None)
    CONTENT = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Content']", None)
    GRAPHICS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Graphics']", None)
    HARDWARE = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Hardware']", None)
    MEDIA = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Media']", None)
    NFC = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='NFC']", None)
    OS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='OS']", None)
    PREFERENCE = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Preference']", None)
    SECURITY = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Security']", None)
    TEXT = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Text']", None)
    VIEWS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Views']", ViewsPageBase)

    def get_xpath(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]
