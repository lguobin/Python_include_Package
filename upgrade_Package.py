#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : _Package.exe
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$


from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

import os
from sys import version_info


class _check():
	def __init__(self):
		self._pip = raw_input("Please input your pip2 or pip3.x ? ") if version_info.major == 2 else input("Please input your pip2 or pip3.x ? ") if version_info.major == 3 else 1

	def index(self):
		'''Start'''
		try:
			while True:
				print("==========")
				print("")
				print(u"1、查看已安装的包")
				print(u"2、查看包有无更新")
				print(u"3、更新所有的包")
				print(u"4、单独更新某个包例如：A")
				print(u"5、卸载包")
				print("")
				print("==========")
				print(u"退出输入：0")
				print("")
				print(u"输入对应的数字进入不同的功能")
				n = int(raw_input("Please enter the number (1,2,3,4,5/0)? ")) if version_info.major == 2 else int(input("Please enter the number (1,2,3,4,5/0)? ")) if version_info.major == 3 else 1
				if n == 1:
					self._Package_ALL_()
				elif n == 2:
					self._Check_Package_()
				elif n == 3:
					self._Upgrade_()
				elif n == 4:
					Pack = raw_input("Please Pack? ") if version_info.major == 2 else input("Please Pack? ") if version_info.major == 3 else 1
					self._Alone(Pack)
				elif n == 5:
					Pack = raw_input("Please Pack? ") if version_info.major == 2 else input("Please Pack? ") if version_info.major == 3 else 1
					self._Uninstall(Pack)
				elif n == 0:
					break
				else:
					print(u"input Error~")
					continue
		except ValueError as e:
			raise ValueError("number input Error")

# # # # # ================
# # # # # ================
# # # # # ================

	def _Package_ALL_(self):
		print(" ======  Upgrade Package  ====== ")
		call("%s list " %self._pip, shell=True)
		print("\n")
		print("Done~~\n\n\n")

	def _Check_Package_(self):
		call("%s list --outdated " %self._pip, shell=True)
		self._Proceed()

	def _Upgrade_(self):
		number = 0
		for data in get_installed_distributions():
			number += 1
			call("%s install --upgrade  %s" %(self._pip, data.project_name), shell=True)
		print("\n")
		print("Done~~\n\n\n")

	def _Alone(self, Package):
		URL = "https://pypi.tuna.tsinghua.edu.cn/simple"
		call("%s install %s -i %s" %(self._pip, Package, URL), shell=True)
		print("\n")
		print("Done~~\n\n\n")

	def _Uninstall(self, Package):
		call("%s uninstall  %s " %(self._pip, Package), shell=True)
		print("\n")
		print("Done~~\n\n\n")	

	def _Proceed(self):
		if version_info.major == 2:
			ask = raw_input("Proceed (y/n)? ")
		elif version_info.major == 3:
			ask = input("Proceed (y/n)? ")
		if ask == "y" or ask == "yes" or ask == "Yes":
			self._Upgrade_()
		elif ask == "n" or ask == "no" or ask == "NO":
			self._Done()
		else:
			print("Error~")

	def _Done(self):
		'''End'''
		print("\n \n \t\t\t======  Ok~ OK~  ======\n \n")
		print("\t \t======  You are the Boss!  ======")

	def log(self):
		call("%s list " %self._pip, shell=True)

if __name__ == '__main__':
	test = _check()
	test.index()