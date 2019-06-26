#coding=UTF-8
from log import myLog
import time

def sleep(s):
    time.sleep(s)

def health_feedback_add(dr)
    dr.XPath_click("//div[text()='卫生反馈']")
    dr.XPath_click("//div[text()='新增反馈']")
    dr.class_name_s_sendkey("el-input__inner",5)