# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re
from time import sleep
from edit import edit
from organization import organization,organization_del
from meeting_room import meeting_room,meeting_room_del
from meeting_type import meeting_type,meeting_type_del
from user import user,user_del
from meeting import meeting,meeting_del
from meeting_staff import meeting_staff
from meeting_agenda import meeting_agenda,meeting_agenda_del
from meeting_vote import meeting_vote,meeting_vote_del
from meeting_questionnaire import meeting_questionnaire,meeting_questionnaire_del
from meeting_message import meeting_message,meeting_message_del
from meeting_file import meeting_file,meeting_file_del
from meeting_summary import meeting_summary,meeting_summary_del
import logging

driver = webdriver.Chrome()
URL = "http://localhost/admin/"
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(URL)

#用户登录
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("//span[contains(.,'Sign in')]").click()
try:
    driver.find_element_by_xpath("//span[text()='会议列表']")
    print(u"登录成功")
except:
    logging.error("登录失败")
    #编辑信息
driver.find_element_by_xpath("//span[text()='我的面板']").click()
sleep(1)
edit(driver)
#点击系统设置
while(1):
    try:
        driver.find_element_by_xpath("//span[text()='系统设置']").click()
        break
    except:
        pass
sleep(1)
organization_del(driver)           #清空机构
organization(driver)               #创建机构

meeting_room_del(driver,1)         #清空会议室
meeting_room(driver,0)             #创建会议室

meeting_type_del(driver,1)         #清空会议类型
meeting_type(driver,0)             #创建会议类型

user_del(driver)                   #清空用户
user(driver)                       #创建用户
while(1):
    try:
        driver.find_element_by_xpath("//span[text()='会议列表']").click()   #点击会议列表
        break
    except:
        pass
meeting_del(driver)        #清空会议
meeting(driver)            #创建会议
try:
    driver.find_element_by_xpath("//span[text()='自动化大会0']").click()    #打开会议详情
except:
    print (u"无该会议")
    driver.quit()
sleep(1)
meeting_staff(driver)              #参会人员

meeting_agenda_del(driver)         #清空议程
meeting_agenda(driver)             #会议议程

meeting_file(driver)               #会议资料
meeting_file_del(driver)           #删除资料
meeting_agenda_del(driver)         #删除议程

meeting_summary_del(driver)        #清空纪要
meeting_summary(driver)            #会议纪要

meeting_vote_del(driver)           #清空投票
meeting_vote(driver)               #会议投票
meeting_vote_del(driver)           #删除投票

meeting_questionnaire_del(driver)  #清空问卷
meeting_questionnaire(driver)      #会议问卷
meeting_questionnaire_del(driver)  #删除问卷

meeting_message_del(driver)        #清空通知
meeting_message(driver)            #会议通知
meeting_message_del(driver)        #删除通知
sleep(3)
driver.quit()


