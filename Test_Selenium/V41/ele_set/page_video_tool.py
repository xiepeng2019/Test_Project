#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class OneToOnePageEle:
    """
    1:1
    """
    #
    one_to_one_into_btn = 'css=img[alt="照片一比一"]'
    #
    left_file_ele = 'css=.images>div:first-child input'
    left_img_site_ele = 'css=.images>div:first-child .rz-upload-dragger'
    left_lib_btn = 'css=.images>div:first-child .tip'
    right_file_ele = 'css=.images>div:nth-of-type(3) input'
    right_img_site_ele = 'css=.images>div:nth-of-type(3) .rz-upload-dragger'
    right_lib_btn = 'css=.images>div:nth-of-type(3) .tip'
    pk_btn = 'css=.result+.rz-button--primary'
    result_txt = 'css=.result>.content'
    export_btn = 'css=.icon-export'
    # 人像库选择人像
    alert_lib_ele = 'css=.tabs>div:last-child'
    # alert_lib_ele = 'css=.images-list-wrap div.rz-image-card'   # 取人像列表中第一个图片
    all_img_ele = 'css=.rz-scrollbar__view .rz-image-card'  # 人像列表
    cancel_btn = 'css=.dialog-footer .rz-button--info'
    confirm_btn = 'css=.dialog-footer .rz-button--primary'
    keyword_ipt = 'css=input[placeholder="请输入姓名/身份ID"]'