# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/09/06

import time
import gevent.monkey
gevent.monkey.patch_socket()
import gevent
import requests

"""
同步与异步发http请求
"""
def fetch(pid):
    response = requests.get('http://httpbin.org/get', timeout=50)
    print('请求结果 %s: %s' % (pid, response.status_code))
    return response.text
def synchronous():
    start = time.time()
    for i in range(1, 10):
        fetch(i)
    end = time.time()
    print("同步任务执⾏时间: {}".format(end - start))
def asynchronous():
    start = time.time()
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)
    end = time.time()
    print("异步任务执⾏时间: {}".format(end - start))

# print('同步执⾏:')
# synchronous()

print('异步执⾏:')
asynchronous()