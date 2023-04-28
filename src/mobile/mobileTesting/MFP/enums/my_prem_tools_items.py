from enum import Enum


class MyPremToolsItem(Enum):
    MORE_APP_CUSTOMIZATION = ('More App Customization', 'Choose the right settings for your goals.')
    DEEPER_NUTRITIONAL_INSIGHTS = ('Deeper Nutritional Insights', 'Discover which foods fuel you best.')
    GUIDED_WORKOUT_AND_MEAL_PLANS = ('Guided Workout & Meal Plans', 'Build healthy habits with daily coaching.')

    def get_header_text(self):
        return self.value[0]

    def get_desc_text(self):
        return self.value[1]