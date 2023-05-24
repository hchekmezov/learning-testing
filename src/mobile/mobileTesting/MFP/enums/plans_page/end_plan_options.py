from enum import Enum


class EndPlanOption(Enum):
    WANT_DIFFERENT_PLAN = 'I want to start a different plan.'
    WAS_NOT_HELPFUL = 'The plan wasn’t helpful to me.'
    JUST_WANTED_SEE_A_PLAN = 'I just wanted to see what the plan was about.'
    WAS_NOT_EXPECTED = 'The plan wasn’t what I expected.'
    OTHER_PRIORITIES = 'Other priorities in my life took precedent.'
    FORGOT = 'I forgot about it.'
    WANT_RESTART = 'I want to restart the plan.'
    LOST_INTEREST = 'I lost interest.'
    TOO_HARD = 'The plan was too hard to follow.'
