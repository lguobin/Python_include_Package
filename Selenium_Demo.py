#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : While_RunTime_Test.py.Py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from selenium.webdriver.common.keys import Keys


#
# 修改 element_wait 方法名，暂时没想好
# 修改 get_element 方法名，暂时没想好
# 
# 
# el 就是 element
#

# PWTS is Python World Test Selenium

class PS(object):
    '''
        PS framework for the main class

        What is PS?
        The by Selenium original provided, repackaged to PS, make it easy for use.
    '''
    def __init__(self, browser='ff'):
        '''
            browser default is ff(firefox),Run Python2.x and Python3.x.
        The PS officially supports the following browsers:

            Browsers            Ver
        #========================================
            Firefox             54.x and newer
            Chromium            All Ver
            Internet Explorer   6 and newer
            phantomjs           2.x and newer
            Opera               10.5 and newer
            Safari.             10 and newer
        #========================================
        Location: https://selenium.hq.github.io/docs/index.html
        '''
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        # # # ======================
        elif browser == "Opera":
            driver = webdriver.Opera()
        elif browser == "Safari"or browser == "safari":
            driver = webdriver.Safari()
        elif browser == "Edge"or browser == "edge":
            driver = webdriver.Edge()
        elif browser == "remote"or browser == "Remote":
            driver = webdriver.remote()
        # # # ======================
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser." % browser)

    def element_wait(self, css, secs=5):
        '''
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

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
            raise NameError("Please enter the correct elements")

    def get_element(self, css):
        '''
        Find elements.
        '''
        if "=>" not in css:
            raise NameError("Syntax errors, lack of '=>' .")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

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
            raise NameError("Please enter the correct elements")
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
        Set browser max.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, width, height):
        '''
        Set width and height.

        Usage:
        driver.set_window(width,height)
        '''
        self.driver.set_window_size(width, height)

    def input_text(self, css, text):
        '''
        input box text.

        Usage:
        driver.input_text("css=>#el","selenium")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):
        '''
        Clear input box.

        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()

    def click(self, css):
        '''
        Simulate left mouse button click Any content.

        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.click()

    def right_click(self, css):
        '''
        Simulate right mouse button.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        '''
        Mouse hover to element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double-Click HTML Element

        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

##================
##================
##================
    # def move_by_offset(self, xoffset, yoffset):
    #     '''
    #     Mouse moves to some coordinate

    #     Usage:
    #     driver.move_by_offset("css=>#xoffset","css=>#yoffset")
    #     '''
    #     ActionChains(self.driver).move_by_offset(xoffset, yoffset).perform()



    def drag_and_drop(self, el_css, ta_css):
        '''
        Move element drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(driver).drag_and_drop(element, target).perform()

    def drag_and_drop_by_offset(self, el_css, xoffset, yoffset):
        '''
        Move offset element.

        Usage:
        driver.drag_and_drop_by_offset("css=>#el","css=>#xoffset","css=>#yoffset")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
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
        self.driver.quit()

    def submit(self, css):
        '''
        Submit uploading form.

        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

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
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get Webelement text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        '''
        Gets Webelement display.

        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

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
        Get selenium Screenshots Png.

        Usage:
        driver.get_windows_img('file_path')
        '''
        self.driver.get_screenshot_as_file(file_path)

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
##================
##================
##================
    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver._switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver._switch_to.default_content()

    def open_new_window(self, css):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)

    def a(self):
        pass

    def element_keys(self):
        '''
        Operation keyboard.

        Usage:
        
        '''
        # # ==============
        key framework
        send_keys(Keys.ENTER)
        send_keys(Keys.TAB)
        send_keys(Keys.SPACE)
        send_keys(Kyes.ESCAPE)
        send_keys(Keys.BACK_SPACE)
        send_keys(Keys.SHIFT)
        send_keys(Keys.CONTROL)
        send_keys(Keys.ARROW_DOWN)
        send_keys(Keys.CONTROL,'a')
        send_keys(Keys.CONTROL,'c')
        send_keys(Keys.CONTROL,'x')
        send_keys(Keys.CONTROL,'v')

    def get_element_size(self):
        '''
        Get window element_size.

        Usage:
        driver.get_element_size()
        '''
        return self.driver.size

    def get_element_location(self):
        '''
        Get window location.

        Usage:
        driver.get_element_location()
        '''
        return self.driver.location

    def get_element_tag_name(self):
        '''
        Get window tag_name.

        Usage:
        driver.get_element_tag_name()
        '''
        return self.driver.tag_name


    def get_element_page_source(self):
        '''
        Get window page_source.

        Usage:
        driver.get_element_page_source()
        '''
        return self.driver.page_source

    def get_element_is_enabled(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_element_is_enabled("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_enabled()

    def get_element_is_selected(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_element_is_selected("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_selected()


    def select_method(self, css, text):
        '''
            [Select]下拉选择框，以下是三种选择下拉框的方式，注意：  
        a.select_by_index(1)
        a.select_by_value("o2val")
        a.select_by_visible_text("With spaces")
        a.select_by_visilbe_text("    With nbsp")
        1. index从 0 开始
        2. value是option标签的一个属性值，并不是显示在下拉框中的值
        3. visible_text是在option标签中间的值，是显示在下拉框的值
        2、3 需要加 " "
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.select_by_index(text) # 选择第二项选项：o1
        el.select_by_value(text) # 选择value="o2"的项
        el.select_by_visible_text(text) # 选择text="o3"的值，即在下拉时我们可以看到的文本

    def deselect_method(self, css, text ):
        '''
            [Select-取消选择]下拉选择框，以下是三种选择下拉框的方式，注意：
        a.deselect_by_index(index) 
        a.deselect_by_value(value) 
        a.deselect_by_visible_text(text) 
        a.deselect_all()
        前三种分别于select相对应，第四种是全部取消选择，是全部取消。
        有一种特殊的select标签，即设置了multiple=”multiple”属性的select，
        这种select框是可以多选的，你可以通过多次select，选择多项选项，而通过deselect_all()来将他们全部取消。
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.deselect_by_index(text)
        el.deselect_by_value(text)
        el.deselect_by_visible_text(text)
        el.deselect_all()

if __name__ == '__main__':
    driver = PS()
    # driver.Pyse("ff")
