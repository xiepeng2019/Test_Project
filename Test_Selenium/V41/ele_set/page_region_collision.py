#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
class RegionCollisionEle:
    task_status_button = "xpath=//*[@class='rz-select selector-status rz-select--medium']"  # 任务状态下拉框
    task_status = "xpath=//*[@class='rz-select-dropdown rz-popper'][1]//span[text()='{typo}']"  # 不限，排队中，进行中，已完成，失败，已终止
    creator_button = "xpath=//*[@class='rz-select selector-creator rz-select--medium']"  # 创建者下拉框
    create_user = "xpath=//*[@class='rz-select-dropdown rz-popper'][2]//span[text()='{typo}']"  # 不限，我的任务，其他人的任务
    task_input = "xpath=//*[@class='rz-input rz-input--suffix']/input"  # 任务输入框
    add_region_task_button = "xpath=//*[@class='rz-button rz-button--primary']/span[text()='新建']"  # 新建区域碰撞按钮
    case_name_input = "xpath=//*[@class='rz-input']/input[@placeholder='{typo}']"  # 区域碰撞 请输入案件名称，请输入案件编号
    region_time = "xpath=//*[@class='rz-form task-content-form']/div[{typo}]"  # 传入数字  4 区域一时间  6区域二时间
    video1 = "xpath=//*[@class='rz-form task-content-form']/div[4]//div[@class='video-source']"  # 首个选择视频源按钮
    video2 = "xpath=//*[@class='rz-form task-content-form']/div[7]//div[@class='video-source']"  # 第二个选择视频源按钮
    threshold_value_input = "xpath=//*[@class='rz-input rz-input--small rz-input--suffix']/input"  # 阈值输入框
    case_remark = "xpath=//*[@class='rz-textarea']/textarea[@placeholder='请输入案件备注']"  # 请输入案件备注文本框
    cancel_or_ensure_button = "xpath=//*[@class='footer-btn']/button[{typo}]"  # 传入1是取消，传入2是确定
    check_results_or_delete_button = "xpath=//*[@class='table-operations']/span[text()='{typo}']"  # 查看结果  删除 编辑 终止
    case_status1 = "xpath=//*[@class='c-primary'][text()='排队中']"  # 碰撞任务状态：  排队中
    case_status2 = "xpath=//*[@class='c-success'][text()='进行中']"  # 碰撞任务状态：  进行中
    case_status3 = "xpath=//*[@class='status-normal'][text()='{typo}']"  # 碰撞任务状态：  已完成 已终止
    stop_case_task = "xpath=//*[@class='rz-button rz-button--primary']/span[text()='{typo}']"  # 终止 删除碰撞任务
    video_choose = "xpath=//*[@class='dialog-reference']"  # 查看结果页，视频源按钮
    image_list = "xpath=//*[@class='list-left']"  # 结果详情左侧页数据
    first_result = "xpath=//*[@class='result-content']/div[1]"  # 首个结果
    judge_button = "xpath=//*[@class='rz-button rz-button--primary rz-button--large']"  # 研判按钮
    judge_button_cancel = "xpath=//*[@class='rz-button rz-button--info rz-button--large']"  # 研判取消
    judge_button_complete = "xpath=//*[@class='rz-button complete-button rz-button--primary rz-button--large']"  # 完成研判
    group = "xpath=//*[@class='group-button']/button[{typo}]"  # 传入数字 1.上一组  2.下一组
    sort = "xpath=//*[@class='order-dropdown rz-dropdown']"  # 排序
    sort_type = "xpath=//*[@class='rz-dropdown-menu rz-popper']/li[{typo}]"  # 传入数字 1.按时间排序，2.按视频源排序
    table_body = "xpath=//*[@class='rz-table__body']"  # 碰撞任务body
    camera_ele = "css=.trigger-input"  # 视频源控件
    camera_page_cam_tree = "css=.rz-big-data-tree.root-tree>div>div>label"  # 一级部门全/反选checkbox
    camera_slt_cate_ele = "css=.rz-dropdown-link"  # 分组/视频源 选择处
    camera_slt_cate_group = "css=body>ul:last-child>li:nth-of-type(1)"  # 分组
    camera_slt_cate_camera = "css=body>ul:last-child>li:nth-of-type(2)"  # 视频源
    camera_slt_cate_txt = "css=.main-input-area input:first-of-type"  # 分组/视频源搜索框
    camera_slt_cate_txt_search = "css=.rz-search-input-suffix.rz-icon-search"  # 搜索文本后的 搜索按钮
    camera_slt_cate_search_check_box = "css=.rz-big-data-tree-node.is-leaf label"  # 搜索后选取视频源
    camera_cancel_btn = "css=.dialog-footer button:first-child"  # 取消按钮
    camera_confirm_btn = "xpath=//*[@class='rz-button rz-button--primary rz-button--medium']"  # 确定按钮