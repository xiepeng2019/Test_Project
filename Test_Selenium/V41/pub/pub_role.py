#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import time

from common.common_func import shadow
from sc_common.sc_define import define
from v43.ele_set.page_role import RolePageEle
from v43.pub.pub_base import PublicClass
from common import common_func as CF


class RoleAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el_role = RolePageEle
        self.df = define()

    def chk_role(self, role_name, status="不限"):
        now_srh_status = self.driver.ele_get_val(self.el_role.srh_status_ele, attr_name='value', chk_visit=True)
        if now_srh_status != status:
            self.wid.wid_drop_down(val=status, trig_wid=self.el_role.srh_status_ele)
        self.driver.ele_input(self.el_role.search_role_input, role_name, enter=True)
        self.wid.wid_chk_loading()
        if not self.driver.ele_exist(self.el_role.role_row):
            return False
        for row_ in range(len(self.driver.ele_list(self.el_role.role_row))):
            now_tr = self.el_role.role_row + ':nth-of-type({})>'.format(row_ + 1)
            row_name = self.driver.ele_get_val(self.el_role.role_row_name.format(now_tr))
            if row_name == role_name:
                return now_tr
        else:
            self.log.warning("未发现指定的角色名[{}]".format(role_name))
            return False

    def goto_role_detail(self, role_name):
        role_row = self.chk_role(role_name=role_name)
        self.driver.ele_click(self.el_role.role_row_detail.format(role_row))

    def goto_role_edit(self, role_name):
        role_row = self.chk_role(role_name=role_name)
        self.driver.ele_click(self.el_role.role_row_edit.format(role_row))

    def goto_get_role_num(self):
        return CF.get_num_from_str(self.driver.ele_get_val(self.el_role.role_total_num_ele))


class RoleModule(RoleAction):

    @shadow("新建角色")
    def new_role(self, role_name=None, chg_right_dict='all', enable_role=True):
        role_name = role_name or CF.get_random_name(self.df.name_prefix)
        self.driver.ele_click(self.el_role.add_role_button)
        self.wid.wid_chk_loading()
        self.driver.ele_input(self.el_role.role_input_name, role_name)
        self.chg_role_power(chg_right_dict=chg_right_dict)
        self.driver.ele_click(self.el_role.save_button)
        create_res = self.wid.wid_get_alert_label()
        # 判断是否有创建成功的内容
        if "新建角色成功" not in create_res:
            return False
        self.collect_resource(self.df.key_role, role_name)
        if enable_role and not self.chg_role_status(role_name=role_name):
            return False
        return role_name

    @shadow("新建角色v2")
    def new_role_v2(self, role_name=None, only_right=None, remove_right=None, enable_role=True):
        role_name = role_name or CF.get_random_name(self.df.name_prefix)
        self.driver.ele_click(self.el_role.add_role_button)
        self.wid.wid_chk_loading()
        self.driver.ele_input(self.el_role.role_input_name, role_name)
        self.chg_role_power_v2(only_right=only_right, remove_right=remove_right)
        self.driver.ele_click(self.el_role.save_button)
        create_res = self.wid.wid_get_alert_label()
        # 判断是否有创建成功的内容
        if "新建角色成功" not in create_res:
            return False
        self.collect_resource(self.df.key_role, role_name)
        if enable_role and not self.chg_role_status(role_name=role_name):
            return False
        return role_name

    @shadow("删除角色")
    def del_role(self, role_name, rtn_msg=False):
        role_row = self.chk_role(role_name=role_name)
        self.driver.ele_click(self.el_role.role_row_del.format(role_row))
        tips = self.driver.ele_get_val(self.el_role.del_tips_msg)
        if '无法删除，所选角色正在被用户使用。' in tips:
            self.log.error(tips)
            self.driver.ele_click(self.el_role.del_tips_btn)
            return False if not rtn_msg else tips
        self.driver.ele_click(self.el_role.ensure_delete_role_button)
        if self.wid.wid_get_alert_label():
            self.collect_resource(self.df.key_role, remove_value=role_name)
            return True

    @shadow("修改角色状态")
    def chg_role_status(self, role_name, enable=True):
        role_row = self.chk_role(role_name=role_name)
        status_el = self.el_role.role_row_status.format(role_row)
        status_btn = self.el_role.role_row_enable.format(role_row)
        if ("禁用" in self.driver.ele_get_val(status_el) and enable) or (
                "启用" in self.driver.ele_get_val(status_el) and not enable):
            self.driver.ele_click(status_btn, wait_time=2)
            self.driver.ele_click(self.el_role.ensure_ban_role)
            new_res = self.wid.wid_get_alert_label()
            if not new_res:
                return False
            time.sleep(1)
        now_status = self.driver.ele_get_val(status_el, chk_visit=True)
        return (enable and "启用" in now_status) or (not enable and "禁用" in now_status)

    @shadow("修改角色")
    def chg_role(self, role_name, new_role_name=None, chg_dict=None):
        self.goto_role_edit(role_name=role_name)
        new_role_name and self.driver.ele_input(self.el_role.role_input_name, new_role_name)
        chg_dict and self.chg_role_power(chg_dict=chg_dict)
        self.driver.ele_click(self.el_role.save_button)
        if self.wid.wid_get_alert_label():
            self.collect_resource(self.df.key_role, resource_value=new_role_name, remove_value=role_name)
            return True

    @shadow("获取角色权限")
    def get_role_power(self, role_name):
        self.goto_role_detail(role_name=role_name)
        time.sleep(1)
        return self.wid.wid_role_power_tree()

    @shadow("修改角色权限")
    def chg_role_power(self, chg_right_dict):
        if isinstance(chg_right_dict, str) and chg_right_dict.lower() == 'all':
            self.driver.ele_click(self.el_role.role_power_slt_all)
        elif isinstance(chg_right_dict, dict):
            self.wid.wid_role_power_tree(chg_right_dict=chg_right_dict)
        else:
            raise Exception("Args error: [{}]".format(chg_right_dict))

    @shadow("修改角色权限v2")
    def chg_role_power_v2(self, only_right=None, remove_right=None):
        def split_right(right_lst, power=False):
            void_dict = {}
            for per in right_lst:
                if '-' in per:
                    if per.split('-')[0] not in void_dict:
                        void_dict[per.split('-')[0]] = {per.split('-')[1]: power}
                    else:
                        void_dict[per.split('-')[0]].update({per.split('-')[1]: power})
            return void_dict

        only_right = self.cf.convert_to_array(only_right)
        remove_right = self.cf.convert_to_array(remove_right)
        if not only_right:
            self.driver.ele_click(self.el_role.role_power_slt_all)
            if remove_right:
                self.wid.wid_role_power_tree(chg_right_dict=split_right(remove_right, False))
        else:
            self.wid.wid_role_power_tree(chg_right_dict=split_right(only_right, True))

    def main(self):
        self.get_role_power(role_name='hw')
