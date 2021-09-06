# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/09/06

import gevent
from gevent import queue
q1 = queue()


def consumer(name):
    while not q1.empty():
        print('%s 从队列获取数据 %s' % (name, q1.get()))
        gevent.sleep(0)
    print(name, '退出')
def producer():
    for i in range(1, 10):
        q1.put(i)
    gevent.joinall([
gevent.spawn(producer),
gevent.spawn(consumer, 'liudan'),
gevent.spawn(consumer, 'shangcl'),
gevent.spawn(consumer, 'hhc'),
])