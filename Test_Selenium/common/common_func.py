#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import os
import socket
import struct
import time
import random
import re
import traceback
import uuid
import base64
from datetime import timedelta, datetime, date
import json
from functools import wraps

related_path = "material" + os.sep + "SenseFace" + os.sep + "API"
home_path = os.environ.get("HOME_PATH") if "HOME_PATH" in os.environ.keys() else \
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "..")
full_path = os.path.join(home_path, related_path)


def get_file_abspath(key):
    """
    获取文件绝对路径(相对于full_path)
    :param key:
    :return:
    """
    file_list = os.listdir(full_path)
    files = list(filter(lambda f: os.path.join(full_path, f), file_list))
    if "" == key:
        return {"abspath_list": files}
    return {"abspath": os.path.join(full_path, random.choice(filter(lambda f: re.match(key, f), file_list)))}


def file_binary(abspath):
    with open(abspath, "rb") as f:
        bytes_str = base64.b64encode(f.read())
        return bytes_str


def file_no_base64_binary(abspath):
    with open(abspath, "rb") as f:
        bytes_str = f.read()
        return bytes_str


def random_int(min, max, return_str=False):
    return str(random.randint(min, max)) if return_str else random.randint(min, max)


def random_range(min, max, return_str=False):
    return str(random.randrange(min, max)) if return_str else random.randrange(min, max)


def random_uniform(min, max, return_str=False):
    return str(random.uniform(min, max)) if return_str else random.uniform(min, max)


def random_choice(boundary, return_str=False):
    return str(random.choice(boundary)) if return_str else random.choice(boundary)


def random_data_time_string(rule, return_str=False):
    nowTime = time.time()
    if rule == "time_s":
        return str(int(nowTime)) if return_str else int(nowTime)
    elif rule == "time_ms":
        return str(int(round(nowTime * 1000))) if return_str else int(round(nowTime * 1000))
    else:
        time_str = time.strftime(rule, time.localtime(nowTime))
        return time_str


def get_user_list(user_list):
    user_array = []
    for user in user_list:
        if "state" in user and "userId" in user and user["state"] == 1:
            user_array.append(user["userId"])
    return user_array


def id_generator():
    arr = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    last = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (
        random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18),
        random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * arr[i]
    id_card = '%s%s' % (x, last[y % 11])
    return id_card


