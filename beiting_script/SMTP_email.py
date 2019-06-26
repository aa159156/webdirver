# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
def email(file,email):
    my_sender='897619809@qq.com'    # 发件人邮箱账号
    my_pass = 'pasiclzvmnwebdec'              # 发件人邮箱密码
    my_user=email      # 收件人邮箱账号，我这边发送给自己

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octest-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1.add_header('Content-Disposition','attachment',filename="无纸化会议系统项目测试报告.html")


    msg = MIMEMultipart()
    msg.attach(MIMEText('自动化测试报告', 'html', 'utf-8'))
    msg['From']=formataddr(["test",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    subject ="自动化测试报告"                # 邮件的主题，也可以说是标题
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(att1)

                    
    server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接


