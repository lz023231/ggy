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
    def pubApp(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'发布应用')]").click()
    def addUser(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'加用户')]").click()
    def clickUser(self):
        self.driver.find_element_by_xpath('//a[contains(text(),"客户")]').click()
    def selectHost(self):
        self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").click()
    def test_1_client(self):
        #path1='//a[contains(text(),"客户")]'
        #self.driver.find_element_by_xpath('//a[contains(text(),"客户")]').click()
        self.clickUser()
        time.sleep(1)
    def test_2_showClient(self):
        #path = '//a[contains(text(),"显示更多")]'
        self.driver.find_element_by_xpath("//a[contains(text(),'添加客户')]/following-sibling::a[contains(text(),'显示更多')]").click()
        time.sleep(1)
        #发布应用
        #self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").click()
        self.selectHost()
        time.sleep(1)
        self.pubApp()
        #self.driver.find_element_by_xpath("//a[contains(text(),'发布应用')]").click()
        self.driver.find_element_by_xpath("//label[contains(text(),'cmd')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(1)
        self.pubApp()
        self.driver.find_element_by_xpath("//label[contains(text(),'cmd')]").click()
        #self.driver.find_element_by_xpath("//a")
        self.driver.find_element_by_xpath("//input[@value='确定']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").click()
        time.sleep(1)
        self.pubApp()
        time.sleep(1)
        #self.driver.find_element_by_xpath("//input[@value='取消']").cleck()

        #加用户
    def test_3_addUserS(self):
        self.clickUser()
        self.selectHost()
        self.addUser()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        self.addUser()
        self.driver.find_element_by_name('maxonlinenum').clear()
        self.driver.find_element_by_name('maxonlinenum').send_keys(1)
        time.sleep(3)

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
        print('test')
if __name__ == '__main__':
    unittest.main()