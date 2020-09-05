#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class UserPageEle:
    """
    角色模块元素集
    """
    # __first_level_department = "一级部门（可修改名称）"    # 一级部门名称
    # __not_expand_ele = "xpath=//*[@class='name']/../../../span[@class='rz-tree-node__expand-icon rz-icon-caret-right']"  # 部门展开元素
    # __create_same_level_ele = "xpath=//div[@class='leaves']/div[@class='book-mark']/ul[@class='mark-ul']/li[@class='mark-li'][1]"  # 创建同级部门
    # __create_lower_level_ele = "xpath=//div[@class='leaves']/div[@class='book-mark']/ul[@class='mark-ul']/li[@class='mark-li'][2]"  # 创建下级部门
    # __view_department_ele = "xpath=//div[@class='leaves']/div[@class='book-mark']/ul[@class='mark-ul']/li[@class='mark-li'][3]"  # 查看设置
    # __edit_department_ele = "xpath=//div[@class='leaves']/div[@class='book-mark']/ul[@class='mark-ul']/li[@class='mark-li'][4]"  # 编辑设置
    # __delete_department_ele = "xpath=//div[@class='leaves']/div[@class='book-mark']/ul[@class='mark-ul']/li[@class='mark-li'][5]"  # 删除部门
    # __create_input_depart_name_ele = "css=.rz-input__inner[placeholder=请输入部门名称]"   # 创建部门时输入部门名框
    # __edit_input_depart_name_ele = "css=.rz-input__inner[placeholder=请输入部门名称]"  # 编辑部门时输入部门名框
    # __create_cancel_ele = "xpath=//div[3]/span/button[1]"   # 创建部门取消元素
    # __create_confirm_ele = "xpath=//div[3]/span/button[2]"  # 创建部门确认元素
    # __edit_confirm_ele = "css=div.user-tree div.user-details > div > div > div.rz-dialog__footer > span > button.rz-button.rz-button--primary"  # 编辑部门确认按钮
    # __delete_confirm_ele = "xpath=//button[2]/span[text()='删除']"

    # 用户 列表界面
    filter_role_ipt = 'css=.role input'
    filter_status_ipt = 'css=.state input'
    srh_input = 'css=input[placeholder="请输入关键字"]'
    tbl = 'css=.user-table>.table-wrap tbody'
    tbl_tr = '{}>tr'.format(tbl)
    tbl_name = '{}>td:nth-of-type(1)'
    tbl_role = '{}>td:nth-of-type(2)'
    tbl_dep = '{}>td:nth-of-type(3)'
    tbl_phone = '{}>td:nth-of-type(4)'
    tbl_status = '{}>td:nth-of-type(5)'
    tbl_detail = '{}>td:nth-of-type(6) span:nth-of-type(1)'
    tbl_edit = '{}>td:nth-of-type(6) span:nth-of-type(2)'
    tbl_en_dis = '{}>td:nth-of-type(6) span:nth-of-type(3)'
    tbl_more = '{}>td:nth-of-type(6) span:nth-of-type(4) i'

    tbl_rst = 'css=body>div:last-child>span:first-child'
    tbl_del = 'css=body>div:last-child>span:last-child'
    tbl_del_cancel_btn = 'css=.user-footer+div .rz-button--info'
    tbl_del_confirm_btn = 'css=.user-footer+div .rz-button--primary'
    tbl_del_close_btn = 'css=.user-footer+div .rz-icon-close'

    # 用户新建
    new_user_btn = "xpath=//button[@class='rz-button rz-button--primary']/span[text()='新建用户']"  # 新建用户按钮
    new_user_user_name = "xpath=//input[@placeholder='请输入账号'][@class='rz-input__inner']"  # 新建用户的用户名
    new_user_real_name = "xpath=//input[@placeholder='请输入姓名'][@class='rz-input__inner']"  # 新建用户的 姓名
    new_user_dep = "xpath=//input[@placeholder='请选择所属部门'][@class='rz-input__inner']"  # 新建用户的部门

    new_user_NO = "xpath=//div/input[@placeholder='请输入警号'][@class='rz-input__inner']"  # 新建用户的警号
    new_user_phone = "xpath=//div/div/input[@placeholder='请输入手机号码'][@class='rz-input__inner']"  # 新建用户的 Phone
    new_user_save_btn = "xpath=//span[@class='dialog-footer']/button/span[text()='保存']"  # 新建用户的 保存按钮
    # 新建用户 部门选择
    new_user_dep_srh = 'css=.rz-search-input input[placeholder="请输入部门名称"]'  # 新建用户 部门选择 触发框
    new_user_slt_role = "xpath=//span/div/input[@placeholder='请选择角色']"  # 新建用户 角色触发框
    new_user_slt_role_ = "xpath=//span[2]/p[@title='{}']"  # 新建用户 选择角色
    new_user_role_cancel_btn = 'css=.roles-wrap+div>button:first-child'  # 新建用户 选择角色后的取消按钮
    new_user_role_save_btn = 'css=.roles-wrap+div>.is-primary-text'  # 新建用户 时  角色的保存按钮
    new_user_slt_camera_input = "xpath=//span/div/input[@placeholder='请选择视频源'][@class='rz-input__inner']"  # 选择视频源的 触发 框
    new_user_slt_camera_cancel_btn = 'css=.rz-tree+div>button:first-child'  # 选择视频源后，的清空 按钮
    new_user_slt_camera_save_btn = 'css=.rz-tree+div>.is-primary-text'  # 选择视频源后，的保存 按钮
    new_user_slt_lib_input = "xpath=//div/span/div/input[@readonly='readonly'][@placeholder='请选择人像库']"  # 新建用户 库 选择 触发框

    new_user_slt_lib_slt_all_ele = 'css=.all-select .rz-checkbox__inner'
    new_user_slt_lib_slt_static_lib = 'xpath=//div[text()="静态库"]'
    new_user_slt_lib_slt_alert_lib = 'xpath=//div[text()="布控库"]'

    lib_content = 'css=div.libraries-conent'  # 判定是否存在库
    new_user_lst_lib_cancel_ele = 'css=.core+div button:first-child'  # 取消/清空按钮
    new_user_lst_lib_save_ele = 'css=.core+div .is-primary-text'  # 保存按钮

    # 部门
    new_dep_input = 'css=input[placeholder="请输入部门名称"]'  # 新建部门时的 部门名称
    new_dep_confirm_btn = 'css=.leaves+div .rz-button--primary'  # 新建部门时的 确认 按钮
    del_dep_confirm_btn = 'css=.leaves+div+div .rz-button--primary'  # 删除部门时的 确认按钮
    dep_close_btn = 'css=.leaves+div .rz-icon-close'  # 部门详情关闭
    # 用户总数 及已删除用户
    total_user_num_ele = 'css=.all-users'
    del_user_num = 'css=.del-users>span'
    del_user_tbl = 'css=.del-user-table-wrap tbody'
    # 用户详情页
    detail_info_ele = 'css=.rz-form>div>div'  # 列表 12个值
    detail_close_btn = 'css=.user-table .user-details .rz-icon-close'
    # 部门详情页
    dep_info_ele = 'css=.user-form>div>div'

