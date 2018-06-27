#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : Python_login_Demo.Py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$

import os

user = {'name':'admin','password':'admin'}
_counts=0

while 1:
    _name = input('Name: ')
    _psw = input('Password: ')
    if ( _name == user['name'] and _psw == user['password'] ):
        print('=' *8)
        print('== Login OK~')
        print('=' *8)
        cmd = input('command$:')
        while True:
            while cmd != 'out':
                cmd = input('command$:')
            break
    elif not ( _name == user['name'] and _psw == user['password']):
        _counts=_counts + 1
        print ("\n Name or Password Error \n Please try again\n")
        if _counts > 2:
            print('Sorry Login error 3 times !')
            break            
    # else:
    #     print('Login Name or Password Error!\n')
    #     continue
