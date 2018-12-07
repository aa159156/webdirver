# -*- coding: utf-8 -*-
from time import sleep
import os
def meeting_summary_add(driver):
    pdf  = r'C:\Users\Administrator\Desktop\file\file_pdf.exe'
    txt  = r'C:\Users\Administrator\Desktop\file\file_upload.exe'
    doc  = r'C:\Users\Administrator\Desktop\file\file_docx.exe'
    xlsx = r'C:\Users\Administrator\Desktop\file\file_xlsx.exe'
    image= r'C:\Users\Administrator\Desktop\file\logo.exe'
    rar  = r'C:\Users\Administrator\Desktop\flie\rar.exe'
    try:
        driver.find_element_by_xpath("//span[text()='会议纪要']").click()
    except:
        pass
    sleep(1)
    for list in range(5):
        try:
            delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            driver.find_element_by_xpath("//span[text()='上传文件']").click()
        except:
            pass
        if list == 0:
            os.system(image)
            text = "image"
        if list == 1:
            os.system(txt)
            text = "txt"
        if list == 2:
            os.system(pdf)
            text = "pdf"
        if list == 3:
            os.system(xlsx)
            text = "xlsx"
        if list == 4:
            os.system(doc)
            text = "doc"
        # if list == 5:
        #     os.system(rar)
        #     text = "rar"
        sleep(1)
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            if len(compare) != len(delete):
                print (u"纪要上传成功",text)
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"纪要上传失败",text)
                break
            sleep(time_1)
            time_1 = time_1 - 1
        meeting_summary_del(driver)
        sleep(1)

def meeting_summary_del(driver):
    try:
        driver.find_element_by_xpath("//span[text()='会议纪要']").click()
    except:
        pass
    sleep(1)
    delete = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
    while(len(delete) != 0):
        try:
            driver.find_element_by_xpath("//span[contains(text(),'删除')]").click()
            del_text = driver.find_element_by_xpath("//p[text()='确定删除该纪要？']").text
            driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()
            print (del_text)
        except:
            pass
        time_1 = 3
        while (1):
            compare = driver.find_elements_by_xpath("//span[contains(text(),'删除')]")
            if len(compare) != len(delete):
                delete = compare
                print (u"纪要删除成功")
                break
            elif time_1 == 0 and len(compare) == len(delete):
                print (u"纪要删除失败")
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)
def meeting_summary(driver):
    meeting_summary_add(driver)