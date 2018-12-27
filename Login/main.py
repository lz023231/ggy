from Login.gyyLogin import *
import unittest
from selenium import webdriver
import time


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://yun.gnway.com/admin")

    def test_1_login_pwd_error(self):
        username = 'hdlagent'
        password = '123456'
        time.sleep(3)
        Login().login(self.driver,username,password)
        time.sleep(2)

    def test_2_login_pwd_null(self):
        username = 'hdlagent'
        password = ''
        time.sleep(3)
        Login().login(self.driver,username,password)
        time.sleep(2)

    def test_3_login_user_error(self):
        username = '123456'
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver,username,password)
        time.sleep(2)

    def test_4_login_user_null(self):
        username = ''
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver,username,password)
        time.sleep(2)
    def test_5_login_seccess(self):
        username = 'hdlagent'
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()