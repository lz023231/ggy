from client.clientPage import *
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium import webdriver
'''
修改管理员密码的功能计划和管理员登录一起
'''
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
    def findHost(self):
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
    def selectHost(self):
        while True:
            try:
                e = self.driver.find_element_by_xpath("//input[@value='959']").is_displayed()
                print("---")
                print(e)
            except:
                e = False
                print("----")
                print(e)
            if e == False:

                self.findHost()
                time.sleep(2)
                self.driver.find_element_by_xpath("//a[contains(text(),'后一页')]").click()
            else:
                break

        t = self.driver.find_element_by_xpath("//input[@value='959']").is_selected()
        while t == False:
            try:
                element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//input[@value='959']")))
                element.click()
                if t == True:
                    return
                break
            except:
                print("选择主机失败")

    def clickHost(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'主机')]")))
            element.click()
        except:
            print("点击主机按钮失败")

    def addCustomer(self):
        print("---------------------------增加客户------------------------------")
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'增加客户')]")))
            element.click()
        except:
            print("没有找到增加客户按钮")
    #def findHost(self):


    def test_1_addCus(self):
        self.clickHost()
        time.sleep(2)
        self.selectHost()
        time.sleep(1)
        self.addCustomer()
        time.sleep(2)
        t = datetime.datetime.now().strftime('%Y-%m-%d')
        y = t.split("-")
        k = '{}{}{}'.format('ceshi',y[1],y[2])
        h = '{}{}{}{}'.format('ceshi',y[1],y[2],'.yun.gnway.com')
        print(k)
        try:
            self.driver.find_element_by_xpath("//input[@value='确认']").is_displayed()
        except:
            print("没有出现增加客户的二级菜单")
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户访问域名 例如:xxx.yun.gnway.com']").send_keys(h)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").send_keys("gnway")
        time.sleep(1)
        #self.driver.find_element_by_xpath("//input[@placeholder='设置登录云平台的管理账户']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_name('contact').send_keys("gnwaytest")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='备注']").send_keys(k)












    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()