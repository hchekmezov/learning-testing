from enum import Enum


class HomePagePlaylistTitle(Enum):
    WORKOUT = 'Workout'
    YOGA = 'Yoga'
    DANCE = 'Dance'
    Meditate = 'Meditate'
    MENTAL_HEALTH = 'Mental Health'
    SLEEP = 'Sleep'

    @staticmethod
    def get_playlist_titles_values():
        result = [e.value for e in HomePagePlaylistTitle]
        return result

