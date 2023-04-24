from enum import Enum
from deprecated import deprecated
import warnings

# @deprecated(reason="Maybe not needed to use in python case")
def device_type(page_type, parent_class):
    def decorator(cls):
        cls.page_type = page_type
        cls.parent_class = parent_class
        return cls

    warnings.warn("device_type is deprecated. Maybe don't need to use in python!", DeprecationWarning, stacklevel=2)
    return decorator

# @deprecated(reason="Maybe not needed to use in python case")
class DeviceType(Enum):
    DESKTOP = ("desktop", "desktop")
    ANDROID_TABLET = ("android_tablet", "android")
    ANDROID_PHONE = ("android_phone", "android")
    ANDROID_TV = ("android_tv", "android")
    IOS_TABLET = ("ios_tablet", "ios")
    IOS_PHONE = ("ios_phone", "ios")
    APPLE_TV = ("apple_tv", "tvos")

    # warnings.warn("DeviceType is deprecated. Maybe don't need to use in python!", DeprecationWarning, stacklevel=2)

    def get_type(self):
        return self.value[0]

    def get_family(self):
        return self.value[1]


