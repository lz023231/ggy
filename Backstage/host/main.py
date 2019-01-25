import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from Backstage.Login.gyyLogin import *
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
        #拖动滚动条到最下面
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
    def selectHost(self):
        while True:
            try:
                #查看当前页面是否出现value=959的用户，如果没有出现，点击下一页，循环寻找
                e = self.driver.find_element_by_xpath("//input[@value='959']").is_displayed()
                print(e)
            except:
                e = False
                print(e)
            if e == False:
                #点击后一页
                self.findHost()
                time.sleep(2)
                self.driver.find_element_by_xpath("//a[contains(text(),'后一页')]").click()
            else:
                break
        #判断是否被勾选时是，如果被勾选上，退出循环，没有勾选上，则勾选上
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
        #点击主机按钮
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'主机')]")))
            element.click()
        except:
            print("点击主机按钮失败")

    def addCustomer(self):
        #点击增加客户按钮
        print("---------------------------增加客户------------------------------")
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'增加客户')]")))
            element.click()
        except:
            print("没有找到增加客户按钮")
    #def findHost(self):

    def userList(self):
        #选择主机之后，点击客户列表
        try:
            url = self.driver.current_url
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='btnListCustom']")))
            element.click()
            time.sleep(2)
            new_url = self.driver.current_url
            #e = WebDriverWait(self.driver,10,1).until(EC.ur)
            if url == new_url:
                print('进入客户列表失败')

        except:
            print("点击客户列表失败")
    def editHost(self):
        try:
            self.driver.find_element_by_xpath("//*[@id='btnEditHost']").is_displayed()
            self.driver.find_element_by_xpath("//*[@id='btnEditHost']").click()
            q = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,'//input[@value="取消"]')))
            if q == True:
                return

        except:
            print('点击主机失败')


    def test_1_addCus(self):
        self.clickHost()
        time.sleep(2)
        self.selectHost()
        time.sleep(1)
        #self.userList()
        #time.sleep(2)



        self.addCustomer()
        time.sleep(2)
        t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        y = t.split("-")
        k = '{}{}{}{}{}'.format('ceshi',y[1],y[2],y[3],y[4])
        h = '{}{}{}{}{}{}'.format('ceshi',y[1],y[2],y[3],y[4],'.yun.gnway.com')
        print(k)
        #查看是否出现二级菜单
        try:
            self.driver.find_element_by_xpath("//input[@value='确认']").is_displayed()
        except:
            print("没有出现增加客户的二级菜单")

        #什么都不添加时，查看是否有提示
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//*[@id='domainauto-error']").is_displayed()
        except:
            print("增加用户时什么都不写，没有出现提示")
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(2)
        self.addCustomer()
        time.sleep(2)

        #填写信息
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户访问域名 例如:xxx.yun.gnway.com']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户访问域名 例如:xxx.yun.gnway.com']").send_keys(h)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='设置登录云平台的管理账户']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='设置登录云平台的管理账户']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='password']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_name('contact').clear()
        time.sleep(1)
        self.driver.find_element_by_name('contact').send_keys("gnwaytest")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='备注']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='备注']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(3)

        #查看添加用户后界面是否正常
        try:
            self.driver.find_element_by_xpath("//input[@placeholder='设置登录云平台的管理账户']").is_displayed()

            print("添加用户后，添加用户界面依然存在")
        except:
            print("添加完成后界面正常")

        #在用户列表查看是否添加成功
        self.selectHost()
        time.sleep(1)
        self.userList()
        time.sleep(2)
        try:
            #compo = WebDriverWait(self.driver,10,1).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='customlist']/tbody/tr[1]/td[2]/div[@title='1']/../following-sibling::td[2]/div[@class='tdhidden']")))
            comp = self.driver.find_element_by_xpath("//*[@id='customlist']/tbody/tr[1]/td[2]/div[@title='1']/../following-sibling::td[2]/div[@class='tdhidden']").text
            if comp == k:
                print("添加客户成功")
        except:
            print("添加客户失败")



    def test_2_editHost(self):
        self.clickHost()
        time.sleep(2)
        self.selectHost()
        time.sleep(2)
        self.editHost()
        time.sleep(2)
        try:
            textIP = self.driver.find_element_by_xpath('//*[@id="addhostform"]/div/div[1]/div/input').get_attribute('value')
            print(type(textIP))
            textPort = self.driver.find_element_by_xpath('//*[@id="addhostform"]/div/div[2]/div/input').get_attribute('value')
            if textIP == "221.221.138.254" and textPort == "2251":
                print("编辑成功")
        except:
            print("编辑主机失败")





    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()