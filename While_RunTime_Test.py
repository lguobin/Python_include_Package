#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : While_RunTime_Test.py.Py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$


import timeit

def while_one():
	i = 0
	while 1:
		i += 1
		if i == 2000000:
			break

def while_true():
    i = 0
    while True:
        i += 1
        if i == 2000000:
        	break

if __name__ == '__main__':

	'''
		# While_one in Python 2.x Faster while_true 
		# But Python3.x while_true and while_one RunTime Same
		# My god~~~
	'''
	one = timeit.timeit(while_one, "from __main__ import while_one", number=3)
	true = timeit.timeit(while_true, "from __main__ import while_true", number=3)
	print("while_one: %s\n while_true: %s" % (one, true))