def id_verification(id_no):
    arr = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    last = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    xlen = len(id_no)
    if xlen != 18 and xlen != 15:
        return '身份证号码长度错误'

    try:
        if xlen == 18:
            x2 = id_no[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                return '时间错误，超过允许的时间范围'
        else:
            x2 = time.strptime(id_no[6:12], '%y%m%d')
    except Exception as e:
        return '时间错误，非合法时间' + str(e)

    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(id_no[i]) * arr[i]

        if last[y % 11] != id_no[-1].upper():
            return '验证码错误'
    return True


def get_uuid1():
    temp = str(uuid.uuid1()).replace('-', '')
    return temp


def get_uuid4():
    """
    保证同一命名空间中不同名字的唯一性和不同命名空间的唯一性
    :return:
    """
    temp = str(uuid.uuid4()).replace('-', '')
    return temp


def get_uuid3(namespace, name):
    temp = str(uuid.uuid3(namespace, name)).replace("-", "")
    return temp


def get_uuid5(namespace, name):
    temp = str(uuid.uuid5(namespace, name)).replace("-", "")
    return temp


def eval_str(eval_str):
    temp = eval_str.strip('"')
    return temp


def get_delta_time(rule="%Y-%m-%d %H:%M:%S", days=0, hours=0, minutes=0, seconds=0):
    """
    csf add 20190428 以时间戳计算当前前后时间
    :param rule:
    :param days:
    :param hours:
    :param minutes:
    :param seconds:
    :return:
    """
    time_delta = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
    new_time_stamp = int(time.time()) + time_delta
    return str(time.strftime(rule, time.localtime(new_time_stamp)))


def convert_format_time_to_timestamp(format_date, format_rule="%Y-%m-%d %H:%M:%S"):
    """
    csf 返回指定格式时间 的时间戳
    :param format_date:
    :param format_rule:
    :return:  13位整形 时间戳
    """
    return int(time.mktime(time.strptime(format_date, format_rule))) * 1000


def gen_futuretime(rule, days, hours=0, minutes=0, seconds=0):
    """
    #pengjun
    :param rule:
    :param days:
    :param hours:
    :param minutes:
    :param seconds:
    :return:
    """
    # return __cal_delta_time(rule,"+",days,hours,minutes,seconds)
    today = datetime.now()
    futureday = today + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    futuretime = futureday.strftime(rule)
    temp = futureday.strftime("%Y.%m.%d")
    if "w" in rule.lower() and futuretime == "0":
        futuretime = "7"
    new_date = (today + timedelta(minutes=10)).strftime("%Y.%m.%d")
    if days == 0 and hours == 0 and str(temp) != str(new_date):
        time.sleep(600)
        return gen_futuretime(rule=rule, days=days, hours=hours, minutes=minutes, seconds=seconds)
    return str(futuretime)


def gen_pasttime(rule, days, hours=0, minutes=0, seconds=0):
    """
    #pengjun
    :param rule:
    :param days:
    :param hours:
    :param minutes:
    :param seconds:
    :return:
    """
    # return __cal_delta_time(rule,"-",days,hours,minutes,seconds)
    today = datetime.now()
    pastday = today - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    pasttime = pastday.strftime(rule)
    temp = pastday.strftime("%Y.%m.%d")
    if "w" in rule.lower() and pasttime == "0":
        pasttime = "7"
    past_date = (today - timedelta(minutes=10)).strftime("%Y.%m.%d")
    fur_date = (today + timedelta(minutes=10)).strftime("%Y.%m.%d")
    if days == 0 and hours == 0 and (str(temp) != str(past_date) or str(temp) != str(fur_date)):
        time.sleep(600)
        return gen_pasttime(rule=rule, days=days, hours=hours, minutes=minutes, seconds=minutes)
    return str(pasttime)


def gen_first_and_last_day_in_month(rule, mode="default", year=0, month=0):
    """
    获取一个月的第一天和最后一天
    :param rule: 输出字符串格式，例如%Y-%m-%d
    :param mode: default:默认按照当前时间算，year、month相对于当前时间，进行加减； custom：按照指定年月算，指定具体年与月
    :param year:
    :param month:
    :return: {"fist_day":fist_day.strftime(rule), "last_day":last_day.strftime(rule)}
    """
    if not mode or mode.lower() == "default":
        month_date = date.today().month + month
        year_date = date.today().year + year
        fist_day = date(year_date, month_date, 1)
        last_day = date(year_date, month_date + 1, 1) - timedelta(1)
        return {"first_day": fist_day.strftime(rule), "last_day": last_day.strftime(rule)}
    else:
        fist_day = date(year, month, 1)
        last_day = date(year, month + 1, 1) - timedelta(1)
        return {"first_day": fist_day.strftime(rule), "last_day": last_day.strftime(rule)}


def get_random_name(name_prefix="", name_suffix=""):
    """
    获取一个随机字符串
    :param name_prefix:字符串前缀
    :param name_suffix:字符串后缀
    :return: 大于30位自动截取
    """
    uuid_result = get_uuid1()[2:8] + get_uuid1()[16:20]
    name_str = name_prefix + uuid_result + name_suffix
    return name_str if len(name_str) <= 30 else name_str[:30]


def get_str(message, indent=4, trim_symbol=False):
    """
    格式化字符换
    :param message: 字符串
    :param indent:根据数据格式缩进显示，为None时，则不缩进
    :param trim_symbol:转换字符串之后，是否去掉首位符号
    :return:
    """
    try:
        msg = json.dumps(message, encoding='utf-8', ensure_ascii=False, indent=indent)
        if trim_symbol:
            msg = msg.replace(" ", "")
            msg = msg.replace("\\\"", "")
            msg = msg.lstrip("[{")
            msg = msg.strip("]}")
        return msg
    except:
        message = str(message)
        if trim_symbol:
            message = message.replace(" ", "")
            message = message.replace("\\\"", "")
            message = message.lstrip("[{")
            message = message.strip("]}")
        return message


def get_ip_in_str(message, index=0, is_all=False):
    try:
        ip_reg = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
        ip_list = re.findall(ip_reg, message)
        if is_all:
            return ip_list
        if index is not None and len(ip_list) <= index:
            return message
        elif index is not None:
            return ip_list[int(index)]
    except Exception:
        return message


def get_local_ip():
    """
    获取本机IP
    :return:
    """
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]
    finally:
        s.close()


def getrand(num, many):
    # 获取小写字母、数字随机数
    """
    :param num: 位数
    :param many: 个数
    :return:
    """
    s = ""
    for x in range(many):
        s = ""
        for i in range(num):
            n = random.randint(1, 2)
            if n == 1:
                numb = random.randint(0, 9)
                s += str(numb)
            else:
                nn = random.randint(1, 2)
                cc = random.randint(1, 26)
                if nn == 1:
                    numb = random.randint(0, 9)
                    s += str(numb)
                else:
                    numb = chr(96 + cc)
                    s += numb
    return s


def fail_ip_port(prefix_rtsp=False):
    """
    ycy
    随机生成ip:port
    :return:
    """
    ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    port = random_int(1000, 10000)
    ip_port = str(ip) + ":" + str(port)
    return "rtsp://" + ip_port + "/" + getrand(5, 1) if prefix_rtsp else ip_port


