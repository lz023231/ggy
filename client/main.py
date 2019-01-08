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
        while True:
            e = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").is_displayed()
            if e == False:
                self.driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
            else:
                break
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
    def addTime(self):
        try:
            #self.driver.find_element_by_xpath("//a[contains(text(),'加时间')]").click()
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'加时间')]")))
            element.click()
        except:
            print('添加时间出错')
    def editUser(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[cintains(text(),'编辑')]")))
            element.click()
        except:
            print("点击编辑按钮出错")
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
        num = self.driver.find_element_by_xpath("//table/*/tr[5]/td[5]/div[@class='tdhidden']").get_attribute("title")
        num = int(num)
        print(num)
        self.selectHost()
        time.sleep(1)
        self.addUser()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'请设置正确的登陆用户数')]").is_displayed()
        except:
            print('没有出现提示:请设置正确的登录用户数（添加数为0）')
        else:
            print('出现提示：请设置正确的登录用户数（添加数为0）')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(1)
        self.addUser()
        time.sleep(1)
        self.driver.find_element_by_name('maxonlinenum').clear()
        time.sleep(1)
        self.driver.find_element_by_name('maxonlinenum').send_keys(1)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print('没有出现提示：此次操作扣费（添加数为1）')
        else:
            print('出现提示：添加数为1')
        self.driver.find_element_by_xpath("//input[@value='取消']"). click()
        time.sleep(2)
        self.addUser()
        time.sleep(1)
        self.driver.find_element_by_name('maxonlinenum').clear()
        time.sleep(1)
        self.driver.find_element_by_name('maxonlinenum').send_keys(1)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print('没有出现提示：此次操作扣费（添加数为1）')
        else:
            print('出现提示：此次操作扣费（添加数为1）')
        time.sleep(3)
        #self.driver.find_element_by_xpath("//input[@value='确定']").click()
        time.sleep(3)
        num2 = self.driver.find_element_by_xpath("//table/*/tr[5]/td[5]/div[@class='tdhidden']").get_attribute("title")
        num2 = int(num2)
        print(num2)
        if num + 1 == num2:
            print('添加用户成功')
        else:
            print('添加用户失败')
    def test_4_addTime(self):
        self.clickUser()
        time.sleep(1)
        date = self.driver.find_element_by_xpath("//table/*/tr[5]/td[9]/div[@class='tdhidden']").get_attribute("title")
        d1 = datetime.datetime.strptime(date,'%Y-%m-%d')
        self.selectHost()
        time.sleep(1)
        self.addTime()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(1)
        self.addTime()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'结束日期不合法,无法计算增加的时间')]").is_displayed()
        except:
            print('没有出现提示：增加x个月')
        else:
            print('出现提示：增加x个月')
        self.driver.find_element_by_id("FastSelect").click()
        time.sleep(2)
        try:
            s = Select(self.driver.find_element_by_id("FastSelect"))
            s.select_by_value("1")
            time.sleep(3)
        except:
            print("没有出现下拉框")
        self.driver.find_element_by_xpath("//input[@value='确定']").click()
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print("没有出现提示：此次操作扣费（增加一个月时）")
        else:
            print("出现提示：此次操作扣费（增加一个月时）")
        self.driver.find_element_by_xpath("//input[@value='确定']").click()
        time.sleep(3)
        date2 = self.driver.find_element_by_xpath("//table/*/tr[5]/td[9]/div[@class='tdhidden']").get_attribute("title")
        d3 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        m = round((d3 - d1).days/30)
        if  m == 1:
            print("增加时间成功")
        else:
            print("增加时间失败")
    def test_5_editUser(self):
        self.clickUser()
        time.sleep(1)
        self.selectHost()
        time.sleep(1)
        self.editUser()
        time.sleep(1)



    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()