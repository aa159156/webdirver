# -*- coding: utf-8 -*-
from time import sleep
import os
def user_message(driver,i):
    try:
        driver.find_element_by_xpath("//span[text()='用户管理']").click()
    except:
        pass
    sleep(1)
    delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
    driver.find_element_by_xpath("//span[text()='添加用户']").click()
    driver.find_element_by_xpath("//span[text()='上传图片']").click()
    try:
        os.system(r'C:\Users\Administrator\Desktop\file\logo.exe')
        sleep(3)
        driver.find_element_by_class_name("upload-img")  # 检查是否有图片
        print (u"logo上传成功")
        sleep(2)
    except:
        print (u"logo上传失败")
    for list in range(4, 14):
        global txt
        mark=0
        if list == 4:  #选择归属部门
            driver.find_elements_by_class_name("el-cascader__label")[1].click()
            sleep(1)
            try:
                driver.find_element_by_xpath("//li[text()='组织机构_自动化公司0']").click()
            except:
                driver.find_element_by_xpath("//label[text()='归属单位与部门']").click()
        elif list == 5:  #姓名
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"用户",i)
        elif list == 6:  #登录名
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"yonghuming",i)
        elif list == 7:  #密码
            global mima
            mima="445566"
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(mima)
        elif list == 8:  #确认密码
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(mima)
        elif list == 9:  #邮箱
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys("y",i,"onghuming@sailfish.com.cn")
        elif list == 10: #电话
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys("020-433423",i)
        elif list == 11: #手机
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys("1562617932",i)
        elif list == 12: #职位
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"普通用户")
        elif list == 13: #工号
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys("001",i)
            mark=1
        if mark == 1:
           sleep(1)
           #选择用户类型
           driver.find_elements_by_xpath("//span[text()='普通用户']")[-1].click()
           #备注
           driver.find_element_by_class_name("el-textarea__inner").clear()
           driver.find_element_by_class_name("el-textarea__inner").send_keys(u"一位普通用户")
           driver.find_elements_by_xpath("//span[text()='确 定']")[1].click()
           time_1 = 3
           while (1):
               compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
               if len(compare) != len(delete):
                   print (u"用户创建成功")
                   break
               elif time_1 == 0 and len(compare) == len(delete):
                   print (u"用户创建失败")
                   break
               sleep(time_1)
               time_1 = time_1 - 1
           sleep(1)

def user_del(driver):
    mark = 0
    try:
        driver.find_element_by_xpath("//span[text()='用户管理']").click()
    except:
        pass
    sleep(1)
    delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
    while(len(delete) != 1):
        mark = 1
        driver.find_elements_by_xpath("//span[contains(text(),'删除')]")[1].click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='此操作将删除该用户, 是否继续?']").text
        print (del_text)
        driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            if len(compare) != len(delete):
                delete = compare
                print (u"用户删除成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"用户删除失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)
    if mark == 1:
        user_cd_del(driver)

def user_cd_del(driver):
    try:
        driver.find_element_by_xpath("//span[text()='查看已删除用户']").click()
    except:
        pass
    while(1):
        try:
            delete = driver.find_elements_by_xpath("//span[text()='彻底删除']")
            break
        except:
            pass
    while(len(delete) != 0):
        sleep(1)
        driver.find_element_by_xpath("//span[text()='彻底删除']").click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='此操作将彻底删除该用户, 是否继续?']").text
        print (del_text)
        driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
        sleep(1)
        compare = driver.find_elements_by_xpath("//span[text()='彻底删除']")
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[text()='彻底删除']")
            if len(compare) != len(delete):
                delete = compare
                print (u"用户彻底删除成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"用户彻底删除失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)
    try:
        driver.find_element_by_xpath("//span[text()='返回']").click()
    except:
        pass

def user(driver):
    for i in range(2):
        user_message(driver,i)