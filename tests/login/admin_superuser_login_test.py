from lib2to3.pgen2.token import EQUAL
from re import T
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://staging.portal.internal.viana.ai/"


class TestAdminSuperuserLogin:
    """
    Portal > Functional Tests > Login > Admin Superuser.
    """

    def test_admin_superuser_can_login_to_viana_portal_ORC_T8(
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
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://staging.portal.internal.viana.ai/")
        # When the user enters a valid username and password
        username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')

        username_field.send_keys("chinny+staging@meldcx.com")
        password_field.send_keys("Chinny@1819")
        # And the user clicks on the "Log In" button
        login_button = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        login_button.click()

        wait.until(EC.url_contains("/dashboard"))
        wait.until(EC.title_contains("Dashboard"))
        wait.until(
            EC.visibility_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="root"]/div[2]/div/main/div/div/div[2]/div/div[1]/div/h1',
                )
            )
        )

        # Then the user should login successfully
        assert "Dashboard" in driver.title
        assert "/dashboard" in driver.current_url

        page_greeting = driver.find_elements(
            By.XPATH,
            '//*[@id="root"]/div[2]/div/main/div/div/div[2]/div/div[1]/div/h1',
        )
        assert page_greeting is not None
