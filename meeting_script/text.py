# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport
import time
from edit import edit
from organization import organization,organization_del
from meeting_room import meeting_room,meeting_room_del
from meeting_type import meeting_type,meeting_type_del
from user import user,user_del
from meeting import meeting,meeting_del,meeting_open,meeting_close
from meeting_staff import meeting_staff
from meeting_agenda import meeting_agenda,meeting_agenda_del,meeting_agenda_open_del
from meeting_vote import meeting_vote,meeting_vote_del
from meeting_questionnaire import meeting_questionnaire,meeting_questionnaire_del,meeting_questionnaire_open_del
from meeting_message import meeting_message,meeting_message_del
from meeting_file import meeting_file,meeting_file_del
from meeting_summary import meeting_summary,meeting_summary_del
import os
import logging
def sleep(a):
    time.sleep(a)
dr = webdriver.Chrome()
class meeting_test_case(unittest.TestCase):
    '''无纸化会议测试用例'''
    def setUp(self,driver = dr):
        print("test start")
        self.driver = dr
        self.driver.implicitly_wait(10)
        self.URL = "http://192.168.199.112/admin/"

    def case_1_add_del(self):
        '''创建->删除测试用例'''
        driver = self.driver
        driver.get(self.URL)
        driver.maximize_window()
        tii = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        logging.basicConfig(filename=r'C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\case_1_add_del\\'+ tii +' test_case.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                            datefmt='%Y-%m-%d')

        logging.debug(driver.find_element_by_name("username").send_keys("admin"))
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//span[contains(.,'Sign in')]").click()
        try:
            mark = driver.find_element_by_xpath("//span[text()='我的面板']")
            print(u"登录成功")
        except:
            print(u"登录失败")
        while(1):
            sleep(1)
            try:
                mark.click()
                break
            except:
                pass
        # 点击系统设置
        while(1):
            try:
                driver.find_element_by_xpath("//span[text()='系统设置']").click()
                break
            except:
                pass
    def case_2_organization(self):
        driver = self.driver
        organization_del(driver)  # 清空机构
        organization(driver)  # 创建机构
        meeting_room_del(driver, 1)  # 清空会议室
        meeting_room(driver, 0)  # 创建会议室
        meeting_type_del(driver, 1)  # 清空会议类型
        meeting_type(driver, 0)  # 创建会议类型
        user_del(driver)  # 清空用户
        user(driver)  # 创建用户
        meeting_del(driver)  # 清空会议
        meeting(driver)  # 创建会议
        while (1):
            sleep(1)
            try:
                driver.find_element_by_xpath("//span[text()='会议列表']").click()
                driver.find_element_by_xpath("//span[text()='自动化大会0']").click()
                break
            except:
                pass
        sleep(1)
        meeting_staff(driver)  # 参会人员
        meeting_agenda(driver)  # 会议议程
        meeting_file(driver)  # 会议资料
        meeting_file_del(driver)  # 删除资料
        meeting_agenda_del(driver)  # 删除议程
        meeting_summary(driver)  # 会议纪要
        meeting_vote(driver)  # 会议投票
        meeting_vote_del(driver)  # 删除投票
        meeting_questionnaire(driver)  # 会议问卷
        meeting_questionnaire_del(driver)  # 删除问卷
        meeting_message(driver)  # 会议通知
        meeting_message_del(driver)  # 删除通知

    def case_2_open_del(self):
        '''会议开启中删除'''
        driver = self.driver
        driver.get(self.URL)
        driver.maximize_window()
        tii = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        logging.basicConfig(filename=r'C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\case_2_open_del\\' + tii + ' test_case.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                            datefmt='%Y-%m-%d')

        logging.debug(driver.find_element_by_name("username").send_keys("admin"))
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//span[contains(.,'Sign in')]").click()
        try:
            driver.find_element_by_xpath("//span[text()='会议列表']")
            print(u"登录成功")
        except:
            print(u"登录失败")
        while (1):
            sleep(1)
            try:
                driver.find_element_by_xpath("//span[text()='会议列表']").click()
                break
            except:
                pass
            #打开会议详情
        while (1):
            sleep(1)
            try:
                driver.find_element_by_xpath("//span[text()='自动化大会0']").click()
                break
            except:
                pass
        sleep(1)
        # meeting_open(driver)
        meeting_agenda(driver)  # 会议议程
        meeting_open(driver)
        meeting_questionnaire(driver)  # 会议问卷
        driver.find_element_by_xpath("//span[text()='已开始']").click()
        meeting_questionnaire_open_del(driver)
        meeting_agenda_open_del(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='会议列表']"))).click()
        sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'彻底删除')]").click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='此操作将彻底删除该会议, 是否继续?']").text
        print(del_text)
        driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()
        text = WebDriverWait(driver, 5, 0.2).until(EC.presence_of_element_located((By.XPATH, "//p[text()='正在进行的会议不允许删除']"))).text
        print(text)
        sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='自动化大会0']"))).click()
        sleep(1)
        meeting_close(driver)
    # def tearDown(self):
    #     self.driver.quit()
    #     print("test end")


# suite1 = unittest.TestSuite(tests=[meeting_test_case('login_case'),meeting_test_case('eee')])
testunit = unittest.TestSuite()
testunit.addTest(meeting_test_case("case_1_add_del"))
testunit.addTest(meeting_test_case("case_2_organization"))
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
report_path = r'C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\result\\'+ now +' test_case.html'
BeautifulReport(testunit).report(filename='项目测试报告', description='创建与删除测试', log_path='.')
