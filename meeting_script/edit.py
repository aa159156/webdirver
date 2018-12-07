# -*- coding: utf-8 -*-
from time import sleep
import os
#编辑信息
def edit_message(driver,list):
    mark=0
    if list == 0:  #姓名
        try:
            driver.find_element_by_xpath("//span[text()='上传图片']").click()
        except:
            pass
        try:
            driver.find_element_by_class_name("upload-img").click()
        except:
            pass
        try:
            os.system(r'C:\Users\Administrator\Desktop\file\logo.exe')
            sleep(3)
            driver.find_element_by_class_name("upload-img")  # 检查是否有图片
            print(u"logo上传成功")
            sleep(2)
        except:
            print(u"logo上传失败")
        data="admin1"
    elif list == 1:  #职位
        data=u"无职位"
    elif list == 2:  #工号
        data="007"
    elif list == 3:  #邮箱
        data="admin@sailfish.com.cn"
    elif list == 4:  #手机号码
        data="15521112604"
    elif list == 5:  #电话号码
        data="020-4321423"
    elif list == 6:  #备注
        data=u"平台管理员"
        mark=1
    driver.find_elements_by_class_name("el-input__inner")[list].clear()
    driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data)
    if mark == 1:
       driver.find_elements_by_xpath("//span[text()='确 定']")[1].click()
       sleep(1)

def edit(driver):
    driver.find_element_by_xpath("//span[text()='编辑信息']").click()
    sleep(1)
    for list in range(7):
        edit_message(driver,list)