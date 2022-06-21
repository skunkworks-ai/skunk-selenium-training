from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://staging.portal.internal.viana.ai/"


class TestStaffLogin:
    """
    Portal > Functional Tests > Login > Staff.
    """

    def test_staff_can_login_to_viana_portal_ORC_T18(self):
        """
        Objective: User should be able to login if both username and password are valid.

        Given the user is on the login page
        When the user enters a valid username and password
        And the user clicks on the "Log In" button
        Then the user should login successfully
        """
        pass

    def test_staff_can_access_the_end_user_terms_page_ORC_T15(self):
        """
        Objective: To be able to navigate to the end user terms page from the login page.

        Given the user is on the login page
        When the user clicks on the "End User Terms" link
        Then the user should be redirected to the end user terms page
        """
        pass
