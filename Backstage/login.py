from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys
class LoginCase(unittest.TestCase):
    def SetUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://yun.gnway.com/admin")

    def login(self, driver, username,password):
        driver.get("http://yun.gnway.com/admin")
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('username').send_keys(Keys.TAB)
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_xpath('//div[contains(text(),"登 录")]').click()

    def test_login_success(self):
        username = "hdlagent"
        password = "GNway123456"
        #self.login(self.driver,username,password)
        print('dfs')
    def test_login_pwd_error(self):
        self.login(self.driver,'hdlagent','123456')
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('password').clear()

    def test_login_pwd_null(self):
        self.Login('hdlagent','')
        self.driver.find_element_by_name('username').clear()

    def test_login_user_error(self):
        self.Login('hdhh','GNway123456')
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('password').clear()

    def test_login_user_null(self):
        self.Login('','GNway123456')
        self.driver.find_element_by_name('password').clear()

    def testDown(self):
        sleep(2)
        print('测试完成')
        self.driver.quit()
        



if __name__ == '__main__':
    unittest.main()
