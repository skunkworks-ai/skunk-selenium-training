from multiprocessing.connection import wait
from click import password_option
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import init_webdriver

BASE_URL = "https://staging.portal.internal.viana.ai/"


class TestStoreManagerLogin:
    """
    Portal > Functional Tests > Login > Store Manager.
    """

    def test_store_manager_can_login_to_viana_portal_ORC_T17(
        self, init_webdriver
    ):
        """
        Objective: User should be able to login if both username and password are valid.

        Given the user is on the login page
        When the user enters a valid username and password
        And the user clicks on the "Log In" button
        Then the user should login successfully
        """
        # Given the user is on the login page
        driver: webdriver.Chrome = init_webdriver
        wait = WebDriverWait(driver, timeout=6)
        driver.get("https://staging.portal.internal.viana.ai/")
        # When the user enters a valid username and password
        username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')

        username_field.send_keys("grace+sbux@meldcx.com")
        password_field.send_keys("Qwertyuiop18$")

        # And the user clicks on the "Log In" button
        login_button = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        login_button.click()

        wait.until(EC.url_contains("/dashboard"))
        wait.until(EC.title_contains("Dashboard"))
        # Then the user should login successfully
        assert "Dashboard" in driver.title
        assert "/dashboard" in driver.current_url
