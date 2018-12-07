# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os
def meeting_add(driver,i):
    while (1):
        sleep(1)
        try:
            driver.find_element_by_xpath("//span[text()='会议列表']").click()
            break
        except:
            pass
    sleep(1)
    delete = driver.find_elements_by_xpath("//span[contains(text(),'彻底删除')]")
    driver.find_element_by_xpath("//span[text()='新建会议']").click()
    mark=0
    for list in range(3,15):
        if list == 3:
            sleep(1)
            driver.find_element_by_xpath("//span[text()='上传图片']").click()
            try:
                os.system(r'C:\Users\Administrator\Desktop\file\logo.exe')
                sleep(3)
                driver.find_element_by_class_name("upload-img")  # 检查是否有图片
                print (u"logo上传成功")
                sleep(2)
            except:
                print (u"logo上传失败")
        elif list == 4:   #选择机构
            driver.find_element_by_class_name("el-cascader__label").click()
            sleep(1)
            driver.find_element_by_xpath("//li[text()='组织机构_自动化公司0']").click()
            sleep(1)
        elif list == 5:   #会议名称
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"自动化大会",i)
        elif list == 6:   #副标题
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"第一百一十次")
        elif list == 7:   #开始时间
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys("202",i,"-1-24 17:53:16")
        elif list == 8:   #结束时间
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys("202",i,"-1-25 17:53:16")
            driver.find_element_by_xpath("//label[text()='结束时间']").click()
        elif list == 9:   #地点
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"北京")
        elif list == 10:  #会议室
             sleep(1)
             if i == 0:
                driver.find_elements_by_class_name("el-input__inner")[list].click()
                sleep(1)
                driver.find_elements_by_xpath("//span[text()='自动化会议室0']")[-1].click()
             else:
                driver.find_elements_by_class_name("el-input__inner")[list].click()
                sleep(1)
                driver.find_elements_by_xpath("//span[text()='自动化会议室1']")[-1].click()
             sleep(3)
             try:
                driver.find_element_by_class_name("el-row")
                print (u"会议室有座位图")
             except:
                print (u"会议室没有座位图")
        elif list == 11:  #主持人
            sleep(1)
            driver.find_elements_by_class_name("el-input__inner")[list].click()
            sleep(1)
            driver.find_elements_by_xpath("//span[text()='用户0']")[-1].click()
        # if list == 12:  #助理
        #     driver.find_elements_by_class_name("el-input__inner")[list].click()
        #     driver.find_elements_by_class_name("el-input__inner")[list].send_keys("2100-11-24 17:53:16")
        elif list == 13:  #会议类型
            driver.find_elements_by_class_name("el-input__inner")[list].click()
            sleep(1)
            driver.find_elements_by_xpath("//span[text()='自动化会议类型0']")[-1].click()
        elif list == 14:  #欢迎语
            sleep(1)
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"欢迎欢迎热烈欢迎")
            mark=1
        if mark == 1:       #开启所有会议功能
            #driver.find_element_by_class_name("el-switch__core").click()
            driver.find_element_by_xpath("//span[text()='确定']").click()
            time_1 = 3
            while (1):
                compare = driver.find_elements_by_xpath("//span[contains(text(),'彻底删除')]")
                if len(compare) != len(delete):
                    delete = compare
                    print (u"会议创建成功")
                    break
                elif time_1 == 0 and len(compare) == len(delete):
                    print (u"会议创建失败")
                    break
                sleep(time_1)
                time_1 = time_1 - 1
        sleep(1)

def meeting_del(driver):
    while (1):
        sleep(1)
        try:
            driver.find_element_by_xpath("//span[text()='会议列表']").click()
            delete = driver.find_elements_by_xpath("//span[contains(text(),'彻底删除')]")
            break
        except:
            pass
    while(len(delete) != 0):
        sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'彻底删除')]").click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='此操作将彻底删除该会议, 是否继续?']").text
        print (del_text)
        driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()
        sleep(2)
        time_1 = 3
        while(1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'彻底删除')]")
            if len(compare) != len(delete):
                delete = compare
                print (u"会议删除成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"会议删除失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)

def meeting_open(driver):
    driver.find_element_by_xpath("//span[text()='会议详情']").click()
    sleep(1)
    WebDriverWait(driver,5,0.2).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='开启会议']"))).click()
    WebDriverWait(driver, 5, 0.2).until(EC.presence_of_element_located((By.XPATH, "//span[text()='关闭会议']")))
    print("开启会议")

def meeting_close(driver):
    driver.find_element_by_xpath("//span[text()='会议详情']").click()
    sleep(1)
    WebDriverWait(driver, 5, 0.2).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='关闭会议']"))).click()
    WebDriverWait(driver, 5, 0.2).until(EC.presence_of_element_located((By.XPATH, "//span[text()='开启会议']")))
    print("关闭会议")
def meeting(driver):
    driver.implicitly_wait(5)
    for i in range(1):
        meeting_add(driver,i)
    #meeting_del(driver)