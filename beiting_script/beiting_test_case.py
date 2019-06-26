# coding=utf-8
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport
#import request
import operator
from PIL import Image
import time
import os
import logging
from browser import BrowserHacker,BrowserType
from party.party import party_add,party_del,party_in_check
from village.health_summarize import health_summarize
from village.health_area import health_area_add,health_area_del,health_area_alter,site_area_alter
from log import myLog
from SMTP_email import email
def sleep(second):
    time.sleep(second)

xie = "\_"
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
dr = BrowserHacker()
class beiting_case(unittest.TestCase):
    def setUp(self):
        self.dr = dr
        self.dr.wait(10)
        self.URL="http://beiting.haituke.com"

    def case_1_login(self):
        """用户登录测试用例"""
        dr = self.dr
        self.dr.open(self.URL)
        dr.XPath_get("//div[contains(text(),'广州大学城小谷围街道北亭村信息平台(阳光北亭)')]")
        dr.Name_sendkey("username","admin")
        dr.Name_sendkey("password","12345678")
        dr.XPath_click("//span[contains(text(),'登录')]")
        if dr.XPath_text("//*[contains(text(),'阳光党建，智慧北亭')]"):
                print("登录成功")
                myLog.info("登录成功")
        else:
            print("登录失败")
            myLog.info("登录失败")
            raise
    def case_2_party(self):
        """党建内容测试用例"""
        dr = self.dr
        title = "自动化文章"
        dr.XPath_click("//span[text()='党务管理']")
        dr.XPath_click("//span[text()='党建内容']")
        dr.XPath_click("//span[text()='写文章']")
        party_in_check(dr)
        party_add(dr,title,"自动化文章") #标题、内容
        party_del(dr,title)

    def case_3_village(self):
        """卫生管理概述测试用例"""
        dr = self.dr
        dr.XPath_click("//span[text()='村务管理']")
        dr.XPath_click("//span[text()='卫生管理']")
        content = "自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——自动化结果测试——"
        health_summarize(dr,content)  #卫生管理概述
        health_area_add(dr)    #卫生片区_新增
        health_area_alter(dr)  #卫生片区_修改
        site_area_alter(dr)    #修改地址关联片区
        health_area_del(dr)    #卫生片区_删除

    def case_4_project(self):
        dr = self.dr
        dr.XPath_click("//span[text()='项目管理']")
        dr.XPath_click("//span[text()='地址管理']")
        dr.XPath_click("//span[text()='用户管理']")

    def close(self):
        dr = self.dr
        sleep(2)
        dr.close()
class beitin_case1(unittest.TestCase):
    def setUp(self):
        self.dr = dr
        self.dr.wait(10)
        self.URL="http://beiting.haituke.com"

    def case(self):
        if dr.XPath_text("//*[contains(text(),'阳光党建，智慧北亭')]"):
                print("登录成功")
                myLog.info("登录成功")
        else:
            print("登录失败")
            myLog.info("登录失败")
            raise

    def close(self):
        dr = self.dr
        sleep(2)
        dr.close()
testunit = unittest.TestSuite()
testunit.addTest(beiting_case("case_1_login"))
# testunit.addTest(beiting_case("case_2_party"))
# testunit.addTest(beiting_case("case_3_village"))
# testunit.addTest(beiting_case("case_4_project"))
# testunit.addTest(beiting_case("close"))
testunit.addTest(beitin_case1("case"))
BeautifulReport(testunit).report(filename=xie + now + '阳光北亭测试报告', description='创建与删除测试',
                                 log_path=r'C:\Users\Administrator\Desktop\beiting_script\result')

file = xie + now + '阳光北亭测试报告.html'
filename = r"C:\Users\Administrator\Desktop\beiting_script\result" + file
f = open(filename,"rb")
content = """status": "失败"""
lines = f.readlines()
for line in lines:
    if content.encode() in line:
        email(filename, "prwu@sailfish.com.cn")