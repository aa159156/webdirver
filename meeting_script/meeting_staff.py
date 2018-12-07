# -*- coding: utf-8 -*-
from time import sleep
def meeting_staff(driver):
    driver.find_element_by_xpath("//span[text()='参会人员']").click()
    sleep(2)
    driver.find_element_by_xpath("//span[text()='选择参会人员']").click()
    sleep(1)
    row = driver.find_elements_by_class_name("el-table__row")
    if row:
        try:
            driver.find_element_by_class_name("el-checkbox__inner").click()
            driver.find_element_by_xpath("//span[text()='添加至会议']").click()
            driver.find_element_by_xpath("//span[text()='固定坐席']").click()
        except:
            pass
    sleep(1)
    driver.find_element_by_xpath("//span[text()='返回参会人员列表']").click()
    sleep(2)
    box = driver.find_elements_by_class_name("el-table__row")
    driver.find_element_by_xpath("//span[text()='修改座位号']").click()
    box = len(box)+1
    for list in range(1,box):
        try:
            driver.find_elements_by_class_name("el-input__inner")[list].clear()
            driver.find_elements_by_class_name("el-input__inner")[list].send_keys(list)
        except:
            pass
            sleep(1)
    driver.find_element_by_xpath("//span[text()='保存座位号']").click()
