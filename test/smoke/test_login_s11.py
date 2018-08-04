import unittest
from selenium.webdriver import Chrome
from lib.ui.loginpage import LoginPage

class TestLoginS11P1(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome(r'C:\Users\Elcot\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://demo.actitime.com")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_invalid_tc1(self):
        #Go to login page
        self.login_page.wait_for_login_page_to_load()
        #Enter username
        self.login_page.get_username_textbox().send_keys("admin")
        #Enter password
        self.login_page.get_password_textbox().send_keys("invalid")
        #Click on login button
        self.login_page.get_login_button().click()
        #Get error message
        actual_error_msg = self.login_page.get_login_error_msg().text
        expected_error_msg = "Username or Password is invalid.. Please try again"
        #Verify error message
        assert actual_error_msg == expected_error_msg