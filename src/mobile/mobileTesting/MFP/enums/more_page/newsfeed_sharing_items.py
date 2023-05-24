from enum import Enum


class NewsfeedSharingItem(Enum):
    I_BECOME_FRIENDS_WITH_SOMEONE = 'I become friends with someone'
    I_REPLY_TO_A_TOPIC_ON_THE_MESSAGE_BOARDS = 'I reply to a topic on the message boards'
    I_CREATE_A_NEW_TOPIC_ON_THE_MESSAGE_BOARDS = 'I create a new topic on the message boards'
    I_CREATE_A_NEW_BLOG_POST = 'I create a new blog post'
    I_COMMENTED_ON_SOMEONE_ELSES_NEWS_FEED_UPDATE = "I commented on someone else's news feed update"
    I_WROTE_ON_SOMEONE_ELSES_PROFILE_PAGE = "I wrote on someone else 's profile page"
    I_HAVE_NOT_LOGGED_INTO_MYFITNESSPAL_FOR_SEVERAL_DAYS = 'I have not logged into MyFitnessPal for several days'
    I_HAVE_LOGGED_IN_FOR_SEVERAL_DAYS_IN_ROW = 'I have logged in for several days in row'
    I_HAVE_LOST_WEIGHT = 'I have lost weight'
    I_HAVE_COMPLETED_MY_DIARY_FOR_THE_DAY = 'I have completed my diary for the day'
    I_PERFORM_A_CARDIO_EXERCISE = 'I perform a cardio exercise'
    THERE_ARE_NEW_ARTICLES_FROM_THE_MYFITNESSPAL_BLOG = 'There are new articles from the MyFitnessPal blog'
    THERE_ARE_NEW_VIDEOS_FROM_THE_MYFITNESSPAL_BLOG = 'There are new videos from the MyFitnessPal blog'
