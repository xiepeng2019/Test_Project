#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class SearchPageEle:
    """
    检索通用
    """

    class CommonSearch:
        """
        检索公用 元素控件
        """
        # 第1页
        f_img_ele = "css=.rz-upload__input[type=file]"
        #       日期相关
        f_date_ele = "css=.rz-date-editor--datetimerange"  # 日期控件
        f_date_7_ele = "css=.rz-picker-panel__sidebar-inner>button:nth-of-type(1)"
        f_date_15_ele = "css=.rz-picker-panel__sidebar-inner>button:nth-of-type(2)"
        f_date_30_ele = "css=.rz-picker-panel__sidebar-inner>button:nth-of-type(3)"
        f_date_start_ele = "{}>input:nth-of-type(1)".format(f_date_ele)  # 开始时间
        f_date_end_ele = "{}>input:nth-of-type(2)".format(f_date_ele)  # 结束时间
        f_date_default_btn = "css=.rz-picker-panel__footer button:nth-of-type(1)"  # 恢复默认时间
        f_date_cancel_btn = "css=.rz-picker-panel__footer button:nth-of-type(2)"  # 取消按钮
        f_date_confirm_btn = "css=.rz-picker-panel__footer button:nth-of-type(3)"  # 确定按钮
        # 视频源
        f_camera_ele = "css=.trigger-input"  # 视频源控件
        f_camera_page_cam_tree = "css=.rz-big-data-tree.root-tree>div>div>label"  # 一级部门全/反选checkbox
        f_camera_slt_cate_ele = "css=.rz-dropdown-link"  # 分组/视频源 选择处
        f_camera_slt_cate_group = "css=body>ul:last-child>li:nth-of-type(1)"  # 分组
        f_camera_slt_cate_camera = "css=body>ul:last-child>li:nth-of-type(2)"  # 视频源
        f_camera_slt_cate_txt = "css=.main-input-area input:first-of-type"  # 分组/视频源搜索框
        f_camera_slt_cate_txt_search = "css=.rz-search-input-suffix.rz-icon-search"  # 搜索文本后的 搜索按钮
        f_camera_slt_cate_search_check_box = "css=.rz-big-data-tree-node.is-leaf label"  # 搜索后选取视频源
        f_camera_cancel_btn = "css=.dialog-footer button:first-child"  # 取消按钮
        f_camera_confirm_btn = "css=.dialog-footer button:last-child"  # 确定按钮
        # 文本检索
        f_txt_trig_ele = 'css=.icon-fontT'  # 文本检索 触发
        f_txt_input_ele = 'css=.text-input-area input'  # 输入文本
        f_txt_id_checkbox = "xpath=//span[@class='rz-radio__label'][contains(text(),'{}')]"  # 身份识别/车牌识别的选择
        # 按钮
        f_search_button = "css=.default-btn"  # 检索按钮
        f_history_text = "css=.btn-title"  # 历史检索按钮
        # 结果展示页
        history_btn = "//span[text()='历史检索']"  # 历史检索按钮 # mx 2020.8.20修改，原：'css=.history-btn'
        his_cap_lst = 'css=.list>div>.rz-image-card__content'
        his_page_btn = 'css=.rz-pager>li'
        # 结果展示页 左侧菜单
        left_menu_threshold_ = 'css=.rz-input-number input'  # 左侧菜单 的阈值 input
        left_menu_threshold_face = "xpath=(// div[contains( @class ,'rz-input-number')] // input)[1]"
        left_menu_threshold_body = "xpath=(// div[contains( @class ,'rz-input-number')] // input)[2]"
        left_menu_srh_btn_search = "xpath=//span[text()='检索']"
        left_menu_rst_btn = 'css=footer>button.rz-button--info'  # 左侧菜单 重置按钮
        left_menu_srh_btn = 'css=footer>button.rz-button--primary'  # 左侧菜单 检索按钮
        left_search_camera_ipt = 'css=.main-input-area input'
        # # 返回按钮z-message-box__wrapper .rz-button--pr
        #         # back_btn = 'css=.back-btn'  # 返回按钮
        #         # back_confirm_btn = 'css=.rimary'   # 返回时，确认清除按钮
        #
        s_back_button = "css=.back-btn"  # 返回按钮
        s_date_ele = f_date_ele  # 日期控件
        s_camera_ele = "css=.icon-video"  # 视频源控件
        s_rst_button = "css=.reset"  # 重置按钮
        s_search_button = "css=.confirm"  # 检索按钮
        s_new_target_ele = "css=.target-plus"  # 新增目标
        s_target_a = "xpath=//span[@class='target'][text()='{}']".format("目标A")
        s_target_b = "xpath=//span[@class='target'][text()='{}']".format("目标B")
        s_select_only = "css=.just-show-comparison"  # 只看比中
        s_select_total = "css=.comparison>span:nth-of-type(2)"  # 比中总数
        s_fav_select = "css=.rz-icon-star-off"  # 收藏比中
        s_export_select = "css=.export-comparison"  # 导出比中
        s_trace = "css=.comparison-trail"  # 查看轨迹
        s_intel_select = "css=.intelligent-comparison .rz-on-off__core"  # 智能比中
        s_threshold_left = "css=.condition .rz-slider__input-box .rz-input__inner"  # 左边阈值
        s_threshold_intel = "css=.slide-intelligent .rz-input__inner"  # 右边智能比中阈值
        s_threshold_intel_confirm = "css=.rz-button.btn-confirm.rz-button--text"  # 右边智能阈值确定
        # 图片相关
        s_img_page = "css=.container-wrapper.scroller-wrap"  # 整个图片页面
        s_img_ele = "css=.results-item.item"  # 图片元素,重复型
        s_back_top = "css=.rz-backtop__word"  # 图片滚动后返回顶层按钮

        # 抓拍图相关
        # all_capture_data_ele = 'css=.container>div'
        all_capture_data_ele = 'css=.container'
        all_capture_ele = 'css=.list>div'  # 所有抓拍图片的元素  限于相似度排序，
        #
        all_capture_lst_ele = 'css=.container div.results-item'  # 所有抓拍图片的元素
        all_capture_lst_slt_ele = 'css=.container div.results-item label'  # 比中按钮
        all_capture_plate_no = 'css=.container .rz-image__info'  # 所有车牌号
        all_capture_img_info_no = 'css=.container .rz-image-card__content'  # 所有车牌号
        #
        all_cap_ele = 'css=.rz-image-card'  # 所有抓拍图片的元素
        all_cap_ele = 'css=.list .rz-image-card'  # 所有抓拍图片的元素
        per_cap_ele = '%s:nth-of-type({})' % all_capture_ele  # 单张抓拍图
        cap_slt_status_ele = '%s label' % per_cap_ele
        cap_slt_cbox = '%s label' % per_cap_ele
        # cap_slt_cbox = '%s label .rz-checkbox__original' % per_cap_ele
        cap_threshold_ele = '%s .rz-image__info' % per_cap_ele
        cap_info_ele = '%s .content' % per_cap_ele
        # 抓拍图相关 库抓拍图
        all_lib_capture_ele = 'css=.list>div'
        per_lib_capture_ele = '%s:nth-of-type({})' % all_lib_capture_ele
        per_lib_cap_threshold_ele = '%s .rz-image__info>span:last-child' % per_lib_capture_ele  # 单图片 阈值
        per_lib_cap_name_ele = '%s .target-name' % per_lib_capture_ele  # 单图片 名字
        per_lib_cap_id_ele = '%s .identity-id' % per_lib_capture_ele  # 单图片 ID
        per_lib_cap_lib_ele = '%s .tarLib-name' % per_lib_capture_ele  # 单图片 所属库名
        per_lib_cap_more_lib_ele = '%s .tarLib-name+span .rz-tag' % per_lib_capture_ele  # 单图片 融合库名
        per_lib_cap_more_lib_lst = 'css=body>div:last-child .tagIt'  # 更多 库时 的库列表

        # 页面
        page_title_ele = 'css=.crumbs'  # 页面标题
        # 轨迹页
        trace_slt_wid_ele = 'css=.sc-map__container+div .title'  # 比中结果 大控件
        trace_active_wid_ele = 'css=.sc-map__container+div+div .title'  # 活动规律 大控件
        trace_companion_wid_ele = 'css=.sc-map__container+div+div+div .title'  # 同行人 大控件
        # 双目标 轨迹页相关
        trace_double_modify_btn = '%s>div' % trace_slt_wid_ele  # 双目标时的 轨迹页面-比中结果 更改
        trace_double_judge_card = 'css=.card-total-2'
        trace_double_judge_card_img = 'css=.card-total-2>.rz-image'

        trace_companion_ele = 'css=.icon-walker'  # 轨迹同行人 控件, 双目标时叫 显示轨迹
        trace_play_ele = 'css=.icon-play'  # 轨迹页 播放轨迹
        trace_dis_ele = 'css=.icon-track'  # 轨迹页 显示轨迹
        # 轨迹排序处
        trace_sort_trig = 'css=.video-filter'  # 轨迹排序目前 的值
        trace_filter_trig = 'css=.icon-filter'  # 轨迹 时间过滤过滤
        # 轨迹过滤 下拉
        trace_filter_all = 'css=.selectOperation>label'  # 全选
        trace_filter_date = 'css=.selectOperation>div>label>span:last-child'  # 日期列表
        trace_filter_reset_btn = 'css=.operate_btn>li:first-child>button'  # 日期过滤 重置按钮
        trace_filter_cancel_btn = 'css=.operate_btn>li:last-child>.cancel'  # 日期过滤 取消按钮
        trace_filter_confirm_btn = 'css=.operate_btn>li:last-child>.confirm'  # 日期过滤 确定按钮
        # 轨迹排序，默认的时间排序时 相关控件
        trace_sort_day_ele = 'css=.integration-search-matchedResult--list'
        trace_sort_group_title_ele = '%s>.group-title' % trace_sort_day_ele  # 图片分组列表
        trace_sort_per_cap_ele = '%s>div>.content' % trace_sort_day_ele  # 图片列表
        # 点位点击
        # trace_dot_ele = 'css=.search-Primary.active'       # 抓拍图点位 点击
        trace_dot_ele = 'css=div.active'  # 抓拍图点位 点击
        trace_map_plus = 'css=i.rz-icon-plus'  # 地图放大，
        trace_map_minus = 'css=i.rz-icon-minus'  # 地图缩小，
        trace_dot_camera_lst = 'css=.search-map-camera-info--name>span'  # 抓拍图点位 点击后视频源列表
        trace_dot_dot_lst = 'css=.occurrences'  # 检查当前比中点 有几个点位  如首现点/末现点/常现点
        # 抓拍记录页
        trace_dot_capture_num = 'css=.capture-record-left-body li:first-child span'

        # 人脸相关
        flt_camera_trig_el = 'css=.video-filter'
        flt_camera_close_el = 'css=.icon-wrong'
        flt_sort_trig_el = 'css=div.sort-filter'
        only_show_el = 'css=.just-show-comparison>label'
        only_show_slt_el = 'css=.just-show-comparison>label>span>span'
        only_show_slt_num_el = 'css=.just-show-comparison>span'
        # 人脸过滤
        flt_face_trig = 'css=.feature-action'
        flt_sex_input = 'css=input[placeholder="请选择性别"]'
        flt_age_input = 'css=input[placeholder="请选择年龄"]'
        flt_glass_input = 'css=input[placeholder="请选择眼镜款式"]'
        flt_beard_input = 'css=input[placeholder="请选择胡型"]'
        flt_mask_input = 'css=input[placeholder="请选择口罩"]'
        flt_cat_input = 'css=input[placeholder="请选择帽子款式"]'
        flt_confirm_btn = 'css=.selector-footer .is-primary-text'
        flt_cancel_btn = 'css=.selector-footer .cancel'
        flt_reset_btn = 'css=.selector-footer>button'
        flt_drop_list = "div[title='{}']+div ul"
        # 智能比中按钮
        # intel_slt_btn = 'css=.intelligent-comparison .rz-on-off'    # 智能比中开关
        intel_slt_btn = 'css=div.results-filter .rz-on-off'  # 智能比中开关
        intel_slt_threshold_ele = 'css=.threshold-percent'  # 默认智能比阈值
        intel_threshold_ipt = "css=.slide-intelligent input[max='100']"  # 智能比中阈值设置
        intel_reset_btn = 'css=.slide-btn>.slide-left>button'
        intel_cancel_btn = 'css=.slide-btn .cancel'
        intel_confirm_btn = 'css=.slide-btn .btn-confirm'  # 修改智能比中阈值后 保存按钮

        rst_search_btn = 'css=.reset'
        slt_num_ele = 'css=.comparison>span:last-child'  # 比中数量
        fav_search_status_ele = 'css=.collect-comparison'  # 收藏比中的按钮
        fav_search_ele = 'css=.collect-comparison>i'  # 收藏比中的按钮
        export_search_ele = 'css=.export-comparison'  # 导出比中的按钮
        trace_ele = 'css=.icon-track1'  # 轨迹按钮
        # 智能检索 结果页的 更多 列表
        result_more = 'css=div.more'  # 智能检索结果页 的四个更多
        # COMMON
        tab_sw_com = 'xpath=//span[@class="rz-radio-button__inner"][contains(text(),"{}")]'
        filter_com_el = 'xpath=//span[text()="{}"]'  # 右上角筛选属性
        filter_com_btn = 'xpath=//div[@role="tooltip"]//span[text()="{}"]'  # 筛选选项的按钮 重置/取消/确定

        property_ele = 'css=.feature-action-text'  # 属性
        property_rst_ele = '//section/button/span[text()="重置"]|#车辆属性过滤-重置按钮'  # 属性

    # 以下为各检索 差异控件
    class FS(CommonSearch):
        menu_name = "人脸检索"
        pass

    class PS(CommonSearch):
        menu_name = "行人检索"

    class IS(CommonSearch):
        menu_name = "融合检索"
        filter_priority_ele = 'css=.priorityMode'  # 结果页排序时的 人脸优先/人体优先

    class VS(CommonSearch):
        menu_name = "车辆检索"

    class LS(CommonSearch):
        menu_name = "身份检索"
        # 身份检索 Index
        slt_lib_trig = 'css=.rz-select'
        # 身份检索结果页 属性过滤处
        lib_tag_slt_all = 'css=.content>header>label'  # 全选按钮
        lib_tag_ele = 'css=.trigger-block'  # 库标签
        lib_tag_lst = 'css=.rz-tagList>span'  # 库标签列表
        lib_tag_reset_btn = 'css=footer>li:first-child>button'  # 库标签时的 重置按钮
        lib_tag_cancel_btn = 'css=li>button.cancel'  # 库标签时的 取消按钮
        lib_tag_confirm_btn = 'css=li>button.confirm'  # 库标签时的 确认按钮

        lib_property_ele = 'css=.feature-action-text'  # 身份属性
        lib_property_hometown_ele = 'css=.cascader-title+span input'  # 身份属性 户籍
        lib_property_ps_ele = 'css=input[placeholder="请输入备注"]'  # 身份属性备注

    class OS(CommonSearch):
        menu_name = "离线检索"

    class TS(CommonSearch):
        menu_name = "时空过滤"
        search_tab_lst_ele = 'css=label.rz-radio-button'

    class CS(FS, LS, VS, IS):
        menu_name = "智能检索"
        # result_more = 'css=div.more'    # 智能检索结果页 的四个更多
        result_pick_up = 'css=div.pick-up'  # 智能检索页 四种检索结果页的 收起 按钮
        result_tab_sw = 'xpath=//label/span[contains(text(),"{}")]'  # 四种检索结果页的切换

        # intel_slt_btn = 'css=.rz-scrollbar .intelligent-comparison .rz-on-off'

        # intel_slt_btn = 'css=.main-content .intelligent-comparison .rz-on-off'    # 智能比中开关
        intel_slt_threshold_ele = 'css=.main-content span.threshold-percent'  # 默认智能比阈值
        intel_threshold_ipt = "css=div[x-placement='bottom'] .slide-intelligent input[max='100']"  # 智能比中阈值设置
        intel_reset_btn = 'css=div[x-placement="bottom"] .slide-left>button'
        intel_cancel_btn = 'css=div[x-placement="bottom"] .cancel'
        intel_confirm_btn = 'css=div[x-placement="bottom"] .btn-confirm'  # 修改智能比中阈值后 保存按钮
