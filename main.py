#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:main.py
@time:2022/09/17
"""
from Qndxx import Qndxx

if __name__ == '__main__':
    laravel_session = "x6aUCqw36uDo02lt1WOqDjGn0CW2eAMb9ZkdRN8P"
    qndxx = Qndxx(laravel_session)
    qndxx.login()
    qndxx.confirm()
