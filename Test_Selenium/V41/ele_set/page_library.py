#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class LibraryPageEle:
    text_dict = {"library_alert": "新建布控库", "library_static": "新建静态库", "library_alert_name": "请输入布控库名称",
                 "library_static_name": "请输入静态库名称", "library_search": "请输入库名/备注", "portrait_name": "请输入姓名",
                 "portrait_identity_id": "请输入证件号", "portrait_gender": "请输入性别", "portrait_date": "请输入日期",
                 "library_next_step": "下一步", "library_confirm": "确定", "library_manage": "人像管理",
                 "library_look": "查看", "library_update": "编辑", "library_del": "删除", "save": "保存",
                 "alert_button": "布控库", "static_button": "静态库", "portrait_search": "请输入姓名/身份ID",
                 "identity": "身份", "remark": "备注", "por_remark": "非必填", "input_remark": "请输入备注",
                 "attribute_name": "请输入属性名称", "attribute_info": "请输入描述", "por_sort": "人像数",
                 "create_time_sort": "创建时间", "update_time_sort": "更新时间", "por_gender": "性别", "por_age": "年龄",
                 "por_census": "户籍"}
    library_type_button = "xpath=//div[@class='lib-tabs']/div[text()='{}']"  # 布控库
    create_library_button = "xpath=//div[@class='lib-tabs']/button[@class='rz-button create rz-button--primary']/span[text()='{}']"  # 新建库:新建布控库
    library_portrait_name = "xpath=//input[@autocomplete='off' and @placeholder='{}']"  # 库名称:请输入布控库名称、请输入库名/备注、
                    # 请输入姓名、请输入证件号、请输入性别、请输入日期、请输入姓名/身份ID、请输入属性名称、请输入描述
    library_remark = "xpath=//textarea[@class='rz-textarea__inner' and @placeholder='请输入']"  # 库备注
    library_assist_button = "xpath=//button[@class='rz-button rz-button--primary']/span[text()='{}']"  # 下一步按钮:下一步、确定、点击删除后确定按钮、保存
    library_manage = "xpath=//div[@class='table-operations']/span[text()='{}']"  # 库管理按钮: 人像管理、查看、编辑、删除
    library_search_button = "xpath=//i[@class='rz-search-input-suffix rz-icon-search']"  # 库搜索按钮
    library_list_button = "xpath=//div[@class='tarLibName']/span[@class='title rz-tooltip']"  # 库列表
    library_count_button = "xpath=//div[@class='counts']/span[@class='libTotal']"  # 库个数
    library_create_attribute = "xpath=//button[@class='rz-button addAttr rz-button--primary']/span"  # 新建属性
    library_attribute = "xpath=//span[@class='rz-radio__input']/span[@class='rz-radio__inner']"  # 库属性
    library_attribute_del = "xpath=//button[@class='rz-button operation rz-button--text is-primary-text']/span"  # 库属性删除
    library_del_confirm = "xpath=//button[@class='rz-button rz-button--primary rz-button--primary ']/span"  # 库属性删除确定按钮
    library_sort_button = "xpath=//div[text()='{}']/span[@class='caret-wrapper']/i[@class='sort-caret descending']"  # 库排序按钮:人像数、创建时间、更新时间
    library_sort = "xpath=//table[@class='rz-table__body']/tbody/tr/td[{}]"  # 库排序

    portrait_add_button = "xpath=//button[@class='rz-button add-protrait rz-button--primary']/span[text()='添加人像']"  # 添加人像
    portrait_upload_button = "xpath=//div[@class='rz-upload-slot']/i[@class='rz-icon-plus']"  # 上传
    portrait_import_button = "xpath=//button[@class='rz-button import-button rz-button--text']/span[text()='导入']"  # 导入
    portrait_cancel_button = "xpath=//button[@class='rz-button rz-button--info']/span[text()='取消']"  # 取消
    portrait_count_button = "xpath=//div[@class='portrait-total']/span"  # 人像个数
    portrait_static_count = "xpath=//div[@class='operation']//span"  # 静态人像个数
    portrait_sum_button = "xpath=//span[@class='total']"  # 人像总数
    portrait_list_button = "xpath=//div[@class='content']/p[@class='name']"  # 人像列表
    portrait_id_remark = "xpath=//ul[@class='rz-dropdown-menu rz-popper']/li[text()='{}']"  # 身份、备注
    portrait_id_down = "xpath=//div[@class='rz-dropdown']/span[@class='rz-dropdown-link rz-dropdown-selfdefine']"  # 身份、备注下拉
    portrait_update_button = "xpath=//button[@class='rz-button rz-button--primary']/span[text()='编辑']"  # 人像编辑
    portrait_del_button = "xpath=//button[@class='rz-button rz-button--info']/span[text()='删除']"  # 人像删除
    portrait_confirm_del = "xpath=//button[@class='rz-button rz-button--primary rz-button--medium']/span[text()='删除']"  # 人像确定删除
    portrait_back_button = "xpath=//button[@class='rz-button flex-middle back-btn rz-button--text rz-button--medium']/span[text()='返回']"  # 返回到库界面
    portrait_x_button = "xpath=/html/body/div[1]/div[1]/main/div/div[2]/div[1]/div[3]/div/div/div[1]/button/i"  # 编辑后点击X
    portrait_gender = "xpath=//ul[@class='rz-scrollbar__view rz-select-dropdown__list']/li/span"  # 人像性别
    portrait_census = "xpath=//div[@class='rz-form-item__content']/span[@class='rz-cascader input-item rz-cascader--medium']"  # 人像户籍
    portrait_address = "xpath=//div[@class='rz-scrollbar__view']/li/span[text()]"  # 人像地址
    portrait_area = "xpath=//div[@class='rz-scrollbar__view']/li[@class='rz-cascader-menu__item']/span"  # 人像区域
    portrait_select_button = "xpath=//span[text()='{}']/..//input[@autocomplete='off']"  # 人像筛查
    portrait_census_select = "xpath=//span[@class='rz-cascader filter-select rz-cascader--small']/span[@class='rz-cascader__label']"  # 人像户籍筛查
    portrait_select_confirm = "xpath=//button[@class='rz-button rz-button--text is-primary-text']/span[text()='确定']"  # 人像筛查确定
    portrait_select_verify = "xpath=//div[text()='{}']/../div[@class='item-value']"  # 人像筛查校验