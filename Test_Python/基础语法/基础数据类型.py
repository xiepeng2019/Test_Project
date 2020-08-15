from collections import Iterable


"""
主动抛出异常
"""
# def my_abs(x):
#     # 判断变量类型后，⼿动抛出异常
#     if not isinstance(x, (int, float)):
#     # 抛出异常
#         raise TypeError('您传⼊的参数不是浮点，或者整型')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs('d'))

"""迭代取值1、取K。2、取V。3、同时迭代"""
# d = {"name": "duoceshi", "age": 4, "score": 99}
# a = []
"""迭代K"""
# for i in d:
#     a.append(i)
# print(a)
"""迭代V"""
# for v in d.values():
#     a.append(v)
# print(a)
"""双迭代"""
# for k,v in d.items():
#     print(k,v)
# for i in d:
#     print(i,d[i])

"""判断对象是否可迭代"""
# print(isinstance("123",Iterable))

"""生成平方"""
# a=[]
# for i in range(1,11):
#     for j in range(1,11):
#         if i % 2 == 0:
#             a.append(i + j)
# print(a)

"""字典生成列表"""
# a = {"name": "duoceshi", "age": 4}
# b = [str(k) + str(v) for k ,v in a.items()]
# print(b)


"""高阶函数：一个函数接收另一个函数作为参数"""

"""内建高阶函数
1、map()函数，接收两个参数，一个函数，一个可迭代对象
    将可迭代对象依次代入函数，将结果组成list返回
    对一个列表统一进行一个操作时使用
"""
# a = [1, 2, 3, 4, 5]
# b = []
# for i in a:
#     f = str(i)
#     b.append(f)
# print(b)

# c = map(str,a)
# print(list(c))

"""
2、filter()函数，接收一个函数，一个可迭代对象
    将可迭代对象依次传入函数，通过ture和false决定去留
    过滤和筛选
"""
# a = [1,2,3,4,5,6,7]
# def fa(x):
#     if x > 5:
#         return True
# b = filter(fa,a)
# print(list(b))

"""匿名函数"""
# a = list(map(lambda x: x * x, [1,2,3,4,5,6,7,8,9]))
# print(a)

"""logging使用"""
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
# def loging(a=0,b=0):
#     logging.info("[正在执行的函数是]：{}".format(loging.__name__))
#     logging.info("[参数a为]：{}".format(a))
#     logging.info("[参数b为]：{}".format(b))
#     c = a + b
#     return c
# print(loging(6,8))

"""装饰器"""
# def use_loging(func):
#     def wrapper(*args,**kwargs):
#         logging.info("[当前调用的函数是]：{}".format(func.__name__))
#         for i in range(len(args)):
#             logging.info("[第{}参数是]：{}".format(i,args(i)))
#         for k,v in kwargs.items():
#             logging.info("key 是: {} value 是: {}".format(k,v))
#         return func(*args,**kwargs)
#     return wrapper
#
# @use_loging
# def ab(a,b):
#     c = a + b
#     return c
# print(ab(a=4,b=4))

"""类属性"""
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def a_score(self):
#         print('%s:%s' % (self.name,self.score))
#         return
#
# dcs = Student("duoceshi","12")
# print(dcs.a_score())
"""类的继承"""
# class Name_a():
#     def run(self):
#         print("类的继承")
# a = Name_a()
# print(isinstance(a,Name_a))


"""json解析数据操作"""
"增加"
# h = {"name":"duoceshi"}
# h["sex"]="男"
# print(h)
"删除"
# del h["name"]
# print(h["sex"])

"""json序列化"""
import json

# data1 = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
# data2 = { 'a':'A', 'b':(2, 4), 'c':3.0 }
"转成str"
# a = repr(data1)
# b = json.dumps(data1)
# print(type(b))
# c = json.loads(b)
# print(type(c))
"""filter过滤和异常处理"""
try:
    a = list(filter(lambda x:x>10,[1,2,3,4,5,6,7,8,9,12,34,56,33,22,11,77]))
    print(type(a))
    print(isinstance(a,list))
except SyntaxError:
    print("语法错误，请检查语法")
else:
    print("执行成功")
finally:
    print("执行数据清理")
