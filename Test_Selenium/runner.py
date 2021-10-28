#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from datetime import datetime
import sys
import os
import importlib
import time

from report_temp import *
from common.w_driver import WDriver


class Timer(object):

    def __init__(self, wait_time, sleep_interval=0.5):

        # '2018-09-28 22:45:50.000'
        self.wait_time = datetime.strptime(wait_time, "%Y-%m-%d %H:%M:%S")
        self.sleep_interval = sleep_interval

    def start(self, ):
        print('正在等待到达设定时间:%s' % self.wait_time)
        now_time = datetime.now
        while True:
            if now_time() >= self.wait_time:
                print('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)


def scan_script(script_dir_, project_dir):
    parent_str = '.py'
    script_dict = {}
    for i, _, k in os.walk(script_dir_):
        for kk in k:
            if kk.endswith(parent_str) and '__init__' not in kk:
                script_dict[os.path.splitext(kk)[0]] = i.replace(project_dir, '').strip('\\')
    return script_dict


def exec_script(script_dict, test_conf, driver=None):
    tst_module_config_file = "tst_module.ini"
    run_result = {}
    need_tst_lst = [x.split('#')[0].strip('\r\n ') for x in
                    open(tst_module_config_file, 'r', encoding="utf-8").readlines() if x.strip('\r\n ') and not
                    x.startswith('#')]

    def filter_(a):
        return [x for x in need_tst_lst if x in a]

    need_tst_dict = {}
    for script, path in script_dict.items():
        if filter_(path):
            need_tst_dict[script] = path
    for script, path in need_tst_dict.items():
        import_path = os.path.join(path, script).replace('\\', '.')
        now_i = importlib.import_module(import_path)
        current_script = [now_i.__getattribute__(x) for x in dir(now_i) if
                          not x.startswith('__') and 'scripts' in str(now_i.__getattribute__(
                              x))][0]
        this_script_result = current_script.main(current_script, driver, config=test_conf)
        this_script_result['path'] = path
        run_result.update({script: this_script_result})
    return run_result


def runner_main(script_path, conf, driver=None):
    scan_res = scan_script(script_dir_=script_path, project_dir=project_path)
    exec_res = exec_script(script_dict=scan_res, test_conf=conf, driver=driver)
    if conf.get('fail_retry'):
        # 失败重试 过滤出error和fail用例 建集合重运行
        new_scan_res = {}
        for kk, vv in exec_res.items():
            if vv['test_result'].lower() != "pass":
                new_scan_res[kk] = scan_res[kk]
        new_exec_res = exec_script(script_dict=new_scan_res, test_conf=conf, driver=driver)
        for kk, vv in new_exec_res.items():
            if kk in exec_res:
                if exec_res[kk]['test_result'].lower() == "fail":
                    retry_type = "Fail"
                else:
                    retry_type = "Error"
                vv['test_name'] = vv['test_name'] + '   =={} retry'.format(retry_type)
                exec_res[kk] = vv
    # 拆解用例 分组
    exec_res_dict = {}
    for script, script_detail in exec_res.items():
        script_path = script_detail['path'].split('\\')[-1]
        if script_path not in exec_res_dict:
            exec_res_dict[script_path] = {script: script_detail}
        else:
            exec_res_dict[script_path].update({script: script_detail})
    cost_time = int(time.time() - t_start)
    cost_time_format = '{}h{}m{}s'.format(int(cost_time / 3600), int(cost_time % 3600 / 60), cost_time % 60)
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t_start))
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    generate_report(exec_res_dict, {'cost_time': cost_time_format, 'start_time': start_time, 'end_time': end_time},
                    retry_flag=conf.get('fail_retry'))


if __name__ == '__main__':
    expect_date_time = "2020-06-30 12:00:30"
    Time = Timer(expect_date_time)
    Time.start()
    local_env_info_file = r"d:\sf_ip.txt"
    web = None
    project_path = os.getcwd()  # r"D:\\Ui_Auto\sensecity_ui\\"
    sys.path.append(project_path)
    script_dir = os.path.join(project_path, 'v42', 'scripts', 'Main_flow')
    t_start = time.time()
    with open(local_env_info_file, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip('\r\n') or f.readline().strip('\r\n') or f.readline().strip('\r\n')
        host, user, pwd = first_line.split('\t')
    tst_conf = {
        "host": host,  # "http://10.111.32.72",
        "user": user,  # "chi",
        "pwd": pwd,  # "admin1234",
        "hub_url": "http://10.9.242.37:4444/wd/hub",
        "browser": "chrome",
        "fairy": True,
        "fail_retry": False,
    }
    # web = WDriver(**conf)
    runner_main(script_path=script_dir, conf=tst_conf, driver=web)
