# !/usr/bin/python3.7
# -*- coding: utf-8 -*-
import time

from common.common_func import shadow
from sc_common.sc_define import define
from v43.ele_set.page_video_tool import OneToOnePageEle
from v43.pub.pub_base import PublicClass
from common import common_func as CF


class OneToOneAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = OneToOnePageEle
        self.df = define()

    def slt_img_from_lib(self, lib_img=None):
        self.driver.ele_click(self.el.alert_lib_ele, load=True)
        if lib_img:
            self.driver.ele_input(self.el.keyword_ipt, lib_img, enter=True, load=True)
        all_cap_lst = self.driver.ele_list(self.el.all_img_ele)
        all_cap_lst[0].click()
        self.driver.ele_click(self.el.confirm_btn)

    def slt_left_img(self, img=None, lib_img=None):
        if img and '.' in img:
            self.driver.ele_upload(img_path=self.df.get_file(img), ele=self.el.left_file_ele)
        else:
            self.driver.ele_move(self.el.left_img_site_ele)
            self.driver.ele_click(self.el.left_lib_btn)
            self.slt_img_from_lib(lib_img=lib_img)

    def slt_right_img(self, img=None, lib_img=None):
        if img and '.' in img:
            self.driver.ele_upload(img_path=self.df.get_file(img), ele=self.el.right_file_ele)
        else:
            self.driver.ele_move(self.el.right_img_site_ele)
            self.driver.ele_click(self.el.right_lib_btn)
            self.slt_img_from_lib(lib_img=lib_img)

    def into_one_to_one(self):
        self.driver.ele_click(self.el.one_to_one_into_btn, load=True)


class VideoToolModule(OneToOneAction):

    @shadow("1：1比对")
    def img_pk(self, left_img=None, right_img=None):
        self.slt_left_img(img=left_img)
        self.slt_right_img(img=right_img)
        self.driver.ele_click(self.el.pk_btn, load=True)
        rst_txt = self.driver.ele_get_val(self.el.result_txt)
        self.log.warning(rst_txt)
        return rst_txt

    def export_pk(self):
        self.driver.ele_click(self.el.export_btn)