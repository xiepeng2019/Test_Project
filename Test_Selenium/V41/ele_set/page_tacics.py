#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = "huangyongchang"

#
# class Common:
#     task_status_list = "css=.rz-input.rz-input--small>input"  # 任务状态下拉框
#     search_type_list = "css=.rz-dropdown-link"  # 案件搜索类型下拉框
#     case_search_input = "css=.main-input-area>.rz-input>input"  # 案件搜索输入框
#     create_task = "css=.top-bar>.rz-button"  # 新建任务
#     # task_name_input = "xpath=//label[text()='案件名称']//../div/div/input"  # 案件名称输入框
#     # time_select = "xpath=//label[text()='时间范围']/../div/div/div"  # 时间选择框
#     # place_select = "xpath=//label[text()='地点']/../div/div/div"  # 地点视频源选择
#     # remark_input = "xpath=//label[text()='备注']/../div/div/input"  # 备注输入框
#     # appear_times_input = "xpath=//label[text()='出现次数阈值(次)']/../div/div/input"   # 出现次数阈值(次) 输入框
#     # select_lib_list = "xpath=//label[text()='选择库']/../div/div/div"        # 选择库
#     # exclude_lib_list = "xpath=//label[text()='排除库']/../div/div/div"       # 排除库
#     # case_num_input = "xpath=//label[text()='案件编号']/../div/div/input"     # 案件编号输入框
#     create_task_input_frame = "xpath=//label[text()='{}']/../div/div/input"          # 新建任务业务输入框
#     create_task_select_frame = "xpath=//label[text()='{}']/../div/div/div"           # 新建任务业务下拉选择框


