from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://staging.portal.internal.viana.ai/"


class TestAdminLogin:
    """
    Portal > Functional Tests > Login > Admin.
    """

    def test_admin_can_login_to_viana_portal_ORC_T16(self):
        """
        Objective: User should be able to login if both username and password are valid.

        Given the user is on the login page
        When the user enters a valid username and password
        And the user clicks on the "Log In" button
        Then the user should login successfully
        """
        pass
