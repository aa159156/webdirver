#coding=UTF-8
import unittest
import pymysql
import requests
import json
import time
from BeautifulReport import BeautifulReport
from user_API import user_API
xie = "\_"
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
class beiting_User_API(unittest.TestCase):
      @classmethod
      def login(self):
         """用户登录"""
         self.url = "https://beiting.haituke.com"
         token = user_API.login(self.url,username=18925662425,password=12345678)
         self.header = {
                     "Authorization": "Bearer " + token[1],
                     "Content-Type": "application/json"
                  }
      def User_findOne(self):
         """根据认证用户ID查看认证用户信息"""
         user_API.findOne(self.url,self.header,user_id=41)
      def User_modify(self):
         """根据认证用户ID修改认证用户信息"""
         user_API.modify(self.url,self.header,user_id=41,name="吴派睿",IdCard=445202199612147718,phone=18925662425,organization="")
      def User_findAll(self):
         """分页查询所有认证用户信息"""
         user_API.findAll(self.url,self.header,page=1,pagesize=3)
      def User_addIdentity(self):
         """新增认证用户身份"""
         user_API.addIdentity(self.url,self.header,user_id=41,type="PARTY_MEMBER",houseid="",roomnumber="")
      def User_deleteIdentity(self):
         """删除认证用户身份"""
         user_API.deleteIdentity(self.url,self.header,user_id=41,type="PARTY_MEMBER",houseid="",roomnumber="")

testunit = unittest.TestSuite()
testunit.addTest(beiting_User_API("login"))
testunit.addTest(beiting_User_API("User_findOne"))
testunit.addTest(beiting_User_API("User_modify"))
testunit.addTest(beiting_User_API("User_findAll"))
testunit.addTest(beiting_User_API("User_addIdentity"))
testunit.addTest(beiting_User_API("User_deleteIdentity"))
BeautifulReport(testunit).report(filename=xie + now + '阳光北亭接口测试报告', description='接口测试',
                                 log_path=r'C:\Users\Administrator\Desktop\beiting_script\接口自动化\result')


















# connect = pymysql.connect(host="beiting.haituke.com",port=3306,user="shennong-user",password="Zq1BokxCJxz1Uouc",db="shennong_db")
# cursor = connect.cursor()
# sql = "select id,real_name,mobile_phone from data_center_user WHERE real_name = '吴沛睿'"
# # 执行SQL语句
# cursor.execute(sql)
# # 获取所有记录列表
# results = cursor.fetchall()
# for row in results:
#    id = row[0]
#    name = row[1]
#    phone = row[2]
#    phone1 = row[3]
#   # 打印结果
# print("id=%s | real_name=%s | mobile_phone=%s" %(id,name,phone))

