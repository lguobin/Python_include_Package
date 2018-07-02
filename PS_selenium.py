#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : PS.py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

import time,os,sys
import json

#   function
# 修改 wait_element_timeing 方法名，暂时没想好
# 修改 find_element_ 方法名，暂时没想好
#  
# el 就是 element
#
# Python Selenium Tests

class PS(object):
    '''
        PS framework for the main class

        What is PS?
        The by Selenium original provided, repackaged to PS, make it easy for use.
    '''
    def __init__(self, Browser='ff'):
        '''
            Browser default is ff(firefox),Run Python2.x and Python3.x.
        The PS officially supports the following Browsers:

            Browsers            Ver
        #========================================
            Firefox             54.x and newer
            Chromium            All Ver
            Internet Explorer   6 and newer
            Opera               10.5 and newer
            Safari.             10 and newer
            phantomjs           abandoned(Selenium Ver.2.x support phantomjs 2.x)
        #========================================
        Location: https://selenium.hq.github.io/docs/index.html
        '''
        if Browser == "firefox" or Browser == "ff":
            driver = webdriver.Firefox()
        elif Browser == "chrome":
            driver = webdriver.Chrome()
        elif Browser == "internet explorer" or Browser == "ie":
            driver = webdriver.Ie()
        elif Browser == "phantomjs":
            driver = webdriver.PhantomJS()
        # # # ======================
        elif Browser == "Opera":
            driver = webdriver.Opera()
        elif Browser == "Safari"or Browser == "safari":
            driver = webdriver.Safari()
        elif Browser == "Edge"or Browser == "edge":
            driver = webdriver.Edge()
        elif Browser == "remote"or Browser == "Remote":
            driver = webdriver.remote()
        # # # ======================
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s Browser." % Browser)

    def wait_element_timeing(self, css, secs=5):
        '''
        Waiting for an element to display.

        Usage:
        driver.wait_element_timeing("css->#eles",10)
        '''
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0]
        value = css.split("->")[1]

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        # # # ======================
        elif by == "tag":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.Tag_name, value)))
        # elif by == "tag":
        # WebDriverWait(self.driver, secs, 1).until(
        #         EC.presence_of_element_located((By.Tag_name, value)))
        # # # ======================
        else:
            raise NameError("Element not found, Please check the element name.")

    def find_element_(self, css):
        '''
        Find elements.

        Usage:
        driver.wait_element_timeing("css->#eles")
        '''
        if "->" not in css:
            raise NameError("Syntax errors, lack of '->' .")

        by = css.split("->")[0]
        value = css.split("->")[1]

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        # # # ======================
        elif by == "tag":
            element = self.driver.find_element_by_tag_name(value)
        # # # ======================
        else:
            raise NameError("Element not found, Please check the element name.")
        return element

    def open(self, url):
        '''
        open url.

        Usage:
        driver.open("https://www.google.com")
        '''
        self.driver.get(url)

    def max_window(self):
        '''
        Set Browser max.

        Usage:
        driver.max_window()
        '''
        try:
            self.driver.maximize_window()
        except Exception as e:
            print(e)

    def set_window_size(self, width, height):
        '''
        Set width and height.

        Usage:
        driver.set_window_size(width,height)
        '''
        self.driver.set_window_size(width, height)

    def input_text(self, css, text):
        '''
        input box text.

        Usage:
        driver.input_text("css->#eles","selenium")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        eles.send_keys(text)

    def clear(self, css):
        '''
        Clear input box.

        Usage:
        driver.clear("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        eles.clear()

    def click(self, css):
        '''
        Simulate left mouse button click Any content.

        Usage:
        driver.click("css->#eles")
        '''
        try:
            self.wait_element_timeing(css)
            eles = self.find_element_(css)
            eles.click()
        except Exception as e:
            print("Find elements Click Error!")

    def right_click(self, css):
        '''
        Simulate right mouse button.

        Usage:
        driver.right_click("css->#eles")
        '''
        self.wait_element_timeing(css)
        el = self.find_element_(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        '''
        Mouse hover to element.

        Usage:
        driver.move_to_element("css->#eles")
        '''
        self.wait_element_timeing(css)
        el = self.find_element_(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double-Click HTML Element

        Usage:
        driver.double_click("css->#eles")
        '''
        self.wait_element_timeing(css)
        el = self.find_element_(css)
        ActionChains(self.driver).double_click(el).perform()

##================
##================
##================
##================
##================
##================
##================
##================
    # def move_by_offset(self, xoffset, yoffset):
    #     '''
    #     Mouse moves to some coordinate

    #     Usage:
    #     driver.move_by_offset("css->#xoffset","css->#yoffset")
    #     '''
    #     ActionChains(self.driver).move_by_offset(xoffset, yoffset).perform()



    def drag_and_drop(self, el_css, ta_css):
        '''
        Move element drops it.

        Usage:
        driver.drag_and_drop("css->#eles","css->#ta")
        '''
        self.wait_element_timeing(el_css)
        element = self.find_element_(el_css)
        self.wait_element_timeing(ta_css)
        target = self.find_element_(ta_css)
        ActionChains(driver).drag_and_drop(element, target).perform()

    def drag_and_drop_by_offset(self, el_css, xoffset, yoffset):
        '''
        Move offset element.

        Usage:
        driver.drag_and_drop_by_offset("css->#eles","css->#xoffset","css->#yoffset")
        '''
        self.wait_element_timeing(el_css)
        element = self.find_element_(el_css)
        ActionChains(driver).drag_and_drop_by_offset(element, xoffset, yoffset).perform()

    def click_text(self, text):
        '''
        Click the element by the link text.

        Usage:
        driver.click_text("News")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        '''
        Simulates user close Browser.
        
        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Simulates user Quit Browser.

        Usage:
        driver.quit()
        '''
        try:
            self.driver.quit()
        except Exception as e:
            print(e)

    def submit(self, css):
        '''
        Submit uploading form.

        Usage:
        driver.submit("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        eles.submit()

    def F5(self):
        '''
        Refresh page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def javaScript(self, javaScript):
        '''
        Run JavaScript.

        Usage:
        driver.javaScript("js")
        '''
        self.driver.execute_script(javaScript)

    def get_attribute(self, css, attribute):
        '''
        Get Webelement attribute.

        Usage:
        driver.get_attribute("css->#eles","type")
        '''
        eles = self.find_element_(css)
        return eles.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get Webelement text information.

        Usage:
        driver.get_text("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.text

    def get_display(self, css):
        '''
        Gets Webelement display.

        Usage:
        driver.get_display("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.is_displayed()

    def get_title(self):
        '''
        Get Webelement title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get Webelement URL address.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):
        '''
        Get selenium Full screen shot function.
        File extension best to .png

        Usage:
        driver.get_windows_img('file_path.png')
        '''
        time_day = self.get_time_day()
        try:
            self.driver.get_screenshot_as_file(file_path + time_day + ".png")
        except Exception as e:
            raise e
        # else:
        #     pass
        # # self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses warning box.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css->#eles")
        '''
        self.wait_element_timeing(css)
        iframe_el = self.find_element_(css)
        self.driver._switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns to the Previous frame.
        Contrary to function switch_to_frame()

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver._switch_to.default_content()

    def open_new_window(self, css):
        '''
        New Browser Window handle and control it.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        eles = self.find_element_(css)
        eles.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)

    def find_element__size(self, css):
        '''
        Get window element_size.

        Usage:
        driver.find_element__size("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.size

    def find_element__location(self, css):
        '''
        Get window element location.

        Usage:
        driver.find_element__location("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.location

    def find_element__tag_name(self, css):
        '''
        Get window element tag_name.

        Usage:
        driver.find_element__tag_name("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.tag_name


    def find_element__page_source(self):
        '''
        Get window page_source.

        Usage:
        driver.find_element__page_source()
        '''
        return self.driver.page_source

    def find_element__is_enabled(self, css):
        '''
        Get the element to display,function return result is true or false.

        Usage:
        driver.find_element__is_enabled("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.is_enabled()

    def find_element__is_displayed(self, css):
        '''
        Get the element to display,function return result is true or false.

        Usage:
        driver.find_element__is_displayed("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.is_displayed()

    def find_element__is_selected(self, css):
        '''
        Get the element to display,function return result is true or false.

        Usage:
        driver.find_element__is_selected("css->#eles")
        '''
        self.wait_element_timeing(css)
        eles = self.find_element_(css)
        return eles.is_selected()

    def get_time_day(self):
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        return now
        
#===============
#===============

    # def keyboard_hotkey(self, css, value):
    #     '''
    #     Operation keyboard hotkey.

    #     Usage:
    #     driver.element_keyboard(Keys."value")
    #     Demo:
    #     driver.element_keyboard(Keys.F1)
    #     '''
    #     self.wait_element_timeing(css)
    #     eles = self.find_element_(css)
    #     eles.send_keys(value)
    #     # eles.send_keys(Keys.value)

    # def keyboard_control(self, css, value):
    #     '''
    #     Operation keyboard Keys.

    #     Usage:
    #     driver.element_keyboard(Keys.CONTROL, "value")
    #     Demo:
    #     driver.element_keyboard(Keys.CONTROL, "v")
    #     '''
    #     self.wait_element_timeing(css)
    #     eles = self.find_element_(css)
    #     eles.send_keys(Keys.CONTROL, value)
    
    # def select_method(self, css, text):
    #     '''
    #         [Select]下拉选择框，以下是三种选择下拉框的方式，注意：  
    #     a.select_by_index(1)
    #     a.select_by_value("o2val")
    #     a.select_by_visible_text("With spaces")
    #     a.select_by_visilbe_text("    With nbsp")
    #     1. index从 0 开始
    #     2. value是option标签的一个属性值，并不是显示在下拉框中的值
    #     3. visible_text是在option标签中间的值，是显示在下拉框的值
    #     2、3 需要加 " "
    #     '''
    #     self.wait_element_timeing(css)
    #     eles = self.find_element_(css)
    #     eles.select_by_index(text) # 选择第二项选项：o1
    #     eles.select_by_value(text) # 选择value="o2"的项
    #     eles.select_by_visible_text(text) # 选择text="o3"的值，即在下拉时我们可以看到的文本

    # def deselect_method(self, css, text ):
    #     '''
    #         [Select-取消选择]下拉选择框，以下是三种选择下拉框的方式，注意：
    #     a.deselect_by_index(index) 
    #     a.deselect_by_value(value) 
    #     a.deselect_by_visible_text(text) 
    #     a.deselect_all()
    #     前三种分别于select相对应，第四种是全部取消选择，是全部取消。
    #     有一种特殊的select标签，即设置了multiple=”multiple”属性的select，
    #     这种select框是可以多选的，你可以通过多次select，选择多项选项，而通过deselect_all()来将他们全部取消。
    #     '''
    #     self.wait_element_timeing(css)
    #     eles = self.find_element_(css)
    #     eles.deselect_by_index(text)
    #     eles.deselect_by_value(text)
    #     eles.deselect_by_visible_text(text)
    #     eles.deselect_all()


#===============

    def get_cookie(self):

        return self.driver.get_cookies()

    def save_cookie(self, file_path):

        cook_save = self.driver.get_cookies()
        cook = json.dumps(cook_save)
        with open(file_path, 'w') as f:
            f.write(cook)

    def load_cookie(self, file_path):

        with open(file_path, 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        self.driver.add_cookie(cookie_dict)

    def del_all_cookie(self):

        return self.driver.delete_all_cookies()


    def a(self):
        pass

    '''
    登录并保存cookie
    '''
    #前面部分代码用于填写登录信息并登录
    '''
    # 获取cookie并通过json模块将dict转化成str
    dictCookies = self.browser.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    # 登录完成后，将cookie保存到本地文件
    with open('cookies.json', 'w') as f:
        f.write(jsonCookies)

    ###===================================================
    ###===================================================
    ###===================================================

    # 初次建立连接，随后方可修改cookie
    self.browser.get('http://xxxx.com')
    # 删除第一次建立连接时的cookie
    self.browser.delete_all_cookies()
    # 读取登录时存储到本地的cookie
    with open('cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        self.browser.add_cookie({
            'domain': '.xxxx.com',  # 此处xxx.com前，需要带点
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })
    # 再次访问页面，便可实现免登陆访问
    self.browser.get('http://xxx.com')


    # https://www.cnblogs.com/zhao-ying-jie/p/7084636.html
    '''

if __name__ == '__main__':
    driver = PS()
    # driver.PS("ff")
