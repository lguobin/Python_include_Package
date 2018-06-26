#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : Load_Test_Python_Code.Py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$

import requests

import urllib.request
from concurrent.futures import ProcessPoolExecutor
import threading
import os
import json
import time

class Requests():
	'''
		# Load_Test_Python_Code
		# Give you 2 ways requests
		# 1. requests package
		# 2. Python urllib.request package
	'''
	def __init__(self):
		'''
			# Test info
		'''
		self.url = 'https://www.google.com'
		self.login = 'https://www.google.com/login'
		self.login_body = {"name":"name","password":"password"}

	def get(self):
		try:
			# r = urllib.request.urlopen(self.url)
			# r = r.read().decode("utf-8")
			r = requests.get(self.url)
			r.encoding = r.apparent_encoding
			'''
				# Warning
				# -->	{'DATA'} is your response msg or HTTP code
			'''
			if "{'DATA'}" in r.text: 
				print(r)
			else:
				print("Sorry Not DATA match !!")
		except Exception as e:
			print(e)

	def post(self):
		try:
			r = requests.post(self.login , json = self.login_body)
			if "access_token" in r.text and "code" not in r.text:
				if "a" in r.text:
					print(r)
				else:
					print("Sorry Not DATA match !!")
			else:
				print("Sorry Not DATA match !!")
		except Exception as e:
			print(e)

def start():
	start = Requests()
	# return start.get()
	return start.post()

if __name__ == '__main__':
	try:
		i = 0
		# Load_test_start
		# tasks_number is send Requests Quantity
		tasks_number = 10
		print('start~~')
		time1 = time.clock()
		while i < tasks_number:
			t = threading.Thread(target=start())
			t.start()
			i +=1
		time2 = time.clock()
		times = time2 - time1
		print(f"{times/tasks_number}")
	except Exception as e:
		print(e)