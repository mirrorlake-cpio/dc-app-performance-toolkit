import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action_pivotchart(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_pivotchart")
    def measure():

        @print_timing("selenium_app_custom_action:view_dashboard_mirrorlake_pivotchart")
        def sub_measure():
            #!!!!!! VERIFY AND CORRECT THE DASHBOARD ID
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/Dashboard.jspa?selectPageId=10100")
            #!!!!!! VERIFY AND CORRECT THE GADGET-TITLE-ID
            page.wait_until_visible((By.ID, "gadget-10100-title"))  # Wait for gadget visible
            #page.wait_for_page_loaded()
        sub_measure()

    measure()

def app_specific_action_planchart(webdriver, datasets):

    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_planchart")
    def measure():

        @print_timing("selenium_app_custom_action:view_dashboard_mirrorlake_planchart")
        def sub_measure():
            #!!!!!! VERIFY AND CORRECT THE DASHBOARD ID
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/Dashboard.jspa?selectPageId=10101")
            #!!!!!! VERIFY AND CORRECT THE GADGET-TITLE-ID
            page.wait_until_visible((By.ID, "gadget-10101-title"))  # Wait for gadget visible
            #page.wait_for_page_loaded()
        sub_measure()

    measure()
