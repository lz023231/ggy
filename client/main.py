from client.clientPage import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
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
        try:
            #检查发布应用按钮是否为可见并且是可点击的
            #self.driver.find_element_by_xpath("//a[contains(text(),'发布应用')]").click()
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.ID,"btnIssueApp")))
            #WebDriverWait(self.driver,10).until(lambda x: x)
            element.click()
        except:
            print('发布应用出错')
    def addUser(self):
        try:
            #self.driver.find_element_by_xpath("//a[contains(text(),'加用户')]").click()
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'加用户')]")))
            element.click()
        except:
            print('添加用户出错')
    def clickUser(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'客户')]")))
            element.click()
            #self.driver.find_element_by_xpath('//a[contains(text(),"客户")]').click()
        except:
            print('跳转到客户界面出错')
    def selectHost(self):
        t = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").is_selected()
        print(t)
        while t == False:
            try:
                element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//table/*/tr/td/div/input[@value='12879']")))
                element.click()
                if t == True:
                    return
                break
            except:
                print('选择主机失败')
    '''
        if t == False:
            #try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//table/*/tr/td/div/input[@value='12879']")))
            element.click()
            print('--------')
            #except:
                #print('选择主机失败')
        else:
            print('主机已经选上')
    '''
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
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'请设置正确的登陆用户数')]").is_displayed()
        except:
            print('没有出现提示')
        else:
            print('出现提示')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        self.addUser()
        self.driver.find_element_by_name('maxonlinenum').clear()
        self.driver.find_element_by_name('maxonlinenum').send_keys(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print('没有出现提示')
        else:
            print('出现提示')
        self.driver.find_element_by_xpath("//input[@value='取消']"). click()
        self.addUser()
        self.driver.find_element_by_name('maxonlinenum').clear()
        self.driver.find_element_by_name('maxonlinenum').send_keys(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print('没有出现提示')
        else:
            print('出现提示')
        time.sleep(3)

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()