# -*- coding: utf-8 -*-
from time import sleep
def meeting_type_add(driver,data,i):
    while(1):
        sleep(1)
        try:
            driver.find_element_by_xpath("//span[text()='会议类型管理']").click()
            break
        except:
            pass
    sleep(2)
    driver.refresh()
    delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")  #创建前，用于compare创建后的对比
    while(1):
        sleep(1)
        try:
            driver.find_element_by_xpath("//span[text()='添加会议类型']").click()
            break
        except:
            pass
    #会议类型名称
    driver.find_elements_by_class_name("el-input__inner")[-2].send_keys(data[0],i)
    #会议类型描述
    driver.find_elements_by_class_name("el-input__inner")[-1].send_keys(data[1],i)
    #会议类型备注
    driver.find_element_by_class_name("el-textarea__inner").send_keys(u"会议类型_备注")
    sleep(1)
    driver.find_elements_by_xpath("//span[text()='确 定']")[1].click()
    time_1 = 3
    while (1):
        compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
        if len(compare) != len(delete):
            delete = compare
            print (u"会议类型创建成功")
            break
        elif time_1 == 0 and len(compare) == len(delete):
            print (u"会议类型创建失败")
            break
        sleep(time_1)
        time_1 = time_1 - 1
        sleep(1)
    sleep(1)

def meeting_type_del(driver,data):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议类型管理']").click()
            break
        except:
            pass
    sleep(2)
    delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
    while(len(delete) != 0):
        driver.find_element_by_xpath("//span[contains(text(),'删除')]").click()
        sleep(1)
        del_text = driver.find_element_by_xpath("//p[text()='此操作将删除该会议类型, 是否继续?']").text
        print (del_text)
        driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            if len(compare) != len(delete):
                delete = compare
                print (u"会议类型删除成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"会议类型删除失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)
def meeting_type(driver,mark):
    data= [u"自动化会议类型", u"会议类型_描述"]
    if mark == 0:
        for i in range(2):
            meeting_type_add(driver,data,i)
    if mark == 1:
        meeting_type_del(driver,data)