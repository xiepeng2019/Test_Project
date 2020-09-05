#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class PersonalCenterPageEle:
    """
    个人中心模块元素集
    """
    # 全部事项
    # all_title_typo = "xpath=//*[@class='custom-tabs']/div[{}]"  # 1.全部事项 2.我的收藏 3.个人信息
    all_title_typo = "xpath=//*[@class='custom-tabs']/div[contains(text(),'{}')]"  # 1.全部事项 2.我的收藏 3.个人信息
    search_task_input = "xpath=//*[@class='rz-input rz-input--suffix']/input"  # 任务名称搜索框
    search_task_button = "xpath=//*[@class='rz-search-input-suffix rz-icon-search']"  # 任务名称搜索按钮
    task_details = "xpath=//*[@class='table-operations']/span[1]"  # 任务详情
    task_pass = "xpath=//*[@class='table-operations']/span[2]"  # 任务通过
    task_rejected = "xpath=//*[@class='table-operations']/span[3]"  # 任务驳回
    idea_input = "xpath=//*[@class='rz-textarea']/textarea"  # 审批意见文本框
    idea_cancel_button = "xpath=//*[@class='rz-button rz-button--info']"  # 任务通过的取消按钮
    task_status = "css=.rz-table__row>td:nth-of-type(7)>div>span"  # 任务状态
    idea_ensure_button = "xpath=//*[@class='rz-button rz-button--primary']"  # 任务通过的确定按钮
    detail_edit_button = "xpath=//div[@class='task-details-footer']/button/span"  # 任务详细下的编辑按钮
    task_name_input = "xpath=//*[@class='rz-input']/input"  # 任务名称文本框
    accurate_alarm_input = "xpath=//*[@class='slider-wrap']//input"  # 精准告警文本框
    edit_save_submit_button = "xpath=//div[@class='task']/div/button[2]/span"  # 编辑保存并提交按钮
    app_reason_input = "xpath=//div[@class='auditReason-content']/div/div/textarea"  # 申请理由输入框
    edit_ensure_button = "xpath=//div/div/span/button/span[text()='确定']"  # 编辑确定按钮
    source = "xpath=//div[@class='task-filter']/div[1]//input"  # 来源
    status = "xpath=//div[@class='task-filter']/div[2]//input"  # 状态
    filter_task_list = "xpath=//tbody/tr"  # 过滤任务列表
    return_back = "xpath=//span[text()='返回']"  # 返回

    class ApplyTaskDetail:
        base_info = "xpath=//div[@class='basic-info-content']/form/div[{}]/div/span"  # 基本信息列表
        lib_name_text = "xpath=//tbody//div[@class='lib-name']/span"  # 人像库名称

    # 我的收藏
    all_collection = "xpath=//*[@class='rz-radio-group tab-buttons']/label[{}]"  # 各类型检索：人脸检索，行人检索，车辆检索，身份检索， 融合检索
    collection_image = "xpath=//*[@class='rz-s-image__container']"  # 检索收藏结果
    collection_detail = "xpath=//div[@class='favourite-info']//div[2]/span[@class='title']"  # 收藏详情
    collection_search_result = "xpath=//div[@class='list']/div[1]/div"
    result_detail_text = "xpath=//span[@class='rz-dialog__title'][text()='结果详情']"  # 结果详情 （text）
    result_detail_operate_list = "xpath=//div[@class='rz-frame-player__control-bar-right']/div"  # 结果详情下操作列表
    result_detail_close = "xpath=//span[text()='结果详情']/../button/i"  # 结果详情关闭按钮
    # collection_image_info = "css=div.rz-image-card__content"  # 检索收藏结果
    collection_image_info = "css=.content div.content"  # 检索收藏结果 增加车牌号检索的适配
    cancel_collection = "xpath=//*[@class='collect-comparison']"  # 取消收藏
    cancel_button = "xpath=//*[@class='rz-button rz-button--info']"  # 取消收藏的取消按钮
    ensure_button = "xpath=//*[@class='rz-button rz-button--primary rz-button--primary']"  # 取消收藏的确定按钮
    export_image = "xpath=//*[@class='export-comparison']/span"  # 导出比中
    track = "xpath=//*[@class='comparison-trail']/span"  # 查看轨迹
    track_text = "xpath=//div[@class='crumbs']/div[3]/span[1]"  # 查看轨迹 text

    # 个人信息
    user_info = "xpath=//*[@class='rz-form person-info-form']"  # 用户信息
    editor_user = "xpath=//*[@class='rz-button rz-button--text is-primary-text']//span"  # 编辑用户
    user_info_input = "xpath=//*[@class='rz-form rz-form--label-left']/div[{typo}]//input"  # 2 姓名文本框 5 警号文本框 6.手机号文本框
    police_number = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[4]/div/div/div[2]/div/form/div[5]/div/div/input"  # 警号文本框
    phone_number = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[4]/div/div/div[2]/div/form/div[6]/div/div/input"  # 手机号文本框
    cancel_editor_user = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[4]/div/div/div[3]/span/button[1]"  # 取消编辑用户
    ensure_editor_user = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[4]/div/div/div[3]/span/button[2]"  # 确定编辑用户

    change_password = "xpath=//*[@class='person-account-summary']//span"  # 修改密码
    input_old_password = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[3]/div/div/div[2]/div/form/div[1]/div/div[1]/input"  # 输入旧密码
    input_new_password = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[3]/div/div/div[2]/div/form/div[2]/div/div[1]/input"  # 输入新密码
    again_input_new_password = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[3]/div/div/div[2]/div/form/div[3]/div/div[1]/input"  # 再次输入新密码
    cancel_editor_password = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[3]/div/div/div[3]/span/button[1]"  # 取消修改密码
    ensure_editor_password = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[3]/div/div/div[3]/span/button[2]"  # 确定修改密码
    oneself = "xpath=//span[text()='{}']"  # 用户
    user_center = "xpath=//*li[text()='个人中心'][@class='rz-dropdown-menu__item item']"  # 个人中心
    # 　我的收藏　检索部分　====>
    top_menu = '//span[text()="{}"]'  # 取消收藏/导出比中/查看轨迹
    cancel_fav_confirm_btn = '//span[contains(text(),"{}")]'