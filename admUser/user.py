from Backstage.Login.gyyLogin import *
import time
import datetime ,sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from pykeyboard import PyKeyboard
import os
from selenium.webdriver.common.action_chains import ActionChains


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://testzzl01.yun.gnway.com")
        username = 'testzzl01'
        password = 'testzzl01'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)

    #判断重复登录按钮
    def judge_repeat_login(self):
        #判断单选框是否勾选
        y = self.driver.find_element_by_xpath("//input[@name='repeatlogin']").is_selected()
        #如果被选上，查看是否出现下面的输入框
        if y == True:
            r = self.driver.find_element_by_xpath("//input[@placeholder='0-2040，默认为最大']").is_displayed()
            if r == True:
                print("勾选重复登录时显示正常")
            else:
                print("勾选重复登录时显示不正常")
        else:
            print("-----------")
            try:
                #查看没有勾选时，是否出现输入框
                self.driver.find_element_by_xpath("//input[@placeholder='0-2040，默认为最大']").is_displayed()
                print("没有勾选时显示错误")
            except:
                print("没有勾选时显示正确")
    def changePasswd(self):
        try:
            #等待修改密码框的出现，查看是否出现并且可以点击
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'修改密码')]")))
            element.click()
            #查看是否出现二级菜单
            self.driver.find_element_by_xpath("//strong[contains(text(),'旧密码')]").is_displayed()
        except:
            print("点击修改密码失败或没有出现二级菜单")


    def addUser(self):
        try:
            #等待添加用户按钮出现，并且查看是否可以点击
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'添加普通用户')]")))
            element.click()
        except:
            print("点击添加普通用户失败")

    def editUser(self):
        try:
            #等待编辑用户按钮出现
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'编辑用户')]")))
            element.click()
        except:
            print("点击编辑用户失败")


    def generalChangePasswd(self):
        try:
            #点击修改密码按钮
            self.driver.find_element_by_xpath("//span[contains(text(),'修改密码')]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='editpassword']").is_displayed()
        except:
            print("没有出现修改密码界面")



    def findUser(self):
        #将滚动条滑至最下方
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
    def selectUser(self):
        while True:
            try:
                #判断第一个用户前的单选框是否出现
                e = self.driver.find_element_by_xpath("//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']").is_displayed()
                print("---")
                print(e)
                break
            except:
                e = False

                print("第一分用户前没有勾选框")
                print(e)
                break
        '''
            if e == False:

                self.findUser()
                time.sleep(2)
                self.driver.find_element_by_xpath("//a[contains(text(),'后一页')]").click()
            else:
                break
        '''

        #查看单选框是否被勾选上，如果没有勾选上就点击单选框
        t = self.driver.find_element_by_xpath("//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']").is_selected()
        while t == False:
            try:
                element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']")))
                element.click()
                if t == True:
                    return
                break
            except:
                print("选择用户失败")

    def test_1_deleteUser(self):
        print('--------------------------删除用户-----------------------------------')
        try:
            #选取当前页面第二个用户
            self.driver.find_element_by_xpath(
                "//div[@title=2]/../preceding-sibling::td[1]/div/input[@type='checkbox']").click()
        except:
            print("选取当前页面第二个用户失败")

        #获取第二个单选框的value值
        x = self.driver.find_element_by_xpath(
            "//div[@title=2]/../preceding-sibling::td[1]/div/input[@type='checkbox']").get_attribute('value')

        x = int(x)
        print(x)
        try:

            #点击删除用户
            self.driver.find_element_by_id("btnDeleteGroupUser").click()
            time.sleep(2)

            '''
            #a = EC.alert_is_pr//*[@id="dialog-confirm"]/pesent()(self.driver)
            #a = self.driver.switch_to.alert()
            #a.text()
            #return a
            #element = WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dialog-confirm"]/p')))
            '''

            #获取提示内容
            a = self.driver.find_element_by_xpath('//*[@id="dialog-confirm"]/p').text
            print(a)
            if a == "这些数据将被永久删除,并且无法恢复.您确定吗?":
                print("dsdfsdf")
            else:
                print("删除时没有出现提示")
            #点击取消按钮
            self.driver.find_element_by_xpath("//span[contains(text(),'取消')]").click()  #取消
            time.sleep(2)
            #刷新
            self.driver.refresh()
            time.sleep(1)

            #再次获取单选框value值
            x2 = self.driver.find_element_by_xpath(
            "//div[@title=2]/../preceding-sibling::td[1]/div/input[@type='checkbox']").get_attribute('value')
            x2 = int(x2)
            #print(x2)
            if x == x2:
                print("点击取消按钮没有被删除")
            else:
                print("点击取消按钮后用户被删除")
                return



            time.sleep(2)
            #选中第二个用户
            self.driver.find_element_by_xpath(
                "//div[@title=2]/../preceding-sibling::td[1]/div/input[@type='checkbox']").click()
            time.sleep(2)
            #点击删除按钮
            self.driver.find_element_by_id("btnDeleteGroupUser").click()
            time.sleep(2)

            #获取提示
            b = self.driver.find_element_by_xpath('//*[@id="dialog-confirm"]/p').text
            print(b)
            if b == "这些数据将被永久删除,并且无法恢复.您确定吗?":
                print("出现提示")
            else:
                print("删除时没有出现提示")

            #点击确定按钮
            self.driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
            time.sleep(2)
            self.driver.refresh()

            #获取目前的单选框value值
            x3 = self.driver.find_element_by_xpath(
            "//div[@title=2]/../preceding-sibling::td[1]/div/input[@type='checkbox']").get_attribute('value')
            x3 = int(x3)
            if x3 == x:
                print("点击确定后，用户没有被删除")
            else:
                print("删除用户成功")


        except:
            print("删除用户出错")

    def test_2_addUser(self):
        print("---------------------------添加用户-----------------------------")

        #获取第一个用户的用户名
        time.sleep(2)
        h = self.driver.find_element_by_xpath(
            "//div[@title=1]/../following-sibling::td[1]/div[@class='tdhidden']").get_attribute('title')
        print(h)

        #点击尾页
        self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
        time.sleep(3)

        #查看尾页上有几个用户（tbody下的tr标签代表一个用户）
        s = self.driver.find_elements_by_css_selector("tbody>tr")
        # print(len(s))
        l = len(s)
        #print(h)
        #self.selectUser()
        #time.sleep(2)
        self.addUser()
        print("------------")
        time.sleep(2)
        #获取当前时间并格式化
        t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        y = t.split("-")

        #整合成一个字符串作为添加用户时的用户名
        k = '{}{}{}{}{}'.format('ceshi', y[1], y[2], y[3], y[4])

        #查看是否出现添加用户的二级菜单
        try:
            self.driver.find_element_by_xpath("//input[@value='保存']").is_displayed()
        except:
            print("添加用户没有出现二级菜单")
        self.driver.find_element_by_xpath("//input[@value='保存']").click()
        time.sleep(2)


        #什么都不填写时查看是否出现提示
        try:
            self.driver.find_element_by_xpath("//label[@id='username-error']").is_displayed()
            self.driver.find_element_by_xpath("//label[@id='password-error']").is_displayed()
            self.driver.find_element_by_xpath("//label[contains(text(),'请再次输入密码')]").is_displayed()
            print("什么都不填写时出现提示")
        except:
            print("什么都不添写时，点击保存时，没有出现错误提示")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='保存']/following-sibling::input[1]").click()
        time.sleep(2)


        #添加已经存在的用户名，查看是否提示
        try:
            self.addUser()
            self.driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys(h)
            print(120)
            self.driver.find_element_by_xpath("//input[@id='password']").send_keys(h)
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[5]/input[@name='repassword']").send_keys(h)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@value='保存']").click()
            time.sleep(1)
            p =self.driver.find_element_by_xpath("//div[contains(text(),'用户名重复')]").is_displayed()
            if p == True:
                print("添加已有用户名时出现提示")
            else:
                return
        except:
            print("添加已有用户名时没有出现提示")

        #点击取消按钮
        p = self.driver.find_element_by_xpath("//input[@name='repeatlogin']").is_selected()
        if p == True:

            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[13]/input[2]").click()
        else:
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[12]/input[2]").click()
        time.sleep(1)
        self.addUser()
        time.sleep(2)

        #输入用户名、密码等信息
        self.driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[3]/input[@name='descript']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[5]/input[@name='repassword']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='contact']").send_keys(k)
        time.sleep(2)

        #检查重复登录与下面的输入框存在关系（允许重复登录时，下面有输入框）
        self.judge_repeat_login()
        self.driver.find_element_by_xpath("//input[@value='保存']").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'创建系统账号错误')]").is_displayed()
            #if l == True:
            #print("创建用户时出现错误：‘创建系统账号失败’")


        except:
            print("第一次正常")

            self.driver.refresh()
            time.sleep(2)


            self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
            time.sleep(3)
            #m1 = '{}{}{}'.format("//div[@title='", k, "']")
            #查看当前页面是否有添加的用户
            try:
                r1 = k + "']"
                n1 = self.driver.find_element_by_xpath("//div[@title='" + r1).is_displayed()
                #h =
                print(n1)
                if n1 == True:
                    print('第一次添加用户成功')
                else:
                    print("第一次添加用户失败")
            except:
                print('添加用户失败')





            '''
            s2 = self.driver.find_elements_by_css_selector("tbody>tr")
            l2 = len(s2)
            if l == l2:
                print("第一次添加用户失败")
            else:
                print("第一次添加用户成功")
            
            j = self.driver.find_element_by_xpath(
                "//div[@title=1]/../following-sibling::td[1]/div[@class='tdhidden']").get_attribute('title')
            if h == j:
                print("第一次添加用户成功")
            else:
                print("第一次添加用户失败")
            '''


            #self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
            self.driver.refresh()
            time.sleep(2)
            #s3 = self.driver.find_elements_by_css_selector("tbody>tr")
            #l3 = len(s3)
            self.addUser()
            time.sleep(2)

            #查看是否出现二级菜单
            try:
                self.driver.find_element_by_xpath("//input[@value='保存']").is_displayed()
            except:
                print("添加用户没有出现二级菜单")

            #添加用户时两次密码输入不一致
            self.driver.find_element_by_xpath("//input[@name='repeatlogin']").click()

            self.driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys(k + '1')
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[3]/input[@name='descript']").send_keys(k + '1')
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='password']").send_keys(k + '1')
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[5]/input[@name='repassword']").send_keys(k + '2')
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='contact']").send_keys(k + '1')
            time.sleep(2)
            #self.judge_repeat_login()
            #self.driver.find_element_by_xpath("//input[value='保存']").click()
            #print("-------------")
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath("//label[contains(text(),'两次密码输入不一致')]").is_displayed()
            except:
                print("两次密码不一致时没有出现提示")
            self.driver.find_element_by_xpath("//input[@placeholder='确认密码']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@placeholder='确认密码']").send_keys(k + '1')
            time.sleep(1)

            #点击重复登录按钮
            #self.driver.find_element_by_xpath("//input[@name='repeatlogin']").click()
            time.sleep(3)
            self.judge_repeat_login()
            time.sleep(3)
            #点击保存按钮
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[12]/input[1]").click()
            time.sleep(2)
            try:

                self.driver.find_element_by_xpath("//div[contains(text(),'创建系统账号错误')]").is_displayed()
                #if l1 == True:
                #print("创建用户时出现错误：‘创建系统账号失败’")
                #os._exit()
                #exit()

            except:
                print("第二次正常")

                self.driver.refresh()
                self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
                time.sleep(3)
                try:
                    z = k + "1"
                    r = z + "']"
                    #查看当前页面是否出现添加的用户：通过xpath路径定位
                    print(110)
                    n = self.driver.find_element_by_xpath("//div[@title='" + r).is_displayed()
                    #n = self.driver.find_element_by_xpath("//div[@title='" + r).is_displayed()
                    print(120)
                    if n == True:
                        print('第二次添加用户成功')
                    else:
                        print("第二次添加用户失败")
                except:
                    print("检查第二次用户是否添加成功时失败")
            else:
                print("第二次出现错误提示")

        else:
            print("第一次出现错误提示")



            '''    
                s4 = self.driver.find_elements_by_css_selector("tbody>tr")
                l4 = len(s4)
                if l3 == l4:
                    print("第二次添加用户失败")
                else:
                    print("第二次添加用户成功")
        
                
                
                b = self.driver.find_element_by_xpath(
                    "//div[@title=1]/../following-sibling::td[1]/div[@class='tdhidden']").get_attribute('title')
                if b == k + '1':
                    print("第二次添加用户成功")
                else:
                    print("第二次添加用户失败")
                '''



    def test_3_editUser(self):
        print("--------------------------编辑用户------------------------------")
        #选择用户
        self.selectUser()
        time.sleep(2)
        self.editUser()
        #读取第一个用户的密码
        d = self.driver.find_element_by_xpath("//input[@id='password']").get_attribute('value')
        d = int(d)
        d = d + 1
        print(d)
        try:
            #self.driver.find_element_by_xpath("//input[@name='username']").clear()
            #time.sleep(1)
            #self.driver.find_element_by_xpath("//input[@name='username']").send_keys(d + '1')
            #time.sleep(1)
            #清除之前的描述
            self.driver.find_element_by_xpath(
                "//*[@id='addgroupform']/div/div/div[3]/input[@name='descript']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//*[@id='addgroupform']/div/div/div[3]/input[@name='descript']").send_keys(d)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='password']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='password']").send_keys(d)
            time.sleep(1)
            #确定密码
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[5]/input[@name='repassword']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[5]/input[@name='repassword']").send_keys(d)
            time.sleep(1)
            #联系人
            self.driver.find_element_by_xpath("//input[@name='contact']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='contact']").send_keys(d)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@placeholder='备注']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@placeholder='备注']").send_keys(d)
            time.sleep(1)
            #取消重复登录按钮
            self.driver.find_element_by_xpath("//input[@name='repeatlogin']").click()
            self.judge_repeat_login()
            self.driver.find_element_by_xpath("//input[@value='保存']").click()
            time.sleep(3)
            self.driver.refresh()
            self.selectUser()
            time.sleep(1)
            self.editUser()
            time.sleep(1)
            k = self.driver.find_element_by_xpath("//input[@name='repeatlogin']").is_selected()
            if k == False:
                print("第一次编辑成功")
            else:
                print("第一次编辑失败")

            self.driver.find_element_by_xpath("//input[@name='repeatlogin']").click()
            self.judge_repeat_login()
            time.sleep(1)


            #q1 = self.driver.find_element_by_xpath("//input[@name='username']").get_attribute('value')
            #time.sleep(1)

            #获取密码、描述等信息
            q2 = self.driver.find_element_by_xpath(
            "//*[@id='addgroupform']/div/div/div[3]/input[@name='descript']").get_attribute('value')
            time.sleep(1)
            q3 = self.driver.find_element_by_xpath("//input[@id='password']").get_attribute('value')
            time.sleep(1)
            q4 = self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[5]/input[@name='repassword']").get_attribute('value')
            time.sleep(1)
            q5 = self.driver.find_element_by_xpath("//input[@name='contact']").get_attribute('value')
            time.sleep(1)
            q6 =self.driver.find_element_by_xpath("//input[@placeholder='备注']").get_attribute('value')
            self.driver.find_element_by_xpath("//input[@value='保存']").click()
            print(d,q2,q3,q4,q5,q6)
            q3 = int(q3)
            q4 = int(q4)
            q5 = int(q5)
            q6 = int(q6)
            q2 = int(q2)
            d = int(d)
            if q2 == d and q3 == d and q4 == d and q5 == d and q6 == d:
                print('编辑成功')
            else:
                print('编辑失败')
        except:
            print("--ee--")
            print('编辑失败')
    def test_4_changePasswd(self):
        print("-----------------------------修改密码-------------------------------")
        try:
            #点击修改密码
            self.changePasswd()
            time.sleep(2)
            #输入旧密码和新密码
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys('testzzl01')
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='newpassword']").send_keys("1")
            self.driver.find_element_by_xpath("//input[@name='renewpassword']").send_keys("1")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@value='确认']").click()
            self.driver.refresh()
            #获取当前的url
            url = self.driver.current_url
            #退出到登录页面
            self.driver.find_element_by_xpath("//a[contains(text(),'退出')]").click()
            time.sleep(1)
            self.driver.refresh()
            url2 = self.driver.current_url
            #判断两个url是否相同
            print(url2)
            if url == url2:
                print("没有退出到登录界面")
            else:
                print("退出成功")
            #使用新密码登录
            Login().login(self.driver,'testzzl01','1')
            time.sleep(2)
            url3 = self.driver.current_url
            print(url3)
            #判断是否登录成功
            if url2 == url3:
                print('登录失败，修改密码失败')
            else:
                print("登录成功，修改密码成功")
                self.changePasswd()
                time.sleep(1)
                self.driver.find_element_by_xpath("//input[@name='password']").send_keys("1")
                time.sleep(1)
                self.driver.find_element_by_xpath("//input[@name='newpassword']").send_keys("testzzl01")
                time.sleep(1)
                self.driver.find_element_by_xpath("//input[@name='renewpassword']").send_keys("testzzl01")
                time.sleep(1)
                self.driver.find_element_by_xpath("//input[@value='确认']").click()
        except:
            print("修改密码失败")


    #普通用户界面
    def test_5_generalUser(self):
        print("---------------------终端用户-----------------------")
        #获取页面上第一个用户的用户名
        h = self.driver.find_element_by_xpath(
            "//div[@title=1]/../following-sibling::td[1]/div[@class='tdhidden']").get_attribute('title')
        self.selectUser()
        time.sleep(1)
        self.editUser()
        time.sleep(1)
        #获取密码
        h2 = self.driver.find_element_by_xpath("//input[@id='password']").get_attribute('value')
        #退出编辑
        #self.driver.find_element_by_xpath("//input[@value='保存']").click()
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[13]/input[2]").click()
        #self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[contains(text(),'退出')]").click()
        time.sleep(1)
        #登录终端用户
        Login().login(self.driver,h,h2)
        time.sleep(2)

        #下载Windows PC版
        s = self.driver.find_element_by_xpath("//span[contains(text(),'下载客户端')]")

        #ActionChains是一个动作链，当调用这个方法时，所有的操作会被存储在一个队列中，当执行perform()方法时，就会按顺序执行队列中的方法，move_to_element()这个方法是指悬浮在某元素上
        ActionChains(self.driver).move_to_element(s).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'Windows PC版')]").click()
        time.sleep(2)
        # self.driver.switch_to.alert.accept()
        k = PyKeyboard()
        #k.tap_key(k.tab_key)
        time.sleep(2)
        #k.tap_key(k.enter_key)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.enter_key)
        time.sleep(5)
        path = r"C:\Users\lz\Downloads\setup_std_client.exe"
        e = os.path.exists(path)
        print(e)
        if e == False:
            print("下载文件失败")
            return
        else:
            os.remove(path)
            print("下载文件成功")

        #下载MAC OS X版文件
        ActionChains(self.driver).move_to_element(s).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'MAC OS X版')]").click()
        time.sleep(2)
        # self.driver.switch_to.alert.accept() ：这是关于弹窗的方法
        k = PyKeyboard()
        # k.tap_key(k.tab_key)
        time.sleep(2)
        # k.tap_key(k.enter_key)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.tab_key)
        time.sleep(1)
        k.tap_key(k.enter_key)
        time.sleep(5)
        path = r"C:\Users\lz\Downloads\GNWayESLMACClient.zip"

        #查看path这个路径是否存在（因为这里path是一个压缩包，所以就是查看这个文件是否存在）
        e = os.path.exists(path)
        print(e)
        if e == False:
            print("下载文件失败")
            return
        else:
            os.remove(path)
            print("下载文件成功")

            time.sleep(10)












        try:
            #点击二维码
            self.driver.find_element_by_xpath("//span[contains(text(),'手机扫码登录')]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='qrcode']/canvas").is_displayed()
            print('出现二维码')
        except:
            print("没有出现二维码")
        #取消二维码
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/span/a").click()
        time.sleep(1)
        #点击修改密码
        self.generalChangePasswd()
        time.sleep(1)
        #输入密码（确认密码不一致）
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(h2)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='newpassword']").send_keys('1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='renewpassword']").send_keys('12')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(2)
        #查看是否出现提示
        try:
            self.driver.find_element_by_xpath("//label[contains(text(),'两次密码输入不一致')]").is_displayed()
        except:
            print("两次密码不一致时，没有出现提示")

        #输入错误旧密码
        self.driver.find_element_by_xpath("//input[@name='password']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(h2 + '1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='newpassword']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='newpassword']").send_keys('1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='renewpassword']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='renewpassword']").send_keys('1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(1)

        #查看是否出现提示
        try:
            self.driver.find_element_by_xpath("//*[@id='formerror']").is_displayed()
        except:
            print('原密码出现错误时没有出现提示')
        #退出修改密码框
        self.driver.find_element_by_xpath("//input[@value='取消']").click()
        time.sleep(1)

        #h2 = int(h2)
        h3 = h2 + "11"
        print(h3)
        self.generalChangePasswd()
        time.sleep(1)
        #输入正确的信息
        self.driver.find_element_by_xpath("//input[@name='password']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(h2)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='newpassword']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='newpassword']").send_keys(h3)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='renewpassword']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='renewpassword']").send_keys(h3)
        time.sleep(1)

        self.driver.find_element_by_xpath("//input[@value='确认']").click()
        time.sleep(2)

        #获取当前的url
        url1 = self.driver.current_url
        self.driver.find_element_by_xpath("//span[contains(text(),'安全退出')]").click()
        time.sleep(2)
        #获取当前url
        url2 = self.driver.current_url
        if url1 == url2:
            print("退出失败")
        else:
            print('退出成功')

        #使用旧密码登录
        Login().login(self.driver,h,h2)
        time.sleep(1)
        url3 = self.driver.current_url
        try:
            #查看使用旧密码是否出现提示
            self.driver.find_element_by_xpath("//*[@id='ee']").is_displayed()
            time.sleep(2)
        except:
            if url2 == url3:
                print('修改密码后用旧密码登录没有出现提示')
            elif url1 == url3:
                print('修改密码后用旧密码登录成功')

        #使用新密码登录
        Login().login(self.driver,h,h3)
        time.sleep(2)
        url4 = self.driver.current_url
        if url1 == url4:
            print('新密码登录成功')
            self.generalChangePasswd()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys(h3)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='newpassword']").send_keys(h2)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='renewpassword']").send_keys(h2)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@value='确认']").click()

        else:
            print('新密码登录失败')






    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()