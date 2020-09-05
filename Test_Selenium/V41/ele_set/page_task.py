#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class TaskPageEle:
    task_main = "//*[@class='icon iconfont icon-crimnalunderSurveillance']"  # 布控任务页面入口
    # 基本信息
    add_task = "//*[@class='rz-button rz-button--primary rz-button--small']"  # 新增任务按钮
    task_name_input = "//*[@class='rz-input']/input"  # 任务名称文本框
    effective_time = "//*[@class='rz-radio is-checked']/span[2]"  # 有效时间
    custom_time = "//*[@class='rz-radio']/span[2]"  # 自定义时间
    switch_fuzzy = "//*[@class='slider-switch']//span/span"  # 模糊阈值开关
    alarm_input = "//*[@class='slider-wrap']//input"  # 精准告警文本框
    fuzzy_alarm_input = "//*[@class='fuzzy']//input"  # 模糊告警文本框
    remark_input = "//*[@class='rz-textarea']//textarea"  # 备注文本框
    cancel_task = "//*[@class='rz-button rz-button--info rz-button--large']"  # 任务取消
    next_add_task = "//*[@class='rz-button rz-button--primary rz-button--large']"  # 新建任务下一步
    app_reason_input = "xpath=//textarea"              # 提交布控任务理由输入框
    submit_task_confirm = "css=main>div>div:nth-of-type(3)>div>div>span>button>span"     # 提交任务确认框
    # 选择布控对象
    monitor_lib = "//*[@class='source-group']//span[2]"  # 选择布控库和照片选项的list
    add_monitor_lib = "//*[@class='lib-tool']//button//span"  # 添加布控库按钮
    lib_search_input = "//*[@class='rz-input rz-input--suffix']//input"  # 人像库搜索文本框
    lib_search_button = "//*[@class='rz-search-input is-round is-focus-active']//i"  # 搜索按钮
    other = "//*[@class='rz-dialog__body']/div[@class='statistics']"  # 空白地方
    all_choose = ".all-select>label"  # 人像库全选
    search_target_type = "//*[@class='rz-dropdown-link']"  # 搜索类型选择框
    target_identity = "//*[@class='rz-dropdown-menu rz-popper']/li[1]"  # 搜索类型：身份
    target_remark = "//*[@class='rz-dropdown-menu rz-popper']/li[2]"  # 搜索类型：备注
    cancel_lib = "/html/body/div[2]/div/div[3]/span/button[1]"  # 人像库选择页取消按钮
    # ensure_lib = "/html/body/div[2]/div/div[3]/span/button[2]"  # 人像库选择页确定按钮
    ensure_lib = '//div[contains(@class,"select-library-popup")]//span[text()="确定"]'  # 人像库选择页确定按钮
    photo_task = "//*[@class='rz-radio']"  # 选择照片布控按钮
    switch_task = "//*[@class='rz-button rz-button--primary rz-button--medium']//span[text()='切换']"  # 切换布控任务
    upload_image = "//*[@class='rz-upload-slot']"  # 上传照片
    image_name_input = "//*[@class='rz-input__inner'][@placeholder='请输入姓名']"  # 人像姓名文本框
    image_id_input = "//*[@class='rz-input__inner'][@placeholder='请输入证件号']"  # 人像证件号文本框
    empty_photo = "//*[@class='button-wrap']//button[1]"  # 照片清空按钮
    save_photo = "//*[@class='button-wrap']//button[2]"  # 照片保存按钮
    # 选择视频源
    select_video = "//input[@placeholder='请选择']"  # 选择框
    video_type = "//*[@class='rz-scrollbar__view rz-select-dropdown__list']"  # 视频源类型list
    video_search_type = "//*[@class='rz-dropdown-link rz-dropdown-selfdefine  ']"  # 搜索类型
    video = "//*[@class='rz-dropdown-menu__item']"  # 搜索类型：视频源
    video_group = "//*[@class='rz-dropdown-menu__item selected']"  # 搜索类型：视频源分组
    video_search_input = "//*[@class='main-input-area']//input"  # 视频源搜索文本框
    video_search_button = "//*[@class='rz-search-input-suffix rz-icon-search']"  # 视频源搜索按钮
    video_all_choose = "/html/body/div[1]/div[1]/main/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/label/span/span"  # 视频源全选
    last_step = "/html/body/div/div[1]/main/div/div[1]/div[2]/div[2]/div/div[2]/button[1]"  # 上一步
    # 布控任务权限
    department = "//*[@class='filter-condition']//input"  # 所属部门下拉框
    department_list = "//*[@class='rz-select-dropdown__item']"  # 部门列表
    permissions_add_user = "//*[@class='rz-button add-user-btn rz-button--primary']"  # 布控权限新增用户
    search_department_user = "//*[@class='rz-input__inner'][@placeholder='请输入用户或部门名称']"  # 搜索部门
    search_department_user_button = "//*[@class='rz-search-input-suffix rz-icon-search']"  # 部门及用户搜索

    # 任务列表中各个功能
    task_staus = "//*[@class='rz-select width1 rz-select--medium']//div"  # 任务状态下拉框
    status_com_ = "//*[@class='rz-scrollbar__view rz-select-dropdown__list']//span[text()='{}']"
    # run = status_com_.format('运行中')  # 运行中
    # wait = status_com_.format('等待中')  # 等待中
    # stop = status_com_.format('已终止')  # 已终止
    task_source = "//*[@class='rz-select width2 rz-select--medium']//div"  # 任务来源
    task_src_com = "//*[@class='rz-scrollbar__view rz-select-dropdown__list']//span[text()='{}']"  # 已终止
    infinite = task_src_com.format('不限')  # 已终止
    icreate = task_src_com.format('我创建的任务')  # 已终止
    distribution = task_src_com.format('分配给我的任务')  # 已终止

    infinite_time = "//*[@class='rz-radio-button rz-radio-button--medium is-active']"  # 日期不限
    seven_day = "//*[@class='rz-radio-button rz-radio-button--medium']//span[text()=' 近7天']"  # 近7天
    fifteen_day = "//*[@class='rz-radio-button rz-radio-button--medium']//span[text()=' 近15天']"  # 近15天

    alarm_info = "//*[@class='table-operations']//span[text()='告警记录']"  # 告警记录按钮
    task_info = "//*[@class='table-operations']//span[text()='任务详情']"  # 任务详情按钮
    editor_task = "//*[@class='table-operations']//span[text()='编辑']"  # 编辑按钮
    first_editor = "xpath=//*[@class='rz-button rz-button--text is-primary-text']/span[text()='好的，知道了!']"  # 首次编辑或克隆任务时候的提示
    more = "xpath=//*[@class='rz-icon-more']"  # 任务更多操作
    stop_task_button = "//body/div[@class='rz-popover rz-popper table-operations-more'][last()]/span[text()='终止任务']"  # 终止任务操作按钮
    ensure_stop_task = "//*[@class='rz-button rz-button--primary rz-button--primary ']"  # 确定终止布控任务
    clone_task_button = "//*[@class='rz-popover rz-popper table-operations-more']//span[text()='克隆任务']"  # 克隆任务操作按钮
    restart_task_ele = "//*[@class='table-operations']//span[text()='重启']"  # 重启任务按钮
    ensure_restart_task = "//*[@class='rz-button rz-button--primary']"  # 重启任务确定按钮
    restart_task_success = "//*[@class='rz-icon-success success']"  # 重启任务成功弹窗
    restart_task_success_button = "//*[@class='rz-button rz-button--primary rz-button--medium']"
    task_search = "//*[@class='rz-input__inner'][@placeholder='请输入任务名称/创建人等']"  # 任务搜索框
    task_search_button = "//*[@class='rz-form-item tasks-filter-bar-button rz-form-item--medium']//i[@class='rz-search-input-suffix rz-icon-search']"  # 任务搜索按钮
    # 告警列表
    only_check_than_in_the = "//*[@class='rz-checkbox__input']"  # 告警列表页只看比中
    cancel_only_check_than_in_the = "//*[@class='rz-checkbox__label']"  # 取消只看比中
    silence_personnel = "//*[@class='hidden-person']//span[text()='查看']"  # 告警列表查看告警沉默人员按钮
    ed_silence_target = "//*[@class='hidden-portrait hidden-portrait-card'][{number}]//button[1]".format(
        number="1")  # 编辑沉默目标,默认第一个
    move_silence_target = "//*[@class='hidden-portrait hidden-portrait-card'][{number}]//button[2]".format(
        number="1")  # 移除沉默目标,默认第一个
    move_silence_ensure = "//*[@class='rz-button rz-button--primary']//span[text()='移除']"  # 移除确定
    first_alarm = "xpath=//*[@class='image-list-container']/div[1]/div[1]"  # 告警列表第一个告警
    first_than_in_the_alarm = "xpath=//*[@class='image-list']/div[@class='image-card comparison-image-card is-checked'][1]"  # 告警列表第一个比中的告警
    alarm_remark = "//*[@class='rz-textarea__inner'][@placeholder='输入内容']"  # 目标告警备注
    alarm_remark_commit = "//*[@class='input-confirm']"  # 目标告警备注确定
    target_judge = "//*[@class='rz-checkbox__label'][text()='比中 ']"  # 告警详情中的研判
    close_alarm_details = "//div[@class='content']//span[text()='告警详情']/following-sibling::button"  # 关闭告警详情页

    all_alarm = "//*[@class='view-all']"  # 查看该告警人像的全部历史告警
    check_track = "//*[@class='top-bar flex-middle navigator top']//button[@class='rz-button rz-button--text rz-button--small']"  # 查看轨迹
    track_alarm_list = "xpath=//*[@class='alarm-list'][1]/div[@class='locus-image-card-wrapper'][1]"  # 轨迹告警列表首个告警
    track_page_alarm_total = "xpath=//*[@class='matched-alarm-list-wrapper']/div/span"  # 查看轨迹页的历史告警数量
    tarck_marker_total = "xpath=//*[@class='locus-marker']/div/div"  # 轨迹视频源点位的告警数量
    hover_tarck_marker_total = "xpath=//*[@class='locus-marker is-hovering']/div/div"  # 悬浮鼠标后轨迹视频源点位的告警数量
    tarck_only_check_than_in_the = "xpath=//*[@class='filter-item']//span[@class='rz-checkbox__inner']"  # 查看轨迹页只看比中
    tarck_silence_set = "xpath=//*[@class='name-wrapper']//button"  # 查看轨迹页设置沉默时间
    video_list = "//*[@class='video-selection-text']"  # 告警列表视频源
    lib_list = "//*[@class='rz-input rz-input--suffix rz-popover__reference']//input[@placeholder='请选择库']"  # 告警列表布控库
    lib_cansel_selected = "//*[@class='all-select']//span[@class='rz-checkbox__inner'][1]"  # 告警列表人像库全选或取消全选
    lib_input = "//*[@class='tool']//input"  # 告警列表人像库搜索文本框
    lib_button = "//*[@class='tool']//i"  # 告警列表人像库搜索按钮
    lib_save = "//*[@class='rz-button rz-button--text is-primary-text']"  # 告警列表人像库确定选择
    lib_other = "//*[@class='btn-wrap']"  # 空白地方
    similar = "//*[@class='similarity-text rz-dropdown-selfdefine']"  # 告警列表相似度下拉框
    similar_input = "//*[@class='rz-input rz-input--small rz-input--suffix']//input"  # 告警列表相似度输入框
    id_attribute = "//*[@class='rz-button rz-button--text']//span[text()='身份属性']"  # 告警列表身份属性下拉框
    gender_input = "//*[@class='rz-select gender-selection']//input"  # 告警列表身份属性性别下拉框
    age_input = "//*[@class='rz-select age-selection']//input"  # 告警列表身份属性年龄段下拉框
    gender_age_input = "//*[@class='rz-scrollbar__view rz-select-dropdown__list']//span[text()='{typo}']"  # 告警列表身份属性性别，年龄段选择
    target_input = "//*[@class='rz-search-input search-input is-round']//input"  # 告警列表人像告警搜索文本框
    target_input_button = "//*[@class='rz-search-input search-input is-round']//i"  # 告警列表人像告警搜索按钮
    video_input = "xpath=//*[@class='rz-input rz-input--suffix']//input[@placeholder = '请输入视频源名称']"  # 告警列表视频源搜索文本框
    alarm_video_all_choose = "xpath=//*[@class='rz-big-data-tree root-tree']/div/div/label/span/span"  # 告警列表视频源全选
    video_button = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div[1]/div/div[3]/div/div[3]/div/button[2]"  # 告警列表视频源搜索确定按钮
    alarm_push_set = "//*[@class='push-config']//div[1]//button"  # 告警列表告警推送方式编辑
    alarm_push_select_video = "//*[@class='trigger-input']"  # 告警列表告警推送方式选择视频源
    alarm_push_select_video_button = "css=body>div:nth-last-of-type(2) .rz-button--primary"  # 告警列表告警推送方式选择视频源确定按钮
    sound_open = "//*[@class='rz-form-item__content']//span[text()='开启']"  # 告警列表-告警推送方式-声音提示开启
    sound_close = "//*[@class='rz-form-item__content']//span[text()='关闭']"  # 告警列表-告警推送方式-声音提示关闭
    alarm_push_ensure = "//*[@class='rz-button rz-button--primary rz-button--medium']//span[text()='确定']"  # 告警列表-告警推送方式-确定按钮
    check_push_config = "xpath=//*[@class='push-config']//span[text()='查看']"  # 告警列表查看告警推送区域按钮
    sound_status = "xpath=//*[@class='sound-status'][text()='{status}']".format(status='已关闭')  # 声音状态
    sound_status = 'css=.item>.sound-status'
    silence_set = "//*[@class='set-silent-time']"  # 设置沉默时间
    silence_ensure = "//*[@class='rz-button rz-button--primary']//span[text()='确定']"  # 设置沉默确定按钮
    silence_reason_input = "//*[@class='rz-textarea']//textarea[@placeholder='请输入沉默原因']"  # 沉默原因文本框
    silence_editor = "xpath=/html/body/div[3]/div/div[3]/span/button[2]"  # 告警详情，编辑沉默时间
    move_silence = "xpath=/html/body/div[3]/div/div[3]/span/button[1]"  # 告警详情，移除沉默时间
    details_move_silence_ensure = "xpath=/html/body/div[3]/div/div[3]/span/button[2]"  # 告警详情，移除沉默时间
    # 地图模式
    alarm_list_map = "xpath=//*[@class='mode-switcher-item']"  # 告警列表地图模式
    alarm_list_map_target = "xpath=//*[@class='alarm-list'][1]/div[@class='image-card-wrapper'][1]"  # 告警列表地图模式首个告警
    map_alarm_count = "xpath=//*[@class='matched-alarm-list-wrapper']//span"  # 点位图告警数量
    map_alarm_total = "xpath=//*[@class='total-items']"  # 告警列表数量
    video_marker_alarm_count = "xpath=//*[@class='count-wrapper']/div"  # 视频源标记位中的告警数量
    hover_video_marker_alarm_count = "xpath=//*[@class='alarm-marker is-hovering']/div/div"  # 悬浮视频源标记位中的告警数量
    heat_map = "xpath=//*[@class='map-switcher-item']"  # 热力图
    video_marker = "xpath=//*[@class='count-wrapper']"  # 视频源标记位
    hover_video_marker = "xpath=//*[@class='alarm-marker is-hovering']/div"  # 悬停视频源标记位
    video_details = "xpath=//*[@class='filter-item']//span[text()='0%']"  # 视频源详情页相似度下拉框
    video_details_snap = "xpath=//*[@class='target-activity']/div[1]"  # 视频源详情抓拍记录
    alarm_score = "xpath=//*[@class='image-list']//div[3][@class='rz-image']//span[2]"  # 告警分数

    # 视频源选择
    camera_ele = "css=.trigger-input"  # 视频源控件
    camera_page_cam_tree = "css=.rz-big-data-tree.root-tree>div>div>label"  # 一级部门全/反选checkbox
    camera_slt_cate_ele = "css=.rz-dropdown-link"  # 分组/视频源 选择处
    camera_slt_cate_group = "css=body>ul:last-child>li:nth-of-type(1)"  # 分组
    camera_slt_cate_camera = "css=body>ul:last-child>li:nth-of-type(2)"  # 视频源
    camera_slt_cate_txt = "css=.main-input-area input:first-of-type"  # 分组/视频源搜索框
    camera_slt_cate_txt_search = "css=.rz-search-input-suffix.rz-icon-search"  # 搜索文本后的 搜索按钮
    camera_slt_cate_search_check_box = "css=.rz-big-data-tree-node.is-leaf label"  # 搜索后选取视频源
    camera_cancel_btn = '//button[@class="rz-button rz-button--info rz-button--large"]'  # 取消按钮
    # camera_confirm_btn = "xpath=//*[@class='rz-button rz-button--primary rz-button--large']"  # 确定按钮
    camera_confirm_btn = "//*[contains(@class,'rz-button rz-button--primary rz-button--large')]|#系统设置-功能设置页的编辑/确定按钮"
    task_list_table = "xpath=//*[@class='rz-table__body']//tbody"  # 布控任务列表表格
    task_list_table_tr = "xpath=//*[@class='rz-table__body']//tr"  # tr标签数据，每个tr代表一个任务的数据
    # 任务详情中各个功能
    task_base_info = "//*[@class='step']//span[text()='{typo}']"  # 1.基本信息 2.选择布控对象 3.选择视频源 4.布控任务权限
    stop_task = "//*[@class='rz-button rz-button--danger rz-button--large is-plain']"  # 任务详情中终止布控任务

    # 铃铛
    small_bell = "//*[@class='nav-bar-item']//i[@class='icon iconfont icon-notice']"  # 铃铛
    stop_push_message = "//*[@class='rz-on-off is-checked']//span[@class='rz-on-off__core--circle']"  # 关闭推送
    count_alarm = "xpath=//*[@class='rz-badge__content is-fixed']"  # 铃铛的告警数量

    # 返回
    go_back = "xpath=//*[@class='rz-button flex-middle back-btn rz-button--text rz-button--medium']"  # 返回

    # 系统设置设置阈值
    all_push = "xpath=//*[@class='rz-form task-edit']//span[text()='全部']"  # 推送全部
    # threshold_value = "xpath=//*[@class='rz-input__inner']"  # 阈值
    setting_lbl_el = '//label[contains(text(),"{}")]/following-sibling::div|# 系统设置-功能配置页面-标签值'# 4.2
    setting_ipt_el = '//label[contains(text(),"{}")]/following-sibling::div//input'  # 系统设置-功能配置页面 input元素， 4.2
    setting_ipt_ele = "xpath=//*[@class='rz-form task-edit']/div[4]/div/div//input"     #系统设置-功能配置页面 任务持续时长
    setting_ipt_elc = "xpath=//*[@class='rz-form task-edit']/div[5]/div/div//input"     #系统设置-功能配置页面 人体检索范围