#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from datetime import datetime
import logging
import os
import platform
import random
import time
import re

from cloghandler import ConcurrentRotatingFileHandler as LogHandler


def get_simple_log(file_name="info", log_level=logging.INFO, path="", formatter=None):
    """获取一个简单的log"""
    if not formatter:
        formatter = "%(asctime)s [%(levelname)s] [%(filename)s %(funcName)s %(lineno)d]: %(message)s "
    log_file = os.path.join(path, file_name + ".log")
    log = logging.getLogger(log_file)
    log.setLevel(log_level)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter_set = logging.Formatter(formatter)
    file_handler.setFormatter(formatter_set)
    log.addHandler(file_handler)
    return log


if platform.system() == "Windows":
    from logging.handlers import RotatingFileHandler as LogHandler, RotatingFileHandler

# csf add color for console 20190415
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[%d;%d;%dm"


# BOLD_SEQ = "\033[1m"

def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ)  # .replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


COLORS = {
    'CRITICAL': [1, CYAN, RED],
    'ERROR': [0, -2, RED],
    'WARNING': [0, -2, BLUE],
    'INFO': [0, -2, GREEN],
    'DEBUG': [0, -2, BLACK]
}


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (
            COLORS[levelname][0], 30 + COLORS[levelname][2], 40 + COLORS[levelname][1]) + '[{}]'.format(levelname)
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


class ColoredLogger(logging.Logger):
    FORMAT = '%(levelname)s[%(process)d][%(thread)d]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s$RESET'
    COLOR_FORMAT = formatter_message(FORMAT, True)

    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)
        color_formatter = ColoredFormatter(self.COLOR_FORMAT)
        console = logging.StreamHandler()
        console.setFormatter(color_formatter)
        self.addHandler(console)


#  csf add color for console 20190415 as above


def log_config(f_level=logging.INFO, c_level=logging.INFO, out_path='', filename='info', fix=False):
    logfile = os.path.join(out_path, filename) + '-' + time.strftime('%Y_%m%d_%H%M%S', time.localtime()) + '.log' \
        if not fix else os.path.join(out_path, filename) + '.log'
    logger = logging.getLogger(logfile)

    if f_level is None:
        logger.setLevel(c_level)
    else:
        logger.setLevel(f_level)

    formatter = logging.Formatter(
        '[%(levelname)s][%(process)d][%(thread)d]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')
    if platform.system() == "Windows":
        FORMAT = '%(levelname)s[%(process)d][%(thread)d]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s$RESET'
        COLOR_FORMAT = formatter_message(FORMAT, True)
        color_formatter = ColoredFormatter(COLOR_FORMAT)
        ch = logging.StreamHandler()
        ch.setFormatter(color_formatter)
        ch.setLevel(c_level)
        logger.addHandler(ch)
    else:
        ch = logging.StreamHandler()
        ch.setLevel(c_level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if f_level is not None:
        fh = LogHandler(logfile, maxBytes=100 * 1024 * 1024, backupCount=50, encoding='utf-8')
        fh.setLevel(f_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    if len(logger.handlers)>2:
        logger.removeHandler(ch)
        f_level and logger.removeHandler(fh)
    return logger, logfile


def get_simple_file_log(file_name="info", log_level=logging.INFO, path="",
                        formatter="[%(levelname)s]-%(asctime)s:%(message)s"):
    log_file = os.path.join(path, file_name + ".log")
    log = logging.getLogger(log_file)
    log.setLevel(log_level)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter_set = logging.Formatter(formatter)
    file_handler.setFormatter(formatter_set)
    log.addHandler(file_handler)
    return log


def set_app_log(app):
    """
    设置flask自带的log
    :param app:
    :return:
    """
    l_format = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s %(funcName)s %(lineno)d]: %(message)s ")
    r_handler = LogHandler("app.log", maxBytes=20480000, backupCount=10, encoding='UTF-8')
    r_handler.setLevel(logging.INFO)
    r_handler.setFormatter(l_format)
    app.logger.addHandler(r_handler)



######## 为调试用例使用 ##################
class define_class:
    """
    csf add 20190409 为单用例脚本debug时使用，可保证每个脚本的入口代码完全一致，消除服务器和脚本名的差异
    """
    sf_define_file = "d:/sf_ip.txt"
    sf_debug_log_dir = "../../../logs"
    sf_debug_log_prefix = 'AT_SF_'
    if os.path.exists(sf_define_file):
        __host, user, pwd = [x.strip('\r\n\t ') for x in[x for x in open(sf_define_file, encoding="utf-8").readlines() if len(x) > 10][0].split('\t')]
        sf_host = "{}:10219".format(__host)
    else:
        sf_host = "0.0.0.0"
        user, pwd = 'admin', 'admin2018'
    if not (os.path.exists(sf_debug_log_dir) and os.path.isdir(sf_debug_log_dir)):
        try:
            os.mkdir(sf_debug_log_dir)
        except Exception as e:
            print(e)
            __sf_debug_log_dir = ''


sf_define = define_class
random_name = lambda name_prefix: name_prefix + time.strftime("%Y%m%d_%H%M%S_") + str(
    random.randint(100000, 999999))
__func_key = lambda file_local: re.findall("\.(.+)'", str(type(file_local['self'])))[0]
log_define = lambda file_local: \
    log_config(f_level=logging.INFO, c_level=logging.INFO, out_path=define_class.sf_debug_log_dir,
               filename=random_name('{}{}_'.format(define_class.sf_debug_log_prefix, __func_key(file_local))),
               fix=True)[0]
func_define = lambda file_local: file_local[__func_key(file_local)]

######## 为调试用例使用 ##################
