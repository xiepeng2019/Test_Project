#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class SysSettingEle:
    """
    ckm 系统设置 相关元素
    """

    setting_info = {

    }
    menu_name = "系统设置"

    # 一级左侧元素
    sys_info = "Xpath=//span[@class='iconfont spanIcon icon-systemM']"  # 左侧系统信息
    function_conf = "Xpath=//span[@class='iconfont spanIcon icon-featuresD']"  # 左侧功能配置
    sys_maintain = "Xpath=//span[@class='iconfont spanIcon icon-systemP']"  # 左侧系统维护
    join_back_plat = "Xpath=//span[@class='iconfont spanIcon icon-playP']"  # 左侧接入回放平台管理
    login_ip = "Xpath=//span[@class='iconfont spanIcon icon-loginIP']"  # 左侧登录ip管理

    # 点击系统设置后二级元素定位
    sys_info_r = "Xpath=//h1[@class='title']"  # 右侧系统信息
    sys_name_r = "Xpath=//div[@class='system-information']//form/div[1]/label"  # 右侧系统名称
    sys_name_r_c = "Xpath=//div[@class='system-information']//form/div[1]/div"  # 右侧系统名称对应内容
    version_r = "Xpath=//div[@class='system-information']//form/div[2]/label"  # 右侧版本号
    version_r_c = "Xpath=//div[@class='system-information']//form/div[2]/div"  # 右侧版本号对应内容
    license_r = "Xpath=//div[@class='system-information']//form/div[3]/label"  # 右侧license截止日期
    license_r_c = "Xpath=//div[@class='system-information']//form/div[3]/div"  # 右侧license截止日期对应内容

    # 点击功能配置后二级元素定位
    function_conf_r = "Xpath=//h1[@class='title']"  # 右侧功能配置
    d_c = "Xpath=//div[@class='content-title']/h2"  # 右侧布控
    alarm_num = "Xpath=//form[@class='rz-form task-view']/div[1]/label"  # 右侧告警推送条数
    alarm_num_c = "Xpath=//form[@class='rz-form task-view']/div[1]/div"  # 右侧告警推送条数对应内容
    threshold_floor = "Xpath=//form[@class='rz-form task-view']/div[2]/label"  # 右侧布控任务阈值下限
    threshold_floor_c = "Xpath=//form[@class='rz-form task-view']/div[2]/div"  # 右侧布控任务阈值下限对应值
    edit_r = "Xpath=//div[@class='button-wrap']//span"  # 编辑

    # 功能配置点击编辑之后元素
    all_button = "Xpath=//div[@class='rz-radio-group']/label[1]"  # 全部按钮
    custom_button = "Xpath=//div[@class='rz-radio-group']/label[2]"  # 自定义按钮
    threshold_value = "Xpath=//div[@class='rz-form-item']//input"  # 阈值输入按钮
    cancel_button = "Xpath=//button[@class='rz-button rz-button--info rz-button--large']"  # 取消按钮
    confirm_button = "Xpath=//button[@class='rz-button rz-button--primary rz-button--large']"  # 确认按钮
    custom_value = "Xpath=//div[@class='diy-number']//input"  # 自定义条数

    # 接入/回放平台
    platform_btn = 'xpath=//h2[contains(text(), "{}")]/../following-sibling::button'  # 按钮 两个，主要为gb 和1400
    # 新建平台弹出信息框中的 所有输入型控件
    new_platform_ipt = 'xpath=//span[contains(text(),"{}")]/../following-sibling::div/descendant::input[contains(@placeholder, "{}")]'
    new_platform_confirm_btn = 'xpath=//span[contains(text(),"{}")]/../following-sibling::div/descendant::button/span[text()="{}"]'  # 新建平台最后的确定按钮