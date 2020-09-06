#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from v43.pub.pub_base import PublicClass
from common.common_func import shadow
import time
from sc_common.sc_define import ResDefine
from v43.ele_set.page_region_collision import RegionCollisionEle


class RegionCollisionAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = RegionCollisionEle

    def into_region(self):
        self.into_menu(menu_name="视图工具")

    @shadow("区域碰撞-新建碰撞任务")
    def add_region_task(self, case_name, threshold_value, videos1=None, videos2=None, case_remark=""):
        self.driver.ele_click(self.el.add_region_task_button)
        self.driver.ele_input(self.el.case_name_input.format(typo="请输入案件名称"), case_name)
        self.driver.ele_click(self.el.region_time.format(typo="3"))
        self.wid.wid_slt_date(start_time=self.cf.get_delta_time(minutes=-6),
                              end_time=self.cf.get_delta_time(minutes=-1),
                              module="region_time")
        self.driver.ele_click(self.el.video1)
        for camera_ in videos1:
            self.driver.ele_input(self.el.camera_slt_cate_txt, input_value=camera_, enter=True)
            time.sleep(2)
            self.driver.ele_click(self.el.camera_slt_cate_search_check_box)
        self.driver.ele_click(self.el.camera_confirm_btn)
        self.driver.chk_loading()
        # self.driver.ele_click(self.el.region_time.format(typo="5"))
        # self.wid.wid_slt_date(start_time=self.cf.get_delta_time(minutes=-6), end_time=self.cf.get_delta_time(minutes=-1),
        #                       module="region_time")

        self.driver.ele_click(self.el.video2)
        for camera_ in videos2:
            self.driver.ele_input(self.el.camera_slt_cate_txt, input_value=camera_, enter=True)
            time.sleep(2)
            self.driver.ele_click(self.el.camera_slt_cate_search_check_box)
        self.driver.ele_click(self.el.camera_confirm_btn)
        self.driver.chk_loading()
        self.driver.ele_input(self.el.threshold_value_input, threshold_value, cln=1)
        if case_remark:
            self.driver.ele_input(self.el.case_remark, case_remark)
        self.driver.ele_click(self.el.cancel_or_ensure_button.format(typo="2"))
        self.collect_resource(resource_type=ResDefine.key_region_task, resource_value=case_name)
        return True

    @shadow("区域碰撞-过滤搜索区域碰撞任务")
    def search_region_task(self, task_status=None, task_source=None, search_info=None):
        """

        :param task_status:
        :param task_source:
        :param search_info:
        :return:
        """
        if task_status:
            self.driver.ele_click(self.el.task_status_button)
            self.driver.chk_loading()
            if task_status not in ["不限", "排队中", "进行中", "已完成", "失败", "已终止"]:
                self.log.error("请输入正确的状态：不限，排队中，进行中，已完成，失败，已终止")
                return False
            self.wid.wid_drop_down(task_status)

        if task_source:
            self.driver.ele_click(self.el.creator_button)
            self.driver.chk_loading()
            if task_source not in ["不限", "我的任务", "其他人的任务"]:
                self.log.error("请输入正确的创建者：不限，我的任务，其他人的任务")
                return False
            self.wid.wid_drop_down(task_source)
        if search_info:
            self.driver.chk_loading()
            self.driver.ele_input(self.el.task_input, search_info, enter=True)
        return True

    @shadow("区域碰撞-获取相应状态的碰撞任务")
    def get_case_status(self, name, status=None, count=30, time_sleep=3):
        self.search_region_task(task_status="不限", task_source=None, search_info=name)
        if status == "排队中":
            status_el = self.el.case_status1
        elif status == "进行中":
            status_el = self.el.case_status2
        elif status == "已完成":
            status_el = self.el.case_status3.format(typo="已完成")
        else:
            self.log.error("当前传入的状态为：{}，请输入正确的任务状态：".format(status))
            return False
        for j in range(count):
            self.wid.wid_chk_loading()
            time.sleep(time_sleep)
            if self.driver.ele_exist(status_el):
                self.log.info("碰撞任务已变成自己所需要的的任务状态：{}".format(status))
                return True
            else:
                self.driver.chk_loading()
                self.driver.ele_input(self.el.task_input, name, enter=True)
                continue
        else:
            self.log.error("查询次数达到最大次数，仍未获取到{}状态的碰撞任务，请检查环境！".format(status))
            return False

    @shadow("区域碰撞-查看结果，结果过滤")
    def check_region_task(self, videos=False):
        """

        :param videos:
        :return:
        """
        self.driver.ele_click(self.el.check_results_or_delete_button.format(typo='查看结果'))
        if videos:
            self.driver.ele_click(self.el.video_choose)
        return True

    @shadow("区域碰撞-删除碰撞任务")
    def delete_region_task(self, name):
        self.driver.refresh_driver()
        self.wid.wid_chk_loading()
        self.into_menu("区域碰撞")
        self.search_region_task(task_status="不限", task_source=None, search_info=name)
        if self.driver.ele_exist(self.el.check_results_or_delete_button.format(typo='终止')):
            self.driver.ele_click(self.el.check_results_or_delete_button.format(typo='终止'))
            self.driver.ele_click(self.el.stop_case_task.format(typo="终止"))
        time.sleep(1)
        if self.driver.ele_exist(self.el.check_results_or_delete_button.format(typo="删除")):
            self.driver.ele_click(self.el.check_results_or_delete_button.format(typo="删除"))
            self.driver.ele_click(self.el.stop_case_task.format(typo="删除"))
        time.sleep(0.5)
        return True

    @shadow("区域碰撞-查看结果详情，研判，排序，下一组")
    def operation_results(self, judge=False, group=False, sort=False):
        """

        :param judge:
        :param group:
        :param sort:
        :return:
        """
        self.driver.ele_click(self.el.first_result)
        if judge:
            self.driver.ele_click(self.el.judge_button)
            self.driver.ele_click(self.el.judge_button_complete)
        if group:
            self.driver.ele_click(self.el.group.format(typo=group))
        if sort:
            self.driver.ele_click(self.el.sort)
            self.driver.ele_click(self.el.sort_type.format(typo=sort))
        return True
