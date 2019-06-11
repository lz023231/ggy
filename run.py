from Backstage.Login.gyyLogin import *
import unittest
from selenium import webdriver
import time
import HTMLTestRunnerCN
import sendMail

def runer(basedir,parrten):
    #test_dir = "./"

    # 定义discover，start_str为需要测试的目录，pattern为正则表达式，也可以为具体文件
    discover = unittest.defaultTestLoader.discover(start_dir=basedir, pattern=parrten)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filePath = "./report/" + now + 'result.html'
    n = now + 'result.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title=u'公有云测试报告', description=u'测试用例结果', tester="赵泽雷")
    runner.run(discover)
    # 关闭文件
    fp.close()
    sendMail.sendMail(filePath, n)