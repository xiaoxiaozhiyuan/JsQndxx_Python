#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:main.py
@time:2022/09/17
"""
from Qndxx import Qndxx

if __name__ == '__main__':
    laravel_session = "8rAucTd84mpMLxilmCjeWO08rbtC7opDnrwosdaa"
    qndxx = Qndxx(laravel_session)
    qndxx.login()
    qndxx.confirm()