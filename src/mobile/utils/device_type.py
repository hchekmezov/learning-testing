from enum import Enum
import warnings


def device_type(page_type, parent_class):
    def decorator(cls):
        cls.page_type = page_type
        cls.parent_class = parent_class
        return cls

    warnings.warn("device_type is deprecated. Maybe don't need to use in python!", DeprecationWarning, stacklevel=2)
    return decorator


class DeviceType(Enum):
    DESKTOP = ("desktop", "desktop")
    ANDROID_TABLET = ("android_tablet", "android")
    ANDROID_PHONE = ("android_phone", "android")
    ANDROID_TV = ("android_tv", "android")
    IOS_TABLET = ("ios_tablet", "ios")
    IOS_PHONE = ("ios_phone", "ios")
    APPLE_TV = ("apple_tv", "tvos")

    def get_type(self):
        return self.value[0]

    def get_family(self):
        return self.value[1]
