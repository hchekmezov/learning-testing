import base64
import logging
import os
import time

import pytest
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import attach_test_run_artifact

from src.mobile.mobileTesting.API_Demos.enums.api_demos_page_items import ApiDemosPageItem
from src.mobile.mobileTesting.API_Demos.enums.popup_menu_button_items import PopupMenuButtonItem
from src.mobile.mobileTesting.API_Demos.enums.start_page_items import StartPageItem
from src.mobile.mobileTesting.API_Demos.enums.views_page_items import ViewsPageItem
from src.mobile.mobileTesting.API_Demos.enums.visibility_page_fields import VisibilityPageField
from src.mobile.mobileTesting.API_Demos.pages.commons.content_page_base import ContentPageBase
from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.api_demos_page_base import \
    ApiDemosPageBase
from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.start_page_base import StartPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import attach_screenshot

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


@pytest.mark.skip
def test_first(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing

    content_page_base = init_page_or_uiobject(driver, ContentPageBase)

    if content_page_base.is_page_opened():
        start_page_base = content_page_base.click_ok_button()
    else:
        start_page_base = init_page_or_uiobject(driver, StartPageBase)

    assert start_page_base.is_page_opened(), "[Start Page] Start Page is not opened!"
    attach_screenshot(driver)

    api_demos_page_base = start_page_base.open_page(StartPageItem.API_DEMOS)
    assert api_demos_page_base.is_page_opened(), "[API Demos] API Demos page is not opened!"
    attach_screenshot(driver)

    views_page_base = api_demos_page_base.open_page(ApiDemosPageItem.VIEWS)
    assert views_page_base.is_page_opened(), "[Views Page] Views Page is not opened!"
    attach_screenshot(driver)

    drag_and_drop_page_base = views_page_base.open_page(ViewsPageItem.DRAG_AND_DROP)
    assert drag_and_drop_page_base.is_page_opened(), "[Drag and Drop Page] Drag adn Drop Page is not opened!"
    attach_screenshot(driver)

    drag_and_drop_page_base.make_drag_and_drop_dot1_and_dot2()
    assert drag_and_drop_page_base.is_drag_and_dropped_dot1_and_dot2(), "[Drag and Drop Page] Text about " \
                                                                        "drag and drop is not present. It can " \
                                                                        "mean that drag and drop was unsuccessfull!"
    attach_screenshot(driver)


@pytest.mark.skip
def test_second(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing

    content_page_base = init_page_or_uiobject(driver, ContentPageBase)

    if content_page_base.is_page_opened():
        start_page_base = content_page_base.click_ok_button()
    else:
        start_page_base = init_page_or_uiobject(driver, StartPageBase)

    assert start_page_base.is_page_opened(), "[Start Page] Start Page is not opened!"
    attach_screenshot(driver)

    api_demos_page_base = start_page_base.open_page(StartPageItem.API_DEMOS)
    assert api_demos_page_base.is_page_opened(), "[API Demos] API Demos page is not opened!"
    attach_screenshot(driver)

    views_page_base = api_demos_page_base.open_page(ApiDemosPageItem.VIEWS)
    assert views_page_base.is_page_opened(), "[Views Page] Views Page is not opened!"
    attach_screenshot(driver)

    popup_menu_page_base = views_page_base.open_page(ViewsPageItem.POPUP_MENU)
    assert popup_menu_page_base.is_page_opened(), "[Popup Menu Page] Popup Menu Page is not opened!"
    attach_screenshot(driver)

    popup_menu_page_base.make_a_toast_for(PopupMenuButtonItem.ADD)
    assert popup_menu_page_base.is_toast_shown_for(PopupMenuButtonItem.ADD), \
        "[Popup Menu Page] Toast not shown for {}".format(PopupMenuButtonItem.ADD)
    attach_screenshot(driver)


def test_third(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing

    content_page_base = init_page_or_uiobject(driver, ContentPageBase)

    if content_page_base.is_page_opened():
        start_page_base = content_page_base.click_ok_button()
    else:
        start_page_base = init_page_or_uiobject(driver, StartPageBase)

    assert start_page_base.is_page_opened(), "[Start Page] Start Page is not opened!"
    attach_screenshot(driver)

    api_demos_page_base = start_page_base.open_page(StartPageItem.API_DEMOS)
    assert api_demos_page_base.is_page_opened(), "[API Demos] API Demos page is not opened!"
    attach_screenshot(driver)

    views_page_base = api_demos_page_base.open_page(ApiDemosPageItem.VIEWS)
    assert views_page_base.is_page_opened(), "[Views Page] Views Page is not opened!"
    attach_screenshot(driver)

    visibility_page_base = views_page_base.open_page(ViewsPageItem.VISIBILITY)
    assert visibility_page_base.is_page_opened(), "[Visibility Page] Visibility Page is not opened!"
    attach_screenshot(driver)

    assert visibility_page_base.is_field_visible(VisibilityPageField.FIELD_B), "[Visibility Page] {} is not visible " \
                                                                               "while it should be!"\
        .format(VisibilityPageField.FIELD_B)
    attach_screenshot(driver)

    visibility_page_base.click_invisible_button()
    assert not visibility_page_base.is_field_visible(VisibilityPageField.FIELD_B), "[Visibility Page] {} is " \
                                                                                   "visible while it should not be!"\
        .format(VisibilityPageField.FIELD_B)
    attach_screenshot(driver)

    visibility_page_base.click_gone_button()
    assert not visibility_page_base.is_field_visible(VisibilityPageField.FIELD_B), "[Visibility Page] {} is " \
                                                                                   "visible while it should not be!"\
        .format(VisibilityPageField.FIELD_B)
    attach_screenshot(driver)