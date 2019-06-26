# coding=utf-8
import time
from log import myLog
import random
def sleep(s):
    time.sleep(s)

def party_in_check(dr):
    """*********************文章类型为空**********************"""
    dr.Class_name_s_sendkey("el-input__inner","自动化文章标题", 5)  # 输入文章标题
    dr.frame("textEditDialog_ifr")
    dr.tag_name_sendkey("body", "自动化文章内容")  # 输入文章内容
    dr.frame_return()
    dr.XPaths_array_click("//span[text()='确 定']", 2)
    i = 1
    if dr.XPath_get("//div[contains(text(),'请选择目录')]"):
        print("文章类型不能为空")
        myLog.info("文章类型不能为空")
    else:
        print("与预期不符，文章类型可以为空")
        myLog.error("与预期不符，文章类型可以为空")

    """*********************文章标题为空**********************"""
    if i == 1:
        dr.XPaths_array_click("//span[text()='取 消']",2)
        dr.XPath_click("//span[text()='写文章']")
        dr.Class_name_s_click("el-input__inner", 6)
        dr.XPaths_array_click("//span[text()='党建活动']", -1)  # 选择文章类型
        dr.frame("textEditDialog_ifr")
        dr.tag_name_sendkey("body", "自动化文章内容")  # 输入文章内容
        dr.frame_return()
        dr.XPaths_array_click("//span[text()='确 定']", 2)
        i = 2
        if dr.XPath_get("//div[contains(text(),'请输入标题名称')]"):
            print("文章标题不能为空")
            myLog.info("文章标题不能为空")
        else:
            print("与预期不符，文章标题可以为空")
            myLog.error("与预期不符，文章标题可以为空")

    """*********************文章内容为空**********************"""
    if i == 2:
        dr.Class_name_s_sendkey("el-input__inner","自动化文章标题", 5)  # 输入文章标题
        dr.Class_name_s_click("el-input__inner", 6)
        dr.XPaths_array_click("//span[text()='党建活动']", -1)  # 选择文章类型
        dr.frame("textEditDialog_ifr")
        dr.tag_name_clear("body")  # 清空文章内容
        dr.tag_name_click("body")
        dr.frame_return()
        sleep(2)
        dr.XPaths_array_click("//span[text()='确 定']", 2)
        if dr.XPath_get("//p[contains(text(),'文章内容不能为空')]"):
            print("文章内容不能为空")
            myLog.info("文章内容不能为空")
        else:
            print("与预期不符，文章内容可以为空")
            myLog.error("与预期不符，文章内容可以为空")

def party_add(dr,title,content):  #文章类型(党建活动、学习资料、三会一课、主题党日)、标题、内容、是否发布
    # dr.XPath_click("//span[text()='党务管理']")
    # dr.XPath_click("//span[text()='党建内容']")
    for i in range(4):
        if   i == 0:
            type = "党建活动"
            send = random.choice([True, False])
        elif i == 1:
            type = "学习资料"
            send = random.choice([True, False])
        elif i == 2:
            type = "三会一课"
            send = random.choice([True, False])
        elif i == 3:
            type = "主题党日"
            send = random.choice([True, False])
        dr.XPath_click("//span[text()='写文章']")
        dr.Class_name_s_sendkey("el-input__inner",title + type,5)  #输入文章标题
        dr.Class_name_s_click("el-input__inner",6)
        dr.XPaths_array_click("//span[text()='"+ type +"']",-1)  #选择文章类型
        if   send == True:
            dr.XPath_click("//span[text()='是']")
        elif send == False:
            dr.XPath_click("//span[text()='否']")
        dr.frame("textEditDialog_ifr")
        dr.tag_name_sendkey("body",""+ content +"")   #输入文章内容
        dr.frame_return()
        dr.XPaths_array_click("//span[text()='确 定']",2)
        if dr.XPath_get("//span[text()='"+ title + type +"']"):
            print(""+ title + type +"创建成功")
            myLog.info(""+ title + type +"创建成功")
        else:
            print(""+ title + type +"创建失败")
            myLog.error("" + title + type + "创建失败")

def party_del(dr,title):
    # dr.XPath_click("//span[text()='党务管理']")
    # dr.XPath_click("//span[text()='党建内容']")
    dr.Class_name_s_sendkey("el-input__inner",title,2)
    dr.XPath_click("//span[text()='搜索文章']")
    delete = dr.XPaths_get("//span[text()='删除']")
    mark = len(delete)
    print("标题包含“自动化文章”的文章数量：",mark)
    for i in range(mark):
        dr.XPath_click("//span[text()='删除']")
        dr.XPath_click("//span[contains(text(),'确定')]")
    sleep(2)
    mark = dr.XPaths_get("//span[contains(text(),'自动化文章')]")
    if len(mark) == 0:
        print("标题包含“自动化文章”的文章数量：",len(mark))
        myLog.info("文章删除成功")
        print("文章删除成功")
    else:
        myLog.error("文章删除失败")
        print("文章删除失败")





