from enum import Enum

from src.mobile.mobileTesting.MFP.enums.plans_page.filter_by_buttons import FilterByButton


def get_list_of_texts_by_button(button: FilterByButton):
    enum_values = [e.value for e in PlansPageItem]
    result_list = []
    for val in enum_values:
        if button in val[1]:
            result_list.append(val[0])
    return result_list


class PlansPageItem(Enum):
    LOW_CARB = ('Low Carb', [FilterByButton.MEAL_PLAN])
    REACHING_YOUR_CALORIE_GOAL = ('Reaching Your Calorie Goal', [FilterByButton.NUTRITION])
    TOTAL_BODY_POWER = ('Total Body Power', [FilterByButton.WORKOUT])
    EAT_GREEN = ('Eat Green', [FilterByButton.FREE, FilterByButton.NUTRITION])
    INTERMITTENT_FASTING = ('Intermittent Fasting', [FilterByButton.FREE, FilterByButton.NUTRITION])
    SUPPORT_YOUR_IMMUNE_SYSTEM = ('Support Your Immune System', [FilterByButton.NUTRITION])
    EATING_FOR_IMPACT = ('Eating for Impact', [FilterByButton.FREE, FilterByButton.NUTRITION])
    STEPS_6000_A_DAY = ('6,000 Steps a Day', [FilterByButton.WALKING])
    STEPS_11000_A_DAY = ('11,000 Steps a Day', [FilterByButton.WALKING])
    STEPS_9000_A_DAY = ('9,000 Steps a Day', [FilterByButton.WALKING])
    TONED_UPPER_BODY = ('Toned Upper Body', [FilterByButton.WORKOUT])
    JUMPSTART_YOUR_HEALTH = ('Jumpstart Your Health', [FilterByButton.FREE, FilterByButton.NUTRITION])
    CORE_PLUS = ('Core Plus', [FilterByButton.WORKOUT])
    INTRO_TO_MACRO_TRACKING = ('Intro to Macro Tracking', [FilterByButton.NUTRITION])
    MYFITNESSPAL_101 = ('MyFitnessPal 101', [FilterByButton.FREE])
    PROGRESSIVE_DUMBBELL = ('Progressive Dumbbell', [FilterByButton.WORKOUT])
    LOW_IMPACT_STRENGTH = ('Low Impact Strength', [FilterByButton.WORKOUT])
    BUILDING_HEALTHY_HABITS = ('Building Healthy Habits', [FilterByButton.NUTRITION])
    HIGH_PROTEIN = ('High Protein', [FilterByButton.MEAL_PLAN])
    STRONG_GLUTES_AND_THIGHS = ('Strong Glutes & Thighs ', [FilterByButton.WORKOUT])
    HEALTHY_KICKSTART = ('Healthy Kickstart', [FilterByButton.NUTRITION])
    PROGRESSIVE_BODYWEIGHT = ('Progressive Bodyweight', [FilterByButton.WORKOUT])
    MINDFUL_AND_MOTIVATED = ('Mindful + Motivated', [FilterByButton.FREE, FilterByButton.NUTRITION])
