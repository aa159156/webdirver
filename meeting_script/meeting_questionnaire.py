# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def meeting_questionnaire_add(driver):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议问卷']").click()
            driver.find_element_by_xpath("//span[text()='新建问卷']").click()
            break
        except:
            pass
    sleep(1)
    driver.find_elements_by_class_name("el-input__inner")[3].clear()  #问卷主题
    driver.find_elements_by_class_name("el-input__inner")[3].send_keys(u"会议问卷_主题")
    driver.find_elements_by_class_name("el-input__inner")[4].clear()  #问卷副主题
    driver.find_elements_by_class_name("el-input__inner")[4].send_keys(u"会议问卷_副主题")
    driver.find_element_by_class_name("el-textarea__inner").clear()   #问卷说明
    driver.find_element_by_class_name("el-textarea__inner").send_keys(u"该会议投票的说明")
    driver.find_element_by_xpath("//span[text()='新建']").click()
    sleep(1)
    driver.find_elements_by_xpath("//span[text()='查看详情']")[-1].click()
    sleep(1)
    delete = driver.find_elements_by_xpath("//span[text()='删除']")
    for i in range(3):
        if i % 2 == 0:
            txt=u"多选"
            type = 2
        else:
            txt=u"单选"
            type = 1
        driver.find_element_by_xpath("//span[text()='新建问题']").click()
        sleep(1)
        driver.find_elements_by_class_name("el-input__inner")[0].clear()  #问卷问题题目
        driver.find_elements_by_class_name("el-input__inner")[0].send_keys(u"问卷问题_题目",txt)
        driver.find_elements_by_class_name("el-input__inner")[1].click()
        sleep(1)
        if type == 2:
            try:
                driver.find_element_by_xpath("//span[text()='多选']").click()
            except:
                pass
        else:
            try:
                driver.find_element_by_xpath("//span[text()='单选']").click()
            except:
                pass
        sleep(1)
        driver.find_elements_by_class_name("el-input__inner")[2].clear()  #问题选项内容
        driver.find_elements_by_class_name("el-input__inner")[2].send_keys(u"问卷问题_内容",txt)
        for list in range(3,5):
            driver.find_element_by_class_name("el-icon-circle-plus").click()  # 添加选项内容
            driver.find_elements_by_class_name("el-input__inner")[list].clear()  # 问题选项内容
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(u"问卷问题_内容",txt,list)
        driver.find_element_by_xpath("//span[text()='创建']").click()
        sleep(1)
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[text()='删除']")
            if len(compare) != len(delete):
                delete = compare
                print (u"问卷问题创建成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"问卷问题创建失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
    driver.find_element_by_xpath("//span[text()='返回']").click()
    sleep(1)

def meeting_questionnaire_del(driver):
        #删除问卷问题
        try:
            driver.find_element_by_xpath("//span[text()='会议问卷']").click()
        except:
            pass
        sleep(2)
        xq = driver.find_elements_by_xpath("//span[text()='查看详情']")
        if len(xq) == 0:
           print (u"没有问卷")
        else:
            while(1):
                try:
                    driver.find_element_by_xpath("//span[text()='查看详情']").click()
                    break
                except:
                    pass
            sleep(2)
            delete = driver.find_elements_by_xpath("//span[text()='删除']")
            while (len(delete) != 0):
                driver.find_element_by_xpath("//span[text()='删除']").click()
                sleep(1)
                del_text = driver.find_element_by_xpath("//p[text()='确定删除该问题？']").text
                print (del_text)
                driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
                time_1 = 3
                while (1):
                    compare = driver.find_elements_by_xpath("//span[text()='删除']")
                    if len(compare) != len(delete):
                        delete = compare
                        print (u"问卷问题删除成功")
                        break
                    elif time_1 == 0 and len(compare) == len(delete):
                        print (u"问卷问题删除失败")
                        break
                    sleep(time_1)
                    time_1 = time_1 - 1
                sleep(1)
            driver.find_element_by_xpath("//span[text()='返回']").click()
        sleep(1)
        #删除问卷
        driver.find_element_by_xpath("//span[text()='会议问卷']").click()
        delete = driver.find_elements_by_xpath("//span[text()='删除']")
        while (len(delete) != 0):
            driver.find_element_by_xpath("//span[text()='删除']").click()
            sleep(1)
            del_text = driver.find_element_by_xpath("//p[text()='确定删除该问卷？']").text
            print (del_text)
            driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
            time_1 = 3
            while (1):
                compare = driver.find_elements_by_xpath("//span[text()='删除']")
                if len(compare) != len(delete):
                    delete = compare
                    print (u"问卷删除成功")
                    break
                elif time_1 == 0 and len(compare) == len(delete):
                    print (u"问卷删除失败")
                    break
                sleep(time_1)
                time_1 = time_1 - 1
                sleep(1)
        sleep(1)

def meeting_questionnaire_open_del(driver):
    try:
        driver.find_element_by_xpath("//span[text()='会议问卷']").click()
    except:
        pass
    sleep(1)
    driver.find_element_by_xpath("//span[text()='查看详情']").click()
    sleep(1)
    WebDriverWait(driver, 10,0.2).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='删除']"))).click()
    WebDriverWait(driver, 10,0.2).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'确定')]"))).click()
    element_1 = WebDriverWait(driver, 5, 0.2).until(EC.presence_of_element_located((By.XPATH, "//p[text()='删除失败，当前问卷已开启']"))).text
    print(element_1)
    sleep(2)
    driver.find_element_by_xpath("//span[text()='返回']").click()
    sleep(1)
    WebDriverWait(driver, 10,0.2).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='删除']"))).click()
    WebDriverWait(driver, 10,0.2).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'确定')]"))).click()
    open_del = WebDriverWait(driver, 5, 0.2).until(EC.presence_of_element_located((By.XPATH, "//p[text()='删除失败，当前问卷已开启']"))).text
    print(open_del)
    sleep(1)
def meeting_questionnaire(driver):
    meeting_questionnaire_add(driver)
    #meeting_questionnaire_del(driver)