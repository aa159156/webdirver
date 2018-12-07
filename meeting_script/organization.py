# -*- coding: utf-8 -*-
from time import sleep
import os
import logging
def organization_add(driver,i):
    while(1):
        sleep(1)
        try:
            driver.find_element_by_xpath("//span[text()='组织机构管理']").click()
            break
        except:
            pass
    guanli = driver.find_element_by_xpath("//span[text()='组织机构管理']")
    delete = guanli.find_elements_by_xpath("//span[text()='删除']")
    driver.find_element_by_xpath("//span[text()='添加机构']").click()
    sleep(1)
    mark = 0
    for list in range(1,13):
        if list == 1:
            driver.find_element_by_xpath("//span[text()='上传图片']").click()
            try:
                os.system(r'C:\Users\Administrator\Desktop\file\logo.exe')
                sleep(3)
                driver.find_element_by_class_name("upload-img")  # 检查是否有图片
                #print u"logo上传成功"
                logging.info('logo上传成功')
                sleep(2)
            except:
                #print u"logo上传失败"
                logging.warning('logo上传失败')
        elif list == 2:   #机构名称
            data=u"组织机构_自动化公司"
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data,i)
        # elif list == 3:  #上级机构
        #       driver.find_element_by_class_name("el-cascader__label").click()
        #       sleep(1)
        #       try:
        #           xiala=driver.find_element_by_xpath("//div[@x-placement='bottom-start']")
        #           xiala.find_element_by_xpath("//li[@id='menu-6544-0-0']").click()
        #       except:
        #           driver.find_element_by_xpath("//label[text()='上级机构']").click()
        elif list == 4:  #机构编码
              data = "0000-0000"
              driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data)
              sleep(1)
        elif list == 5:  #机构类型
              driver.find_elements_by_class_name("el-input__inner")[list].click()
              sleep(1)
              driver.find_elements_by_xpath("//span[text()='公司']")[-1].click()
              sleep(1)
        elif list == 6:  #联系地址
              data = u"广东省广州市白云区"
              driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data)
        elif list == 7:  #邮政编码
              data = "522000"
              driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data)
        elif list == 9:  #电话
              data = "0663-865432"
              driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data,i)
        elif list == 11: #邮箱
              data = "jigou@jigou.com.cn"
              driver.find_elements_by_class_name("el-input__inner")[list].send_keys(i,data)
        elif list == 12: #备注
              data = u"一家公司"
              driver.find_elements_by_class_name("el-input__inner")[list].send_keys(data)
              mark=1
        if mark == 1:
            driver.find_elements_by_xpath("//span[text()='确 定']")[1].click()
            time_1 = 3
            while (1):
                compare = guanli.find_elements_by_xpath("//span[text()='删除']")
                if len(compare) != len(delete):
                    delete = compare
                    print (u"组织机构创建成功")
                    break
                elif time_1 == 0 and len(compare) == len(delete):
                    print (u"组织机构创建失败")
                    break
                sleep(time_1)
                time_1 = time_1 - 1
            sleep(1)

def organization_del(driver):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='组织机构管理']").click()
            break
        except:
            pass
    sleep(2)
    delete = driver.find_elements_by_xpath("//span[text()='删除']")
    sleep(1)
    while(len(delete) != 0):
        driver.find_element_by_xpath("//span[text()='删除']").click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='确定要删除此项机构？']").text
        print (del_text)
        driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
        time_1 = 3
        while(1):
            compare = driver.find_elements_by_xpath("//span[text()='删除']")
            if len(compare) != len(delete):
                delete = compare
                print (u"组织机构删除成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"组织机构删除失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)
def organization(driver):
    for i in range(2):
        organization_add(driver,i)
    # organization_del(driver)