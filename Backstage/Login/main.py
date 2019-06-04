from Backstage.Login.gyyLogin import *
import unittest
from selenium import webdriver
import time
import HTMLTestRunnerCN
import sendMail


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://yun.gnway.com/admin")

    def test_1_login_pwd_error(self):
        username = 'hdlagent'
        password = '123456'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//strong[contains(text(),'您输入的账号或密码有错误，请确认后重试！')]")
        except:
            print("密码错误时没有出现提示")

    def test_2_login_pwd_null(self):
        url = self.driver.current_url
        username = 'hdlagent'
        password = ''
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
        url1 = self.driver.current_url
        if url != url1:
            print("不输入密码时登录出现错误，url产生变化")

    def test_3_login_user_error(self):
        username = '123456'
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//strong[contains(text(),'您输入的账号或密码有错误，请确认后重试！')]").is_displayed()
        except:
            print("用户名错误时，没有出现提示")

    def test_4_login_user_null(self):
        url2 = self.driver.current_url
        username = ''
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
        url3 = self.driver.current_url
        if url2 != url3:
            print("不输入用户名时登录出现错误，url产生变化")

    def test_5_login_success(self):
        username = 'hdlagent'
        password = 'GNway123456'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
        url4 = self.driver.current_url
        if url4 != "http://yun.gnway.com/index/index":
            print("用户名和密码都正确时，登录错误")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    '''
    当测试用例比较多的时候，这种方式会比较繁琐，会一直加用例，discover的方式只需要标明目录和正则就可以了
    suite = unittest.TestSuite()
    test_suite = [LoginTest("test_1_login_pwd_error"), LoginTest("test_2_login_pwd_null"),
                  LoginTest("test_3_login_user_error"), LoginTest("test_4_login_user_null"),
                  LoginTest("test_5_login_success")]
    suite.addTests(test_suite)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filePath = "./report/" + now + 'restut.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title=u'公有云测试报告', description=u'测试用例结果', tester="赵泽雷")
    runner.run(suite)
    fp.close()
    '''
    # 使用discover的方式
    # 定义当前目录
    test_dir = "./"

    # 定义discover，start_str为需要测试的目录，pattern为正则表达式，也可以为具体文件
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='main.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filePath = "./report/" + now + 'restut.html'
    n = now + 'result.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title=u'公有云测试报告', description=u'测试用例结果', tester="赵泽雷")
    runner.run(discover)
    # 关闭文件
    fp.close()
    sendMail.sendMail(filePath, n)
