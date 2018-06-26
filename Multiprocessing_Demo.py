#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : Multiprocessing_Demo_Code.py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$


from bs4 import BeautifulSoup

import math
import time
import os
import re
import json
import urllib.request
import multiprocessing
from multiprocessing import Process
from concurrent import futures

class test():
	# def test_1(self):
	# 	url = "http://www.manmanbuy.com"
	# 	req = urllib.request.Request( url = url )
	# 	req = urllib.request.urlopen( req )
	# 	req = req.read()
	# 	req = req.decode('gbk')
	# 	# print(req)

	# 	return_info= BeautifulSoup( req,"html.parser")

	# 	if "sInput" in return_info.findAll("div",class_="sInput"):
	# 		pass
	# 	else:
	# 		for pages in return_info.findAll("div",class_="sInput"):
	# 			temp = pages.findAll("input")
	# 			for a in temp:
	# 			    print(a.get("data-bijia") ,"\t\n" ,a.get("data-zekou"))
	def a(self):
		run_nums = 0
		for a in range(0,5):
			run_nums += 1
			print("当前运行： %s " %a)

	def b(self,num):
		return time.ctime(),num

if __name__ == '__main__':
	aaa = test()
	p1 = multiprocessing.Process(target = aaa.a())
	p1.start()
	p2 = multiprocessing.Process(target = aaa.a())
	p2.start()
	for p in multiprocessing.active_children():
		# time.sleep(10)
		print("child   p.name:" + p.name + "\tp.id:" + str(p.pid))

	print("==" *20)

	while_run_nums = 0
	while True:
		while_run_nums += 1
		p=Process(target = aaa.a())
		p.start()
		p.join()
		if while_run_nums > 2:
			break

	print("==" *20)

	with futures.ThreadPoolExecutor(max_workers=1) as executor:
		future = executor.submit(aaa.b,1)
		print (future.result())

	print("==" *20)

	data=[1,2,3]
	with futures.ThreadPoolExecutor(max_workers=1) as executor:
		for future in executor.map(aaa.b,data):
			print (future)

	print("==" *20)

	data=[1,2,3]
	name = ["a","b","c","d"]
	while_run_nums = 0
	while 1:
		ex = futures.ThreadPoolExecutor(max_workers=2)
		for future in ex.map(aaa.b,name):
			print (future)
		while_run_nums += 1
		if while_run_nums == 2:
	            break


	


	
# 	aaa.test_1()
