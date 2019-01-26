import datetime
from Backstage.Login.gyyLogin import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
    def pubApp(self):
        #t = self.driver.find_element_by_id("btnIssueApp").is_selected()
        #while t == False:
        try:
            #检查发布应用按钮是否为可见并且是可点击的
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.ID,"btnIssueApp")))
            element.click()
            time.sleep(2)

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
    def findHost(self):
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)

    def selectHost(self):
        while True:
            try:
                #查看value=12879的单选框是否出现
                e = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").is_displayed()
                #print("1111")
                print(e)
            except:
                e = False
                #print("2222")
                print(e)
            if e == False:
                #如果没有出现，则点击后一页，循环查找
                self.findHost()
                time.sleep(2)
                self.driver.find_element_by_xpath("//a[contains(text(),'后一页')]").click()

            else:
                break
        #查看value=12879的单选框是否被选中
        t = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").is_selected()
        print(t)

        #如果没有选中则点击单选框，如果选中退出循环
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
            print('点击添加时间按钮出错')
    def editUser(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'编辑')]")))
            element.click()
        except:
            print("点击编辑按钮出错")
    def reduceUser(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'更多')]")))
            element.click()
        except:
            print("点击更多按钮出错")
    def details(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'详情')]")))
            element.click()
            time.sleep(2)
        except:
            print("点击详情按钮出错")
    def test_1_client(self):
        #path1='//a[contains(text(),"客户")]'
        #self.driver.find_element_by_xpath('//a[contains(text(),"客户")]').click()
        self.clickUser()
        time.sleep(2)
    def test_2_showClient(self):
        print('---------------------------发布应用------------------------------')
        #path = '//a[contains(text(),"显示更多")]'
        #点击显示更多按钮
        self.driver.find_element_by_xpath("//a[contains(text(),'添加客户')]/following-sibling::a[contains(text(),'显示更多')]").click()
        time.sleep(2)
        #发布应用
        #self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").click()
        self.selectHost()
        time.sleep(2)
        self.pubApp()
        time.sleep(2)
        #self.driver.find_element_by_xpath("//a[contains(text(),'发布应用')]").click()
        #查看cmd应用是否被选中
        t = self.driver.find_element_by_xpath("//input[@value='4']").is_selected()
        print("ew")
        print(t)
        #确认cmd处于没被选中状态
        while t == True:
            try:
                print("--------")
                element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'cmd')]")))
                element.click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//input[@value='确定']").click()
                time.sleep(3)
                self.selectHost()
                time.sleep(2)
                self.pubApp()
                time.sleep(2)
                print("------")
                break
            except:
                print("应用为未点击状态")

         #点击取消按钮，查看应用是否被发布
        self.driver.find_element_by_xpath("//label[contains(text(),'cmd')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(2)
        self.pubApp()
        h = self.driver.find_element_by_xpath("//input[@value='4']").is_selected()
        if h == True:
            print("点击取消，应用依然被发布")
        else:
            print("点击取消，应用没有被发布")

        self.driver.find_element_by_xpath("//label[contains(text(),'cmd')]").click()
        time.sleep(2)
        #self.driver.find_element_by_xpath("//a")
        self.driver.find_element_by_xpath("//input[@value='确定']").click()
        time.sleep(2)
        #self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']").click()
        self.selectHost()
        time.sleep(2)
        self.pubApp()
        time.sleep(2)
        e = self.driver.find_element_by_xpath("//input[@value='4']").is_selected()
        print("---")
        print(e)
        if e == False:
            print("发布应用失败")
        else:
            print("发布应用成功")
        #self.driver.find_element_by_xpath("//input[@value='取消']").cleck()

        #加用户
    def test_3_addUserS(self):
        print('---------------------------添加用户------------------------------')







        self.clickUser()
        time.sleep(2)
        self.selectHost()
        #获取目前允许登录用户数
        num = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[4]/div[@class='tdhidden']").get_attribute("title")
        num = int(num)
        print(num)
        time.sleep(2)

        #直接点击确定，不输入用户数，查看是否有提示
        self.addUser()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'请设置正确的登陆用户数')]").is_displayed()
        except:
            print('没有出现提示:请设置正确的登录用户数（添加数为0）')
        else:
            print('出现提示：请设置正确的登录用户数（添加数为0）')
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(2)

        #向新增用户数框中输入1，点击确认
        self.addUser()
        time.sleep(2)
        self.driver.find_element_by_name('maxonlinenum').clear()
        time.sleep(2)
        self.driver.find_element_by_name('maxonlinenum').send_keys(1)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(3)
        #查看是否出现提示
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print('没有出现提示：此次操作扣费（添加数为1）')
        else:
            print('出现提示：添加数为1')
        self.driver.find_element_by_xpath("//input[@value='取消']"). click()
        time.sleep(2)

        #再次获取允许登录数，查看点击取消时，添加用户是否成功
        num1 = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[4]/div[@class='tdhidden']").get_attribute("title")
        num1 = int(num1)
        if  num + 1 == num1:
            print("错误：点击取消按钮，添加用户成功")
        else:
            print("点击取消按钮，添加用户失败")

        #点击确认按钮，查看添加用户数是否成功
        self.addUser()
        time.sleep(2)
        self.driver.find_element_by_name('maxonlinenum').clear()
        time.sleep(2)
        self.driver.find_element_by_name('maxonlinenum').send_keys(1)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print('没有出现提示：此次操作扣费（添加数为1）')
        else:
            print('出现提示：此次操作扣费（添加数为1）')
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@value='确定']").click()
        time.sleep(3)
        num2 = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[4]/div[@class='tdhidden']").get_attribute("title")
        num2 = int(num2)
        print(num2)
        if num + 1 == num2:
            print('添加用户成功')
        else:
            print('添加用户失败')
    def test_4_addTime(self):
        print("---------------------------增加时间------------------------------")
        self.clickUser()
        time.sleep(2)
        self.selectHost()

        #获取到期时间，并将数据格式化
        date = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[8]/div[@class='tdhidden']").get_attribute("title")
        d1 = datetime.datetime.strptime(date,'%Y-%m-%d')
        time.sleep(2)
        self.addTime()

        #确认是否能正常取消
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(2)

        #点击确认按钮，查看是否出现提示
        self.addTime()
        time.sleep(2)
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

        #导入Select模块，选择下拉框里值为1的选项
        try:
            s = Select(self.driver.find_element_by_id("FastSelect"))
            s.select_by_value("1")
            time.sleep(3)
        except:
            print("没有出现下拉框")

        #点击确定，查看是否出现提示
        self.driver.find_element_by_xpath("//input[@value='确定']").click()
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'此次操作扣费')]").is_displayed()
        except:
            print("没有出现提示：此次操作扣费（增加一个月时）")
        else:
            print("出现提示：此次操作扣费（增加一个月时）")


        #再次点击确定，查看是否添加成功
        self.driver.find_element_by_xpath("//input[@value='确定']").click()
        time.sleep(3)
        date2 = self.driver.find_element_by_xpath("//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[8]/div[@class='tdhidden']").get_attribute("title")
        d3 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        m = round((d3 - d1).days/30)
        if  m == 1:
            print("增加时间成功")
        else:
            print("增加时间失败")
    def test_5_editUser(self):
        print('---------------------------编辑用户和对比详情------------------------------')
        global i
        self.clickUser()
        time.sleep(2)
        self.selectHost()
        time.sleep(2)
        self.editUser()
        time.sleep(2)

        #查看编辑里原本是否出现编辑界面
        try:
            self.driver.find_element_by_xpath("//input[@value='testzzl01.yun.gnway.com']").is_displayed()
            self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").is_displayed()
            self.driver.find_element_by_xpath("//input[@value='testzzl01']").is_displayed()
        except:
            print('没有出现编辑界面')
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(2)

        self.editUser()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//input[@value='testzzl01.yun.gnway.com']").is_displayed()
            self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").is_displayed()
            self.driver.find_element_by_xpath("//input[@value='testzzl01']").is_displayed()
        except:
            print("没有出现编辑界面（第二次）")

        #在域名后面添加一个字母P，查看是否出现提示
        self.driver.find_element_by_xpath("//input[@value='testzzl01.yun.gnway.com']").send_keys('p')
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").click()
        time.sleep(2)
        try:
            t = self.driver.find_element_by_id("domainauto-error").text
            print(t)
            if t == "请检查该域名是否拼写错误testzzl01.yun.gnway.comp":
                print("出现提示：请检查该域名是否拼写错误testzzl01.yun.gnway.comp")
            else:
                return 0
        except:
            print("没有出现提示：请检查该域名是否拼写错误testzzl01.yun.gnway.comp")

        #去掉字母P
        self.driver.find_element_by_xpath("//input[@value='testzzl01.yun.gnway.com']").send_keys(Keys.BACK_SPACE)
        time.sleep(2)

        #获取公司名称，并在添加后进行比较，查看是否添加成功
        try:
            text1 = text2 = self.driver.find_element_by_xpath(
            "//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[3]/div[@class='tdhidden']").get_attribute(
            "title")
            self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").send_keys("01")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@value='确认']").click()
            time.sleep(3)
            self.driver.refresh()
            time.sleep(2)
            #根据父元素的兄弟元素定位
            text2 = self.driver.find_element_by_xpath(
            "//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[3]/div[@class='tdhidden']").get_attribute(
            "title")
            time.sleep(2)
            if text2 == text1 + '01':
                print("修改成功")
        except:
            print("修改公司名称失败")
        self.selectHost()
        time.sleep(2)
        self.editUser()
        time.sleep(2)
        ch = self.driver.find_element_by_xpath("//input[@name='username']").is_enabled()
        if ch == True:
            print("error:管理员账户可以修改")
        else:
            print("管理员账户为不可修改状态")

        #将公司名称改回cehsi
        self.driver.find_element_by_xpath("//input[@placeholder='填写联系人']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='备注']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").clear()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='设置用户公司名称']").send_keys("ceshi")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.selectHost()
        time.sleep(2)
        self.editUser()
        time.sleep(2)

        #编辑备注和联系人
        while True:
            try:
                self.driver.find_element_by_xpath("//input[@placeholder='备注']").clear()
                time.sleep(1)
                self.driver.find_element_by_xpath("//input[@placeholder='备注']").send_keys("test")
                self.driver.find_element_by_xpath("//input[@placeholder='填写联系人']").clear()
                time.sleep(1)
                self.driver.find_element_by_xpath("//input[@placeholder='填写联系人']").send_keys("test")
                time.sleep(2)
                self.driver.find_element_by_xpath("//input[@value='确认']").click()
                time.sleep(3)
                i = 0
            except:
                print("编辑备注失败")
            #查看编辑的内容在详情里是否显示正确

            if i == 0:
                self.details()
                note = self.driver.find_element_by_xpath("//td[contains(text(),'备注')]/following-sibling::td[1]").text
                cont = self.driver.find_element_by_xpath("//td[contains(text(),'联系人')]/following-sibling::td[1]").text
                if note == "test" and cont == "test":
                    print("详情显示正确")
                else:
                    print("详情显示错误")
            else:
                print("编辑备注时失败")
            break

    def test_6_reduceUser(self):
        print("--------------------------------减用户-----------------------------------")
        self.clickUser()
        time.sleep(2)
        self.selectHost()
        time.sleep(2)

        #获取用户数
        num = self.driver.find_element_by_xpath(
            "//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[4]/div[@class='tdhidden']").get_attribute(
            "title")
        print('---')
        num = int(num)
        print(num)
        print('----')
        self.reduceUser()
        time.sleep(2)
        #while True:

        #查看是否出现二级菜单
        result = self.driver.find_element_by_xpath("//a[contains(text(),'减用户')]").is_displayed()
        if result == True:
            print("出现二级菜单")

            #点击减用户
            self.driver.find_element_by_xpath("//a[contains(text(),'减用户')]").click()
            time.sleep(2)
            #查看是否出现输入框
            res =  self.driver.find_element_by_xpath("//input[@placeholder='减少用户数']").is_displayed()
            if res == True:
                self.driver.find_element_by_xpath("//input[@value='取消']").click()
                time.sleep(2)
            else:
                return 0
            self.reduceUser()
            time.sleep(2)
            self.driver.find_element_by_xpath("//a[contains(text(),'减用户')]").click()
            time.sleep(2)

            #减用户数为0，查看是否出现提示
            self.driver.find_element_by_xpath("//input[@value='确认']").click()
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath("//div[contains(text(),'减少的人数不能为0或者负数!')]").is_displayed()
            except:
                print("减用户数为0是没有出现提示")



            self.driver.find_element_by_xpath("//input[@value='取消']").click()
            time.sleep(2)
            self.reduceUser()
            time.sleep(2)
            self.driver.find_element_by_xpath("//a[contains(text(),'减用户')]").click()
            time.sleep(2)

            #向输入框中输入1，点击确定，并查看是否出现提示
            self.driver.find_element_by_xpath("//input[@placeholder='减少用户数']").clear()
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@placeholder='减少用户数']").send_keys("1")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@value='确认']").click()
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath("//div[@id='formerror']").is_displayed()
            except:
                print("没有出现提示（减掉一个用户时）")
            self.driver.find_element_by_xpath("//input[@value='确定']").click()
            time.sleep(3)
            self.driver.refresh()
            time.sleep(2)

            #查看减用户是否成功
            num2 = self.driver.find_element_by_xpath(
            "//table/*/tr/td/div/input[@value='12879']/../../following-sibling::td[4]/div[@class='tdhidden']").get_attribute(
            "title")
            num2 = int(num2)
            if num2 == num:
                print("减用户成功")
            else:
                print("减用户失败")
        else:
            print("没有出现二级菜单")



    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()