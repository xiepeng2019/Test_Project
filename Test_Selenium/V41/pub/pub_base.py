#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# __author__ = 'csf'
# 此部分 各模块公共方法的母类,抽取共性,简化代码
from common.common_func import convert_to_array, shadow
from common import common_func
from sc_common.sc_define import define, define_camera
from v43.ele_set.page_menu import LoginPageEle
from v43.pub.pub_menu import MainPage
from v43.pub.pub_widget import WidPub
import time


class PublicClass(object):
    def __init__(self, driver, **kwargs):
        self.driver = driver
        self.df = define()
        self.df_cam = define_camera()
        self.cf = common_func
        self.el = None
        self.log = kwargs.get('log')
        self.wid = WidPub(self.driver, **kwargs)
        self.menu_name = kwargs.get('local_mod')
        self.store_key = define.store_key
        self.host = kwargs.get('host')
        self.user = kwargs.get('user')
        self.pwd = kwargs.get('pwd')
        if kwargs.get('local_mod') == kwargs.get('mod_NO1'):
            self.wid.wid_alarm_msg()
            # MainPage.into_menu(driver, kwargs.get('mod_NO1'))  # 多模块时的第一导航
            self.insert_small_bag()
        # self.wid.wid_chk_loading()
        # self.wid.wid_alarm_msg()

    @shadow("WEB导航")
    def into_menu(self, menu_name=None):  # 各属性模块的导航
        menu_name = menu_name or self.menu_name
        MainPage.into_menu(self.driver, menu_name)

    @shadow("注销登录")
    def login_out(self):  #
        return MainPage.login_out(self.driver)

    @shadow("登录WEB")
    def login_in(self, user, pwd):
        return not MainPage.login_in(self.driver, username=user, password=pwd)

    @shadow("新用户首次登录")
    def login_first(self, user, dft_pwd=None, new_pwd=None):
        dft_pwd = dft_pwd or self.df.dft_new_user_pwd
        new_pwd = new_pwd or self.df.new_pwd
        return MainPage.login_first_act(self.driver, user=user, dft_pwd=dft_pwd, new_pwd=new_pwd)

    @shadow("切换到新用户")
    def switch_new_user(self, user, dft_pwd=None, new_pwd=None):
        dft_pwd = dft_pwd or self.df.dft_new_user_pwd
        new_pwd = new_pwd or self.df.new_pwd
        self.login_out()
        self.login_first(user=user, dft_pwd=dft_pwd, new_pwd=new_pwd)
        # time.sleep(5)   # 修改完密码后，需等待自动跳转到登录页
        print(self.driver.ele_exist(LoginPageEle.login_btn, timeout=1))
        if not self.login_in(user=user, pwd=new_pwd):
            self.log.error('新帐户[{}]登录失败'.format(user))
            return False
        return self.wid.wid_alarm_msg()

    @shadow("切换用户")
    def switch_user(self, user, pwd=None):
        pwd = pwd or self.df.new_pwd
        self.login_out()
        login_res = self.login_in(user=user, pwd=pwd)
        self.wid.wid_alarm_msg()
        # if not login_res and 'UI_pre_' in user:
        #     return self.switch_new_user(user=user)
        return login_res

    def insert_small_bag(self):
        """
        csf 为log插入bag属性并生成一个字典，key为user [后续此key可能在并发时需扩充识别度]
        :return:
        """
        # resource_key = args[0].get('host').replace('.','_')+args[0].get('user')
        # resource_store_key = args_tuple[0].get('user')
        log_ = self.log
        resource_store_key = self.store_key
        if not hasattr(log_, 'bag'):
            log_.bag = {}
        if resource_store_key not in log_.bag:
            log_.bag['files_'] = []
            log_.bag[resource_store_key] = {
                define.key_crowd_task: [],
                define.key_camera: [],
                define.key_camera_group: [],
                define.key_camera_block: [],
                define.key_lib: [],
                define.key_static_lib: [],
                define.key_task: [],
                define.key_role: [],
                define.key_dep: [],
                define.key_user: [],
                define.key_region_task: [],
                define.key_into_lib_task: [],
                define.key_check_repeat: []
            }

    def collect_resource(self, resource_type=None, resource_value=None, remove_value=None):
        """
        csf  搜集资源时使用key;
        :param resource_type:
        :param resource_value: name
        :param remove_value: name
        :return:
        """
        log_ = self.log
        store_key = self.store_key
        if not isinstance(resource_value, bool):
            resource_value = convert_to_array(resource_value)
        if hasattr(log_, 'bag') and store_key in log_.bag:
            if resource_value:
                if resource_type == 'files_':
                    log_.bag[resource_type].extend(resource_value)
                else:
                    log_.bag[store_key][resource_type].extend(resource_value)
            if remove_value and remove_value in log_.bag[store_key][resource_type]:
                log_.bag[store_key][resource_type].remove(remove_value)
