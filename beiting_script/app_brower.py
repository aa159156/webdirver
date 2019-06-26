# coding=utf-8
from appium import webdriver
import time

class positioning:
    def __init__(self,desired_caps):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def wait(self,time):
        self.driver.implicitly_wait(time)

    def accessibility_id_sendkey(self,id,data):
        element = self.driver.find_element_by_accessibility_id(id)
        element.send_key(data)

    def accessibility_id_click(self,id):
        element = self.driver.find_element_by_accessibility_id(id)
        element.click()

    def XPath_click(self,xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()