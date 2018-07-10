#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : 邮件.py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
 
class Myemail:
	def __init__(self,mail_list,mail_title,mail_content):
		self.mail_list = mail_list
		self.mail_title = mail_title
		self.mail_content = mail_content
		self.mail_host = "smtp.163.com"
		self.mail_user = "你自己邮箱@163.com"
		self.mail_pass = "你的密码"
		self.mail_postfix = "163.com"

	def SendMail(self):
		info = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
		msg = MIMEMultipart()
		msg['Subject'] = '接口测试报告：'
		msg['From'] = info
		msg['To'] = ";".join(self.mail_list)

		with open("/temp/Report.html", 'r') as f:
        	Report_content = f.read().encode("utf-8")
		puretext = MIMEText(Report_content, 'html', 'utf-8')
    	msg.attach(puretext)

	try:
		s = smtplib.SMTP() #创建邮件服务器对象
		s.connect(self.mail_host) #连接到指定的smtp服务器。参数分别表示smpt主机和端口
		s.login(self.mail_user, self.mail_pass) #登录到你邮箱
		s.sendmail(me, self.mail_list, msg.as_string()) #发送内容
		s.close()
		return True
	except Exception, e:
		print str(e)
		return False

if __name__ == '__main__':
	# 邮件登录
	mailto_list = ["你领导的邮件@163,com","aaaa@163.com"]
	mail_title = 'Hey subject'
	mail_content = 'Hey this is content'
	test = Myemail(mailto_list, mail_title, mail_content)
	print(test.SendMail())