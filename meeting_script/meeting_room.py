# -*- coding: utf-8 -*-
from time import sleep
import os
def meeting_room_add(driver,data,i):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议室管理']").click()
            break
        except:
            pass
    guanli = driver.find_element_by_xpath("//span[text()='会议室管理']")
    delete = guanli.find_elements_by_xpath("//span[contains(text(),'删除')]")
    driver.find_element_by_xpath("//span[text()='添加会议室']").click()
    sleep(1)
    for list in range(2):
        driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data[list],i)
        sleep(1)
    if list == 1:
        driver.find_element_by_xpath("//span[text()='上传图片']").click()
        try:
            os.system(r'C:\Users\Administrator\Desktop\file\meeting_room_image.exe')
            sleep(3)
            driver.find_element_by_class_name("upload-img")  #检查是否有图片
            print (u"座位图上传成功")
            sleep(2)
        except:
            print (u"座位图上传失败")
        driver.find_elements_by_xpath("//span[text()='确 定']")[1].click()
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            if len(compare) != len(delete):
                delete = compare
                print (u"会议室创建成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"会议室创建失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)

def meeting_room_del(driver,data):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议室管理']").click()
            break
        except:
            pass
    sleep(2)
    delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
    sleep(1)
    while(len(delete) != 0):
        driver.find_element_by_xpath("//span[contains(text(),'删除')]").click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='此操作将删除该会议室, 是否继续?']").text
        print (del_text)
        driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
        time_1 = 2
        while (1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            if len(compare) != len(delete):
                delete = compare
                print (u"会议室删除成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"会议室删除失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)

def meeting_room(driver,mark):
    data = [u"自动化会议室",12]#会议室名称 会议室座位号
    if mark == 0:
        for i in range(2):
            meeting_room_add(driver,data,i)
    if mark == 1:
         meeting_room_del(driver,data)
