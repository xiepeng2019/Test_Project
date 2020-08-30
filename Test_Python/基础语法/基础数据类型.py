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


import json
"""格式化输出"""
# name = input("name>>>:")
# age = input("age>>>:")
# print("my name is {},my age is {}".format(name,age))

"""字典插入数据"""
# a = {"name":"lisi","age":27,"sex":"nan"}
# a["student"]="xiepeng"
# print(a)
"""删除字典数据"""
# del a ["name"]
# print(a)
"""字典转成json"""
# b = json.dumps(a)
# print(type(b))
"""常量字符串拼接，注：变量需要+进行拼接，并且不同类型需要先转换成字符串"""
# bytes_1 = "Python教程""http://c.biancheng.net/python/"
# print(bytes_1)
"""字符串截取,从第七个开始截图，不包含22的下标"""
# url = 'http://c.biancheng.net/java/'
# print(url[7:22])

"""字符串的分割"""
# b = "C语言中文网 >>> c.biancheng.net"
# list1 = b.split('>>>')
# print(list1)

"""字符串合并"""
# list = ['c', 'biancheng', 'net']
# print(type('.'.join(list)))

"""字符串统计"""
#从下标2开始进行统计
# str = "c.biancheng.net"
# print(str.count('.',2))

"""查找字符串中的子串"""
# str = "c.biancheng.nect"
# print(str.find('c',1,-1))
"""
1、startswith用于检索字符串是否以指定字符开头，是：response->true，否：response->false
2、endswith用于检索字符串是否以指定字符串结尾,是：response->true，否：response->false
3、字符串大小写转换：
    title:将每个单词首字母转成大写，其余小写str.title()
    lower:将字符串中的所有大写字母转换为小写字母，该方法会返回新得到的字符串str.lower()
    upper:将字符串中的所有小写字母转换为大写字母str.upper()
4、去除字符串中的空格
    strip()：删除字符串前后（左右两侧）的空格或特殊字符
    lstrip()：删除字符串前面（左边）的空格或特殊字符
    rstrip()：删除字符串后面（右边）的空格或特殊字符
"""

"""自定义函数len"""
# def my_lenth(str):
#     n = 0
#     for _ in str:
#         n = n + 1
#     return n
#
# a = my_lenth('2132dsadsa')
# print(a)

"""return表达式的值"""
# def str_max(str,str1):
#     return str if str>str1 else str1
# b = str_max('23','32')
# print(b)

"""函数return返回值"""
# def add(a,b):
#     c = a + b
#     return c
# d = add(5,6)
# print(d)
"""函数中可以有多个return，但只执行一个，立即结束"""
def isGreater(x):
    if x > 0:
        return True
    else:
        return False
print(isGreater(-9))
