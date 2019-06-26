#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.select import Select
from enum import Enum
from log import myLog
import time

'''
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

BrowserType = enum("CHROME", "FIREFOX", "IE")
'''
n = 2
def sleep(second):
    time.sleep(second)

class BrowserType(Enum):
    CHROME = 1
    FIREFOX = 2
    IE = 3

class BrowserHacker:
    def __init__(self, type = BrowserType.CHROME, proxy = None, dimension = None):
        '''
        proxy : "HOST_IP:PORT" like "127.0.0.1:1080"
        dimension: windows dimension, values like "(800, 500)"; None is maximum
        '''
        if type == BrowserType.FIREFOX:
            profile = None
            if (proxy is not None):
                profile = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': proxy,
                'ftpProxy': proxy,
                'sslProxy': proxy,
                'noProxy':''})
            self.driver = webdriver.Firefox(proxy = profile)
        elif type == BrowserType.CHROME:
            self.driver = webdriver.Chrome()
        elif type == BrowserType.IE:
            self.driver = webdriver.Ie()
        else:
            print ("unknown driver type of " + type)

        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)
        if dimension is None:
            self.driver.maximize_window()
        else:
            self.driver.set_window_rect(0, 0, *dimension)
        self._isReady = False
        self.absoluteOffsetY = 0
        self.absoluteOffsetX = 0
        self.viewWidth = 0
        self.viewHeight = 0
    def driver_d(self,driver):
        self.driver = driver
        print("#############")

    def open(self,url = "https://www.baidu.com"):
        try:
            self.driver.get(url)
            self.viewWidth = self.driver.execute_script('return window.innerWidth;')
            self.viewHeight = self.driver.execute_script('return window.innerHeight;')
            self.absoluteOffsetY = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
            self.absoluteOffsetX = self.driver.execute_script('return window.outerWidth - window.innerWidth;')
            self._isReady = True
        except TimeoutException as ex:
            print ("Error: open url " + url + " encount an timeout exception")
            self._isReady = False
        return self._isReady

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def input(self, element, text):
        element.clear()
        element.send_keys(text)
		
    def waitUtilElementPresentByClassName(self, class_name):
        try:
            self._wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        except TimeoutException as ex:
            return False
        return True 

    def waitUtilElementPresent(self, id_tag):
        try:
            self._wait.until(EC.presence_of_element_located((By.ID, id_tag)))
        except TimeoutException as ex:
            return False
        return True 

    def waitUtilElementTextContains(self, id_tag, value):
        try:
            self._wait.until(EC.text_to_be_present_in_element((By.ID, id_tag), value))
        except TimeoutException as ex:
            return False
        return True

    def waitUtilElementTextContainsByClassName(self, class_name, value):
        try:
            self._wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, class_name), value))
        except TimeoutException as ex:
            return False
        return True

    """***************find_element_by_tag_name******************"""
    def tag_name_sendkey(self,id_tag,data):
        for i in range(n):
            try:
                element = self.driver.find_element_by_tag_name(id_tag)
                element.clear()
                element.send_keys(data)
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)

    def tag_name_clear(self,id_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_tag_name(id_tag)
                element.clear()
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)

    def tag_name_click(self,id_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_tag_name(id_tag)
                element.click()
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)
    """***************find_element_by_id******************"""
    def Id_get(self,id_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_id(id_tag)
                return element
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)
				

    def Id_click(self,id_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_id(id_tag)
                element.click()
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)

    def Id_claer(self,id_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_id(id_tag)
                element.clear()
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)

    def Id_sendkey(self,id_tag,data):
        for i in range(n):
            try:
                element = self.driver.find_element_by_id(id_tag)
                element.clear()
                element.send_keys(data)
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)

    def Id_text(self,id_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_id(id_tag)
                text = element.text
                print(text)
                return text
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + id_tag)
                # sleep(1)
             if i == n-1:
                myLog.error("超过限定时间，未捕捉到" + id_tag)

    """********************find_element_by_name******************"""
    def Name_get(self, name_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_name(name_tag)
                return element
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + name_tag)
                # sleep(1)
             if i == n - 1:
                myLog.error("超过限定时间，未捕捉到" + name_tag)

    def Name_click(self, name_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_name(name_tag)
                element.click()
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + name_tag)
                # sleep(1)
             if i == n - 1:
                myLog.error("超过限定时间，未捕捉到" + name_tag)

    def Name_claer(self, name_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_name(name_tag)
                element.clear()
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + name_tag)
                # sleep(1)
             if i == n - 1:
                myLog.error("超过限定时间，未捕捉到" + name_tag)

    def Name_sendkey(self, name_tag, data):
        for i in range(n):
            try:
                element = self.driver.find_element_by_name(name_tag)
                element.clear()
                element.send_keys(data)
                return
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + name_tag)
                # sleep(1)
             if i == n - 1:
                myLog.error("超过限定时间，未捕捉到" + name_tag)

    def Name_text(self,name_tag):
        for i in range(n):
            try:
                element = self.driver.find_element_by_name(name_tag)
                text = element.text
                print(text)
                return text
            except Exception:
                # myLog.info("未捕捉到元素，正在加载中：" + name_tag)
                # sleep(1)
             if i == n - 1:
                myLog.error("超过限定时间，未捕捉到" + name_tag)

    """***************find_element_by_class_name******************"""
    def Class_name_get(self, class_name):
        for i in range(n):
            try:
                element = self.driver.find_element_by_class_name(class_name)
                return element
            except Exception:
                pass


    def Class_name_click(self, class_name):
        for i in range(n):
            try:
                element = self.driver.find_element_by_class_name(class_name)
                element.click()
                return
            except Exception:
                pass


    def Class_name_clear(self, class_name):
        for i in range(n):
            try:
                element = self.driver.find_element_by_class_name(class_name)
                element.clear()
                return
            except Exception:
                pass

    def Class_name_sendkey(self, class_name,data):
        for i in range(n):
            try:
                element = self.driver.find_element_by_class_name(class_name)
                element.clear()
                element.send_keys(data)
                return
            except Exception:
                pass



    def Class_name_text(self,class_name):
        for i in range(n):
            try:
                element = self.driver.find_element_by_class_name(class_name)
                text = element.text
                print(text)
                return text
            except Exception:
                pass

    """*********************find_elements_by_class_name***************************"""

    def Class_name_s_get(self, class_name):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_class_name(class_name)
                return element
            except Exception:
                pass

    def Class_name_s_click(self,class_name,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_class_name(class_name)[array]
                element.click()
                return
            except Exception:
                pass

    def Class_name_s_clear(self, class_name,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_class_name(class_name)[array]
                element.clear()
                #return
            except Exception:
                pass

    def Class_name_s_sendkey(self,class_name,data,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_class_name(class_name)[array]
                element.clear()
                element.send_keys(data)
                return
            except Exception:
                pass

    def Class_name_s_text(self,class_name):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_class_name(class_name)
                text = element.text
                print(text)
                return text
            except Exception:
                pass

    """***************find_element_by_xpath******************"""
    def XPath_get(self, xpath):
        for i in range(n):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                return element
            except Exception:
                pass
	
    def XPath_click(self, xpath):
        for i in range(n):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                element.click()
                return
            except Exception:
                pass

    def XPath_clear(self, xpath):
        for i in range(n):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                return
            except Exception:
                pass

    def XPath_sendkey(self, xpath, data):
        for i in range(n):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                element.send_keys(data)
                return
            except Exception:
                pass

    def XPath_text(self,xpath):
        for i in range(n):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                text = element.text
                print(text)
                return text
            except:
                pass

    """***************find_elements_by_xpath******************"""
    def XPaths_array_get(self, xpath,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)[array]
                return element
            except Exception:
                pass


    def XPaths_array_click(self, xpath,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)[array]
                element.click()
                return
            except Exception:
                pass

    def XPaths_array_clear(self, xpath,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)[array]
                element.clear()
                return
            except Exception:
                pass

    def XPaths_array_sendkey(self, xpath,data,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)[array]
                element.clear()
                element.send_keys(data)
                return
            except Exception:
                pass

    def XPaths_array_text(self,xpath,array):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)[array]
                text = element.text
                print(text)
                return text
            except Exception:
                pass

    """***************find_elements_by_xpath不带元素******************"""

    def XPaths_get(self, xpath):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)
                return element
            except Exception:
                pass

    def XPaths_click(self, xpath):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)
                element.click()
                return
            except Exception:
                pass

    def XPaths_clear(self, xpath):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)
                element.clear()
                return
            except Exception:
                pass

    def XPaths_sendkey(self, xpath, data):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)
                element.clear()
                element.send_keys(data)
                return
            except:
                pass

    def XPaths_text(self, xpath):
        for i in range(n):
            try:
                element = self.driver.find_elements_by_xpath(xpath)
                text = element.text
                print(text)
                return text
            except:
                pass

    """******************switch_to.frame************************"""
    def frame(self,data):
        return self.driver.switch_to.frame(data)

    def frame_return(self):
        return self.driver.switch_to.default_content()
    """*************************title************************"""
    def getTitle(self):
        return self.driver.title

    def refresh(self):
        return self.driver.refresh()

    def inputTextById(self, id_tag, text):
        element = self.driver.find_element_by_id(id_tag)
        self.input(element, text)

    def inputTextByClassName(self, class_name, text):
        element = self.driver.find_element_by_class_name(class_name)
        self.input(element, text)

    def check(self, element, checked):
        if (not element.is_selected() == checked):
            element.click()
        else:
            pass

    def checkById(self, id_tag, checked = True):
        element = self.driver.find_element_by_id(id_tag)
        self.check(element, checked)
		
    def checkByClassName(self, class_name, checked = True):
        element = self.driver.find_element_by_class_name(class_name)
        self.check(element, checked)

    def clickByClassName(self, class_name):
        element = self.driver.find_element_by_class_name(class_name)
        element.click()

        #element = self.driver.find_element_by_id(id_tag)
        #self._action.click(element).perform()
		
    def submitById(self, id_tag):
        element = self.driver.find_element_by_id(id_tag)
        element.submit() 

    def getElementSize(self, element):
        return element.size["width"], element.size["height"]
    
    def getElementSizeById(self, id_tag):
        element = self.driver.find_element_by_id(id_tag)
        return self.getElementSize(element)

    def viewPositionToScreenPosition(self, location):
        x = location["x"]
        y = location["y"]
        orgX = self.getWindowPosition()["x"]
        orgY = self.getWindowPosition()["y"]
        return x + self.absoluteOffsetX + orgX, y + self.absoluteOffsetY + orgY
    
    def ScreenPositionToViewPosition(self, screen):
        x = screen["x"]
        y = screen["y"]
        orgX = self.getWindowPosition()["x"]
        orgY = self.getWindowPosition()["y"]
        return x - self.absoluteOffsetX - orgX, y - self.absoluteOffsetY - orgY

    def getElementScreenPosition(self, element):
        return self.viewPositionToScreenPosition(element.location)

    def getElementScreenPositionById(self, id_tag):
         element = self.driver.find_element_by_id(id_tag)
         return self.getElementScreenPosition(element)

    def getElementRelativePosition(self, element):
        return element.location["x"], element.location["y"]

    def getElementRelativePositionById(self, id_tag):
        element = self.driver.find_element_by_id(id_tag)
        return self.getElementRelativePosition(element)
    
    def getWindowPosition(self):
        return self.driver.get_window_position()

    def selectByIndex(self, element, index):
        Select(element).select_by_index(index)
    
    def selectByValue(self, element, value):
        Select(element).select_by_value(value)
    
    def selectByText(self, element, text):
        Select(element).select_by_visible_text(text)   

    def scrollToView(self, element):
        self.driver.execute_script("arguments[0].focus();", element)#("arguments[0].scrollIntoView();", element)

    def scrollToViewById(self, id_tag):
        element = self.driver.find_element_by_id(id_tag)
        self.scrollToView(element)
    
    def scrollToViewByClassName(self, class_name):
        element = self.driver.find_element_by_class_name(class_name)
        self.scrollToView(element)

    def moveMouseToElementById(self, id_tag):
        element = self.driver.find_element_by_id(id_tag)
        self._action.move_to_element(element).perform()

    def isReady(self):
        return self._isReady

    def isElementInViewPortById(self, id_tag):
        element = self.driver.find_element_by_id(id_tag)
        return self.isElementInViewPort(element)

    def isElementInViewPort(self, element):
        x = element.location["x"]
        y = element.location["y"]
        w = element.size["width"]
        h = element.size["height"]
        return not (x < 0 or y < 0 or (x + w) > self.viewWidth or (y + h) > self.viewHeight)

    def getCookies(self):
        ret = {}
        for cookie in self.driver.get_cookies():
            ret[cookie['name']] = cookie['value']
        return ret

    def getDriver(self):
        return self.driver

    def execJavaScript(self, js):
        return self.driver.execute_script(js)
    
    def screenshot(self, output):
        self.driver.get_screenshot_as_file(output)
    
    def close(self):
        if (self.driver is not None):
            self.driver.quit()
            self.driver = None
            self._isReady = False
