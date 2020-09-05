#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class RolePageEle:
    """
    角色模块元素集
    """
    # 新增角色
    add_role_button = "xpath=//*[@class='module-top roles-module-top']/button"  # 新建角色按钮
    role_input_name = "xpath=//*[@class='rz-input rz-input--medium']/input"  # 角色名称输入框
    role_all_permissions = "xpath=//*[@class='rz-form-item__content']/label"  # 角色权限全选框
    save_button = "xpath=//div[@class='user-details']//button[@class='rz-button rz-button--primary']"  # 保存角色按钮
    close_add_page = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div[2]/div/div/div[1]/button/i"  # 关闭新增角色页面

    # 删除角色
    delete_role_button = "xpath=//*[@class='table-operations']/span[4]"  # 删除角色按钮
    cancel_delete_role_button = "xpath=//*[@class='dialog-footer']/button[1]"  # 删除角色取消按钮
    ensure_delete_role_button = "xpath=//*[@class='dialog-footer']/button[2]"  # 删除角色确定按钮
    del_tips_msg = 'css=.rz-dialog__body'  # 删除时的提示语
    del_tips_btn = 'css=.rz-dialog__footer button'  # 不能删除时的确定按钮

    # 启用角色
    ban_role = "xpath=//*[@class='table-operations']/span[3]"  # 启用角色按钮
    cancel_ban_role = "xpath=//*[@class='dialog-footer']/button[1]"  # 启用角色取消按钮
    ensure_ban_role = "xpath=//*[@class='dialog-footer']/button[2]"  # 启用角色确定按钮

    # 角色详情
    check_role_details = "xpath=//*[@class='table-operations']/span[1]"  # 查看角色详情按钮
    close_check_role_details = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div[2]/div/div/div[1]/button/i"  # 关闭角色详情按钮
    role_detail_delete_role = "xpath=//*[@class='dialog-footer']/button[1]"  # 查看角色详情后删除该角色按钮
    role_detail_editor_role = "xpath=//*[@class='dialog-footer']/button[2]"  # 查看角色详情后编辑该角色按钮

    # 编辑角色
    editor_role = "xpath=//*[@class='table-operations']/span[2]"  # 编辑角色按钮

    # 搜索角色
    search_role_input = "xpath=//*[@class='rz-input rz-input--suffix']/input"  # 搜索角色输入框
    search_role_button = "xpath=/html/body/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/i"  # 搜索角色按钮
    system_setting = "xpath=//span[text()='系统设置']"  # 系统设置导航栏
    role_management = "xpath=//*li[text()='角色管理'][@class='rz-dropdown-menu__item item']"  # 角色管理
    # 角色表格
    role_tbl_ele = 'css=tbody'
    role_row = '{}>tr'.format(role_tbl_ele)
    role_row_name = '{}td:nth-of-type(1)'  # 名字 前为tr元素
    role_row_creator = '{}td:nth-of-type(2)'  # 创建人 前为tr元素
    role_row_create_time = '{}td:nth-of-type(3)'  # 创建时间 前为tr元素
    role_row_update = '{}td:nth-of-type(4)'  # 更新人 前为tr元素
    role_row_update_time = '{}td:nth-of-type(5)'  # 更新时间 前为tr元素
    role_row_status = '{}td:nth-of-type(6)'  # 状态 前为tr元素
    role_row_detail = '{}td:nth-of-type(7) span:nth-of-type(1)'  # 详情 前为tr元素
    role_row_edit = '{}td:nth-of-type(7) span:nth-of-type(2)'  # 编辑 前为tr元素
    role_row_enable = '{}td:nth-of-type(7) span:nth-of-type(3)'  # 启动/禁用 前为tr元素
    role_row_del = '{}td:nth-of-type(7) span:nth-of-type(4)'  # 删除 前为tr元素

    role_total_num_ele = 'css=.statistics'  # 页面角色总数的元素
    # 筛选
    srh_status_ele = 'css=.state input'
    role_power_slt_all = 'css=.rz-form-item__content .rz-checkbox__input'
    # 查看角色详情
    detail_role_name = 'css=.roleName'
