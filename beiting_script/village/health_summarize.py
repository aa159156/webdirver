# coding=utf-8
import operator
from PIL import Image
import time
from log import myLog
def sleep(s):
    time.sleep(s)
"""***************卫生管理概述****************"""
def health_summarize(dr,content):
    dr.XPath_click("//span[text()='编辑信息']")
    dr.frame(dr.XPath_get("//iframe[@allowtransparency='true']"))
    dr.tag_name_clear("body")  # 输入文章内容
    dr.tag_name_click("body")  # 输入文章内容
    dr.frame_return()
    dr.XPaths_array_click("//span[text()='确 定']", -1)
    if dr.XPath_get("//p[text()='内容不能为空']"):
        print("内容不能为空")
        myLog.info("内容不能为空")
    else:
        print("与预期不符，内容可以为空")
        myLog.error("与预期不符，内容可以为空")
        raise
    dr.frame(dr.XPath_get("//iframe[@allowtransparency='true']"))
    dr.tag_name_sendkey("body", content)  # 输入文章内容
    dr.frame_return()
    dr.XPaths_array_click("//span[text()='确 定']",-1)
    sleep(5)
    dr.screenshot(r"C:\Users\Administrator\Desktop\beiting_script\image\卫生管理概述.png")
    expect = Image.open(r"C:\Users\Administrator\Desktop\beiting_script\image\卫生管理概述True.png")
    practical = Image.open(r"C:\Users\Administrator\Desktop\beiting_script\image\卫生管理概述.png")
    Image_1 = operator.eq(expect,practical)
    if Image_1 == True:
        print("图片比对结果相同，修改卫生管理概述成功")
        myLog.info("图片比对结果相同，修改卫生管理概述成功")
    else:
        print("图片比对结果不同，修改卫生管理概述失败")
        myLog.error("图片比对结果不同，修改卫生管理概述失败")