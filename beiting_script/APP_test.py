# coding=utf-8
from appium import webdriver
# from app_brower import positioning
import time
def sleep(s):
    time.sleep(s)

deviceName = ["850ABM3PS9XY","CJL5T16114002069","FHC1SW10006B220233"]# 魅族，华为，PAD
appPackage = ["","","cn.com.sailfish.meeting"]
appActivity =["","",".MainActivity"]
desired_caps = {
                 'platformName':'Android',
                 'deviceName': deviceName[2],
                 'platformVersion':'6.0.1',
                 'appPackage':appPackage[2],
                 'appActivity':appActivity[2],
                 'noReset': True,
                 'unicodeKeyboard': True,
                 'resetKeyboard': True
               }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
# driver.find_element_by_xpath("//android.widget.Button[@text='允许']").click()
sleep(3)
driver.find_element_by_accessibility_id("进入会议").click()
mark = 0
while (driver.find_element_by_accessibility_id("会议资料")):
    driver.find_element_by_accessibility_id("会议资料").click()
    sleep(2)
    while(1):
        driver.tap([(2096,721)])
        sleep(1)
        driver.tap([(1777,713)])
        mark = mark + 1
        print("发送次数：",mark)
        sleep(6)

# sleep(2)
# driver.press_keycode(7)
# driver.find_element_by_accessibility_id("下一步").click()
# driver.find_element_by_xpath("//*[@text=巧文/choovin]").click()
# sleep(2)
# driver
# driver.find_element_by_id("com.tencent.mm:id/alm").send_keys("你好")
sleep(5)
driver.close_app()