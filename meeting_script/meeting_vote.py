# -*- coding: utf-8 -*-
from time import sleep
def meeting_vote_add(driver):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议投票']").click()
            break
        except:
            pass
    sleep(2)
    delete = driver.find_elements_by_xpath("//span[text()='删除']")
    driver.find_element_by_xpath("//span[text()='新建投票']").click()
    sleep(1)
    driver.find_elements_by_class_name("el-input__inner")[3].clear()      # 投票主题
    driver.find_elements_by_class_name("el-input__inner")[3].send_keys(u"自动化会议投票")
    driver.find_elements_by_xpath("//span[text()='开']")[0].click()    #投票显示
    driver.find_elements_by_xpath("//span[text()='关']")[1].click()    #投票匿名
    driver.find_element_by_class_name("el-textarea__inner").clear()  #备注
    driver.find_element_by_class_name("el-textarea__inner").send_keys(u"这是一个会议投票")
    driver.find_element_by_xpath("//span[text()='保存']").click()
    sleep(1)
    time_1 = 3
    while (1):
        compare = driver.find_elements_by_xpath("//span[text()='删除']")
        if len(compare) != len(delete):
            delete = compare
            print (u"投票创建成功")
            break
        elif time_1 == 0 and len(compare) == len(delete):
            print (u"投票创建失败")
            break
        sleep(time_1)
        time_1 = time_1 - 1
    try:
        driver.find_element_by_xpath("//span[text()='会议投票']").click()
    except:
        pass
    sleep(1)
    driver.find_element_by_xpath("//span[text()='新建投票']").click()
    sleep(1)
    delete = driver.find_elements_by_xpath("//span[text()='删除']")
    driver.find_elements_by_class_name("el-input__inner")[3].clear()       # 投票主题
    driver.find_elements_by_class_name("el-input__inner")[3].send_keys(u"自动化会议投票_1")
    driver.find_elements_by_class_name("el-input__inner")[4].click()
    sleep(1)
    driver.find_element_by_xpath("//span[text()='自定义']").click()
    sleep(1)
    driver.find_elements_by_class_name("el-input__inner")[6].clear()    #选项内容
    driver.find_elements_by_class_name("el-input__inner")[6].send_keys(u"自动化会议投票_内容")
    for list in range(7,9):
        driver.find_element_by_class_name("el-icon-circle-plus").click()   #添加选项内容
        driver.find_elements_by_class_name("el-input__inner")[list].clear()  #选项内容
        driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"自动化会议投票_内容")
    driver.find_elements_by_xpath("//span[text()='关']")[0].click()    #投票显示
    driver.find_elements_by_xpath("//span[text()='开']")[1].click()    #投票匿名
    driver.find_element_by_class_name("el-textarea__inner").clear()  #备注
    driver.find_element_by_class_name("el-textarea__inner").send_keys(u"这是一个会议投票")
    driver.find_element_by_xpath("//span[text()='保存']").click()
    time_1 = 3
    while (1):
        compare = driver.find_elements_by_xpath("//span[text()='删除']")
        if len(compare) != len(delete):
            delete = compare
            print (u"投票创建成功")
            break
        elif time_1 == 0 and len(compare) == len(delete):
            print (u"投票创建失败")
            break
        sleep(time_1)
        time_1 = time_1 - 1

    sleep(1)

def meeting_vote_del(driver):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议投票']").click()
            break
        except:
            pass
        sleep(2)
        delete = driver.find_elements_by_xpath("//span[text()='删除']")
        while(len(delete) != 0):
            driver.find_element_by_xpath("//span[text()='删除']").click()
            sleep(1)
            del_text = driver.find_element_by_xpath("//p[text()='此操作将永久删除该投票, 是否继续']").text
            print (del_text)
            driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
            time_1 = 3
            while (1):
                compare = driver.find_elements_by_xpath("//span[text()='删除']")
                if len(compare) != len(delete):
                    delete = compare
                    print (u"投票创建成功")
                    break
                elif time_1 == 0 and len(compare) == len(delete):
                    print (u"投票创建失败")
                    break
                sleep(time_1)
                time_1 = time_1 - 1
            sleep(1)

def meeting_vote(driver):
    for i in range(1):
        meeting_vote_add(driver)
    #meeting_vote_del(driver)