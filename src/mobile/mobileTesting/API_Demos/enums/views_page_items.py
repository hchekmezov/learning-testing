from enum import Enum

from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.views_page.drag_and_drop_page_base import \
    DragAndDropPageBase


class ViewsPageItem(Enum):
    ANIMATION = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Animation']", None)
    AUTO_COMPLETE = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Auto Complete']", None)
    BUTTONS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Buttons']", None)
    CHRONOMETER = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Chronometer']", None)
    CONTROLS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Controls']", None)
    CUSTOM = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Custom']", None)
    DATE_WIDGETS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Date Widgets']", None)
    DRAG_AND_DROP = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Drag and Drop']",
                     DragAndDropPageBase)
    EXPANDABLE_LISTS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Expandable Lists']", None)
    FOCUS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Focus']", None)
    GAME_CONTROLLER_INPUT = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Game Controller Input"
                             "']", None)
    GRID = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Grid']", None)
    HOVER_EVENTS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Hover Events']", None)
    IMAGE_BUTTON = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='ImageButton]", None)
    IMAGE_VIEW = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='ImageView']", None)
    LAYOUT_ANIMATION = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Layout Animation']", None)
    LAYOUTS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Layouts']", None)
    LISTS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Lists']", None)
    POPUP_MENU = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Popup Menu']", None)
    PROGRESS_BAR = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Progress Bar']", None)
    RADIO_GROUP = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Radio Group']", None)
    RATING_BAR = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Rating Bar']", None)
    ROTATING_BUTTON = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Rotating Button']", None)
    SCROLL_BARS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='ScrollBars']", None)
    SEARCH_VIEW = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Search View']", None)
    SECURE_VIEW = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Secure View']", None)
    SEEK_BAR = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Seek Bar']", None)
    SPINNER = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Spinner']", None)
    SPLITTING_TOUCHES_ACROSS_VIEWS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Splitting "
                                      "Touches across Views']", None)
    SWITCHES = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Switches']", None)
    SYSTEM_UI_VISIBILITY = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='System UI Visibility']"
                            , None)
    TABS = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Tabs']", None)
    TEXT_CLOCK = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='TextClock']", None)
    TEXT_SWITCHER = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='TextSwitcher']", None)
    VISIBILITY = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='Visibility']", None)
    WEB_VIEW = ("//*[@resource-id='android:id/list']/android.widget.TextView[@text='WebView']", None)

    def get_xpath(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]
