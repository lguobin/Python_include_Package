#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file    : PS.py
# @Date    : 2018-06-02 14:14:46
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$


def a(*args):
    print(args)


def b(**args):
    print(args)


def c(x, y=2, *args, **kargs):
    print('x-->', x)
    print('y-->', y)
    print('args is', args)
    print('tuple args is', kargs)


def d(arg1, *argv):
    print(arg1)
    for item in argv:
        print(item)


def e(**kwargs):
    '''
            iteritems in Python 3.5 change to items
    Python 3.5.x ↑ Run iteritems is AttributeError: 'dict' object has no attribute 'iteritems'
    Python 3.4.x ↓ Run iteritems and items Nothing
    '''
    if kwargs is not None:
        for key, value in kwargs.items():
            # for key, value in kwargs.iteritems():
            print(key, value)


def F(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

# =========================
# =========================


def test_arg(a, b):
    print("test_arg()")
    print(a, b)


def test1_value_args(*arg2):
    print("test1_value_args")
    print(arg2)


def test2_value_arg(**arg):
    print("test2_value_args")
    print(arg)


def test3_value_args(arg1, *arg2):
    print("test3_value_args")
    print(arg1)
    print(arg2)


def test4_value_args(arg1, **arg2):
    print("test4_value_args")
    print(arg1)
    print(arg2)


def test5_value_args(arg1, *arg2, **arg3):
    print("test5_value_args")
    print(arg1)
    print(arg2)
    print(arg3)


def test6_value_args(arg1, arg2="moren", *arg3, **arg4):
    print("test6_value_args")
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


if __name__ == "__main__":
    test_arg(1, 2)
    test1_value_args()
    test1_value_args(1, 2, 3, 4)

    test2_value_arg()
    test2_value_arg(a="1", b='2')

    test3_value_args(1)
    test3_value_args(1, 2, 3, 4)

    test4_value_args(1, a="2", b="3")

    test5_value_args(1, 2, 3, 4, a="5", b="6")

    test6_value_args(1, a="2", b="3", c="4")
    test6_value_args(1, arg2="3", c="4")


    a(1, 2)

    b(a=1, b=2, c=3)
    c(1, 3, 4, 5, a=1, b=2, c=3)
    d(1, 'name pass...', '2', '3', '4')
    e(name='john')

    args = ("one", '1', '2')
    F(*args)

    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    F(**kwargs)
