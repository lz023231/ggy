from Backstage.Login.gyyLogin import *
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver

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
        y = self.driver.find_element_by_xpath("//input[@name='repeatlogin']").is_selected()
        if y == True:
            r = self.driver.find_element_by_xpath("//input[@placeholder='0-2040，默认为最大']").is_displayed()
            if r == True:
                print("勾选重复登录时显示正常")
            else:
                print("勾选重复登录时显示不正常")
        else:
            print("-----------")
            try:

                self.driver.find_element_by_xpath("//input[@placeholder='0-2040，默认为最大']").is_displayed()
                print("没有勾选时显示错误")
            except:
                print("没有勾选时显示正确")
    def changePasswd(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'修改密码')]")))
            element.click()
            self.driver.find_element_by_xpath("//strong[contains(text(),'旧密码')]").is_displayed()
        except:
            print("点击修改密码失败或没有出现二级菜单")


    def addUser(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'添加普通用户')]")))
            element.click()
        except:
            print("点击添加普通用户失败")

    def editUser(self):
        try:
            element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'编辑用户')]")))
            element.click()
        except:
            print("点击编辑用户失败")

    def findUser(self):
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
    def selectUser(self):
        while True:
            try:
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
        x = self.driver.find_element_by_xpath(
            "//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']").get_attribute('value')
        x = int(x)
        #print(x)
        self.selectUser()
        time.sleep(2)
        try:
            #element = self.driver.find_element_by_id("btnDeleteGroupUser").is_displayed()
            #element.click()
            self.driver.find_element_by_id("btnDeleteGroupUser").click()
            time.sleep(2)
            #a = EC.alert_is_pr//*[@id="dialog-confirm"]/pesent()(self.driver)
            #a = self.driver.switch_to.alert()
            #a.text()
            #return a
            #element = WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dialog-confirm"]/p')))
            a = self.driver.find_element_by_xpath('//*[@id="dialog-confirm"]/p').text
            print(a)
            if a == "这些数据将被永久删除,并且无法恢复.您确定吗?":
                print("dsdfsdf")
            else:
                print("删除时没有出现提示")
            self.driver.find_element_by_xpath("//span[contains(text(),'取消')]").click()  #取消
            time.sleep(2)
            self.driver.refresh()
            x2 = self.driver.find_element_by_xpath("//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']").get_attribute('value')
            x2 = int(x2)
            #print(x2)
            if x == x2:
                print("点击取消没有被删除")
            else:
                print("点击取消按钮后用户被删除")

            self.selectUser()
            time.sleep(2)
            self.driver.find_element_by_id("btnDeleteGroupUser").click()
            time.sleep(2)

            b = self.driver.find_element_by_xpath('//*[@id="dialog-confirm"]/p').text
            print(b)
            if b == "这些数据将被永久删除,并且无法恢复.您确定吗?":
                print("出现提示")
            else:
                print("删除时没有出现提示")

            self.driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
            time.sleep(2)
            self.driver.refresh()
            x3 = self.driver.find_element_by_xpath("//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']").get_attribute('value')
            x3 = int(x3)
            if x3 == x:
                print("点击确定后，用户没有被删除")
            else:
                print("删除用户成功")


        except:
            print("删除用户出错")

    def test_2_addUser(self):
        print("---------------------------添加用户-----------------------------")


        h = self.driver.find_element_by_xpath(
            "//div[@title=1]/../following-sibling::td[1]/div[@class='tdhidden']").get_attribute('title')

        self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
        time.sleep(3)
        s = self.driver.find_elements_by_css_selector("tbody>tr")
        # print(len(s))
        l = len(s)
        #print(h)
        #self.selectUser()
        #time.sleep(2)
        self.addUser()
        print("------------")
        time.sleep(2)
        t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        y = t.split("-")
        k = '{}{}{}{}{}'.format('ceshi', y[1], y[2], y[3], y[4])
        try:
            self.driver.find_element_by_xpath("//input[@value='保存']").is_displayed()
        except:
            print("添加用户没有出现二级菜单")
        self.driver.find_element_by_xpath("//input[@value='保存']").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//label[@id='username-error']").is_displayed()
            self.driver.find_element_by_xpath("//label[@id='password-error']").is_displayed()
            self.driver.find_element_by_xpath("//label[contains(text(),'请再次输入密码')]").is_displayed()
        except:
            print("什么都不添写时，点击保存时，没有出现错误提示")
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//input[@name='username']").send_keys(h)
            self.driver.find_element_by_xpath("//input[@id='password']").send_keys(h)
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").send_keys(h)
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

        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[12]/input[2]").click()
        time.sleep(1)
        self.addUser()
        time.sleep(2)


        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[2]/input[@name='descript']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").send_keys(k)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='contact']").send_keys(k)
        time.sleep(2)
        self.judge_repeat_login()
        self.driver.find_element_by_xpath("//input[@value='保存']").click()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)

        self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
        time.sleep(3)
        #m1 = '{}{}{}'.format("//div[@title='", k, "']")
        r1 = k + "']"
        n1 = self.driver.find_element_by_xpath("//div[@title='" + r1).is_displayed()
        #h =
        print(n1)
        if n1 == True:
            print('第一次添加用户成功')
        else:
            print("第一次添加用户失败")
            '''
        s2 = self.driver.find_elements_by_css_selector("tbody>tr")
        l2 = len(s2)
        if l == l2:
            print("第一次添加用户失败")
        else:
            print("第一次添加用户成功")
        '''
        '''
        j = self.driver.find_element_by_xpath(
            "//div[@title=1]/../following-sibling::td[1]/div[@class='tdhidden']").get_attribute('title')
        if h == j:
            print("第一次添加用户成功")
        else:
            print("第一次添加用户失败")
        '''

        self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
        time.sleep(3)
        s3 = self.driver.find_elements_by_css_selector("tbody>tr")
        l3 = len(s3)
        self.addUser()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//input[@value='保存']").is_displayed()
        except:
            print("添加用户没有出现二级菜单")

        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(k + '1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[2]/input[@name='descript']").send_keys(k + '1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys(k + '1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").send_keys(k + '2')
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
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").send_keys(k + '1')
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name='repeatlogin']").click()
        time.sleep(1)
        self.judge_repeat_login()
        self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[11]/input[1]").click()
        time.sleep(1)
        self.driver.refresh()
        self.driver.find_element_by_xpath("//a[contains(text(),'尾页')]").click()
        time.sleep(3)
        #m = '{}{}{}{}{}{}'.format('"',"//div[@title='",k,'1',"']",'"')
        r = k + "1']"
        n = self.driver.find_element_by_xpath("//div[@title='" + r).is_displayed()
        if n == True:
            print('第二次添加用户成功')
        else:
            print("第二次添加用户失败")
            '''
        s4 = self.driver.find_elements_by_css_selector("tbody>tr")
        l4 = len(s4)
        if l3 == l4:
            print("第二次添加用户失败")
        else:
            print("第二次添加用户成功")

        '''
        '''
        b = self.driver.find_element_by_xpath(
            "//div[@title=1]/../following-sibling::td[1]/div[@class='tdhidden']").get_attribute('title')
        if b == k + '1':
            print("第二次添加用户成功")
        else:
            print("第二次添加用户失败")
        '''



    def test_3_editUser(self):
        self.selectUser()
        time.sleep(2)
        self.editUser()
        d = self.driver.find_element_by_xpath("//input[@id='password']").get_attribute('value')
        d = int(d)
        d = d + 1
        print(d)
        try:
            #self.driver.find_element_by_xpath("//input[@name='username']").clear()
            #time.sleep(1)
            #self.driver.find_element_by_xpath("//input[@name='username']").send_keys(d + '1')
            #time.sleep(1)
            self.driver.find_element_by_xpath(
                "//*[@id='addgroupform']/div/div/div[2]/input[@name='descript']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//*[@id='addgroupform']/div/div/div[2]/input[@name='descript']").send_keys(d)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='password']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='password']").send_keys(d)
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").send_keys(d)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='contact']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='contact']").send_keys(d)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@placeholder='备注']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@placeholder='备注']").send_keys(d)
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='repeatlogin']").click()
            self.judge_repeat_login()
            self.driver.find_element_by_xpath("//input[@value='保存']").click()
            time.sleep(3)
            self.driver.refresh()
            self.selectUser()
            time.sleep(1)
            self.editUser()
            time.sleep(1)

            #q1 = self.driver.find_element_by_xpath("//input[@name='username']").get_attribute('value')
            #time.sleep(1)
            q2 = self.driver.find_element_by_xpath(
            "//*[@id='addgroupform']/div/div/div[2]/input[@name='descript']").get_attribute('value')
            time.sleep(1)
            q3 = self.driver.find_element_by_xpath("//input[@id='password']").get_attribute('value')
            time.sleep(1)
            q4 = self.driver.find_element_by_xpath("//*[@id='addgroupform']/div/div/div[4]/input[@name='repassword']").get_attribute('value')
            time.sleep(1)
            q5 = self.driver.find_element_by_xpath("//input[@name='contact']").get_attribute('value')
            time.sleep(1)
            q6 =self.driver.find_element_by_xpath("//input[@placeholder='备注']").get_attribute('value')
            u = d + '1'
            print(type(q2))
            print(type(u))
            if q2 == u and q3 == u and q4 == u and q5 == u and q6 == u:
                print('编辑成功')
            else:
                print('编辑失败')
        except:
            print('编辑失败')
    def test_4_changePasswd(self):
        try:
            self.changePasswd()
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys('testzzl01')
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='newpassword']").send_keys("1")
            self.driver.find_element_by_xpath("//input[@name='renewpassword']").send_keys("1")
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@value='确认']").click()
            self.driver.refresh()
            url = self.driver.current_url
            self.driver.find_element_by_xpath("//a[contains(text(),'退出')]").click()
            time.sleep(1)
            self.driver.refresh()
            url2 = self.driver.current_url
            print(url2)
            if url == url2:
                print("没有退出到登录界面")
            else:
                print("退出成功")
            Login().login(self.driver,'testzzl01','1')
            time.sleep(2)
            url3 = self.driver.current_url
            print(url3)
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











    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()