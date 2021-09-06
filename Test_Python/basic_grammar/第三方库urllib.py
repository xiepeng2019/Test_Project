# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/09/06

import urllib3


# http = urllib3.PoolManager()
# r = http.request('get','http://www.baidu.com',timeout = 4.0)
# print(r.status)
# print(r.data)



import re
print(re.match("func", "function"))


lst=[1,3,5,3,4,4,2,9,6,7]
r = [x for x in lst if lst.count(x)==1]
print(r)





# print_msg是外围函数
def print_msg():
    msg = "I'm closure"

    # printer是嵌套函数
    def printer():
        print(msg)

    return printer


# 这里获得的就是一个闭包
closure = print_msg()
# 输出 I'm closure
closure()
