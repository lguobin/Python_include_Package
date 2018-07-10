#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-09 13:45:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os



# 通过 Python 特性检查元素是否存在
def test():
    try:
        driver.find_element_by_id("kw")
    except NoSuchElementException, e:
        return False
    return True



# 存在返回 True or False
def isElementExist(id):
    try:
        driver.find_element_by_id(id)
        return True
    except:
        return False




def is_element_exist(css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print "元素未找到:%s"%css
        return False
    elif len(s) == 1:
        return True
    else:
        print "找到%s个元素：%s"%(len(s),css)
        return False
if is_element_exist("#kw"):
    print("存在")



for link in driver.find_elements_by_xpath("//*[@target]"):
    print (link.get_attribute('href'))
    print (link.get_attribute('id'))
    print (link.get_attribute('class'))
    print (link.get_attribute('name'))
    print (link.get_attribute('url'))

for link in driver.find_elements_by_xpath("//*[@href]"):
    print (link.get_attribute('href'))
    print (link.get_attribute('id'))
    print (link.get_attribute('class'))
    print (link.get_attribute('name'))
    print (link.get_attribute('url'))
