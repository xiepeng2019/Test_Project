#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from v43.ele_set.page_task_center import TaskCenterPageEle
from v43.pub.pub_base import PublicClass


class TaskCenterAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = TaskCenterPageEle

    def into_task_center(self):
        """
        进入任务中心
        :return:
        """
        self.driver.click_xpath(self.el.task_center)

    def into_assign_task(self, task_type, child_task=None):
        """
        进入指定的任务
        :param web_driver:
        :param lib_type: 任务类型: 任务调度，我的任务
        :param child_task: 子任务类型: 区域碰撞，分析任务，其他任务
        :return:
        """
        if task_type == '任务调度':
            self.driver.ele_click(self.el.task_schedu)
            if child_task == "区域碰撞":
                self.driver.ele_click(self.el.area_collision)
            elif child_task == "查重":
                pass
            else:
                pass
        else:
            self.driver.ele_click(self.el.my_task)
            if child_task == "分析任务":
                self.driver.ele_click(self.el.area_collision)
            elif child_task == "其他任务":
                pass
        return True


class TaskCenterPage(TaskCenterAction):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)

    def task_schedu(self, name, module_title="区域碰撞"):
        # 进入任务中心-区域碰撞，搜索相关任务
        self.driver.ele_click(self.el.module_title.format(typo=module_title))
        time.sleep(1)
        self.driver.input_xpath(self.el.task_input, name)
        self.driver.click_xpath(self.el.task_button)
        return True

    def my_task(self, name=None, other_task=False, download=False):
        self.driver.click_xpath(self.el.my_task)
        if other_task:
            if download:
                self.driver.click_xpath(self.el.other_task)
                eles = self.driver.ele_list(self.el.download)
                if not eles:
                    return False
                self.driver.click_xpath(eles[-1])
        else:
            self.driver.input_xpath(self.el.task_input, name)
            self.driver.click_xpath(self.el.task_button)
        return True