def getcwd(path_file, root_path=home_path):
    if os.name == "nt":
        path_file = path_file.replace("/", "\\")
    elif os.name == "posix":
        path_file = path_file.replace("\\\\", "/").replace("\\", "/")
    temp = os.path.join(root_path, path_file)
    return temp


def convert_to_array(values, log=None):
    """
    csf 转换str到list
    :param values:
    :param log:
    :return:
    """
    if not values:
        return_list = []
    elif isinstance(values, str) or isinstance(values, int) or isinstance(values, dict):
        return_list = [values]
    elif (isinstance(values, tuple) or isinstance(values, list)) and (
            isinstance(values[0], int) or isinstance(values[0], str)):
        return_list = list(set(list(values)))
        return_list.sort(key=values.index)
    elif isinstance(values, tuple) or isinstance(values, list):
        return_list = list(values)
    else:
        if log:
            log.error("资源传入格式不符合要求")
        return None
    # return_list.sort()
    # return_list.reverse()
    return return_list


def loop_chk(expression, to=5, error_info="循环等待后，未发现", return_bool=False, **kwargs):
    """
    csf 循环查询 处理
    :param expression: 需判定的表达式
    :param to:  超时时间
    :param error_info:  超时未成功的 异常提示
    :return:
    """
    t_start = time.time()
    while time.time() - t_start < to:
        if expression(**kwargs):
            return True
        time.sleep(0.5)
    else:
        if return_bool:
            return False
        else:
            raise STException(error_info)


class STException(Exception):
    """csf"""

    def __init__(self, err=""):
        super().__init__(err)


def shadow(prompt):
    """
    csf add 跟踪函数
    :param prompt:
    :return:
    """

    def decorator(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            log_ = args[0].log
            fun_name = "{}函数[{}]".format(prompt, method.__name__)
            # log_.info(("{} >>>> {}".format('=' * 20, fun_name)))
            # result = method(*args, **kwargs)
            result = try_catch(method, fun_name, log_, *args, **kwargs)
            # log_.info(("<<<< {} {}".format('=' * 20, fun_name)))
            return result

        return wrapper

    return decorator


def try_catch(func_result, test_step=None, log_=None, *args, **kwargs):
    """
    csf 需要异常捕捉的expression
    :param test_step:
    :param func_result:
    :param log_:
    :param args:
    :param kwargs:
    :return:
    """
    t_start = time.time()
    judge = False
    retry_time = 1
    if kwargs.get('retry_time'):
        retry_time = kwargs.get('retry_time') + retry_time
        del kwargs['retry_time']
    if kwargs.get('judge'):
        judge = True
        del kwargs['judge']
    while retry_time:
        retry_time -= 1
        try:
            result = func_result(*args, **kwargs)
        except Exception as e:
            # print(str(traceback.format_exc()))
            if log_:
                log_.error("[{}] 出现异常{},请检查... Total cost {}".format(test_step, e, round(time.time() - t_start, 2)))
            if not retry_time:
                if judge:
                    return False
                else:
                    raise traceback.format_exc()
            time.sleep(0.3)
        else:
            if log_:
                log_.info("[{}] 完成. Total cost {}s".format(test_step, round(time.time() - t_start, 2)))
            return result


def get_num_from_str(src_str):
    """
    csf 过滤字符串中的数字
    :param src_str:
    :return:
    """
    var = re.sub(r'\D', '', src_str)
    return var and int(var)


def get_xls_content(xls_, index_name='RTSP'):
    """
    csf  临时处理xlsx的获取
    :param xls_:
    :param index_name:
    :return:
    """
    import xlrd
    book = xlrd.open_workbook(xls_)
    sheet_ = book.sheet_by_name(index_name)
    xls_dict = {}
    for j in range(1, sheet_.nrows):
        line_lst = [x.value for x in sheet_.row(j) if x.value]
        k, v = line_lst[0], line_lst[1:]
        xls_dict[k] = v
    return xls_dict


def get_random_num(num_len=11, phone=False):
    if not phone:
        return ''.join(str(random.choice(range(10))) for _ in range(num_len))
    else:
        return '13' + ''.join(str(random.choice(range(10))) for _ in range(9))


def get_delta(start_time, end_time=None, format_rule="%Y-%m-%d %H:%M:%S"):
    end_time = end_time and convert_format_time_to_timestamp(end_time, format_rule=format_rule) or int(
        time.time() * 1000)
    start_time = convert_format_time_to_timestamp(start_time, format_rule=format_rule)
    return int((end_time - start_time) / 1000)


def random_str_re(regular, limit=999):
    from xeger import Xeger
    x = Xeger(limit=limit)
    temp = x.xeger(regular)
    return temp


def get_mix_str_num(val_len=20):
    fake_val = ''.join(str(random.choice(range(10))) for _ in range(val_len))
    return fake_val


if __name__ == '__main__':
    a = get_delta_time(days=-7)
    print(a)
