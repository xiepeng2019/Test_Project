#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# __author__ = 'csf'
# 此部分用于放置公共组件
import random
import time
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from common import common_func as CF
from sc_common.sc_define import define
from v43.ele_set.page_wiget import GeneralWidgetEle
from v43.pub.pub_menu import MainPage


class WidPub:
    def __init__(self, driver, **kwargs):
        self.driver = driver
        self.log = kwargs.get('log')
        self.el = GeneralWidgetEle

    def wid_tree(self, need_dep, root_e=None):
        """
        左侧部门树结构 视频源左侧部门选择  弃用==待删除
        :param root_e:  # css=.rz-tree
        :param need_dep:
        :return:
        """
        if not root_e:
            root_e = "css=.rz-tree"
        all_root_ele = self.driver.ele_list(root_e + '>.rz-tree-node')
        # print(len(all_root_ele))
        tmp_set = []
        for i in range(len(all_root_ele)):
            root_node = root_e + '>div:nth-of-type({})'.format(i + 1)
            root_node_1 = root_node + '>div:nth-of-type(1)'
            expand_ele = root_node_1 + '>span'
            grain_ele = root_node_1 + '>div'
            name_ele = grain_ele + '>div:nth-of-type(1)'
            num_ele = grain_ele + '>.count'
            more_ele = grain_ele + '>.more'
            now_name = self.driver.ele_get_val(name_ele)
            # print(now_name)
            if need_dep != now_name:
                tmp_val = self.driver.ele_get_val(expand_ele, attr_name='class', chk_visit=False)
                if tmp_val and 'expand-icon' in tmp_val and 'leaf' not in tmp_val:
                    tmp_set.append(root_node)
            else:
                self.log.warning("=" * 80)
                self.driver.ele_click(name_ele, load=True)
                return name_ele, num_ele, more_ele
        for j in tmp_set:
            expand_el = j + '>div:nth-of-type(1)>span'
            if 'expanded' not in self.driver.ele_get_val(expand_el, 'class', chk_visit=False):
                self.driver.ele_click(expand_el)
                time.sleep(0.5)
            return_val = self.wid_tree(need_dep, j + '>div:nth-of-type(2)')
            if return_val:
                return return_val

    def wid_tree2(self, need_dep, root_e=None, del_grp=False, return_lst=False):
        """
        左侧部门树结构 视频源左侧部门选择
        :param root_e:  # css=.rz-tree
        :param del_grp:
        :param need_dep:
        :return:
        """
        if not root_e:
            root_e = "css=.rz-tree>.rz-tree-node:nth-of-type(2)"  # 一级部门
            if del_grp:
                root_e = "css=.rz-tree>.rz-tree-node:nth-of-type(3)"  # 已删除分组
        expand_ele = root_e + '>div:nth-of-type(1)>span'
        expand_val = self.driver.ele_get_val(expand_ele, 'class', chk_visit=False)
        if 'expand-icon' in expand_val and 'expanded' not in expand_val and 'leaf' not in expand_val:
            self.driver.ele_click(expand_ele)

        # loop start
        def tree_loop(root_ee):
            child_root_node_ele = root_ee + '>div:nth-of-type(2)'
            child_node_ele = child_root_node_ele + '>div'
            all_node_ele = self.driver.ele_list(child_node_ele)
            tmp_set = []
            for i in range(len(all_node_ele)):
                this_node_ = child_node_ele + ':nth-of-type({})'.format(i + 1)
                self_node_ = this_node_ + '>div:nth-of-type(1)'.format(i + 1)
                self_node_expand = self_node_ + '>span'
                self_node_info = self_node_ + '>div'
                self_node__info_name = self_node_info + '>div'
                self_node__info_num = self_node_info + '>span:nth-of-type(1)'
                self_node__info_more = self_node_info + '>span:nth-of-type(2)'
                name = self.driver.ele_get_val(self_node__info_name)
                num = self.driver.ele_get_val(self_node__info_num)
                # print(name, num)
                expanded_val = self.driver.ele_get_val(self_node_expand, 'class', chk_visit=False)
                if 'expand-icon' in expanded_val and 'leaf' not in expanded_val:
                    tmp_set.append(this_node_)
                if name == need_dep:
                    self.driver.ele_click(self_node__info_name)
                    if return_lst:
                        return self_node__info_name, self_node__info_num, self_node__info_more
                    else:
                        return self_node_info
            for j in tmp_set:
                new_expand_el = j + '>div:nth-of-type(1)>span'
                expanded_val_ = self.driver.ele_get_val(new_expand_el, 'class', chk_visit=False)
                if 'expand-icon' in expanded_val_ and 'leaf' not in expanded_val_ and 'expanded' not in expanded_val_:
                    self.driver.ele_click(new_expand_el)
                    time.sleep(0.5)
                return_val = tree_loop(j)
                if return_val:
                    return return_val

        return tree_loop(root_ee=root_e)

    def wid_new_user_camera_tree2(self, dep_list, root_e=None):
        """
        新建用户 时的 视频源选择
        :param root_e:  # css=.rz-tree
        :param dep_list:
        :return:
        """
        root_e = root_e or "css=body>div:nth-last-child(1) .rz-tree>div:first-child"
        expand_ele = root_e + '>div:nth-of-type(1)>span'
        expand_val = self.driver.ele_get_val(expand_ele, 'class', chk_visit=False)
        name_el = self.driver.ele_get_val(root_e + '>div:nth-of-type(1)>span:last-child')
        if name_el in dep_list:
            self.driver.ele_click(root_e + '>div:nth-of-type(1)>label')
            return True
        if 'expand-icon' in expand_val and 'expanded' not in expand_val and 'leaf' not in expand_val:
            self.driver.ele_click(expand_ele)

        # loop start
        def tree_loop(root_ee):
            child_root_node_ele = root_ee + '>div:nth-of-type(2)'
            child_node_ele = child_root_node_ele + '>div'
            all_node_ele = self.driver.ele_list(child_node_ele)
            tmp_set = []
            for i in range(len(all_node_ele)):
                this_node_ = child_node_ele + ':nth-of-type({})'.format(i + 1)
                self_node_ = this_node_ + '>div:nth-of-type(1)'.format(i + 1)
                self_node_expand = self_node_ + '>span'
                self_node_cb = self_node_ + '>label'
                self_node_name = self_node_ + '>span:last-child'
                name = self.driver.ele_get_val(self_node_name)
                # print(name)
                expanded_val = self.driver.ele_get_val(self_node_expand, 'class', chk_visit=False)
                if 'expand-icon' in expanded_val and 'leaf' not in expanded_val:
                    tmp_set.append(this_node_)
                if name in dep_list:
                    self.driver.ele_click(self_node_cb)
                    dep_list.remove(name)
                    if not dep_list:
                        return True
            for j in tmp_set:
                new_expand_el = j + '>div:nth-of-type(1)>span'
                expanded_val_ = self.driver.ele_get_val(new_expand_el, 'class', chk_visit=False)
                if 'expand-icon' in expanded_val_ and 'leaf' not in expanded_val_ and 'expanded' not in expanded_val_:
                    self.driver.ele_click(new_expand_el)
                    time.sleep(0.5)
                return_val = tree_loop(j)
                if return_val:
                    return return_val

        return tree_loop(root_ee=root_e)

    def wid_tree_slt_camera_group(self, need_dep, root_e=None):
        """
        编辑/新建时，视频源分组选择
        :param root_e:  # css=.rz-tree
        :param need_dep:
        :return:
        """
        time.sleep(0.5)
        slt_grp_srh = 'css=.video-group-tree-wrapper .rz-search-input input'  # 分组搜索框
        self.driver.ele_input(slt_grp_srh, need_dep, enter=True)
        return self.driver.ele_click('//span[text()="{}"]'.format(need_dep))
        time.sleep(1)
        self.wid_tree_slt_camera_group2(need_dep=need_dep, root_e=root_e)

    def wid_tree_slt_camera_group2(self, need_dep, root_e=None):
        if not root_e:
            root_e = "css=.tree-content>.rz-tree>.rz-tree-node:nth-of-type(1)"  # 一级部门
        expand_ele = root_e + '>div:nth-of-type(1)>span'
        expand_val = self.driver.ele_get_val(expand_ele, 'class', chk_visit=False)
        if expand_val and 'expand-icon' in expand_val and 'expanded' not in expand_val and 'leaf' not in expand_val:
            self.driver.ele_click(expand_ele)

        # loop start
        def tree_loop(root_ee):
            child_root_node_ele = root_ee + '>div:nth-of-type(2)'
            child_node_ele = child_root_node_ele + '>div'
            if not self.driver.ele_exist(child_node_ele):
                self.driver.ele_click(root_ee + '>div:nth-of-type(1)')
                return True
            all_node_ele = self.driver.ele_list(child_node_ele)
            tmp_set = []
            for i in range(len(all_node_ele)):
                this_node_ = child_node_ele + ':nth-of-type({})'.format(i + 1)
                self_node_ = this_node_ + '>div:nth-of-type(1)'.format(i + 1)
                self_node_expand = self_node_ + '>span'
                self_node_info = self_node_ + '>*:last-child'  # >div 适配用户部门选择
                name = self.driver.ele_get_val(self_node_info)
                # print(name)
                print(self_node_expand)
                expanded_val = self.driver.ele_get_val(self_node_expand, 'class', chk_visit=False)
                if 'expand-icon' in expanded_val and 'leaf' not in expanded_val:
                    tmp_set.append(this_node_)
                if name == need_dep:
                    self.driver.ele_click(self_node_info)
                    return self_node_info
            for j in tmp_set:
                new_expand_el = j + '>div:nth-of-type(1)>span'
                expanded_val_ = self.driver.ele_get_val(new_expand_el, 'class', chk_visit=False)
                if 'expand-icon' in expanded_val_ and 'leaf' not in expanded_val_ and 'expanded' not in expanded_val_:
                    self.driver.ele_click(new_expand_el)
                    time.sleep(0.5)
                return_val = tree_loop(j)
                if return_val:
                    return return_val

        return tree_loop(root_ee=root_e)

    def wid_tree_power_assign(self, need_dep, root_e=None):
        """
        左侧部门树结构 视频源左侧部门选择
        :param root_e:  # css=.rz-tree
        :param need_dep:
        :return:
        """
        if not root_e:
            root_e = "css=.assign-authority-depTree .rz-tree"
        all_root_ele = self.driver.ele_list(root_e + '>.rz-tree-node')
        new_ele_list = [x for x in all_root_ele if
                        'is-hidden' not in self.driver.ele_get_val(x, 'class', chk_visit=False)]
        # print(len(new_ele_list))
        tmp_set = []
        for i in range(len(new_ele_list)):
            root_node = root_e + '>div:nth-of-type({})'.format(i + 1)
            root_node_1 = root_node + '>div:nth-of-type(1)'
            expand_ele = root_node_1 + '>span'
            label_ele = root_node_1 + '>label'
            grain_ele = root_node_1 + '>div'
            name_ele = grain_ele + '>span:nth-of-type(1)'
            num_ele = grain_ele + '>span:nth-of-type(2)'
            now_name = self.driver.ele_get_val(name_ele)
            # print(now_name)
            if need_dep != now_name:
                tmp_val = self.driver.ele_get_val(expand_ele, attr_name='class', chk_visit=False)
                if 'expand-icon' in tmp_val and 'leaf' not in tmp_val and 'is-hidden' not in tmp_val:
                    tmp_set.append(root_node)
            else:
                print("=" * 80)
                if 'is-checked' not in self.driver.ele_get_val(label_ele, 'class', chk_visit=False):
                    self.driver.ele_click(label_ele)
                return label_ele, name_ele, num_ele,
        for j in tmp_set:
            expand_el = j + '>div:nth-of-type(1)>span'
            if 'expanded' not in self.driver.ele_get_val(expand_el, 'class', chk_visit=False):
                self.driver.ele_click(expand_el)
                time.sleep(0.5)
            return_val = self.wid_tree_power_assign(need_dep, j + '>div:nth-of-type(2)')
            if return_val:
                return return_val

    def wid_dep_tree2(self, need_dep=None, root_e=None):
        """
        左侧部门树结构 用户模块
        :param root_e:  # css=.rz-tree
        :param need_dep:
        :return:        #FLAG
        """
        root_e = root_e or "css=.rz-tree"
        all_root_ele = self.driver.ele_list(root_e + '>.rz-tree-node')
        # print(len(all_root_ele))
        tmp_set = []
        for i in range(len(all_root_ele)):
            root_node = root_e + '>div:nth-of-type({})'.format(i + 1)
            root_node_1 = root_node + '>div:nth-of-type(1)'
            #
            expand_ele = root_node_1 + '>span'
            grain_ele = root_node_1 + '>div'
            #
            name_ele = grain_ele + '>div:nth-of-type(2)'
            num_ele = grain_ele + '>div:nth-of-type(3)'
            more_ele = grain_ele + '>div:last-child>span'
            now_name = self.driver.ele_get_val(grain_ele + '>div:nth-of-type(2)')
            # print(now_name)
            if need_dep != now_name:
                tmp_val = self.driver.ele_get_val(expand_ele, attr_name='class', chk_visit=False)
                if 'expand-icon' in tmp_val and 'leaf' not in tmp_val:
                    tmp_set.append(root_node)
            else:
                print("=" * 80)
                self.driver.ele_click(name_ele)
                return name_ele, num_ele, more_ele
        for j in tmp_set:
            node_expand_ele = j + '>div:nth-of-type(1)>span'
            if 'expanded' not in self.driver.ele_get_val(node_expand_ele, 'class', chk_visit=False):
                self.driver.ele_click(node_expand_ele)
            return_val = self.wid_dep_tree2(need_dep, j + '>div:nth-of-type(2)')
            if return_val:
                return return_val

    def wid_dep_tree_win(self, root_e, need_dep=None):
        """
        在弹出框中的 部门树结构
        :param root_e:
        :param need_dep:
        :return:
        """
        all_root_ele = self.driver.ele_list(root_e + '>.rz-tree-node')
        # print(len(all_root_ele))
        tmp_set = []
        tmp2_set = []
        for i in range(len(all_root_ele)):
            root_node = root_e + '>div:nth-of-type({})'.format(i + 1)
            root_node_1 = root_node + '>div:nth-of-type(1)'
            expand_ele = root_node_1 + '>span'
            name_ele = root_node_1 + '>span:nth-of-type(2)'
            now_name = self.driver.ele_get_val(name_ele)
            # print(now_name)
            if need_dep != now_name:
                tmp_val = self.driver.ele_get_val(expand_ele, attr_name='class', chk_visit=False)
                if 'expand-icon' in tmp_val and 'expanded' not in tmp_val and 'leaf' not in tmp_val:
                    tmp_set.append(root_node)
                elif 'expand-icon' in tmp_val and 'expanded' in tmp_val and 'leaf' not in tmp_val:
                    tmp2_set.append(root_node)
            else:
                print("=" * 80)
                return name_ele
        for j in tmp_set:
            self.driver.ele_click(j + '>div:nth-of-type(1)>span')
            time.sleep(0.5)
            return_val = self.wid_dep_tree_win(self.driver, j + '>div:nth-of-type(2)')
            if return_val:
                return return_val
        for j in tmp2_set:
            return_val = self.wid_dep_tree_win(self.driver, j + '>div:nth-of-type(2)')
            if return_val:
                return return_val

    def wid_slt_date(self, start_time=None, end_time=None, module="", tst_flag=False):
        """
        日期控件 时间输入
        :param start_time:
        :param end_time:
        :param tst_flag:
        :param num: 第几个控件
        :return:
        """
        if module == "silence":
            self.driver.click_xpath(self.el.TaskEle.time_widget_input)
            self.wid_chk_loading()
            self.driver.input_xpath(self.el.TaskEle.start_time_day, start_time.split(" ")[0])
            self.driver.input_xpath(self.el.TaskEle.start_time, start_time.split(" ")[1])
            self.driver.input_xpath(self.el.TaskEle.end_time_day, end_time.split(" ")[0])
            self.driver.input_xpath(self.el.TaskEle.end_time, end_time.split(" ")[1])
            self.driver.click_xpath(self.el.TaskEle.time_ensure)
        elif module == "region_time":
            self.wid_chk_loading()
            self.driver.input_xpath(self.el.TaskEle.start_time_day, start_time.split(" ")[0])
            self.driver.input_xpath(self.el.TaskEle.start_time, start_time.split(" ")[1])
            self.driver.input_xpath(self.el.TaskEle.end_time_day, end_time.split(" ")[0])
            self.driver.input_xpath(self.el.TaskEle.end_time, end_time.split(" ")[1])
            self.driver.click_xpath(self.el.TaskEle.time_ensure)
        elif module == "tactics_time":
            (start_time or end_time) and self.driver.ele_click(self.el.DateEle.tactics_date_ele)
            start_time and self.driver.ele_input(self.el.DateEle.date_start_ele, start_time)
            end_time and self.driver.ele_input(self.el.DateEle.date_end_ele, end_time)
            (start_time or end_time) and self.driver.ele_click(self.el.DateEle.tactics_date_confirm)

        else:
            if start_time:
                self.driver.ele_click(self.el.DateEle.date_ele)
                self.driver.ele_input(self.el.DateEle.date_start_ele, start_time, cln=3, enter=True)
            if end_time:
                self.driver.ele_click(self.el.DateEle.date_ele)
                self.driver.ele_input(self.el.DateEle.date_end_ele, end_time, cln=3, enter=True)

    def wid_slt_time(self, start_time=None, end_time=None, module=""):
        """
        选择时间
        :param start_time:
        :param end_time:
        :param module:
        :return:
        """
        self.driver.ele_input(self.el.TacticsCameraEle.start_time, start_time, enter=True)
        self.driver.ele_input(self.el.TacticsCameraEle.end_time, end_time, enter=True)

    def wid_slt_camera(self, camera_lst=None, trig_wid=None, click_confirm=True):
        """
        选择视频源
        :param camera_lst:  视频源名字 支持一个或多个
        :param trig_wid:  触发此控件的元素
        :return:
        """
        camera_lst = CF.convert_to_array(camera_lst)
        if not camera_lst:
            return
        if trig_wid:
            self.driver.ele_click(trig_wid)
        else:
            self.driver.ele_click(self.el.CameraEle.camera_ele)
        self.driver.ele_click(self.el.CameraEle.camera_page_cam_tree)
        trig_ele = self.driver.ele_exist(self.el.CameraEle.camera_slt_cate_div_ele) or self.driver.ele_exist(
            self.el.CameraEle.camera_slt_cate_ele)
        self.wid_drop_down("视频源", trig_ele)
        try_ele = self.driver.ele_exist(self.el.CameraEle.camera_slt_cate_div_txt) or self.driver.ele_exist(
            self.el.CameraEle.camera_slt_cate_txt)
        for camera_ in camera_lst:
            self.driver.ele_input(try_ele, input_value=camera_, enter=True)
            self.driver.chk_loading()
            check_box_el = self.el.CameraEle.camera_slt_cate_search_check_box
            if 'is-check' not in self.driver.ele_get_val(check_box_el, 'class', chk_visit=False):
                self.driver.ele_click(check_box_el)
        self.driver.ele_move(self.el.CameraEle.camera_slt_cate_txt)
        tyr_ele = self.driver.ele_exist(self.el.CameraEle.camera_slt_cate_txt_clear)
        self.driver.ele_click(tyr_ele) if tyr_ele else None
        if click_confirm:
            self.driver.ele_click(self.el.CameraEle.camera_confirm_btn)

    def wid_alarm_msg(self, status="close"):
        """
        页面右部的告警推送, 调用此方法,默认关闭
        :param status:
        :return:
        """
        MainPage.into_menu(self.driver, "消息提醒")
        alarm_div = "css=.aside-alarm-header-item.aside-alarm-header-switch"
        alarm_btn = "{} span".format(alarm_div)
        alarm_status_ele = "{} div".format(alarm_div)
        alarm_status = self.driver.ele_get_val(alarm_status_ele, 'class')
        chk_var = "is-checked"
        if (chk_var in alarm_status and status == "close") or (chk_var not in alarm_status and status == "open"):
            time.sleep(0.5)
            self.driver.ele_click(alarm_btn)
        MainPage.into_menu(self.driver, "消息提醒")
        return True

    def wid_page(self, action='', tbl_ele=None):
        """
        页码处理, 未适配完成, # TODO csf 待完善及适配
        :param action:
        :param tbl_ele:
        :return:
        """
        # 日志统计 css=.user-operation-content .rz-pagination
        # 日志查询 css=.log-query-content .rz-pagination
        # 用户 css=.user-table .rz-pagination

        page_widget = "{}.rz-pagination".format(tbl_ele + ' ' if tbl_ele else '')
        prev_btn = "{}>button:first-of-type".format(page_widget)
        page_no_wid_ = "{}>ul".format(page_widget)
        next_btn = "{}>button:last-of-type".format(page_widget)
        skip_ele = "{} input".format(page_widget)
        if action == "prev":
            self.driver.ele_click(prev_btn)
        elif action == "next":
            self.driver.ele_click(next_btn)

    def wid_upload(self, img_path, ele="css=input[type='file']"):
        """
        图片上传，适用于当前页面只有一个上传入口 ，多个时不可以(如1:1)
        :param img_path:
        :param ele:
        :return:
        """
        self.driver.ele_input(ele, img_path, cln=-1)

    def wid_get_alert_label(self, wait_miss=False, return_msg=False):
        """
        获取 成功/失败的弹出标签，如新建用户成功 etc
        :param wait_miss:
        :param return_msg:是否返回提示信息
        :return:
        """
        time.sleep(0.3)
        alert_ele = "css=.rz-message"
        # alert_el = self.driver.ele_exist(alert_ele, timeout=3)
        # alert_el = self.driver.ele_get_val(alert_ele, attr_name='class', all_flag=True, timeout=3)
        alert_el = CF.try_catch(self.driver.ele_get_val, judge=True, retry_time=1, ele=alert_ele, attr_name='class',
                                all_flag=True, timeout=3)
        if not alert_el:
            self.log.error("未捕获任何提示信息")
            return ""
        msg, msg_status = alert_el  # self.driver.ele_get_val(alert_el, attr_name='class', all_flag=True)
        if wait_miss:
            self.driver.ele_exist(alert_ele, miss=True)
        if 'error' in msg_status:
            self.log.error("异常信息:{}".format(msg))
            return "" if not return_msg else msg
        else:
            self.log.warning("正常信息:{}".format(msg))
            return msg

    def wid_chk_loading(self, loading_to=10, loading_el=None):
        """
        检测 加载圈, 多用于有表格或页面数据加载
        :param loading_to: 加载超时 默认5s
        :return:
        """
        return self.driver.chk_loading(loading_to=loading_to, loading_el=loading_el)

    def wid_drop_down(self, val, trig_wid=None, exact=False, judge=False):
        """
        针对SC的下拉框进行点击操作
        :param val: 下拉框值
        :param trig_wid: 触发此控件的元素
        :param exact: 为true时val必须相等，为false时包含val即可
        :param judge: 判定下拉框是否有值，默认False 无值直接 触发异常
        :return:
        """
        if trig_wid:
            self.driver.ele_click(trig_wid, wait_time=2, load=True)
        wid_div = "css=*[style*='position'] li"  # "css=body>div:last-child li"
        wid_div_common = 'css=div[x-placement="bottom-start"] li'  # "css=body>div:last-child li"
        # wid_ul = "css=body>ul>li"
        wid_ = self.driver.ele_exist(wid_div_common)
        if not wid_:
            wid_ = self.driver.ele_exist(wid_div)
            wid_div_common = wid_div
        if not wid_:
            error_msg = "未到达下拉框页面 或者目前此下拉框还未适配，联系维护人员适配此控件"
            self.log.error(error_msg)
            if judge:
                return -1
            else:
                raise Exception(error_msg)
        drop_down_lst = self.driver.ele_list(wid_div_common)
        for ele_ in drop_down_lst:
            now_option_value = self.driver.ele_get_val(ele_, chk_visit=False)
            print(now_option_value, val)
            if (isinstance(val, bool) and val) or (
                    (exact and val == now_option_value) or (not exact and val in now_option_value)):
                self.driver.ele_click(ele_, move=True, wait_time=1)
                return True
        else:
            return False

    def wid_draw_circle(self, ref_ele):
        """
        绘制 框,目前只针对长框/方框
        :param ref_ele: 参考元素位置,
        :return:
        """
        webdriver.ActionChains(self.driver.driver).move_to_element_with_offset \
            (ref_ele, random.randint(20, 120), random.randint(50, 80)).click_and_hold() \
            .move_to_element_with_offset(ref_ele, random.randint(200, 300),
                                         random.randint(100, 200)).release().perform()

    def wid_power_assign(self, user_list=None, dep_list=None):
        dep_list = CF.convert_to_array(dep_list)
        user_list = CF.convert_to_array(user_list)
        if dep_list or user_list:
            user_ele = 'css=.user-card-ul>li'
            confirm_ele = 'css=body>div:last-child .rz-button--primary'
            self.driver.ele_click('css=.add-user-btn')
            self.wid_chk_loading()
            for dep_ in dep_list:
                self.driver.ele_input('css=input[placeholder="请输入部门名称"]', dep_, enter=True)
                assert self.wid_tree_power_assign(dep_), "未发现部门[{}]".format(dep_)
            # if user_list and int(re.sub('\D', '', self.driver.ele_get_val('css=.user-num'))) > 50:
            #     self.driver.scroll_page(user_ele, 'end')
            for user_ in user_list:
                self.driver.ele_input('css=input[placeholder="请输入姓名"]', user_, enter=True)
                now_all_user = self.driver.ele_list(user_ele)
                for li_num in range(len(now_all_user)):
                    name_ele = "{}:nth-of-type({}) span:last-child".format(user_ele, li_num + 1)
                    if user_ == self.driver.ele_get_val(name_ele):
                        status_ele = '{}:nth-of-type({}) .user-card-match'.format(user_ele, li_num + 1)
                        status_user = self.driver.ele_get_val(status_ele, 'class')
                        if 'select' in status_user or 'disabled' in status_user:
                            self.log.warning('此用户[{}]状态不可点击'.format(user_))
                        else:
                            self.driver.ele_click(status_ele)
                            break
            self.driver.ele_click(confirm_ele)

    def wid_task_tip(self, return_msg=False, wait_miss=False):
        """
        产生任务后,右上角处,任务中心的提示
        :param return_msg:
        :param wait_miss:
        :return:
        """
        time_out = 20
        ele_ = 'css=.rz-popper.global-task-tips'
        ele_ = self.driver.ele_exist(ele_)
        if not ele_:
            return False
        msg = self.driver.ele_get_val(ele_)
        if wait_miss:
            t_start = time.time()
            hidden_val = self.driver.ele_get_val(ele_, attr_name='aria-hidden')
            while hidden_val and 'true' not in hidden_val and time.time() - t_start < time_out:
                msg = self.driver.ele_get_val(ele_) or msg
                if '完成' in msg or '失败' in msg or '成功' in msg:
                    break
                time.sleep(0.3)
        if not msg or '完成' not in msg or '失败' in msg:
            self.log.warning("异常信息:{}".format(msg))
            return False if not return_msg else msg
        else:
            self.log.warning("正常信息:{}".format(msg))
            return msg

    def wid_role_power_tree(self, root_e=None, chg_right_dict=None):
        """
        角色 权限 表,在新建/编辑/详情时可见
        :param root_e: 默认不需要传输
        :param chg_right_dict: 通过传输 True或False 的字典嵌套来修改 模块权限; ={"卡口": {"使用": True},"1:1验证":  {"使用": True},})
        :return:   {'操作导航': {'使用': '不可编辑已勾选'}, '数据汇智': {'使用': '可编辑未勾选'},
        """
        power_dict = {}
        judge_ele = 'css=.user-details .rz-dialog__title'
        detail_flag = "详情" in self.driver.ele_get_val(judge_ele)
        if not root_e:
            root_e = "css=.rz-tree"
        all_root_ele = self.driver.ele_list(root_e + '>.rz-tree-node')
        dep_len = len(all_root_ele)
        # print("====={}".format(dep_len))
        for i in range(dep_len):
            main_ele = "{}>.rz-tree-node:nth-of-type({})".format(root_e, i + 1)
            sub_ele = "{}>div".format(main_ele)
            sub2_ele = "{}>div:last-child".format(main_ele)
            expand_ele = "{}:first-child>span".format(sub_ele)
            expand_status = self.driver.ele_get_val(expand_ele, attr_name='class', chk_visit=False)
            if 'leaf' not in expand_status:
                if 'expanded' not in expand_status:
                    self.driver.ele_click(expand_ele)
                    time.sleep(1)
                node_tree_ele = "{}>div".format(sub2_ele)
                for num_ in range(len(self.driver.ele_list(node_tree_ele))):
                    mod_tree = "{}:nth-of-type({}) .module-tree".format(node_tree_ele, num_ + 1)
                    power_dict = self.__print(mod_tree, power_dict=power_dict, chg_dict=chg_right_dict,
                                              detail_flag=detail_flag)
            else:
                mod_tree = '{}:first-child>.module-tree'.format(sub_ele)
                power_dict = self.__print(mod_tree, power_dict=power_dict, chg_dict=chg_right_dict,
                                          detail_flag=detail_flag)
            if not chg_right_dict:
                break
        print(power_dict)

    def __print(self, mod_tree, power_dict, chg_dict=None, detail_flag=False):
        mod_name_ele = "{}>.module-name".format(mod_tree)
        mode_name = self.driver.ele_get_val(mod_name_ele)
        d_lst = {}
        if detail_flag:
            mod_types_ele = "{}>.module-types>div".format(mod_tree)
            for j in range(len(self.driver.ele_list(mod_types_ele))):
                now_option_ele = '{}:nth-of-type({})'.format(mod_types_ele, j + 1)
                now_option_val = self.driver.ele_get_val(now_option_ele)
                now_option_class = self.driver.ele_get_val(now_option_ele + '>span', attr_name='class')
                d_lst[now_option_val] = 'icon-Check' in now_option_class
            power_dict[mode_name] = d_lst
        else:
            tmp_dict = {}
            mod_types_ele = "{}>.module-types>label".format(mod_tree)
            # print('{}'.format(self.driver.ele_get_val(mod_name_ele)), end='\t')
            # print(mode_name)
            if chg_dict and mode_name in chg_dict:
                tmp_dict = chg_dict[mode_name]
            for j in range(len(self.driver.ele_list(mod_types_ele))):
                chk_box = '{}:nth-of-type({})>span:first-child'.format(mod_types_ele, j + 1)
                v = self.driver.ele_get_val(chk_box, attr_name='class')
                vv = ''
                vv += '不可编辑' if 'disable' in v else '可编辑'
                vv += '已勾选' if 'checked' in v else '未勾选'
                k = self.driver.ele_get_val('{}:nth-of-type({})>span:last-child'.format(mod_types_ele, j + 1))
                # print('{}:{}'.format(k, vv), end='\t')
                d_lst[k] = vv
                if chg_dict and mode_name in chg_dict and k in chg_dict[mode_name]:
                    if (tmp_dict[k] and 'checked' not in v) or (not tmp_dict[k] and 'checked' in v):
                        self.driver.ele_click(chk_box)
                        if mode_name == '数据汇智' or mode_name == "地图中心":
                            tip_btn = 'css=.rz-message-box__btns .rz-button--primary'
                            if self.driver.ele_exist(tip_btn):
                                self.driver.ele_click(tip_btn)
                        del chg_dict[mode_name][k]
            power_dict[mode_name] = d_lst
        # print()
        return power_dict

    def wid_chk_page(self, expect_page):
        """
        判定当前页是否是expect_page, 但限于每个页面控件布局都不一样,暂停,看后续是否可以使用url判定  #TODO csf
        :param expect_page:
        :return:
        """
        pass

    def wid_return_page(self):
        self.driver.ele_click(GeneralWidgetEle.return_btn)
        self.wid_chk_loading()

    def wid_pop_win(self, act='confirm'):
        """
        弹出确认框， 适配部分
        :param act:     confirm  cancel close
        :return:
        """
        if act == 'confirm':
            self.driver.ele_click(self.el.pop_win_confirm_btn)
        elif act == 'cancel':
            self.driver.ele_click(self.el.pop_win_cancel_btn)
        elif act == 'close':
            self.driver.ele_click(self.el.pop_win_close_btn)
        else:
            self.log.error("传参[{}]错误".format(act))

    def scroll_page_act(self, target_widget=None, load_cnt=1, **kwargs):  # x=143, y=180, page_num=150):
        x = 143  # 置信检索页的抓拍加载
        y = 180
        page_num = 150
        if kwargs.get('int_search'):  # 融合检索结果页的加载
            x = 273  # mx 2020.8.21 修改，原：270
            page_num = 40
        if kwargs.get('trace'):  # 轨迹页 抓拍图的加载
            x = -18
        x = kwargs.get('x') or x  # 自定义 的一张图片的宽度 和页码
        page_num = (kwargs.get('page_num') or page_num) * load_cnt
        target_widget = target_widget or 'css=.list>div'
        if not self.driver.ele_exist(target_widget, timeout=3):
            self.log.warning("无检索结果 无图片")
            return False  # 无检索结果 无图片
            # raise Exception("未适配此种图片滚动， 需优化")
        target_lst_widget = self.driver.ele_list(target_widget)
        if len(target_lst_widget) < page_num and not kwargs.get('trace'):  # 采取每页 150个
            self.log.warning("小于加载数量{}, Total {}".format(page_num, len(target_lst_widget)))
            return False
        target_ele = target_lst_widget[page_num - 1 if not kwargs.get('trace') else 0]
        webdriver.ActionChains(self.driver.driver).move_to_element_with_offset(target_ele, x, y).click().send_keys(
            Keys.END).perform()
        return True

    def scroll_loading_all(self, target_widget=None, **kwargs):
        target_widget = target_widget or 'css=.loading'
        cnt = 13
        while cnt:
            judge_value = self.scroll_page_act(load_cnt=14 - cnt, **kwargs)
            cnt -= 1
            if judge_value:
                sleep_cnt = 0
                # time.sleep(0.4)
                print('=' * 30)
                for _ in range(5):
                    time.sleep(0.6)
                    class_val = self.driver.ele_get_val(target_widget, attr_name='class')
                    if class_val and 'listLoading' in class_val:
                        sleep_cnt += 1
                    else:
                        break  # 点击后 等待加载完成，1：未加载状态 2：加载完成状态
            else:
                break
        time.sleep(1)
        return True

    def export_alarm(self, num="1", module="布控", sleep=2):
        self.wid_chk_loading()
        if module == "布控":
            self.driver.ele_click(self.el.TaskEle.alarm_export)
        elif module == "告警中心":
            self.driver.ele_click(self.el.TaskEle.alarm_center_export)
        elif module == "告警中心_历史告警":
            self.driver.ele_click(self.el.TaskEle.alarm_center_history_export)
        elif module == "告警中心_历史告警_视频源详情页":
            self.driver.ele_click(self.el.TaskEle.alarm_center_history_all_video_export)
        elif module == "告警中心_历史告警_告警目标详情页":
            self.driver.ele_click(self.el.TaskEle.alarm_center_target_alarm_export)
        elif module == "解析管理_解析结果":
            self.driver.ele_click(self.el.TaskEle.ananlysis_alarm_export)
        self.wid_chk_loading()
        self.driver.ele_input(self.el.TaskEle.alarm_export_num_input, num)
        self.driver.ele_click(self.el.TaskEle.ensure_alarm_export)
        time.sleep(sleep)
        msg = self.wid_task_tip(wait_miss=True) or self.wid_task_tip(wait_miss=True)
        if not msg:
            self.log.error("导出告警出错")
            return False
        return True

    def move_to_ele_near(self, ele, x, y):
        target_ele = self.driver.ele_get_(ele)
        return webdriver.ActionChains(self.driver.driver).move_to_element_with_offset(target_ele, x, y)

    def wid_draw_rectangle(self, ele, src_x, src_y, width, height, bool_isclick=False):
        """
        画一个长方形
        :param ele: 相对控件位置
        :param src_x: 长方形起点 距 相对控件 横坐标
        :param src_y: 长方形起点 距 相对控件 纵坐标
        :param width: 长方形终点 距 相对控件 横坐标
        :param height: 长方形终点 距 相对控件 纵坐标

        :return:
        """
        target_ele = self.driver.ele_get_(ele)
        src = webdriver.ActionChains(self.driver.driver).move_to_element_with_offset(target_ele, src_x, src_y)
        if bool_isclick:  # mx2020.8.31  画完矩形释放左键后是否点击。
            src.click_and_hold().move_to_element_with_offset(target_ele, width + src_x,
                                                             height + src_y).release().click().perform()
        else:
            src.click_and_hold().move_to_element_with_offset(target_ele, width + src_x,
                                                             height + src_y).release().perform()

    def back_module_index(self):
        self.driver.ele_click(self.el.back_btn, wait_time=3)
        if self.driver.ele_click_or_not(self.el.back_confirm_btn, timeout=1):
            self.driver.ele_click(self.el.back_confirm_btn, load=True)
            # time.sleep(1)

    def draw_line(self, ele, src_x=60, src_y=350, width=850, height=0, slt_direction='down'):
        """
        越线划线
        :param ele:  参照控件
        :param src_x: 线 起点 距离 参照控件的x轴
        :param src_y: 线 起点 距离 参照控件的y轴
        :param width: 线 长度
        :param height: 线 高度
        :param slt_direction:  down, up
        :return:
        """
        # src_x , src_y , width, height  60, 350, 850, 0 默认值 为划横线
        target_ele = self.driver.ele_get_(ele)
        webdriver.ActionChains(self.driver.driver).move_to_element_with_offset(target_ele, src_x,
                                                                               src_y).click().move_to_element_with_offset(
            target_ele, src_x + width, src_y + height).click().perform()
        if slt_direction == 'down':  # 选择下方位
            self.driver.ele_click('css=.arrow-down>i')
        else:  # 选择上方位
            self.driver.ele_click('css=.arrow-up>i')

    # 校验 图片的 放大/缩小/下载/剪切/全屏
    def _return_element(self, ele):
        return self.driver.driver.execute_script("return arguments[0].shadowRoot", ele)

    def verify_dl(self):
        """
        返回最近一个下载，目前仅支持chrome
        :return:
        """
        self.driver.driver.execute_script('window.open("")')
        win_lst = self.driver.driver.window_handles
        self.driver.driver.switch_to_window(win_lst[-1])
        self.driver.driver.get('chrome://downloads')
        first_sd = self._return_element(self.driver.ele_exist('css=downloads-manager'))
        second_sd = self._return_element(first_sd.find_element_by_css_selector("#downloadsList>downloads-item"))
        # self.driver.driver.back()
        name, dl_url = second_sd.find_element_by_css_selector('#details').text.split('\n')[:2]
        self.driver.driver.close()
        self.driver.driver.switch_to_window(win_lst[0])
        return {'name': name, 'dl_url': dl_url}

    def verify_capture_tool(self):
        # self.driver.
        # 放大 缩小测试
        time.sleep(0.5)
        calc_width = lambda x: int(
            re.findall(x + ': (\d{1,5})px;', self.driver.ele_get_val(self.el.CaptureTool.capture_img, 'style'))[0])
        before_wid = calc_width('width')
        self.driver.ele_click(self.el.CaptureTool.t_enlarge)
        time.sleep(0.3)
        after_wid = calc_width('width')
        self.driver.ele_click(self.el.CaptureTool.t_narrow)
        time.sleep(0.3)
        after2_wid = calc_width('width')
        if not (before_wid < after_wid and after2_wid < after_wid):
            self.log.error("图片放大/缩小 测试失败")
            return False
        # 下载测试
        self.driver.ele_click(self.el.CaptureTool.t_dl)
        last_dl = self.verify_dl()
        dl_delta = int((int(time.time() * 1000) - CF.get_num_from_str(last_dl['name'])) / 1000)
        if not last_dl or not (0 <= dl_delta < 20):
            self.log.error("收藏中，导出比中 检查失败")
            return False
        # self.log.warning(last_dl)
        # 剪切测试
        cut_el = self.el.CaptureTool.t_cut
        self.driver.ele_click(cut_el)
        self.wid_draw_rectangle(cut_el, src_x=-640, src_y=-420, width=400, height=200)
        cut_menu = self.driver.ele_list(self.el.CaptureTool.capture_cut_menu)
        if not cut_menu or len(cut_menu) != 5:
            self.log.error("剪切测试 错误")
            return False
        self.driver.ele_click(cut_menu[-1])
        # 放大测试
        self.driver.ele_click(self.el.CaptureTool.t_full)
        now_class = self.driver.ele_get_val(self.el.CaptureTool.capture_img_tool1, 'class')
        if 'full-screen' not in now_class:
            self.log.error("图片全屏 错误")
            return False
        self.driver.ele_click(self.el.CaptureTool.t_full)
        self.driver.ele_click(self.el.CaptureTool.capture_close)
        return True

    def win_draw_close(self, ele=".monitor-area>label", src_x=80, src_y=80, width=600, height=300):
        """
        画一个闭合图(仅支持长方形)
        :param ele: 相对控件位置
        :param src_x: 长方形起点 距 相对控件 横坐标
        :param src_y: 长方形起点 距 相对控件 纵坐标
        :param width: 长方形终点 距 相对控件 横坐标
        :param height: 长方形终点 距 相对控件 纵坐标
        :return:
        """
        target_ele = self.driver.ele_get_(ele)
        src = webdriver.ActionChains(self.driver.driver).move_to_element_with_offset(target_ele, src_x, src_y)
        # src.click_and_hold().move_to_element_with_offset(target_ele, width + src_x, height + src_y).release().perform()
        src.click().move_to_element_with_offset(target_ele, src_x, height + src_y).click(). \
            move_to_element_with_offset(target_ele, width + src_x, height + src_y).click(). \
            move_to_element_with_offset(target_ele, width + src_x, src_y).click(). \
            move_to_element_with_offset(target_ele, src_x, src_y).click().perform()

    def wid_first_use_alert(self):
        alert_msg = self.driver.ele_exist("//span[contains(text(),'知道了!')][contains(text(),'好的')]")
        if alert_msg:
            self.driver.ele_click(alert_msg)