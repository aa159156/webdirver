# comding=UTF-8
from browser import BrowserHacker,BrowserType
import cv2
dr = BrowserHacker()
dr.open("http://www.baidu.com")
htmlcode = read("http://www.baidu.com")
print(htmlcode)