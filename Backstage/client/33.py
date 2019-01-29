
import  datetime
import time
'''
time1 = "2019-1-31"
time2 = "2019-2-28"
d1 = datetime.datetime.strptime(time1,'%Y-%m-%d')
d2 = datetime.datetime.strptime(time2,'%Y-%m-%d')
#m = d2 - d1
#t = m.days/30
t = round((d2 - d1).days/30)
print(t)

t = "ceshi"
x = "ceshi01"
z = t+'01'

if x == t + "01":
    print('3')
else:
    print('ksdhf')
    
t = datetime.datetime.now().strftime('%Y-%m-%d')
y = t.split('-')
print(y)
h = '{}{}{}'.format('ceshi',y[1],y[2])
print(h)

print(t)
'''
#t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
#print(t)
#k = "ds"
#print(k + 'd')

'''
k = "ceshi"
m = '{}{}{}{}{}{}'.format('"',"//div[@title='",k,'1',"']",'"')
print(m)
m1 = '{}{}{}{}{}'.format('"',"//div[@title='",k, "']",   '"')
print(m1)
d = '4'
d = int(d)
d = d + 1
print(d)

for i in range(3):
	print(i)
	'''
from Backstage.Login.gyyLogin import *
from selenium.webdriver.common.action_chains import ActionChains
import time
from pykeyboard import PyKeyboard
import os
from pymouse import PyMouse


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
        username = '7'
        password = '716'
        time.sleep(3)
        Login().login(self.driver, username, password)
        time.sleep(2)


    def test_1_alart(self):
        s = self.driver.find_element_by_xpath("//span[contains(text(),'下载客户端')]")
        ActionChains(self.driver).move_to_element(s).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'Windows PC版')]").click()
        #self.driver.switch_to.alert.accept()
        k = PyKeyboard()
        k.tap_key(k.tab_key)
        time.sleep(2)
        k.tap_key(k.enter_key)
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
        


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
	unittest.main()