class TacticsEle:
    level_one_menu = "xpath=//div[contains(text(),'{}')][@class='title']"  # 技战法的一级菜单
    level_second_menu = "xpath=//p[contains(text(),'{}')]/../.."  # 技战法的二级菜单
    task_status_list = "css=.rz-input.rz-input--small>input"  # 任务状态下拉框
    search_type_list = "css=.rz-dropdown-link"  # 案件搜索类型下拉框
    case_search_input = "css=.main-input-area>.rz-input>input"  # 案件搜索输入框
    case_frame_detail = "xpath=//tbody/tr[{}]/td[{}]/div/div"  # 案件栏项： 第几行案件，第几列详情
    go_back = "css=.crumbs-wrapper.flex-middle>button>span"  # 返回

    create_task = "css=.top-bar>.rz-button"  # 新建任务
    create_task_input_frame = "xpath=//label[text()='{}']/../div/div/input"  # 新建任务业务输入框
    create_task_select_frame = "xpath=//label[text()='{}']/../div/div/div"  # 新建任务业务下拉选择框
    start_analyze = "css=.rz-button.rz-button--primary.rz-button--large"  # 开始分析
    time_widget_input = "css=.rz-date-editor--datetimerange:nth-of-type(1)"  # 创建任务时的时间控件
    ts_crash_task_date_widget = "css=.public-box.is-create>div:nth-of-type({}) .rz-date-editor"  # 时空碰撞任务时间控件
    ts_crash_task_video_widget = "css=.public-box.is-create>div:nth-of-type({}) .public-task-comp"  # 时空碰撞任务视频源控件
    ts_crash_info_delete = ".public-box.is-create>div:nth-of-type({}) .rz-icon-delete"  # 时空信息删除
    add_ts_crash_info = "css=.rz-button.add-btn .rz-icon-plus"  # 添加时空信息
    by_file_id_select = "xpath=//label[text()='选择分析人员']/../div/div/div/div/label[1]/span/span"  # 根据档案ID选择
    ID_dropdown_el = 'css=.public-box div.rz-dropdown'  # 身份/档案ID 下拉框
    file_ip_input_fr = "xpath=//input[@placeholder='请输入档案ID']"  # 档案ID输入框
    direct_upload_picture = "xpath=//label[text()='选择分析人员']/../div/div/div/div/label[2]/span/span"  # 直接上传文件

    class VideoSelectEle:
        camera_confirm_btn = "xpath=//span/button/span[text()='确定']"  # 确定按钮
        camera_cancel_btn = "xpath=//span/button/span[text()='取消']"  # 取消按钮
        camera_search_fr = "css=input[placeholder='请输入视频源名称']"  # 视频源搜索框
        group_search_fr = "css=input[placeholder='请输入分组名称']"  # 分组搜索框
        search_type_cate = "css=body>div:last-child .tree-map-test .rz-dropdown-link"  # 分组/视频源 选择处
        select_video_type = "css=body>div:last-child .rz-tree-map__type .rz-input__inner"  # 选择视频源类型
        camera_check_box = "xpath=//span[text()='{}']/../label"  # 搜索视频源后勾选框
        camera_page_cam_tree = "css=body>div:last-child .rz-big-data-tree.root-tree>div>div>label"  # 一级部门全/反选checkbox
        datetime_widget = "css=.public-box>div:nth-of-type({}) .rz-date-editor"  # 时间控件
        datetime_start = "{}>input:nth-of-type(1)"  # 开始时间
        datetime_end = "{}>input:nth-of-type(2)"  # 结束时间
        datetime_confirm_btn = "css=.rz-button.rz-picker-panel__link-btn.rz-button--primary"  # 日期时间确定按钮

    class CaseDetail:
        view_detail = "xpath=//div[contains(text(), '{}')]/../../../td[{}]/div/div/button"
        view_result = "xpath=//div[contains(text(), '{}')]/../../../td[{}]/div/div/button"
        case_name = "css=.layout-contain>div>div>div>span:nth-of-type(1)"  # 任务名称
        case_detail_text = "css=.crumbs>div:nth-of-type(3)>span"  # 任务详情   text
        detail_result_list = "css=.list-content.scroller-wrap>div>div"  # 结果详情 ele列表
        detail_result_card = "xpath=//*[@class='list']/div[1]"  # 任务结果卡片
        result_detail = "xpath=//span[text()='结果详情']"  # 结果详情
        file_detail = "xpath=//span[text()='档案详情']"  # 档案详情
        result_detail_by_file_id = "xpath=//div[text()='{}']/../../div/div/button[1]/span"  # 结果详情   通过档案ID定位
        file_detail_by_file_id = "xpath=//div[text()='{}']/../../div/div/button[2]/span"  # 档案详情   通过档案ID定位

        class ResultDetail:
            result_detail_text = "xpath=//span[text()='结果详情']"  # 结果详情 text
            go_back = "css=.crumbs-wrapper.flex-middle>button>span"  # 返回

        class FileDetail:
            file_detail_text = "xpath=//span[text()='档案详情']"  # 档案详情

    # general_tactic = "css=.main-scene>li:nth-of-type(1)"   # 通用技战法
    # actual_population = "css=.main-scene>li:nth-of-type(2)"  # 实有人口
    # steal_on_room = "css=.main-scene>li:nth-of-type(3)"   # 入室盗窃
    # appeal_manage = "css=.main-scene>li:nth-of-type(4)"   # 上访管控
    # FK_monitor = "css=.main-scene>li:nth-of-type(5)"      # FK监测
    # hit_drugs = "css=.main-scene>li:nth-of-type(6)"       # 涉毒打击
    # GB_key_point = "css=.main-scene>li:nth-of-type(7)"    # GB重点
    # hospital_trouble = "css=.main-scene>li:nth-of-type(8)"  # 医闹肇事
    # mental_patient = "css=.main-scene>li:nth-of-type(9)"    # 精神病人
    # community_manage = "css=.main-scene>li:nth-of-type(10)"  # 社区管控
    #
    # class GeneralTactic(Common):
    #     often_pass = "css=.sub-scene-content>div:nth-of-type(1)"      # 频繁过人
    #     filter_st_file = "css=.sub-scene-content>div:nth-of-type(2)"  # 时空档案过滤
    #     d_hide_n_out = "css=.sub-scene-content>div:nth-of-type(3)"    # 昼伏夜出
    #     t_s_crash = "css=.sub-scene-content>div:nth-of-type(4)"       # 时空碰撞
    #     first_appear = "css=.sub-scene-content>div:nth-of-type(5)"    # 首次出现
    #     continue_appear = "css=.sub-scene-content>div:nth-of-type(6)"    # 连续出现
    #     pre_leave = "css=.sub-scene-content>div:nth-of-type(7)"          # 感知离开
    #     acc_peer_analyze = "css=.sub-scene-content>div:nth-of-type(8)"   # 精准同行分析
    #     fast_peer_analyze = "css=.sub-scene-content>div:nth-of-type(9)"  # 快速同行分析





