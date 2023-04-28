from enum import Enum


class CustomSummaryItem(Enum):

    FAT = ('Fat', 'Fat')
    SATURATED_FAT = ('Saturated Fat', 'SatFat')
    POLYUNSATURATED_FAT = ('Polyunsaturated Fat', 'PolyFat')
    MONOUNSATURATED_FAT = ('Monounsaturated Fat', 'MonoFat')
    TRANS_FAT = ('Trans Fat', 'TransFat')
    CHOLESTEROL = ('Cholesterol', 'Cholesterol')
    SODIUM = ('Sodium', 'Sodium')
    POTASSIUM = ('Potassium', 'Potassium')
    CARBOHYDRATES = ('Carbohydrates', 'Carbs')
    FIBER = ('Fiber', 'Fiber')
    SUGAR = ('Sugar', 'Sugar')
    PROTEIN = ('Protein', 'Protein')
    VITAMIN_A = ('Vitamin A', 'VitaminA')
    VITAMIN_C = ('Vitamin C', 'VitaminC')
    CALCIUM = ('Calcium', 'Calcium')
    IRON = ('Iron', 'Iron')

    def get_title(self):
        return self.value[0]

    def get_short_version(self):
        return self.value[1]
