from client.clientPage import *
import time
import unittest
from selenium import webdriver
class ClientTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://yun.gnway.com/admin")
        username = 'hdlagent'
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
    def test_1_client(self):
        #path1='//a[contains(text(),"客户")]'
        self.driver.find_element_by_xpath('//a[contains(text(),"客户")]').click()
        time.sleep(2)
    def test_2_showClient(self):
        #path = '//a[contains(text(),"显示更多")]'
        self.driver.find_element_by_xpath('//a[contains(text(),"显示更多")]').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()