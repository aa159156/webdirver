# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport
import operator
from PIL import Image
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
    def setUp(self):
        print("test start")
        self.driver = dr
        self.driver.implicitly_wait(10)
        self.URL = "http://192.168.199.112/admin/"

    def case_1_login(self):
        '''用户登录'''
        driver = self.driver
        driver.get(self.URL)
        driver.maximize_window()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//span[contains(.,'Sign in')]").click()
        try:
            mark = driver.find_element_by_xpath("//span[text()='我的面板']")
            driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\image\登录.png")
        except:
            driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\image\登录.png")
        practical_image = Image.open(r"C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\image\登录.png")
        expect_image = Image.open(r"C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\image\登录成功.png")
        compose = operator.eq(practical_image,expect_image)
        if compose == True:
            print(u"图片比对结果:",compose,"登录成功")
        else:
            print(u"图片比对结果:",compose,"登录失败")
        try:
            mark.click() #点击我的面板
        except:
            pass

    def case_2_organization(self):
        '''组织机构的删除->创建'''
        driver = self.driver
        while(1):
            try:
                driver.find_element_by_xpath("//span[text()='系统设置']").click() # 点击系统设置
                break
            except:
                pass
        organization_del(driver)  # 清空机构
        organization(driver)  # 创建机构

    def case_3_meeting_room(self):
        '''会议室删除->创建'''
        driver = self.driver
        meeting_room_del(driver, 1)  # 清空会议室
        meeting_room(driver, 0)  # 创建会议室

    def case_4_meeting_type(self):
        '''会议类型删除->创建'''
        driver = self.driver
        meeting_type_del(driver, 1)  # 清空会议类型
        meeting_type(driver, 0)  # 创建会议类型

    def case_5_user(self):
        '''用户删除->创建'''
        driver = self.driver
        user_del(driver)  # 清空用户
        user(driver)  # 创建用户

    def case_6_meeting(self):
        '''会议删除->创建'''
        driver = self.driver
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

    def case_7_meeing_staff(self):
        '''参会人员添加'''
        driver = self.driver
        meeting_staff(driver)  # 参会人员

    def case_8_meeting_agenda(self):
        '''会议议程创建'''
        driver = self.driver
        meeting_agenda(driver)  # 会议议程

    def case_9_meeting_file(self):
        '''会议资料添加->删除与议程删除'''
        driver = self.driver
        meeting_file(driver)  # 会议资料
        meeting_file_del(driver)  # 删除资料
        meeting_agenda_del(driver)  # 删除议程

    def case_10_summary(self):
        '''会议纪要添加->删除'''
        driver = self.driver
        meeting_summary(driver)  # 会议纪要

    def case_11_meeting_vote(self):
        '''会议投票添加->删除'''
        driver = self.driver
        meeting_vote(driver)  # 会议投票
        meeting_vote_del(driver)  # 删除投票

    def case_12_meeting_questionnaire(self):
        '''会议问卷添加->删除'''
        driver = self.driver
        meeting_questionnaire(driver)  # 会议问卷
        meeting_questionnaire_del(driver)  # 删除问卷

    def case_13_meeting_message(self):
        '''会议通知添加->删除'''
        driver = self.driver
        meeting_message(driver)  # 会议通知
        meeting_message_del(driver)  # 删除通知

    def case_14_open_del(self):
        '''删除开启中的议程、问卷、会议'''
        driver = self.driver
        while (1):
            sleep(1)
            try:
                driver.find_element_by_xpath("//span[text()='会议列表']").click()     #点击会议列表
                driver.find_element_by_xpath("//span[text()='自动化大会0']").click()  #打开会议详情
                break
            except:
                pass
        sleep(1)
        # meeting_open(driver)
        meeting_agenda_del(driver)
        meeting_agenda(driver)  # 会议议程
        meeting_open(driver)
        meeting_questionnaire(driver)  # 会议问卷
        driver.find_element_by_xpath("//span[text()='已开始']").click()
        meeting_questionnaire_open_del(driver)
        meeting_agenda_open_del(driver)
        while (1):
            sleep(1)
            try:
                driver.find_element_by_xpath("//span[text()='会议列表']").click()     #点击会议列表
                break
            except:
                pass
        sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'彻底删除')]").click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='此操作将彻底删除该会议, 是否继续?']").text
        print(del_text)
        driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()
        try:
            text = WebDriverWait(driver, 5, 0.2).until(EC.presence_of_element_located((By.XPATH, "//p[text()='正在进行的会议不允许删除']"))).text
            print(text)
        except:
            pass
        sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='自动化大会0']"))).click()
        sleep(1)
        meeting_close(driver)
    def tear_Down(self):
        '''关闭浏览器'''
        self.driver.quit()
        print("test end")


# suite1 = unittest.TestSuite(tests=[meeting_test_case('login_case'),meeting_test_case('eee')])
testunit = unittest.TestSuite()
testunit.addTest(meeting_test_case("case_1_login"))
# testunit.addTest(meeting_test_case("case_2_organization"))
# testunit.addTest(meeting_test_case("case_3_meeting_room"))
# testunit.addTest(meeting_test_case("case_4_meeting_type"))
# testunit.addTest(meeting_test_case("case_5_user"))
# testunit.addTest(meeting_test_case("case_6_meeting"))
# testunit.addTest(meeting_test_case("case_7_meeing_staff"))
# testunit.addTest(meeting_test_case("case_8_meeting_agenda"))
# testunit.addTest(meeting_test_case("case_9_meeting_file"))
# testunit.addTest(meeting_test_case("case_10_summary"))
# testunit.addTest(meeting_test_case("case_11_meeting_vote"))
# testunit.addTest(meeting_test_case("case_12_meeting_questionnaire"))
# testunit.addTest(meeting_test_case("case_13_meeting_message"))
# testunit.addTest(meeting_test_case("case_14_open_del"))
testunit.addTest(meeting_test_case("tear_Down"))
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
BeautifulReport(testunit).report(filename=now + '无纸化会议系统项目测试报告', description='创建与删除测试',
                                 log_path=r'C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\result')


'''log输出'''
# tii = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# logging.basicConfig(
#     filename=r'C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\case_1_add_del\\' + tii + ' test_case.log',
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
#     datefmt='%Y-%m-%d')
'''HTMLTestRunner测试报告生成'''
# now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#report_path = r'C:\Users\Administrator\Desktop\seleniumjiaoben\meeting_script\result\\'+ now +' test_case.html'
#fp = open(report_path, "wb")
#初始化一个HTMLTestRunner实例对象，用来生成报告
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                        title=u"无纸化会议系统项目测试报告",
#                                        description=u"用例测试情况：")
#开始执行测试套件
#runner.run(testunit)
# fp.close()