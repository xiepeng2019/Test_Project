#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# __author__ = 'csf'
# 此部分用于放置视频源 页面元素


class CameraPageEle:
    """
    视频源通用
    """

    class Camera:
        """
        检索公用 元素控件
        """
        # menu_name = "视图源管理"
        search_group_ele = 'css=input[placeholder="请输入分组名称"]'  # 分组搜索框
        search_group_icon_ele = 'css=.contain-side .rz-icon-search'  # 分组搜索图标
        group_more_menu = "css=.module-contain .more-operation"  # 分组... 点击菜单
        search_camera_ele = 'css=input[placeholder="名称/编号/IP地址"]'
        # 视频源分组详情
        camera_grp_detail_name = "css=.basicInfo-form>div:nth-of-type(1) span"
        camera_grp_detail_root = "css=.basicInfo-form>div:nth-of-type(2) span"
        camera_grp_detail_creator = "css=.basicInfo-form>div:nth-of-type(4) span"
        camera_grp_detail_date = "css=.basicInfo-form>div:nth-of-type(5) span"
        camera_grp_base_info = 'css=.view-steps>div:first-child'
        camera_grp_power_info = 'css=.view-steps>div:last-child'
        camera_grp_del_btn = 'css=.control button:first-child'  # 视频源分组 详情中的 删除按钮, 编辑中的取消按钮
        camera_grp_edit_btn = 'css=.control button:last-child'  # 视频源分组 详情中的 编辑按钮, 编辑中的保存按钮
        # 视频源状态 统计
        camera_status_cnt = 'css=.video-status-count'  # 视频源状态 统计
        camera_status_cnt_ = '{}>.count-list'.format(camera_status_cnt)  # 视频源状态 各统计
        # 视频源列表
        camera_tbl_refresh = 'css=.container .rz-icon-search|#当前页视频源搜索按钮'
        # camera_total ="//span[@class='count-list']/span[text()='在线']/following-sibling::span[1] |#当前页视频源总数"  #mx 2020.8.25 原：
        camera_total = 'css=.rz-pagination__total|#当前页视频源总数'
        camera_table = 'xpath=(//tbody)[1] |# 当前页视频源表格 '  # 当前页视频源表格' # mx 2020.8.25 原：camera_table = 'css=tbody''
        camera_table = 'css=.list-table>div>div>table>tbody'
        camera_judge_page_ele = '.list-table>div|# 通过判定div数量(div2 为分页器)来判定是否有第二页或更多'
        camera_all_lst = '{}>tr|#表格第一列'.format(camera_table)
        camera_name_ele = '{}>td:nth-of-type(2)|# 指定列tr 视频源名字'
        camera_type_ele = '{}>td:nth-of-type(3)|#指定列tr 视频源规格'
        camera_group_ele = '{}>td:nth-of-type(4)|#指定列tr 视频源所属分组'
        camera_acs_status = '{}>td:nth-of-type(5)|# 指定列tr 视频源接入状态'
        camera_detail_ele = '{}>td:last-child span:first-child|# 指定列tr 详情'
        camera_edit_ele = '{}>td:last-child span:nth-of-type(2)|# 指定列tr 编辑'
        camera_del_ele = '{}>td:last-child span:last-child|# 指定列tr 删除'
        camera_del_confirm_ele = 'css=.container+div .rz-button--primary|# 删除之后 的确认删除按钮'
        # # 恢复
        camera_recovery_ele = '{}>td:last-child span:first-child|# 指定列tr 恢复'
        camera_recovery_confirm_ele = 'xpath=//button/span[text()="恢复"]|# 恢复 确认框'
        # 视频源详情框
        # __camera_det = 'css=.detail-info div:first-child>.classify-main'
        __camera_det = 'css=.is-detail div:first-child>.classify-main'  # 4.2
        # camera_det_type = '{}>div:nth-of-type(1) .text'.format(__camera_det)
        # camera_det_name = '{}>div:nth-of-type(2) .text'.format(__camera_det)

        camera_det_type = '//label[text()="{}"]/following-sibling::div'.format("类型")
        camera_det_name = '//label[text()="{}"]/following-sibling::div'.format("视频源名称")  # 4.2

        camera_det_path = '{}>div:nth-of-type(4) .text'.format(__camera_det)
        camera_det_path_preview = '{}>div:nth-of-type(4) .btn-preview'.format(__camera_det)
        camera_det_group = '{}>div:nth-of-type(5) .text'.format(__camera_det)
        # camera_det_del_ele = 'css=.video-detail>div>div>.rz-dialog__footer .rz-button--info'    # 删除按钮
        # camera_det_edit_ele = 'css=.video-detail>div>div>.rz-dialog__footer .rz-button--primary'    # 编辑按钮

        camera_det_edit_btn = '//div[@class="videos"]/div[last()]//span[contains(text(),"{}")]'
        camera_det_del_ele = camera_det_edit_btn.format("删除")  # 删除按钮
        camera_det_edit_ele = camera_det_edit_btn.format("编辑")  # 编辑按钮      # 4.2
        __camera_detail_status = 'css=.access-status-switch'  # 详情页 的接入控件
        camera_face_status = '{}>div:nth-of-type(1)|#人脸接入状态'.format(__camera_detail_status)
        camera_ped_status = '{}>div:nth-of-type(2)|# 人体接入状态'.format(__camera_detail_status)
        camera_face_ped_status = '{}>div:nth-of-type(3)|# 人脸人体联合 接入状态'.format(__camera_detail_status)
        camera_crowd_status = '{}>div:nth-of-type(4)|# 人脸人体联合 接入状态'.format(__camera_detail_status)
        # camera_detail_close = 'css=.video-detail>div>div>div:first-child .rz-icon-close'    # 详情页 右上角关闭按钮
        camera_detail_close = '//span[text()="视频源详情"]/following-sibling::button|# 详情页 右上角关闭按钮'
        # 视频源编辑页面
        camera_edit_del_btn = 'css=.edit-dialog>div>.rz-dialog__footer .rz-button--info'
        # camera_edit_save_btn = 'css=.edit-dialog>div>.rz-dialog__footer .rz-button--primary'
        camera_edit_save_btn = '//div[@class="videos"]/div[last()]//span[text()="保存"]'
        # 新建分组
        new_group_name = 'css=.rz-form input[placeholder="请输入分组名称"]|# 新建分组 分组名称input, 编辑分组时的 分组名Input'
        new_group_rectangle = 'css=.icon-rectangle|# 矩形框架工具'
        new_group_cancel_btn = 'css=.control .rz-button--info|# 新建分组页，取消按钮'
        new_group_next_btn = 'css=.control .rz-button--primary|# 新建分组页，下一步/确定按钮'
        del_group_confirm_tip = 'css=.rz-message-box__message|# 删除分组时提示语 是否删除该分组'
        del_group_confirm_msg = '是否删除该分组'  # 删除分组时提示语'
        del_group_confirm_btn = 'css=.rz-message-box__btns>.rz-button--primary|# 删除分组时的确认按钮'
        # 新建视频源
        camera_ipt_com = 'css=input[placeholder="{}"]'
        new_camera_btn = "css=.right.rz-button--primary"  # "xpath=//span[text()='新建视频源']"
        new_camera_type = "css=.rz-cascader__label"  # 视频源类型
        # new_camera_type_1 = 'css=.rz-cascader-menus>ul:first-child .rz-scrollbar__view'
        # new_camera_type_2 = 'css=.rz-cascader-menus>ul:last-child .rz-scrollbar__view'
        new_camera_type_ = 'xpath=//div[@class="rz-scrollbar__view"]/li/span[text()="{}"]|# 视频源规格'
        new_camera_name = camera_ipt_com.format("请输入视频源名称")  # 视频源名称
        new_camera_add = camera_ipt_com.format("请输入网络地址")  # 视频源网络地址
        new_camera_group = camera_ipt_com.format("请选择分组")  # 分组
        new_camera_remark = camera_ipt_com.format("请输入备注")  # 备注
        new_camera_longitude = 'css=.longitude>input|# 经度'
        new_camera_latitude = 'css=.latitude >input|# 纬度'
        # new_camera_cancel_btn = 'css=.edit-dialog .rz-dialog__footer .rz-button--info'      # 新建视频源的取消按钮
        camera_btn_com = '//div[@class="videos"]/div[last()]//span[text()="{}"]'
        # new_camera_cancel_btn = camera_btn_com.format("取消")      # 新建视频源的取消按钮
        # new_camera_confirm_btn = 'css=.edit-dialog .rz-dialog__footer .rz-button--primary'  # 新建视频源的确认按钮
        # new_camera_confirm_btn = camera_btn_com.format("确定")  # 新建视频源的确认按钮
        # 通用
        # new_camera_ipt = 'xpath=//div[@class="video-edit"]//input[contains(@placeholder,"{}")]'     # input .format('input提示字符')
        new_camera_ipt = 'xpath=//div[@class="videos"]//input[contains(@placeholder,"{}")]'  # input .format('input提示字符')

        # 批量查询 筛选条件控件
        bat_acs_div = 'css=body>div:last-child|#接入过滤弹出框'
        bat_type_slt_ele = '{} li:nth-of-type({})|#下拉选择框'
        bat_type_ele = 'css=.filter-container>div:nth-of-type(1)>div:nth-of-type(1)|#类型过滤按钮'
        bat_status_ele = 'css=.filter-container>div:nth-of-type(1)>div:nth-of-type(2)|#状态过滤按钮'
        bat_task_ele = 'css=.filter-container>div:nth-of-type(1)>div:nth-of-type(4)|#布控过滤按钮'
        #   # 接入
        bat_acs_ele = 'css=.filter-container>div:nth-of-type(1)>div:nth-of-type(3)|#接入过滤按钮'
        bat_acs_pub_wid = '%s>div:nth-of-type({}) label:nth-of-type({})|#接入过滤标签框中的 公共' % bat_acs_div
        #   # 移入分组
        # 接入类型(人脸/结构化/人脸人体联合/人群)  接入状态(不限/接入/不接入)
        bat_acs_common_wid = 'xpath=//body/div[@role="tooltip"]//div[text()="{}"]/following-sibling::div//span[contains(text(),"{}")]|#接入类型/状态'
        bat_acs_common_btn = 'xpath=//body/div[@role="tooltip"]//span[text()="{}"]|#重置/保存'
        # 过滤处 按钮
        bat_filter_com_btn = 'xpath=//div[@class="filter-buttons"]/button//span[text()="{}"]|#过滤处 按钮-重置/确定'

        # 批量编辑
        bat_edit_status = 'css=.batch-edit|# 批量编辑 状态'
        bat_edit_btn = 'css=.rz-icon-edit-outline|#批量编辑按钮/退出批量编辑'
        bat_edit_all_ele = 'css=.all-page|#全选视频源按钮'
        #   # 批量操作
        bat_edit_move = 'css=.batch-edit-group>button:first-of-type|#批量编辑视频源 移入分组'
        bat_edit_del = 'css=.batch-edit-group>button:last-of-type|#批量编辑视频源 删除'
        bat_edit_acs = 'css=.batch-edit-group>div:first-of-type|#批量编辑视频源 接入 点击'
        bat_edit_acs_cancel = 'css=.batch-edit-group>div:last-of-type|#批量编辑视频源 取消接入 点击'
        bat_edit_cancel_btn = 'css=body>div[class="rz-dialog__wrapper"] .rz-button--info|#接入/取消接入后 确认框 的 取消按钮'
        bat_edit_confirm_btn = 'css=body>div[class="rz-dialog__wrapper"] .rz-button--primary|#接入/取消接入后 确认框 的 确定按钮'
        bat_edit_confirm_no_skip_btn = 'css=.rz-message-box .rz-button--info'
        bat_edit_confirm_skip_btn = 'css=.rz-message-box .rz-button--primary'
        bat_edit_del_cancel = 'css=.move-to-group-tips .rz-button--info|#批量删除后 确认框的 取消按钮'
        bat_edit_del_confirm = 'css=.move-to-group-tips .rz-button--primary|#批量删除/移入分组 后 确认框的 确认按钮'

        # 编辑/新建时，视频源分组选择
        slt_grp_srh = 'css=.video-group-tree-wrapper .rz-search-input input'  # 分组搜索框
        slt_grp_tree = 'css=.video-group-tree-wrapper .rz-tree'  # 第二分组树
        # edit_cancel_btn = new_camera_cancel_btn           # 编辑页 取消按钮
        # edit_save_btn = camera_btn_com.format("保存")           # 编辑页 保存按钮

        # 视频源 导入处控件
        import_icon = 'css=.tool-bar .icon-import'
        import_wid_btn = 'css=.content>button'
        import_template_dl_btn = 'css=.sf-importVideos__templateDownload'
        import_file_ele = "css=input[type='file']"

        # 区块 相关控件
        block_type_new_btn = 'css=.options>div:first-child'  # 区别添加按钮
        block_type_new_name = 'css=input[placeholder="请输入区块类型，最多不超过10个字"]'  # 添加区块类型时的名字
        block_type_new_cancel = 'css=.video-block-top .rz-button--info'  # 新增区块类型时的 取消 按钮
        block_type_new_confirm = 'css=.video-block-top .rz-button--primary'  # 新增区块类型时的 确定 按钮
        block_type_ele = 'xpath=//div[@class="tablist"]//span[text()="{}"]'  # 区块名
        block_type_more_ele = '%s/following-sibling::i' % block_type_ele  # 更多按钮
        block_type_more_edit = 'css=.video-block-top>.more-operation>li:first-child'  # 编辑
        block_type_more_del = 'css=.video-block-top>.more-operation>li:last-child'  # 删除
        # 区块新建
        block_new_name = 'css=input[placeholder="请输入区块名称"]'  # 新建区块， 名字input
        block_new_cancel = 'css=.control .rz-button--info:nth-of-type(2)'  # 新建区块， 取消/上一步按钮
        block_new_confirm = 'css=.control .rz-button--primary'  # 新建区块， 确认/下一步按钮
        block_new_camera_label = 'css=.videolist label'  # 新建区块，选择视频源处
        # 区块删除
        block_del_cancel_btn = 'css=.video-side>div:last-child .rz-button--info'  # 删除区块， 取消 按钮
        block_del_confirm_btn = 'css=.video-side>div:last-child .rz-button--primary'  # 删除区块， 确认 按钮
        # 区块编辑
        block_edit_basic_info = 'css=.view-steps>div:first-child'  # 区块编辑时，基本信息
        block_edit_camera_info = 'css=.view-steps>div:last-child'  # 区块编辑时 视频源信息
        #
        block_export_btn = 'css=.icon-export'  # 区块 导出按钮
        block_import_btn = 'css=.lines+div>.icon-import'  # 区块 导入按钮

