#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from v43.ele_set.page_task import TaskPageEle


class AlarmCenterPageEle(TaskPageEle):
    function_list = "xpath=//div[@class='custom-tabs']/div[{typo}]"  # 功能页，1是全部，2是布控，3是人群
    task_push_list = "xpath=//*[@class='reference-input rz-input rz-input--medium rz-input--suffix']/input"  # 任务告警推送列表
    search_task_push_list = "xpath=//*[@class='rz-input rz-input--medium rz-input--suffix']/input[@placeholder='请输入任务名']"  # 搜索任务
    all_choose = "xpath=//div[@class='popover-content']/label/span[1]"  # 全选
    save = "xpath=//div[@class='popover-action']/button[2]"  # 保存按钮
    close_essage = "xpath=//*[@class='rz-message-box__headerbtn']"  # 任务筛选后关闭通知弹窗
    target_view = "xpath=//*[@class='list-mode']/div"  # 是否按人像显示

    portrait_alarms = "xpath=//*[@class='portrait-alarms']"  # 告警目标抓拍列表数据
    history_list_alarm = "xpath=//*[@class='alarm-card-body']"  # 历史告警中的告警列表
    portrait_card_header = "xpath=//*[@class='portrait-card-header']"  # 告警身份信息
    alarm_card_header = "xpath=//*[@class='alarm-card-header']/div"  # 历史告警中，告警目标的title
    alarm_card_video = "css=div.alarm-card-video"  # 历史告警中，告警目标 video
    history_alarm_not_status = "xpath=//*[@class='alarm-card task-alarms-card']"  # 历史告警告警目标未比中状态
    first_target_view = "xpath=//*[@class='portrait-list']/div[1]/div[2]/div[@class='rz-image portrait-image']"  # 按人像显示首个目标
    history_first_target_view = "xpath=//*[@class='hasFace-wrap']/div[1]/div/div[@class='rz-image portrait-image']"  # 历史告警按人像显示首个目标
    sure_button = "xpath=//*[@class='rz-form filter-bar rz-form--inline']/..//span[text()='确定']" # mx 2020.8.25 原：#sure_button = "xpath=//*[@class='rz-form filter-bar rz-form--inline']/div[7]//button[@class='rz-button rz-button--text rz-button--medium is-primary-text']"
    check_history_alarm = "xpath=//*[@class='rz-button btn-query-history rz-button--text']"  # 查看历史告警
    video_all_alarm = "xpath=//*[@class='noFace-video-wrap']/div[1]/div[1]/div[2]/button"  # 按视频源告警次数排序后点击告警列表中的全部
    #push_setting = "xpath=//*[@class='alarm-center-filter-action-label']"  # 任务推送设置下拉框
    push_setting = "xpath=// *[text() = '推送设置']"  # 任务推送设置下拉框
    push_setting_title = "xpath=//*[@class='rz-tabs__nav is-top']/div[text()='{typo}']"  # 告警推送区域，声音提示
    all_start_or_close = "xpath=//*[@class='popover-content-header']/div[text()='{typo}']".format(
        typo="全部开启")  # 全部开启，全部关闭
    task_input = "xpath=(//*[@class='rz-tabs__content']/div[1]//input[@placeholder='请输入任务名'])[2]"  # 任务搜索框， 1是告警推送区域，2是声音提示

    task_push_set = "css=#pane-first .popover-content div[title='{task_name}']+span+div"  # 告警推送区域任务设置按钮
    video_button = "//*[@class='rz-button rz-button--primary rz-button--medium']//span"  # 告警推送区域设置视频源确定按钮
    video_button_ensure = "xpath=//*[@class='rz-dialog__wrapper video-source-selector']/div/div[3]/div/button[2]"
    first_alarm = "xpath=//*[@class='date-section-content']/div[1]"  # 告警列表首个告警

    history_task_input = "xpath=//*[@class='rz-input rz-input--suffix']//input[@placeholder = '请输入任务名称']"  # 历史告警页输入框
    history_video_button = "xpath=//*[@class='filter-bar-videos rz-input rz-input--medium rz-input--suffix']"  # 历史告警页视频源功能按钮

    history_alarm_sort = "xpath=//*[@class='icon rz-icon--right rz-icon-arrow-down']"  # 历史告警排序下拉按钮
    history_alarm_sort_op = "xpath=//*[@class='rz-dropdown-menu rz-popper dropdown-list-menu']/li[{typo}]"  # 历史告警排序下拉选项，1.按告警时间排序，2.按视频源告警次数排序
    target_details_close = "xpath=/html/body/div[3]/div[1]/div[1]/button"  # 告警中心告警详情关闭
    list_alarm = "xpath=//*[@class='date-section-content']/div"  # 告警列表
    map_first_alarm = "xpath=//*[@class='task-alarms-content']/div/div/div[1]"  # 地图模式告警列表首个告警
    alarm_export_num_input = "xpath=//*[@class='rz-input rz-input--medium end']//input"  # 告警导出数量文本框
    cancel_alarm_export = "xpath=//*[@class='dialog-footer']//button[@class='rz-button rz-button--info']//span[text()='取消']"  # 告警导出取消
    ensure_alarm_export = "xpath=//*[@class='dialog-footer']//button[@class='rz-button rz-button--primary']//span[text()='确定']"  # 告警导出确定
    target_image = "xpath=//div[@class='portrait-list']/div[1]//div[@class='rz-image portrait-image']"  # 按人像显示的最新目标告警
    map_or_list = "xpath=//*[@class='alarm-center-actions']/a[{typo}]"  # 切换列表或地图模式 1 列表 2 地图模式

    silence_set = "//*[@class='set-silent-time']"  # 设置沉默时间
    silence_ensure = "//*[@class='rz-button rz-button--primary']//span[text()='确定']"  # 设置沉默确定按钮
    silence_reason_input = "//*[@class='rz-textarea']//textarea[@placeholder='请输入沉默原因']"  # 沉默原因文本框
    alarm_details_close = "xpath=/html/body/div[2]/div[1]/div[1]/button/i"  # 告警详情关闭

    filter_date_wid = 'css=.rz-form-item__label+div input[placeholder="{}日期"]'
