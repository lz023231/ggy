from Backstage.Login.gyyLogin import *
import time
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
        self.driver.get("https://yun.gnway.com")
        username = 'testzzl01'
        password = 'testzzl01'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)
    def findUser(self):
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)
    def selectUser(self):


        while True:
            try:
                e = self.driver.find_element_by_xpath("//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']").is_displayed()
                print("---")
                print(e)
            except:
                e = False
                print("----")
                print(e)
            if e == False:

                self.findUser()
                time.sleep(2)
                self.driver.find_element_by_xpath("//a[contains(text(),'后一页')]").click()
            else:
                break

        t = self.driver.find_element_by_xpath("//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']").is_selected()
        while t == False:
            try:
                element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//div[@title=1]/../preceding-sibling::td[1]/div/input[@type='checkbox']")))
                element.click()
                if t == True:
                    return
                break
            except:
                print("选择主机失败")

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






    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()