# coding=UTF-8
from log import myLog
import time

def sleep(s):
    time.sleep(s)

"""******************卫生片区创建************************"""
def health_area_add(dr):
    dr.XPath_click("//div[text()='卫生片区']")
    dr.XPath_click("//span[text()='片区管理']")
    dr.XPath_click("//span[text()='新增片区']")
    for i in range(3):
        if i == 0:
            dr.XPaths_array_click("//span[text()='确 定']",2)
            if dr.XPath_get("//div[contains(text(),'请输入片区名称')]"):
                print("片区名称不能为空")
                myLog.info("片区名称不能为空")
            else:
                print("与预期不同，没有提示请输入片区名称")
                myLog.error("与预期不同，没有提示请输入片区名称")
            dr.XPaths_array_click("//span[text()='取 消']",2)
        elif i == 1:
            dr.XPath_click("//span[text()='新增片区']")
            dr.Class_name_sendkey("el-input__inner","自动化片区一区")
            dr.XPaths_array_click("//span[text()='确 定']", 2)
            if dr.XPath_get("//span[text()='自动化片区一区']"):
                    print("卫生片区创建成功")
                    myLog.info("卫生片区创建成功")
            else:
                    print("卫生片区创建失败")
                    myLog.error("卫生片区创建失败")
                    raise
        elif i == 2:
            sleep(3)
            dr.XPath_click("//span[text()='新增片区']")
            dr.Class_name_sendkey("el-input__inner","自动化片区二区")
            dr.XPaths_array_click("//span[text()='确 定']", 2)
            if dr.XPath_get("//span[text()='自动化片区二区']"):
                    print("卫生片区创建成功")
                    myLog.info("卫生片区创建成功")
            else:
                    print("卫生片区创建失败")
                    myLog.error("卫生片区创建失败")
                    raise

"""******************卫生片区修改************************"""
def health_area_alter(dr):
    dr.XPaths_array_click("//span[text()='修改片区']",-1)
    dr.Class_name_s_sendkey("el-input__inner","自动化片区二区_修改",1)
    dr.XPaths_array_click("//span[text()='确 定']", -1)
    if dr.XPath_get("//span[text()='自动化片区二区_修改']"):
        print("卫生片区修改成功")
        myLog.info("卫生片区修改成功")
    else:
        print("卫生片区创建失败")
        myLog.error("卫生片区修改失败")
        raise

"""******************修改地址关联的片区************************"""
def site_area_alter(dr):
    dr.XPath_click("//div[text()='卫生片区']")
    if dr.XPath_get("//span[text()='返回']"):
         dr.XPath_click("//span[text()='返回']")
    dr.XPath_click("//span[text()='修改所处片区']")
    dr.Class_name_s_click("el-input__suffix",-1)
    # dr.XPaths_array_click("//input[text()='请选择' and ]",-1)
    dr.XPaths_array_click("//span[text()='自动化片区一区']",-1)
    dr.XPaths_array_click("//span[text()='确 定']",-1)
    if dr.XPath_get("//span[text()='自动化片区一区']"):
        if dr.XPath_get("//span[text()='修改所处片区']"):
            print("修改所处片区成功")
            myLog.info("修改所处片区成功")
        else:
            print("修改所处片区失败")
            myLog.error("修改所处片区失败")
            raise

"""******************卫生片区删除************************"""
def health_area_del(dr):
    dr.XPath_click("//div[text()='卫生片区']")
    if dr.XPath_get("//span[text()='片区管理']"):
        dr.XPath_click("//span[text()='片区管理']")
    for i in range(2):
        delete = dr.XPaths_get("//span[text()='删除']")
        dr.XPaths_array_click("//span[text()='删除']",-1)
        dr.XPaths_array_click("//span[contains(text(),'确定')]", -1)
        sleep(2)
        compare = dr.XPaths_get("//span[text()='删除']")
        if len(delete) != len(compare):
            print("片区删除成功")
            myLog.info("片区删除成功")
        else:
            print("片区删除失败")
            myLog.error("片区删除失败")
            raise






