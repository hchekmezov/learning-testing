from enum import Enum

from src.mobile.mobileTesting.MFP.pages.commons.more_page.my_premium_tools_page_base import MyPremiumToolsPageBase


class MoreMenuOption(Enum):
    MY_PREMIUM_TOOLS = ('My Premium Tools', MyPremiumToolsPageBase)
    INTERMITTENT_FASTING = ('Intermittent Fasting', None)
    RECIPE_DISCOVERY = ('Recipe Discovery', None)
    PROGRESS = ('Progress', None)
    WORKOUT_ROUTINES = ('Workout Routines', None)
    GOALS = ('Goals', None)
    NUTRITION = ('Nutrition', None)
    RECIPE_MEALS_AND_FOODS = ('Recipes, Meals & Foods', None)
    APPS_AND_DEVICES = ('Apps & Devices', None)
    STEPS = ('Steps', None)
    COMMUNITY = ('Community', None)
    REMINDERS = ('Reminders', None)
    FRIENDS = ('Friends', None)
    MESSAGES = ('Messages', None)
    PRIVACY_CENTER = ('Privacy Center', None)
    SETTINGS = ('Settings', None)
    HELP = ('Help', None)
    SYNC = ('Sync', None)


    def get_base_class(self):
        return self.value[1]

    def get_text(self):
        return self.value[0]
