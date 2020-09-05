#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = "huangyongchang"


class CrowdAnalyzeEle:
    group_list = "css=.group-dropdown"  # 分组列表
    alarm_manage = "xpath=//button/span[text()='告警管理']"  # 告警管理
    task_config = "xpath=//button/span[text()='任务配置']"  # 任务配置
    list_model = "css=.icon.iconfont.icon-listMode"  # 列表模式
    map_model = "css=.icon.iconfont.icon-track1"  # 地图模式
    calc_cpu_statistics = "css=.iconfont.icon-collapse2.icon"  # 算力资源统计
    product_logo = "css=.nav-bar-left>.logo>.icon.iconfont.icon-biglogo"  # 产品logo
    first_alarm_event_info = "css=.alarmEventNotice>div>ul>li:nth-of-type(2)"  # 第一条告警事件通知
    alarm_detail = "xpath=/html/body/div/div/div/span"  # 告警详情
    alarm_detail_next = "css=.rz-button.rz-button--dark.rz-button--large.is-circle>.rz-icon-arrow-right"  # 下一个告警详情
    alarm_detail_front = "css=.rz-button.rz-button--dark.rz-button--large.is-circle"  # 上一个告警详情
    alarm_detail_bigger = "css=.rz-frame-player__control-bar-right>div:nth-of-type(1)"  # 告警详情图片放大
    alarm_detail_smaller = "css=.rz-frame-player__control-bar-right>div:nth-of-type(2)"  # 告警详情图片缩小
    alarm_detail_download = "css=.rz-frame-player__control-bar-right>div:nth-of-type(3)"  # 告警详情图片下载
    alarm_detail_screen_shot = "css=.rz-frame-player__control-bar-right>div:nth-of-type(4)"  # 告警详情图片截图
    alarm_detail_full_screen = "css=.rz-frame-player__control-bar-right>div:nth-of-type(5)"  # 告警详情图片全屏
    alarm_detail_quit_full_screen = "css=.rz-tooltip.iconfont.icon-exit-fullScreen"  # 告警详情图片全屏
    alarm_detail_close = "xpath=/html/body/div/div/div/button"  # 告警详情关闭
    check_line_on_off = "css=.switch>.rz-on-off"  # 检测线段开关
    judge_valid = "css=.judge>div:nth-of-type(1)>div"  # 研判有效
    judge_invalid = "css=.judge>div:nth-of-type(1)>div"  # 研判无效
    remark_input_frame = "css=.rz-textarea__inner"  # 备注输入框
    remark_confirm = "css=.input-content>button"  # 备注确认
    remark_result = "css=.remark-content.ellipsis.rz-tooltip"  # 备注结果
    alarm_point_text = "css=.left>form>div:nth-of-type(1)>.rz-form-item__label"  # 告警点位（text）
    event_type_text = "css=.left>form>div:nth-of-type(2)>.rz-form-item__label"  # 事件类型（text）
    alarm_time_text = "css=.left>form>div:nth-of-type(3)>.rz-form-item__label"  # 告警时间（text）
    event_time_total = "css=.timeTitle"  # 当天XX事件时段统计
    judge_text = "css=.left>div:nth-of-type(3)>h5"  # 研判(text)
    remark_text = "css=.left>div:nth-of-type(5)>h5"  # 备注(text)

    class TaskConfig:
        task_config = "css=.crumbs-item.last-crumbs-item>span"  # 任务配置
        config_status = "css=.has-gutter>tr>th:nth-of-type(3)>div"  # 配置状态
        equip_status_list = "xpath=//label[text()='设备状态']/../div/div/div/input"  # 设备状态下拉框
        config_status_list = "xpath=//label[text()='配置状态']/../div/div/div/input"  # 配置状态下拉框
        alarm_type_list = "xpath=//label[text()='告警类型']/../div/div/div/input"  # 告警类型下拉框
        task_status_list = "xpath=//label[text()='任务状态']/../div/div/div/input"  # 任务状态下拉框
        search_video = "css=.rz-input__inner[placeholder='请输入视频源名称']"  # 视频源名称搜索输入
        video_name = "xpath=//span[@title='{}']"  # 视频源名称
        video_preview = "xpath=//span[@title='{}']/../../../td/div/div/span[1]"  # 指定视频源预览
        task_detail = "xpath=//span[@title='{}']/../../../td/div/div/span[2]"  # 指定视频源任务详情
        config = "xpath=//span[@title='{}']/../../../td/div/div/div/span[1]"  # 指定视频源配置
        pause_reboot = "xpath=//span[@title='{}']/../../../td/div/div/div/span[text()='{}']"  # 指定视频源暂停
        modify_task_status_confirm = "css=.rz-button.rz-button--primary.rz-button--primary"  # 修改任务状态确认建
        terminate = "xpath=//span[@title='{}']/../../../td/div/div/div/span[3]"  # 指定视频源终止
        to_much_event = "css=.view-steps>div[title='过密事件']"  # 过密事件
        cross_line_event = "css=.view-steps>div[title='越线事件']"  # 越线事件
        hover_event = "css=.view-steps>div[title='徘徊事件']"  # 徘徊事件
        invade_event = "css=.view-steps>div[title='入侵事件']"  # 入侵事件
        converse_event = "css=.view-steps>div[title='逆行事件']"  # 逆行事件
        retention_event = "css=.view-steps>div[title='滞留事件']"  # 滞留事件
        event_switch = "css=.rz-on-off__label.rz-on-off__label--right"  # 事件开关转换
        video_play = "css=.icon.iconfont.icon-play"  # 视频播放
        screen_capture = "css=span.crop-text"  # 截图
        draw_direction = "css=.buttonInfo .icon-shear"  # 绘制方向
        box_to_body = "css=.icon.iconfont.icon-frameS"  # 框选人体
        save = "css=.rz-button.rz-button--primary.rz-button--large"  # 保存
        check_region = "xpath=//label[text()='检测区域']"  # 检测区域
        crowd_list_ele = "css=.rz-table__row"  # 人群任务list元素

    class ListModel:
        real_people_total = "css=.sc-crowd__mode-list>div>span:nth-of-type(1)"  # 实时总人数
        today_alarm_total = "css=.sc-crowd__mode-list>div>span:nth-of-type(2)"  # 今日总告警数
        first_alarm_card = "css=.sc-crowd__camera-card.card0>div"  # 第一个人群告警卡片 原:css=.sc-crowd__camera-card.card0>div>img
        first_alarm_card_name = "css=.sc-crowd__camera-card.card0>div>div>div>span"  # 第一个人群告警卡片名
        video_pre_view = "xpath=//span[@class='rz-dialog__title'][text()='视频预览']"  # 视频预览（文字）
        map_point = "xpath=//h5[@class='title'][text()='地图点位']"  # 地图点位(文字)
        alarm_trend = "xpath=//h5[@class='title'][text()='告警趋势 (近7天)']"  # 告警趋势（文字）
        video_play_window = "css=.rz-dialog__wrapper.sc-crowd__camera-detail.hasEvent"  # 视频源播放窗口
        video_play_max_window = "css=i.icon.iconfont.icon-fullScreen"  # 视频源播放最大窗口
        all_full_play = "xpath=//div[1]/div[2][@class='videoplayer-wrapper']"  # 全屏播放
        quit_full_screen = "xpath=//button/span[text()='退出全屏']"  # 退出全屏
        screen_shot = "css=i.icon-shear.icon.iconfont"  # 截图
        pause_play = "css=.icon.iconfont.icon-stop"  # 播放暂停
        start_play = "css=.icon.iconfont.icon-stat"  # 开始播放
        screen_shot_task = "css=.rz-frame-player__cropper-ops>div:nth-of-type(1)"  # 截图中布控
        screen_shot_search = "css=.rz-frame-player__cropper-ops>div:nth-of-type(2)"  # 截图中检索
        screen_shot_download = "css=.rz-frame-player__cropper-ops>div:nth-of-type(3)"  # 截图中下载
        screen_shot_in_store = "css=.rz-frame-player__cropper-ops>div:nth-of-type(4)"  # 截图中入库
        screen_shot_cancel = "css=.rz-frame-player__cropper-ops>div:nth-of-type(5)"  # 截图中取消

    class MapModel:
        calc_cpu_statistics = "xpath=//div/div[text()='算力资源统计']"  # 算力资源统计
        alarm_event_total = "xpath=//div/div[text()='告警事件统计']"  # 告警事件统计

    class AlarmManage:
        event_type = "css=.sc-crowd-alarm-head>div:nth-of-type(2)>div"  # 事件类型
        event_level = "css=.sc-crowd-alarm-head>div:nth-of-type(3)>div"  # 事件等级
        judge_status = "css=.sc-crowd-alarm-head>div:nth-of-type(4)>div"  # 研判状态
        export = "css=.rz-button.export-button.rz-button--text>span"  # 导出
        export_start_num = "css=.rz-input.rz-input--medium.start>input"  # 导出起始编号
        export_end_num = "css=.rz-input.rz-input--medium.end>input"  # 导出终止编号
        export_confirm = "css=.rz-button.rz-button--primary"  # 导出确认按钮
        alarm_manage = "css=.crumbs-item.last-crumbs-item>span"  # 告警管理
        first_alarm_event = "css=.card-list>div:nth-of-type(2)"  # 第一个告警事件
        crowd_alarm_list = "css=div.sc-crowd__alarm-record-card"  # 人群告警列表
        video_select_widget = "css=.rz-big-data-tree__container"  # 视频源选择控件
