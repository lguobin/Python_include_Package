#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file    : Python_Generate_User_token.py
# @Date    : 2018-07-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$

import time
import base64
import hmac


def Generate_User_token(key, Expired=300):
    '''
        @explanation:
            key: str (Agreed user key)
            Expired: int (time second)
        @Return:
            state: str
    '''
    time_str = str(time.time() + Expired)
    time_byte = time_str.encode("utf-8")
    sha1 = hmac.new(key.encode("utf-8"),time_byte,'sha1').hexdigest()
    _t = time_str + ':' + sha1
    _base64_token = base64.urlsafe_b64encode(_t.encode("utf-8"))
    return _base64_token.decode("utf-8")


def Confirm_User_token(key, token):
    '''
        @explanation:
            key: str
            token: str
        @Returns:
            boolean
    '''
    _token_list = base64.urlsafe_b64decode(token).decode('utf-8').split(':')
    if len(_token_list) != 2:
        return False
    ts_str, sha1 = _token_list[0], _token_list[1]
    if float(ts_str) < time.time():
        # token Expired
        return False   
    sha1_check = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1').hexdigest()
    if sha1_check != sha1:
        # token confirm False or True
        return False
    return True

if __name__ == '__main__':

    key  = "admin:admin"
    # Agreed user key
    
    # After 0.5 hour.(0.5 hour is 1800 min, Expired is 1800)
    times = 1

    True_token = Generate_User_token(key, times)
    print(Confirm_User_token(key, True_token))

    # Expired is 300 seconds
    # token is Error

    False_token = "MTUzMDY3Njk0Ny45MjEwMTUzOjI3ZDExZTFmMzVmOTNhYzdkMzg1M2RhYTBmNTEwMWVlMDcyY2MyOTI="
    print(Confirm_User_token(key, False_token))