#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# __author__ = 'csf'
# 此部分用于放置公共组件 控件元素


class GeneralWidgetEle:
    return_btn = 'xpath=//span[text()="返回"]'
    pop_win_close_btn = "css=body>div[role='dialog'] .rz-message-box__headerbtn"  # 关闭按钮
    pop_win_cancel_btn = "css=body>div[role='dialog'] .rz-button--info"  # 取消按钮
    pop_win_confirm_btn = "css=body>div[role='dialog'] .rz-button--primary"  # 确认按钮

    # 返回按钮
    back_btn = 'css=.back-btn'  # 返回按钮
    back_confirm_btn = 'css=.rz-message-box__wrapper .rz-button--primary'  # 返回时，确认清除按钮
    # input 提示语
    input_tip_el = '//input[contains(@placeholder,"{}")]'

    class DateEle:
        # 日期
        tactics_date_ele = "css=.rz-date-editor--datetimerange:nth-of-type(1)"  # 技战任务时间控件
        tactics_date_confirm = "css=.rz-picker-panel__footer button:nth-of-type(2)"  # 技战法时间控件确认按钮
        date_ele = "css=.rz-date-editor--datetimerange"  # 日期控件
        date_start_ele = "{}>input:nth-of-type(1)".format(date_ele)  # 开始时间
        date_end_ele = "{}>input:nth-of-type(2)".format(date_ele)  # 结束时间
        date_default_btn = "css=.rz-picker-panel__footer button:nth-of-type(1)"  # 恢复默认时间
        date_cancel_btn = "css=.rz-picker-panel__footer button:nth-of-type(2)"  # 取消按钮
        date_confirm_btn = "css=.rz-picker-panel__footer button:nth-of-type(3)"  # 确定按钮

    class CameraEle:
        # 视频源
        camera_ele = "css=.trigger-input"  # 视频源控件
        camera_page_cam_tree = "css=.rz-big-data-tree.root-tree>div>div>label"  # 一级部门全/反选checkbox
        camera_slt_cate_ele = "css=.rz-dropdown-link"  # 分组/视频源 选择处         #1
        camera_slt_cate_div_ele = "css=body>div:last-child .tree-map-test .rz-dropdown-link"  # 分组/视频源 选择处          #2
        camera_slt_cate_group = "css=body>ul:last-child>li:nth-of-type(1)"  # 分组
        camera_slt_cate_camera = "css=body>ul:last-child>li:nth-of-type(2)"  # 视频源
        camera_slt_cate_txt = "css=.main-input-area input:first-of-type"  # 分组/视频源搜索框      # 1
        camera_slt_cate_div_txt = "css=body>div:last-child .main-input-area input"  # 分组/视频源搜索框    # 2
        camera_slt_cate_txt_clear = "css=i.rz-input__icon.rz-icon-circle-close.rz-input__clear"  # 分组/视频源搜索框清除按钮
        camera_slt_cate_txt_search = "css=.rz-search-input-suffix.rz-icon-search"  # 搜索文本后的 搜索按钮
        camera_slt_cate_search_check_box = "css=.rz-big-data-tree-node.is-leaf label"  # 搜索后选取视频源
        camera_cancel_btn = "css=.dialog-footer button:first-child"  # 取消按钮
        camera_confirm_btn = "css=.dialog-footer button:last-child"  # 确定按钮    # 1

    class TaskEle:
        time_widget_input = "//*[@class='rz-date-editor rz-range-editor rz-input__inner rz-date-editor--datetimerange is-suffix']"  # 沉默时间输入栏
        start_time_day = "//*[@class='rz-date-range-picker__editors-wrap']//input[@placeholder='开始日期']"  # 沉默开始日期
        start_time = "//*[@class='rz-date-range-picker__editors-wrap']//input[@placeholder='开始时间']"  # 沉默开始时间
        end_time_day = "//*[@class='rz-date-range-picker__editors-wrap is-right']//input[@placeholder='结束日期']"  # 沉默结束日期
        end_time = "//*[@class='rz-date-range-picker__editors-wrap is-right']//input[@placeholder='结束时间']"  # 沉默结束时间
        time_ensure = "//*[@class='rz-button rz-picker-panel__link-btn rz-button--primary']//span"  # 输入时间后的确定按钮
        alarm_export = "xpath=//*[@class='image-list-wrapper alarm']/div/button"  # 告警列表中告警导出按钮
        alarm_export_num_input = "xpath=//*[@class='rz-input rz-input--medium end']//input"  # 告警导出数量文本框
        cancel_alarm_export = "xpath=//*[@class='dialog-footer']//button[@class='rz-button rz-button--info']//span[text()='取消']"  # 告警导出取消
        ensure_alarm_export = "xpath=//*[@class='dialog-footer']//button[@class='rz-button rz-button--primary']//span[text()='确定']"  # 告警导出确定

        alarm_center_export = "xpath=//*[@class='rz-button btn-export rz-button--text']"  # 告警中心告警导出按钮

        alarm_center_history_export = "xpath=//*[@class='rz-button export rz-button--text is-primary-text']"  # 告警中心历史告警导出按钮
        alarm_center_history_all_video_export = "xpath=//*[@class='rz-button rz-button--text rz-button--small']"  # 按视频源告警次数排序后点击告警列表中的全部后的导出按钮
        alarm_center_target_alarm_export = "xpath=//*[@class='top-bar-right']/button"  # 历史告警目标单个人像的具体告警记录页的导出按钮
        ananlysis_alarm_export = "xpath=//*[@class='export-comparison']"  # 解析管理解析结果导出按钮

    class TacticsCameraEle:
        camera_page_cam_tree = "css=.rz-big-data-tree.root-tree>div>div>label"  # 一级部门全/反选checkbox
        camera_slt_cate_ele = "css=.rz-dropdown-link:last-child"  # 分组/视频源 选择处
        start_time = "xpath=//div[@class='time-picker-range-comp']/div/input[@placeholder='开始时间']"  # 起始时间
        end_time = "xpath=//div[@class='time-picker-range-comp']/div/input[@placeholder='结束时间']"  # 结束时间
        ts_crash_camera_slt_cate_ele = "body>div:last-child .tree-map-test .rz-dropdown-link"

    class CaptureTool:
        t_enlarge = 'css=i.icon-enlarge'  # 放大
        t_narrow = 'css=i.icon-narrow'  # 缩小
        t_dl = 'css=i.icon-download'  # 下载
        t_cut = 'css=i.icon-shear'  # 裁剪
        # t_full = 'css=i.icon-fullScreen'    # 全屏
        t_full = 'css=div.rz-frame-player__control-bar-right>*:last-child'  # 全屏/退出全屏

        capture_img_tool = 'css=div.face-detail-body-right'  # 整个右边抓拍图+ 工具栏
        capture_img_tool1 = '{}>div:first-child'.format(capture_img_tool)  # 整个右边抓拍图+ 工具栏 下第一div，用于判定是否全屏
        capture_img = 'css=div.rz-frame-player__zoom-box-inner'  # 右边抓拍图

        capture_cut_menu = 'css=div.rz-frame-player__cropper-ops>div'  # 剪切后出现菜单
        capture_close = 'xpath=//span[text()="结果详情"]/following-sibling::button'  # 关闭抓拍图