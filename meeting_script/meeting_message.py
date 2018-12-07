# -*- coding: utf-8 -*-
from time import sleep
def meeting_message_add(driver):
    try:
        driver.find_element_by_xpath("//span[text()='消息管理']").click()
    except:
        pass
    sleep(1)
    delete = driver.find_elements_by_xpath("//span[text()='删除']")
    for i in range(1,4):
        if   i == 1:
            txt=u"通知"
        elif i == 2:
            txt=u"及时通知"
        else:
            txt=u"公告"
        driver.find_element_by_xpath("//span[text()='添加消息']").click()
        driver.find_elements_by_class_name("el-input__inner")[3].clear()   #消息标题
        driver.find_elements_by_class_name("el-input__inner")[3].send_keys(u"会议消息通知_",txt)
        if i == 3:
            driver.find_elements_by_class_name("el-input__inner")[4].click()   #选择消息类型
            sleep(1)
            driver.find_elements_by_xpath("//span[text()='公告']")[-1].click()
            sleep(1)
        if i == 2:
            driver.find_element_by_class_name("el-switch__core").click()       #是否及时发送
        driver.find_element_by_class_name("el-textarea__inner").clear()
        driver.find_element_by_class_name("el-textarea__inner").send_keys(u"消息通知：春节放假时间")
        try:
            driver.find_element_by_xpath("//span[text()='创建']").click()
        except:
            pass
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[text()='删除']")
            if len(compare) != len(delete):
                delete = compare
                print (u"消息通知_",txt,u"创建成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"消息通知_",txt,u"创建失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)

def meeting_message_del(driver):
    try:
        driver.find_element_by_xpath("//span[text()='消息管理']").click()
    except:
        pass
    sleep(2)
    #删除通知类消息
    driver.maximize_window()
    for i in range(2):
        if i == 0:
            txt = u"通知"
            driver.find_element_by_class_name("el-input__inner").click()
            sleep(1)
            driver.find_elements_by_xpath("//span[text()='通知']")[-1].click()
            sleep(2)
        else:
            txt = u"公告"
            driver.find_element_by_class_name("el-input__inner").click()
            sleep(1)
            driver.find_elements_by_xpath("//span[text()='公告']")[-1].click()
            sleep(1)
        delete = driver.find_elements_by_xpath("//span[text()='删除']")
        while(len(delete) != 0):
                driver.find_element_by_xpath("//span[text()='删除']").click()
                sleep(1)
                del_text = driver.find_element_by_xpath("//p[text()='确定删除该消息?']").text
                print (del_text)
                driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
                time_1 = 3
                while(1):
                    compare = driver.find_elements_by_xpath("//span[text()='删除']")
                    if len(compare) != len(delete):
                        delete = compare
                        print (u"删除成功",txt,i)
                        break
                    elif time_1 == 0 and len(compare) == len(delete):
                        print (u"删除失败",txt,i)
                        break
                    sleep(time_1)
                    time_1 = time_1 - 1
                sleep(1)
    sleep(1)
def meeting_message(driver):
    meeting_message_add(driver)
    #meeting_message_del(driver)