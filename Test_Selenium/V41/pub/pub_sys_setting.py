#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random

from v43.pub.pub_menu import MainPage
from v43.ele_set.page_sys_setting import SysSettingEle
from v43.pub.pub_widget import WidPub
from v43.pub.pub_base import PublicClass


class SettingAction(PublicClass):
    """
    系统设置单个动作
    """

    def __init__(self, web_driver, **kwargs):
        kwargs['local_mod'] = "系统设置"
        super().__init__(web_driver, **kwargs)
        self.driver = web_driver
        self.el = SysSettingEle
        self.log = web_driver.log
        self.wid = WidPub(self.driver, **kwargs)
        self.wid.wid_chk_loading()

    def click_left_menu(self, type_num=1):
        """
        进入系统设置后点击左侧按钮
        :param type_num: int 1.系统信息  2.功能配置   3.系统维护  4.接入/回放平台管理     5.登录IP管理
        :return:
        """
        if type_num == 1:
            self.driver.ele_click(ele=self.el.sys_info)
        if type_num == 2:
            self.driver.ele_click(ele=self.el.function_conf)
        if type_num == 3:
            self.driver.ele_click(ele=self.el.sys_maintain)
        if type_num == 4:
            self.driver.ele_click(ele=self.el.join_back_plat)
        if type_num == 5:
            self.driver.ele_click(ele=self.el.login_ip)


class SettingModule(SettingAction):
    """
    系统设置组合动作
    """

    def get_sys_info(self, info_num=1):
        """
        点击系统信息后获取右侧所有元素
        :param info_num: 1.系统信息4个字, 2.系统名称4个字, 3.系统名称对应的值, 4.版本号3个字 5.版本号对应的值
                        6.License截止日期几个字, 7.License对应值
        :return: 相对应的值
        """
        self.click_left_menu(type_num=1)
        if info_num == 1:
            info = self.driver.ele_get_val(ele=self.el.sys_info_r)
        elif info_num == 2:
            info = self.driver.ele_get_val(ele=self.el.sys_name_r)
        elif info_num == 3:
            info = self.driver.ele_get_val(ele=self.el.sys_name_r_c)
        elif info_num == 4:
            info = self.driver.ele_get_val(ele=self.el.version_r)
        elif info_num == 5:
            info = self.driver.ele_get_val(ele=self.el.version_r_c)
        elif info_num == 6:
            info = self.driver.ele_get_val(ele=self.el.license_r)
        elif info_num == 7:
            info = self.driver.ele_get_val(ele=self.el.license_r_c)
        else:
            self.log.error("传入数字必须是1-7,现在传入的是{}".format(info_num))
            return False
        if not info:
            self.log.error("没有获取到对应的值")
            return False
        else:
            # self.driver.quit()
            return info

    def get_func_conf_info(self, info_num=1):
        """
        获取功能配置信息
        :param info_num: 1.右侧功能配置4个字, 2.布控2个字, 3.告警推送条数6个字 4.告警推送条数对应的值
                         5.布控任务阈值下限8个字 6.阈值对应的值
        :return: 相对应的值
        """
        self.click_left_menu(type_num=2)
        if info_num == 1:
            info = self.driver.ele_get_val(ele=self.el.function_conf_r)
        elif info_num == 2:
            info = self.driver.ele_get_val(ele=self.el.d_c)
        elif info_num == 3:
            info = self.driver.ele_get_val(ele=self.el.alarm_num)
        elif info_num == 4:
            info = self.driver.ele_get_val(ele=self.el.alarm_num_c)
        elif info_num == 5:
            info = self.driver.ele_get_val(ele=self.el.threshold_floor)
        elif info_num == 6:
            info = self.driver.ele_get_val(ele=self.el.threshold_floor_c)
        else:
            self.log.error("传入数字必须是1-6,现在传入的是{}".format(info_num))
            return False
        if not info:
            self.log.error("没有获取到对应的值")
            return False
        else:
            self.driver.quit()
            return info

    def edit_func_conf(self):
        """
        编辑功能配置
        :return:
        """
        pass

    def new_gb_platform(self, platform_name="GB28181"):
        platform_type = 'GB28181'
        ip, port = self.cf.fail_ip_port().split(":")
        self.click_left_menu(type_num=4)
        self.driver.ele_click(self.el.platform_btn.format(platform_type))
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "平台名称"), platform_name)
        # self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "平台ID"), self.cf.get_random_name())
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "平台ID"),
                              ''.join(str(random.choice(range(10))) for _ in range(20)))  # 需求修改：平台ID要20数字
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "平台IP"), ip)
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "端口"), port)
        self.driver.ele_click(self.el.new_platform_confirm_btn.format(platform_type, '确定'), load=True)
        return self.wid.wid_get_alert_label()

    def new_1400_platform(self, platform_name="GAT1400"):
        platform_type = 'GAT1400'
        ip, port = self.cf.fail_ip_port().split(":")
        self.click_left_menu(type_num=4)
        self.driver.ele_click(self.el.platform_btn.format(platform_type))
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "平台名称"), platform_name)
        self.wid.wid_drop_down(platform_type, self.el.new_platform_ipt.format(platform_type, "平台厂商"))
        # self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "输入平台ID"), self.cf.get_random_name())
        # self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "输入我方平台ID"), self.cf.get_random_name())
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "输入平台ID"),
                              ''.join(str(random.choice(range(10))) for _ in range(20)))  # 需求修改：平台ID要20数字
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "输入我方平台ID"),
                              ''.join(str(random.choice(range(10))) for _ in range(20)))  # 需求修改：平台ID要20数字
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "平台IP"), ip)
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "端口"), port)
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "用户名"), "hw")
        self.driver.ele_input(self.el.new_platform_ipt.format(platform_type, "密码"), "hw")
        self.driver.ele_click(self.el.new_platform_confirm_btn.format(platform_type, '确定'), load=True)
        return self.wid.wid_get_alert_label()


if __name__ == '__main__':
    from common.w_driver import WDriver

    driver = WDriver()
    driver.open_url("http://10.111.32.91:10219/#/users")
    MainPage.login_in(driver, 'caokemeng2', 'admin1234')
    b = SettingModule(driver, mod_name="系统设置")
    print(b.get_func_conf_info(info_num=6))
