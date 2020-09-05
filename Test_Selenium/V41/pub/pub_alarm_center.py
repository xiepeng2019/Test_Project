#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from common import common_func
from sc_common.sc_define import TaskDefine, define_camera
from common.common_func import shadow
from v43.pub.pub_base import PublicClass
import time
from sc_common.sc_define import ResDefine
from v43.ele_set.page_alarm_center import AlarmCenterPageEle


class AlarmCenterAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = AlarmCenterPageEle
        self.of = TaskDefine
        self.df = define_camera

    @shadow("告警中心-切换功能页")
    def switch_function_page(self, function="全部", map=False):
        if not self.driver.ele_exist(self.el.function_list.format(typo="1")):
            self.log.warning("厂家设置未开启人群功能，无功能页")
            return True
        typo = ""
        if function == "全部":
            typo = "1"
        elif function == "布控":
            typo = "2"

        elif function == "人群":
            typo = "3"
        if not typo:
            self.log.error("请输入正确的模块名")
            return False
        self.driver.ele_click(self.el.function_list.format(typo=typo))
        if map:
            self.driver.ele_click(self.el.map_or_list.format(typo="2"))
        return True

    @shadow("告警中心-任务告警推送筛选任务")
    def screen_task(self, tasknames):
        tasknames = common_func.convert_to_array(tasknames)
        if not tasknames:
            return
        self.driver.ele_click(self.el.task_push_list)
        self.driver.ele_click(self.el.all_choose)
        for task in tasknames:
            self.driver.ele_input(self.el.search_task_push_list, input_value=task, enter=True)
            self.driver.chk_loading()
            self.driver.ele_click(self.el.all_choose)
        self.driver.ele_click(self.el.save)
        self.wid.wid_chk_loading()
        if self.driver.ele_exist(self.el.close_essage):
            self.driver.ele_click(self.el.close_essage)
        # self.driver.ele_click(self.el.close_essage)
        return True

    @shadow("告警中心-设置沉默时间")
    def alarm_center_silence_setting(self, start_time=None, end_time=None, reason="test"):
        """
        告警目标详情-设置沉默时间
        :param start_time: 时间格式：2020-03-18 00:00:00 年月日与时分秒中间必须包含空格
        :param end_time: 时间格式：2020-03-19 00:00:00 年月日与时分秒中间必须包含空格
        :param reason: 备注
        :return:
        """
        self.driver.click_xpath(self.el.silence_set)
        self.wid.wid_slt_date(start_time=start_time, end_time=end_time, module="silence")
        if reason:
            self.driver.input_xpath(self.el.silence_reason_input, reason)
        self.driver.click_xpath(self.el.silence_ensure)

    @shadow("告警中心-布控设置告警推送区域")
    def alarm_push_region(self, task_name=None, videos=None, push_typo="1"):
        self.driver.ele_click(self.el.push_setting)
        if push_typo == "1":
            self.driver.ele_click(self.el.push_setting_title.format(typo="告警推送区域"))
        elif push_typo == "2":
            self.driver.ele_click(self.el.push_setting_title.format(typo="声音提示"))
        if task_name:
            self.driver.ele_input(self.el.task_input.format(typo=push_typo), task_name, enter=True)
        self.driver.ele_click(self.el.task_push_set.format(task_name=task_name))
        self.wid.wid_chk_loading()
        camera_lst = common_func.convert_to_array(videos)
        if not camera_lst:
            return
        time.sleep(1)
        self.driver.ele_click(self.el.alarm_video_all_choose)
        for camera_ in camera_lst:
            self.driver.ele_input(self.el.video_input, input_value=camera_, enter=True)
            time.sleep(2)
            self.driver.ele_click(self.el.alarm_video_all_choose)
        self.driver.chk_loading()
        self.driver.ele_click(self.el.alarm_push_select_video_button, load=True)
        # self.driver.click_xpath(self.el.video_button)
        return True

    @shadow("告警中心-点击布控告警卡片")
    def get_alarm_details(self):
        if not self.driver.ele_exist(self.el.first_alarm):
            self.log.error("未产生告警推送，请检查环境")
            return False
        self.driver.ele_click(self.el.first_alarm)
        self.wid.wid_chk_loading()
        return True

    @shadow("告警中心-历史告警排序方式")
    def history_alarm_sort(self, typo=1):
        self.wid.wid_chk_loading()
        self.driver.ele_move(self.el.history_alarm_sort, timeout=2)
        self.driver.ele_click(self.el.history_alarm_sort_op.format(typo=typo), wait_time=3)
        return True

    @shadow("告警中心-历史告警过滤")
    def history_alarm_filter(self, task_name=False, videos=None, librarys=None, similar_number=None,
                             identity_attribute=False, gender=None,
                             age=None,
                             search_info=None, only_pitch=False):
        """
         根据输入条件获取布控告警列表
         :param videos: list 选择查询的视频源列表名称
         :param librarys: list 选择查询的人像库列表名称
         :param similar_number: 相似度
         :param identity_attribute: 身份属性
         :param gender: 性别 与identity_attribute配合使用 不限，男，女
         :param age:年龄段 与identity_attribute配合使用 儿童，青年，中年，老年
         :param search_info:搜索内容
         :param only_pitch: 是否只看比中
         :return:
         """
        self.driver.chk_loading()
        # 因默认时间为1970, 需加时间过滤，  csf add it 20200506
        self.wid.wid_slt_date(start_time=self.cf.get_delta_time(days=-7), end_time=self.cf.get_delta_time())
        #
        if videos:
            camera_lst = common_func.convert_to_array(videos)
            if not camera_lst:
                return
            self.driver.ele_click(self.el.history_video_button)
            self.wid.wid_chk_loading()
            self.driver.ele_click(self.el.alarm_video_all_choose)
            for camera_ in camera_lst:
                self.driver.ele_input(self.el.video_input, input_value=camera_, enter=True)
                self.driver.chk_loading()
                self.driver.ele_click(self.el.alarm_video_all_choose)
            self.driver.ele_click(self.el.video_button_ensure)
        # if librarys:
        #     librarys = common_func.convert_to_array(librarys)
        #     if not librarys:
        #         return
        #     self.driver.click_xpath(self.el.lib_list)
        #     self.driver.chk_loading()
        #     self.driver.click_xpath(self.el.lib_cansel_selected)
        #     self.driver.chk_loading()
        #     for lib in librarys:
        #         self.driver.input_xpath(self.el.lib_input, lib)
        #         self.driver.click_xpath(self.el.lib_other)
        #         self.driver.click_xpath(self.el.lib_button)
        #         self.driver.chk_loading()
        #         self.driver.click_xpath(self.el.lib_cansel_selected)
        #     self.driver.click_xpath(self.el.lib_save)
        if similar_number:
            self.driver.chk_loading()
            self.driver.ele_click(self.el.similar)
            self.driver.chk_loading()
            self.driver.ele_input(self.el.similar_input, similar_number)
        if identity_attribute:
            self.driver.chk_loading()
            self.driver.click_xpath(self.el.id_attribute)
            if gender:
                if gender not in ["不限", "男", "女"]:
                    self.driver.log.error("请输入正确的性别")
                    return False
                self.driver.click_xpath(self.el.gender_input)
                self.driver.chk_loading()
                self.driver.click_xpath(self.el.gender_age_input.format(typo=gender))
            if age:
                if age == "儿童":
                    age = "儿童(0 ~ 14)"
                elif age == "青年":
                    age = "青年(15 ~ 28)"
                elif age == "中年":
                    age = "中年(29 ~ 60)"
                elif age == "老年":
                    age = "老年(>60)"
                else:
                    self.log.error("请输入正确的年龄段")
                    return False
                self.driver.click_xpath(self.el.age_input)
                self.driver.chk_loading()
                self.driver.click_xpath(self.el.gender_age_input.format(typo=age))

        # self.driver.ele_click(self.el.sure_button)
        if search_info:
            self.driver.chk_loading()
            self.driver.input_xpath(self.el.target_input, search_info)
            self.driver.click_enter_key()
        if only_pitch:
            self.driver.chk_loading()
            self.driver.click_xpath(self.el.only_check_than_in_the)
        self.wid.wid_chk_loading()
        self.driver.ele_click(self.el.sure_button)
        if task_name:
            self.driver.ele_input(self.el.history_task_input, input_value=task_name, cln=3, enter=True)
            self.wid.wid_chk_loading()
        return True
