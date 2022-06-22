from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://staging.portal.internal.viana.ai/"


class TestStaffLogin:
    """
    Portal > Functional Tests > Login > Staff.
    """

    def test_staff_can_login_to_viana_portal_ORC_T18(self, init_webdriver):

        """
        Objective: User should be able to login if both username and password are valid.

        Given the user is on the login page
        When the user enters a valid username and password
        And the user clicks on the "Log In" button
        Then the user should login successfully
        """
        # Given the user is on the login page
        driver: webdriver.Chrome = init_webdriver
        wait = WebDriverWait(driver, timeout=20)
        driver.get("https://staging.portal.internal.viana.ai/")
        # When the user enters a valid username and password
        username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')

        username_field.send_keys("ray+staff@meldcx.com")
        password_field.send_keys("Test101@")
        # And the user clicks on the "Log In" button
        login_button = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        login_button.click()

        wait.until(EC.url_contains("/dashboard"))
        wait.until(EC.title_contains("Dashboard"))
        # Then the user should login successfully
        assert "Dashboard" in driver.title
        assert "/dashboard" in driver.current_url
