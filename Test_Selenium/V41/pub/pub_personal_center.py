#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from v43.ele_set.page_personal_center import PersonalCenterPageEle
from v43.pub.pub_base import PublicClass
from common.common_func import shadow


class PersonalCenterAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = PersonalCenterPageEle

    @shadow("个人中心-进入指定的个人中心page")
    def into_my_center(self, page_name):
        """
        进入指定的个人中心page

        :param page_name: 个人中心的某一页面名称: 全部事项，我的收藏，个人信息
        :return:
        """
        self.wid.wid_chk_loading()
        self.driver.ele_click(self.el.all_title_typo.format(page_name), load=True)
        # if page_name == '全部事项':
        #     self.driver.click_xpath(self.el.all_title_typo.format(1))
        # elif page_name == '我的收藏':
        #     self.driver.click_xpath(self.el.all_title_typo.format(3))
        # elif page_name == '个人信息':
        #     self.driver.ele_click(self.el.all_title_typo.format(3))
        return True


class PersonalCenterPage(PersonalCenterAction):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)

    @shadow("个人中心-选择我的收藏中各种类型的检索")
    def into_my_collection(self, collection_type):
        """
        个人中心-选择我的收藏中各种类型的检索
        :return:
        """
        self.driver.ele_click(self.el.all_title_typo.format("我的收藏"))
        self.wid.wid_chk_loading()
        if collection_type == "人脸检索":
            self.driver.ele_click(self.el.all_collection.format("1"), wait_time=3)
        elif collection_type == "行人检索":
            self.driver.ele_click(self.el.all_collection.format("2"), wait_time=3)
        elif collection_type == "车辆检索":
            self.driver.ele_click(self.el.all_collection.format("3"), wait_time=3)
        elif collection_type == "身份检索":
            self.driver.ele_click(self.el.all_collection.format("4"), wait_time=3)
        else:
            self.driver.ele_click(self.el.all_collection.format("5"), wait_time=3)
        self.wid.wid_chk_loading()
        return True

    @shadow("个人中心-编辑个人信息")
    def into_user_info(self, is_editor_user=False, name="test", police_number=None,
                       phone_number=None, is_ensure=True):
        """
        个人中心-编辑个人信息
        :return:
        """
        self.wid.wid_chk_loading()
        if is_editor_user:
            self.driver.ele_click(self.el.editor_user)
            if name:
                self.driver.ele_input(self.el.user_info_input.format(typo=2), name)
            if police_number:
                self.driver.ele_input(self.el.user_info_input.format(typo=5), police_number)
            if phone_number:
                self.driver.ele_input(self.el.user_info_input.format(typo=6), phone_number)
            if is_ensure:
                self.driver.ele_click(self.el.ensure_editor_user)
            else:
                self.driver.ele_click(self.el.cancel_editor_user)
        return True

    @shadow("个人中心-修改密码")
    def change_password(self, old_password, new_password, is_ensure=True):
        """
        个人中心-修改密码
        :return:
        """
        self.driver.ele_click(self.el.change_password)
        self.driver.ele_input(self.el.input_old_password, old_password)
        self.driver.ele_input(self.el.input_new_password, new_password)
        self.driver.ele_input(self.el.again_input_new_password, new_password)
        if is_ensure:
            self.driver.ele_click(self.el.ensure_editor_password)
        else:
            self.driver.ele_click(self.el.cancel_editor_password)
        return True

    @shadow("个人中心-我的收藏，进入各个收藏的检索结果收藏详情")
    def retrieve(self, collection_type, cancel_col=False, export=False, check_track=False,
                 result_detail=False, is_ensure=False):
        """
        个人中心-我的收藏，进入各个收藏的检索结果收藏详情
        :return:
        """
        self.into_my_collection(collection_type=collection_type)
        eles = self.driver.ele_list(self.el.collection_image)
        if not eles:
            return False
        self.driver.ele_click(eles[-1])
        assert self.driver.ele_get_val(self.el.collection_detail) == '详情', '进入详情失败'
        if result_detail:
            self.driver.ele_click(self.el.collection_search_result)
            assert self.driver.ele_get_val(self.el.result_detail_text) == '结果详情', '查看结果详情失败'
            ele_list = self.driver.ele_list(self.el.result_detail_operate_list)
            assert len(ele_list) == 6, '结果详情操作列表不为6个'
            self.driver.ele_click(self.el.result_detail_close)
        if export:
            self.driver.ele_click(self.el.export_image)
        if collection_type != "身份检索":
            if check_track:
                self.driver.ele_click(self.el.track)
                assert self.driver.ele_get_val(self.el.track_text) == '查看轨迹', '进入查看轨迹失败'
        if cancel_col:
            self.driver.ele_click(self.el.cancel_collection)
            if is_ensure:
                self.driver.ele_click(self.el.ensure_button)
            else:
                self.driver.ele_click(self.el.cancel_button)
        return True

    @shadow("个人中心-全部事项")
    def all_matter(self, name, details=False, is_approval=False, is_pass=True, idea_input=""):
        """
        个人中心-全部事项
        :return:
        """
        self.driver.ele_input(self.el.search_task_input, name)
        self.driver.ele_click(self.el.search_task_button)
        if details:
            self.driver.ele_click(self.el.task_details)
        if is_approval:
            if is_pass:
                self.driver.ele_click(self.el.task_pass)
            else:
                self.driver.ele_click(self.el.task_rejected)
            if idea_input:
                self.driver.ele_input(self.el.idea_input, idea_input)
            self.driver.ele_click(self.el.idea_ensure_button)
            self.wid.wid_get_alert_label()
        return True

    @shadow('个人中心-全部事项, 编辑审核不通过任务')
    def edit_task_that_no_pass(self, name, new_name=None, new_precise_num=None, app_reason=None):
        """
        :param name:  目标任务名
        :param new_name:  新的任务名
        :param new_precise_num:   新的精准预置
        :param app_reason:   申请理由
        :return:
        """
        self.all_matter(name=name, details=True)
        self.driver.ele_click(self.el.detail_edit_button)
        self.wid.wid_first_use_alert()
        if new_name:
            self.driver.ele_input(self.el.task_name_input, name)
        if new_precise_num:
            self.driver.ele_input(self.el.accurate_alarm_input, new_precise_num)
        self.driver.ele_click(self.el.edit_save_submit_button)
        if app_reason:
            self.driver.ele_input(self.el.app_reason_input, app_reason)
        self.driver.ele_click(self.el.edit_ensure_button)
        return self.wid.wid_get_alert_label(return_msg='编辑成功')

    @shadow('个人中心-全部事项, 过滤筛选任务事项')
    def filter_search_event(self, source=None, status=None, task_name=None):
        """
        :param source:  来源: 我创建的、我审核的
        :param status:  状态:
        :param task_name: 任务名
        :return:
        """
        if source:
            self.wid.wid_drop_down(source, trig_wid=self.el.source)
        if status:
            self.wid.wid_drop_down(status, self.el.status)
        if task_name:
            self.driver.ele_input(self.el.search_task_input, task_name, enter=True)
        return self.driver.ele_list(self.el.filter_task_list)

    def person_search_favourite(self, search_type=None):
        fav_lst = self.driver.ele_list(self.el.collection_image_info)
        self.driver.ele_click(fav_lst[0])
        #
        tst_img_lst = self.driver.ele_list(self.el.collection_image_info)[:3]
        for tst_img in tst_img_lst:
            self.driver.ele_click(tst_img)
            if search_type != 'lib':
                if not self.wid.verify_capture_tool():
                    self.log.error("抓拍图 工具测试失败")
                    return False
            else:
                capture_exist = self.driver.ele_exist("css=div.pop-up")
                self.driver.ele_click(self.wid.el.CaptureTool.capture_close)
                if not capture_exist:
                    self.log.error("比中的 库图片详情检查失败")
                    return False
        # 查看轨迹
        if search_type != 'lib':
            self.driver.ele_click(self.el.top_menu.format("查看轨迹"), load=True)
            self.driver.ele_click(self.driver.ele_list("css=.image-title")[0], load=True)

            plus_el = "css=i.rz-icon-plus"
            for _ in range(6):
                self.driver.ele_click(plus_el)
            self.driver.ele_click("css=.search-map-image+div.active", load=True)
            trace_dot_camera_lst = 'css=.search-map-camera-info--name>span'
            camera_lst = self.driver.ele_list(trace_dot_camera_lst)
            if camera_lst:
                self.driver.ele_click(camera_lst[0])
            com_el = '//div[contains(@class,"top-tab")][text()="{}"]'
            for x in ["抓拍记录", "附近的地点"]:
                if not self.driver.ele_exist(com_el.format(x)):
                    self.log.error("收藏中，查看轨迹失败")
                    return False
            self.wid.wid_return_page()
            time.sleep(0.5)
            self.wid.wid_return_page()
            time.sleep(0.5)
        # 导出
        before_date = int(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        self.driver.ele_click(self.el.top_menu.format("导出比中"))
        if not self.wid.wid_task_tip(wait_miss=True):
            self.log.error("收藏中，导出比中失败")
            return False
        last_dl = self.wid.verify_dl()
        now_date = int(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        export_date = self.cf.get_num_from_str(last_dl['name'])
        # self.log.error('now date is {}, export date is {}, export before date is {}'.format(now_date, export_date, before_date))
        if not last_dl or not (now_date >= export_date >= before_date):  # 待增加判定 收藏记录_20200508_200109.zip
            self.log.error("收藏中，导出比中 检查失败")
            self.log.error('now date is {}, export date is {}, export before date is {}'.format(now_date, export_date,
                                                                                                before_date))
            return False
        # 取消收藏
        self.driver.ele_click(self.el.top_menu.format("取消收藏"))
        confirm_btn = self.el.cancel_fav_confirm_btn.format("确定")
        # if self.driver.ele_exist(confirm_btn):
        self.driver.ele_click(confirm_btn, load=True)
        now_fav_lst = self.driver.ele_list(self.el.collection_image_info) or []
        if not (len(now_fav_lst) + 1 == len(fav_lst)):
            self.log.error("取消比中收藏后，收藏数量未减少")
            return False
        return True



