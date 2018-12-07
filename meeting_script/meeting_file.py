# -*- coding: utf-8 -*-
from time import sleep
import os
def meeting_file_add(driver):
    doc = r'C:\Users\Administrator\Desktop\file\file_docx.exe'
    pdf = r'C:\Users\Administrator\Desktop\file\file_pdf.exe'
    xlsx= r'C:\Users\Administrator\Desktop\file\file_xlsx.exe'
    txt = r'C:\Users\Administrator\Desktop\file\file_upload.exe'
    for list in range(6):
        while (1):
            try:
                driver.find_element_by_xpath("//span[text()='会议资料']").click()
                break
            except:
                pass
        sleep(1)
        row = driver.find_elements_by_class_name("el-table__row")
        while(1):
            try:
                driver.find_element_by_xpath("//span[text()='上传文件']").click()
                break
            except:
                driver.find_element_by_xpath("//span[text()='请上传']").click()
                break
                pass
        if list == 0 or list == 3:
            os.system(doc)
            text = "doc"
        if list == 1 or list == 4:
            os.system(pdf)
            text = "pdf"
        if list == 2 or list == 5:
            os.system(xlsx)
            text = "xlsx"
        # if list == 3 or list == 7:
        #     os.system(txt)
        #     text = "txt"
        time_1 = 4
        while (1):
            compare = driver.find_elements_by_class_name("el-table__row")
            if len(compare) != len(row):
                row = compare
                print (u"文件上传成功",text)
                break
            elif time_1 == 0 and len(compare) == len(row):
                print (u"文件上传失败或格式错误",text)
                break
            sleep(time_1)
            time_1 = time_1 - 1
        sleep(1)

def meeting_file_del(driver):
    while(1):
        try:
            driver.find_element_by_xpath("//span[text()='会议资料']").click()
            break
        except:
            pass
    sleep(1)
    row = driver.find_elements_by_class_name("el-checkbox__inner")
    while(row != 1):
        try:
            driver.find_element_by_class_name("el-checkbox__inner").click()
        except:
            break
        driver.find_element_by_xpath("//span[text()='批量删除']").click()
        try:
            del_text = driver.find_element_by_xpath("//p[text()='确定删除该文件？']").text
            print (del_text)
        except:
            pass
        driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[-1].click()



def meeting_file(driver):
    meeting_file_add(driver)
