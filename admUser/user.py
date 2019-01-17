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
                e = self.driver.find_element_by_xpath("//input[@value='34871']").is_displayed()
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

        t = self.driver.find_element_by_xpath("//input[@value='34871']").is_selected()
        while t == False:
            try:
                element = WebDriverWait(self.driver,10,1).until(EC.element_to_be_clickable((By.XPATH,"//input[@value='34871']")))
                element.click()
                if t == True:
                    return
                break
            except:
                print("选择主机失败")

    def test_1_deleteUser(self):
        self.selectUser()
        time.sleep(2)
        try:
            #element = self.driver.find_element_by_id("btnDeleteGroupUser").is_displayed()
            #element.click()
            self.driver.find_element_by_id("btnDeleteGroupUser").click()
            time.sleep(2)
            #a = EC.alert_is_present()(self.driver)
            a = self.driver.switch_to.alert()
            a.text()
            return a
        except:
            print("-----")






    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()