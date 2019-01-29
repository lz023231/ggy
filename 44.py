from selenium import webdriver
from time import sleep
import time
from Backstage.Login.gyyLogin import *
from selenium.webdriver.common.action_chains import ActionChains
from pykeyboard import PyKeyboard

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\testdown'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(executable_path='D:\\python3.7\\chromedriver.exe', chrome_options=options)
driver.get('http://testzzl01.yun.gnway.com')
driver.maximize_window()
username = '7'
password = '716'
time.sleep(3)
Login().login(driver, username, password)
s = driver.find_element_by_xpath("//span[contains(text(),'下载客户端')]")
ActionChains(driver).move_to_element(s).perform()
time.sleep(2)


driver.find_element_by_xpath("//a[contains(text(),'Windows PC版')]").click()
sleep(3)
driver.quit()

