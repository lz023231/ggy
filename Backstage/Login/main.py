from Backstage.Login.gyyLogin import *
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
        try:
            self.driver.find_element_by_xpath("//strong[contains(text(),'您输入的账号或密码有错误，请确认后重试！')]")
        except:
            print("密码错误时没有出现提示")

    def test_2_login_pwd_null(self):
        url = self.driver.current_url
        username = 'hdlagent'
        password = ''
        time.sleep(3)
        Login().login(self.driver,username,password)
        time.sleep(2)
        url1 = self.driver.current_url
        if url != url1:
            print("不输入密码时登录出现错误，url产生变化")


    def test_3_login_user_error(self):
        username = '123456'
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver,username,password)
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//strong[contains(text(),'您输入的账号或密码有错误，请确认后重试！')]").is_displayed()
        except:
            print("用户名错误时，没有出现提示")


    def test_4_login_user_null(self):
        url2 = self.driver.current_url
        username = ''
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver,username,password)
        time.sleep(2)
        url3 = self.driver.current_url
        if url2 != url3:
            print("不输入用户名时登录出现错误，url产生变化")


    def test_5_login_seccess(self):
        username = 'hdlagent'
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
        url4 = self.driver.current_url
        if url4 != "https://yun.gnway.com/index/index":
            print("用户名和密码都正确时，登录错误")
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()