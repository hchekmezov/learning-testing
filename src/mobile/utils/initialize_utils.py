import os
import importlib.util
import inspect
import logging

from appium.webdriver import Remote
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

"""
OLD TECHNOLOGY (BY DIRECT IMPORT) RETURNED:
EXAMPLE >>  <src.mobile.mobileTesting.MFP.pages.android.preview_page.PreviewPage object at 0x10c0b9730>

NEW TECHNOLOGY (BY METHOD init_page_or_uiobject(driver, base_class)) RETURNS:
EXAMPLE >> <preview_page.PreviewPage object at 0x10c080520>

This does not affect the tests now, but it is not known what will happen in the future (working version from 20.04.2023)
"""


def find_subclass_in_dir(directory, base_class):
    subclasses = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            found_subclasses = find_subclass_in_dir(file_path, base_class)
            if found_subclasses:
                subclasses.extend(found_subclasses)
        elif filename.endswith('.py'):
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            attrs_arr = {}
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                attrs_arr[attr_name] = attr
            if base_class.__name__ in attrs_arr.keys():
                for attr in attrs_arr.values():
                    if isinstance(attr, type) and issubclass(attr, base_class) and attr != base_class:
                        subclasses.append(attr)
    return subclasses if subclasses else None


def init_page_or_uiobject(driver: Remote, base_class):
    file_path = inspect.getfile(base_class)
    if 'uiautomator' in driver.capabilities['automationName'] \
            or driver.capabilities['platformName'].lower() == 'android':
        operating = "android"
    elif 'xcuitest' in driver.capabilities['automationName'] \
            or driver.capabilities['platformName'].lower() == 'ios':
        operating = "ios"
    else:
        raise Exception('Not found child class for this driver capabilities!')

    while not os.path.isdir(os.path.join(file_path, operating)):
        file_path = os.path.abspath(os.path.join(file_path, "../"))

    directory_for_find = os.path.abspath(os.path.join(file_path, operating))
    subclass = find_subclass_in_dir(directory_for_find, base_class)
    subclass = subclass[0]

    return subclass(driver)
