#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from v43.ele_set.page_task import TaskPageEle


class ViedoViewPageEle(TaskPageEle):
    """卡口"""
    one_screen = "xpath=//*[@class='videos-wrapper videos-wrapper common-bg one-screen']"  # 单个屏幕
    one_switch = "xpath=//*[@class='one-switch rz-popover__reference']"  # 检测下拉框
    face_detection_start = "xpath=//*[@class='all-switch-pop']//span[2]"  # 人脸检测开启或关闭
    image_list = "xpath=//*[@class='imageList']"  # 抓拍列表
    new_snap = "xpath=//*[@class='imageList']/div[1]"  # 抓拍列表最新抓拍
    video_operation = "xpath=//*[@class='video-capture-wrapper']//div[@class='videoplayer-wrapper'][1]//button[{typo}]".format(
        typo=2)  # 卡口播放的操作，2缩小，3扩大
    four_split_screen = "css=.four-screen"  # 4分屏按钮
    one_split_screen = "css=.one-screen"  # 1分屏按钮
    all_alarm_button = "xpath=//*[@class='rz-button view-all rz-button--text is-primary-text']"  # 全部告警按钮
    first_alarm = "xpath=//*[@class='alarms alarm-list']/div/div[1]"  # 卡口告警列表首个告警
    all_alarm_list = "xpath=//*[@class='all-alarms allalarm']/div[@class='content']/div/div"  # 点击全部告警后的告警列表
    all_screen_model_button = "xpath=//*[@class='rz-button rz-button--primary']"  # 全屏模式按钮
    four_screen = "xpath=//*[@class='videos-wrapper videos-wrapper common-bg']/div[{typo}]".format(
        typo=1)  # 四分屏，1,2,3,4依次为从左到右的屏幕顺序
    choose_video = "css=.rz-big-data-tree-node.is-leaf span"  # 搜索后选取视频源
    video_playing = "xpath=//*[@class='rz-frame-player']"  # 视频源播放中
    snap_details_close = "xpath=//*[@class='surveillance-wrap']/div[3]//i[@class='rz-dialog__close rz-icon rz-icon-close']"  # 抓拍详情关闭
