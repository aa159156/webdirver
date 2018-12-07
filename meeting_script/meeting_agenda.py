# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os
def meeting_agenda_add(driver):
    doc = r'C:\Users\Administrator\Desktop\file\file_docx.exe'
    pdf = r'C:\Users\Administrator\Desktop\file\file_pdf.exe'
    xlsx= r'C:\Users\Administrator\Desktop\file\file_xlsx.exe'
    txt = r'C:\Users\Administrator\Desktop\file\file_upload.exe'
    list = 1
    list_1 = 2
    while(1):
        try:
            driver.find_element_by_xpath( "//span[text()='会议议程']").click()
            driver.find_element_by_xpath("//li[contains(text(),'编辑议程')]").click()
            break
        except:
            pass
    # 添加议题排序与标题
    sleep(2)
    driver.find_elements_by_class_name("el-input__inner")[list].send_keys("1")
    driver.find_elements_by_class_name("el-input__inner")[list_1].send_keys(u"议题_1")
    for rank in range(2,5):
        list = list + 2
        list_1 = list_1 + 2
        if rank == 2:
            file = pdf
        elif rank == 3:
            file = txt
        else: file = doc
        driver.find_element_by_xpath("//a[text()='请上传']").click()
        try:
            os.system(file)
            print (u"文件上传成功")
        except:
            print (u"文件上传失败")
        sleep(1)
        while(1):
            try:
                driver.find_element_by_xpath("//i[text()='添加行']").click()
                break
            except:
                pass
        sleep(1)
        driver.find_elements_by_class_name("el-input__inner")[list].clear()
        driver.find_elements_by_class_name("el-input__inner")[list].send_keys(rank)
        driver.find_elements_by_class_name("el-input__inner")[list_1].clear()
        driver.find_elements_by_class_name("el-input__inner")[list_1].send_keys(u"议题_",rank)
        sleep(1)
    try:
        driver.find_element_by_xpath("//span[text()='保存']").click()
    except:
        pass
    try:
        driver.find_element_by_class_name("el-table__row")
        print (u"议程创建成功")
    except:
        print (u"议程创建失败")
    sleep(2)
def meeting_agenda_del(driver):
    while(1):
        try:
            driver.find_element_by_xpath( "//span[text()='会议议程']").click()
            driver.find_element_by_xpath("//li[contains(text(),'编辑议程')]").click()
            break
        except:
            pass
    sleep(2)
    delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
    while(len(delete) != 0):
        while(1):
            try:
                driver.find_elements_by_xpath("//span[contains(text(),'删除')]")[-1].click()
                break
            except:
                pass
        text=driver.find_element_by_xpath("//p[text()='确定删除该议题？']").text
        print (text)
        driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            if len(compare) != len(delete):
                delete = compare
                #print u"议程删除成功"
                break
            elif time_1 == 0 and len(compare) == len(delete):
                #print u"议程删除失败"
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(2)
    driver.find_element_by_xpath("//span[text()='取消']").click()
    sleep(1)
    try:
        driver.find_element_by_class_name("el-table__row")
        print (u"议程删除失败")
    except:
        print (u"议程删除成功")
    sleep(1)

def meeting_agenda_open_del(driver):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议议程']").click()
            driver.find_element_by_xpath("//li[contains(text(),'编辑议程')]").click()
            break
        except:
            pass
    sleep(1)
    driver.find_elements_by_xpath("//span[contains(text(),'删除')]")[-1].click()
    element = WebDriverWait(driver,5,0.2).until(EC.presence_of_element_located((By.XPATH,"//p[text()='会议正在进行中，不允许删除会议议程']")))
    text = element.text
    print(text)

def meeting_agenda(driver):
    meeting_agenda_add(driver)
    #meeting_agenda_del(driver)