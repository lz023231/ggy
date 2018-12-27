from selenium.webdriver.common.keys import Keys
from Login.gyyLogin import *
from selenium import webdriver
class ClientPage():
    def client(self, path):
        self.driver = webdriver.Chrome()
        self.driver.get('http://yun.gnway.com/admin')
        Login.login(self.driver, 'hdlagent', 'GNway123456')
        self.driver.find_element_by_xpath(path).click()
