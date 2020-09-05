#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class MenuPageEle:
    """
    csf 菜单 相关元素
    """
    sub_menu_ele = "xpath=//div[@class='submenu-item'][text()='{}']|# 左边二级子菜单"
    map_menu_ele = "css=.icon-mapC|# 地图中心"
    map_center_ele = "css=.docker-logo|# 地图中心中，SenseCityLogo"
    map_load_finish_ele = "css=.data-title|# 地图中心中判定加载完成元素"
    left_menu_ele = "xpath=//div[@class='nav-menu-title'][text()='{}']|#左侧菜单"
    top_person_menu = "css=.rz-badge.personal-center-badge|# 顶部菜单-用户头像(个人中心/退出)"
    top_sub_menu1 = "css=.system-management-dropdown li|# 顶部菜单-系统设置的二级子菜单"
    top_sub_menu2 = "css=.personal-center-dropdown li|# 顶部菜单-个人中心的二级子菜单"
    top_sub_menu = "xpath=//li[contains(text(), '{}')][contains(@class, 'item')]|# 顶部菜单-二级子菜单(7个)"
    top_sub_menu_video_menu = '//h2[text()="设备智检"]/following-sibling::div/div[contains(text(),"管理")]|#设备智检页跳转视频源按钮'
    top_sub_menu_logout = 'css=.logout|# 注销退出'
    top_system_menu = "css=.icon-system|# 顶部菜单-系统设置"
    top_alarm_menu = "css=.icon-alarm2|# 顶部菜单-告警中心"
    top_task_menu = "css=.icon-task|# 顶部菜单-任务中心"
    top_message_menu = "css=.icon-notice|# 顶部菜单-告警消息"
    view_tool_op = "xpath=//*[@class='content']//img[@alt='{typo}']|#视图工具内二级菜单"
    user_account_text = "xpath=//aside/div[2]/div[4]/div/span|# 用户账号  （text）"


class LoginPageEle:
    """
    登录页
    """
    login_btn = "css=.login-btn>span|#登录页-登录按钮"
    login_user = "css=input[placeholder='请输入用户名']|#登录页-登录用户名"
    login_pwd = "css=input[placeholder='请输入密码']|#登录页-登录密码"
    success_ele = 'css=.icon-biglogo|#首页-登录成功后的Logo图标'
    password_login_text = "css=.rz-button.rz-button--text.type-button.password|#登录页-密码登录label"  # 密码登录 （text）
    # 首次登录 修改密码页

    modify_ele = 'css=.password-tooltip-first|#修改密码页-'
    pwd_ipt = 'css=input[placeholder="请输入8～18位字母数字组成的密码，区分大小写"]|#修改密码页-输入密码'
    re_pwd_ipt = 'css=input[placeholder="请输入密码"]|#修改密码页-确认密码'
    cancel_btn = 'css=.rz-button--info|#修改密码页-修改取消按钮'
    confirm_btn = 'css=.rz-button--primary|#修改密码页-修改确认按钮'
