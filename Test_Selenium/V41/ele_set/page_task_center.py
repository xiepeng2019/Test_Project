#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class TaskCenterPageEle:
    """
      任务中心模块元素集
      """
    task_center = "//*[@class='nav-bar-item active']"  # 任务中心
    task_schedu = "//*[@class='lib-tab active']"  # 任务调度

    my_task = "//*[@class='lib-tab']"  # 我的任务
    analyze_task = "//*[@class='tab']"  # 分析任务
    other_task = "//*[@class='tab active']"  # 其他任务
    download = "//*[@class='rz-button rz-button--text is-primary-text']"  # 其他任务下载
    area_collision = "//*[@class='tab active']"  # 区域碰撞
    task_input = "//*[@class='rz-input rz-input--suffix']/input"
    task_button = "//*[@class='rz-search-input-suffix rz-icon-search']"
    task_type = ""
    task_status = ""
    task_stop = "xpath=//*[@class='rz-button rz-button--text is-primary-text']/span[text()='终止']"  # 终止任务
    task_table = "xpath=//*[@class='rz-table__row']"  # 区域碰撞任务表格
    stop_task_ensure = "xpath=//*[@class='rz-button rz-button--primary rz-button--primary ']"  # 终止任务确定
    module_title = "xpath=//*[@class='tabs']/div[text()='{typo}']"