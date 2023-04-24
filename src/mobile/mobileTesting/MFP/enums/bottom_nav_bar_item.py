from enum import Enum

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_page_base import DiaryPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page_base import MorePageBase
from src.mobile.mobileTesting.MFP.pages.commons.newsfeed_page_base import NewsfeedPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page_base import PlansPageBase


class BottomNavBarItem(Enum):
    DASHBOARD = ('Dashboard', DashboardPageBase)
    DIARY = ('Diary', DiaryPageBase)
    NEWSFEED = ('Newsfeed', NewsfeedPageBase)
    PLANS = ('Plans', PlansPageBase)
    MORE = ('More', MorePageBase)

    def get_button_name(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]