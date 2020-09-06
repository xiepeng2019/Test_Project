#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = "huangyongchang"

from v43.ele_set.page_tactics import TacticsEle
from v43.pub.pub_menu import MainPage
from v43.pub.pub_base import PublicClass
from common.common_func import *
from v43.pub.pub_widget import WidPub
from common import common_func as CF
from v43.pub.pub_camera import CameraModule
from sc_common.sc_define import CameraDefine


class TacticsCommonMethod(PublicClass):
    def __init__(self, web_driver, **kwargs):
        super(TacticsCommonMethod, self).__init__(web_driver, **kwargs)
        self.wide_pub = WidPub(web_driver, **kwargs)
        self.tactics_ele = TacticsEle
        self.video_obj = CameraModule(web_driver=web_driver, **kwargs)

    def select_video(self, camera_lst=None, trig_wid=None, click_confirm=True):
        """
        选择视频源
        :param camera_lst:  视频源名字 支持一个或多个
        :param trig_wid:  触发此控件的元素
        :param click_confirm:  确定
        :return:
        """
        camera_lst = CF.convert_to_array(camera_lst)
        if not camera_lst:
            return
        if trig_wid:
            time.sleep(0.5) if not self.driver.ele_exist(trig_wid) else None
            self.driver.ele_click(trig_wid)
        self.driver.ele_click(self.tactics_ele.VideoSelectEle.camera_page_cam_tree)
        self.wide_pub.wid_drop_down("视频源", self.tactics_ele.VideoSelectEle.search_type_cate)
        ele_list = self.driver.ele_list(self.tactics_ele.VideoSelectEle.camera_search_fr)
        for camera_ in camera_lst:
            self.driver.ele_input(ele_list[-1], input_value=camera_, enter=True)
            self.driver.chk_loading()
            check_box_el = self.tactics_ele.VideoSelectEle.camera_check_box.format(camera_)
            if 'is-check' not in self.driver.ele_get_val(check_box_el, 'class', chk_visit=False):
                self.driver.ele_click(check_box_el)
        if click_confirm:
            ele_list = self.driver.ele_list(self.tactics_ele.VideoSelectEle.camera_confirm_btn)
            self.driver.ele_click(ele_list[-1])

    def select_date_time(self, widget_ele=None, start_datetime=None, end_datetime=None):
        """
        选择日期时间
        :param widget_ele: 时间控件元素
        :param start_datetime:
        :param end_datetime:
        :return:
        """
        widget_ele = widget_ele or self.tactics_ele.VideoSelectEle.datetime_widget
        self.driver.ele_click(widget_ele)
        self.driver.ele_input(self.tactics_ele.VideoSelectEle.datetime_start.format(widget_ele), start_datetime)
        self.driver.ele_input(self.tactics_ele.VideoSelectEle.datetime_end.format(widget_ele), end_datetime)
        ele_list = self.driver.ele_list(self.tactics_ele.VideoSelectEle.datetime_confirm_btn)
        self.driver.ele_click(ele_list[-1])

    def into_second_page(self, menu_name):
        """
        进入二级页面
        :param menu_name:
        :return:
        """
        self.driver.ele_click(self.tactics_ele.level_one_menu.format(menu_name))

    def into_third_page(self, menu_name):
        """
        进入三级页面
        :param menu_name:
        :return:
        """
        self.driver.ele_click(self.tactics_ele.level_second_menu.format(menu_name))

    def create_often_pass_task(self, task_name=None, start_datetime=None, end_datetime=None, place=None,
                               appear_times=None,
                               select_lib=None, exclude_lib=None, case_num=None, remark=None):
        """
        创建频繁过人任务
        :param task_name:    案件名称
        :param start_datetime:   起始时间
        :param end_datetime:     结束时间
        :param place:        选择视频源，以列表的形式可传入多个
        :param appear_times: 出现次数
        :param select_lib:   选择库，以列表的形式可传入多个，
        :param exclude_lib:  排除库，以列表的形式可传入多个
        :param case_num:     案件编号
        :param remark:       备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('频繁过人'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.wide_pub.wid_slt_date(start_datetime, end_datetime, module="tactics_time")
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('出现次数阈值(次)'), appear_times)
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def into_case_detail(self, case_name, column="last()"):
        self.find_tactics_task(case_name=case_name)
        self.driver.ele_click(self.tactics_ele.CaseDetail.view_detail.format(case_name, column))
        val_msg = self.driver.ele_get_val(self.tactics_ele.CaseDetail.case_name, chk_visit=True)
        assert case_name in val_msg, "档案名称不正确"
        val_msg = self.driver.ele_get_val(self.tactics_ele.CaseDetail.case_detail_text)
        assert "任务详情" in val_msg, '进入任务详情失败'

    def view_task_result(self, task_name, column="last()"):
        """
        查看结果
        :param task_name:
        :param column:  列数，在第几列
        :return:
        """
        self.find_tactics_task(case_name=task_name)
        self.driver.ele_click(self.tactics_ele.CaseDetail.view_result.format(task_name, column), load=True)
        val_msg = self.driver.ele_get_val(self.tactics_ele.CaseDetail.case_name, chk_visit=False)
        assert task_name in val_msg, "档案名称不正确"

        conunt = 1;
        while not self.driver.ele_exist(self.tactics_ele.CaseDetail.result_detail):
            conunt = conunt + 1
            time.sleep(10)
            self.driver.refresh_driver()
            if conunt == 20:
                assert False, "任务详情页未查找到相关信息"

    def create_space_time_filter_case_task(self, task_name=None, start_datetime=None, end_datetime=None, place=None,
                                           select_lib=None, exclude_lib=None, case_num=None, remark=None):
        """
        创建时空过滤任务
        :param task_name:   案件名称
        :param start_datetime:  起始时间
        :param end_datetime:    结束时间
        :param place:       选择视频源，以列表的形式可传入多个
        :param select_lib:  选择库，以列表的形式可传入多个，
        :param exclude_lib: 排除库，以列表的形式可传入多个
        :param case_num:    案件编号
        :param remark:      备注
        :return:
                """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('时空档案过滤'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.wide_pub.wid_slt_date(start_datetime, end_datetime, module="tactics_time")
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def create_day_hide_night_out(self, task_name=None, start_datetime=None, end_datetime=None, place=None,
                                  appear_days=None, night_start_time=None, night_end_time=None,
                                  select_lib=None, exclude_lib=None, case_num=None, remark=None):
        """
        创建走伏夜出任务
        :param task_name:    案件名称
        :param start_datetime:   起始时间
        :param end_datetime:     结束时间
        :param place:        选择视频源，以列表的形式可传入多个
        :param appear_days:  夜出天数(天)
        :param night_start_time:  夜出起始时间，例如 17:00:00
        :param night_end_time:    夜出结束时间，例如 04:00:00
        :param select_lib:   选择库，以列表的形式可传入多个，
        :param exclude_lib:  排除库，以列表的形式可传入多个
        :param case_num:     案件编号
        :param remark:       备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('昼伏夜出'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.wide_pub.wid_slt_date(start_datetime, end_datetime, module="tactics_time")
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('夜出天数(天)'), appear_days)
        self.wide_pub.wid_slt_time(night_start_time, night_end_time)
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def create_time_space_crash(self, task_name=None, time_space_list=None, crash_times=None,
                                select_lib=None, exclude_lib=None, case_num=None, remark=None):
        """
        创建时空碰撞任务
        :param task_name:    案件名称
        :param time_space_list: 时空碰撞列表,至少两个时空信息，传入形式： [{'video_list': ['视频源1'], "start_time": "2020-04-08 14:49:30", "end_time": "2020-04-15 14:49:30"},
                                                                {'video_list': ['视频源2'], "start_time": "2020-04-08 14:49:30", "end_time": "2020-04-15 14:49:30"}]
        :param crash_times:  碰撞阈值
        :param select_lib:   选择库，以列表的形式可传入多个，
        :param exclude_lib:  排除库，以列表的形式可传入多个
        :param case_num:     案件编号
        :param remark:       备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('时空碰撞'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        if len(time_space_list) < 2:
            raise Exception("时空碰撞列表数量不足，至少两个")
        for i, time_space_info in enumerate(time_space_list):
            video_list = time_space_info['video_list']
            start_time = time_space_info['start_time']
            end_time = time_space_info['end_time']
            if i > 1:
                self.driver.ele_click(self.tactics_ele.add_ts_crash_info)
            self.select_date_time(start_datetime=start_time, end_datetime=end_time,
                                  widget_ele=self.tactics_ele.VideoSelectEle.datetime_widget.format(i + 1))
            self.select_video(camera_lst=video_list, trig_wid=self.tactics_ele.ts_crash_task_video_widget.format(i + 1))
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('碰撞阈值'), crash_times)
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def create_first_appear(self, task_name=None, first_appear_time=None, not_appear_time=None,
                            place=None, select_lib=None, exclude_lib=None, case_num=None, remark=None):
        """
        首次出现
        :param task_name:
        :param first_appear_time:  最早出现时间
        :param not_appear_time:  未出现时间范围：一个月 。。。。十二个月
        :param place:         选择视频源，以列表的形式可传入多个
        :param select_lib:    选择库
        :param exclude_lib:   排除库
        :param case_num:      案件编号
        :param remark:        备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('首次出现'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('最早出现时间点'), first_appear_time, enter=True)
        self.wide_pub.wid_drop_down(not_appear_time,
                                    trig_wid=self.tactics_ele.create_task_select_frame.format('未出现时间范围'), exact=True)
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def create_continue_appear(self, task_name=None, start_datetime=None, end_datetime=None, continue_days=None,
                               place=None, select_lib=None, exclude_lib=None, case_num=None, remark=None):
        """
        连续出现
        :param task_name:
        :param start_datetime:   起始时间
        :param end_datetime:     结束时间
        :param continue_days:  连续天数(天)
        :param place:         选择视频源，以列表的形式可传入多个
        :param select_lib:    选择库
        :param exclude_lib:   排除库
        :param case_num:      案件编号
        :param remark:        备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('连续出现'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.select_date_time(start_datetime=start_datetime, end_datetime=end_datetime,
                              widget_ele=self.tactics_ele.time_widget_input)
        self.wide_pub.wid_slt_date(start_datetime, end_datetime, module="tactics_time")
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('连续天数(天)'), continue_days)
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def create_identify_leave(self, task_name=None, start_datetime=None, end_datetime=None, miss_days=None,
                              place=None, select_lib=None, exclude_lib=None, case_num=None, remark=None):
        """
        感知离开
        :param task_name:
        :param start_datetime:   起始时间
        :param end_datetime:     结束时间
        :param miss_days:  消失天数(天)
        :param place:         选择视频源，以列表的形式可传入多个
        :param select_lib:    选择库
        :param exclude_lib:   排除库
        :param case_num:      案件编号
        :param remark:        备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('感知离开'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.select_date_time(start_datetime=start_datetime, end_datetime=end_datetime,
                              widget_ele=self.tactics_ele.time_widget_input)
        self.wide_pub.wid_slt_date(start_datetime, end_datetime, module="tactics_time")
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('连续消失天数(天)'), miss_days)
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def create_peer_analyze(self, task_name=None, file_id=None, start_datetime=None, end_datetime=None,
                            place=None, peer_time=None, peer_times=None, select_lib=None,
                            exclude_lib=None, case_num=None, remark=None):
        """
        同行人分析
        :param task_name:
        :param file_id:      选择档案编号
        :param start_datetime:   起始时间
        :param end_datetime:     结束时间
        :param peer_time:     前后同行时间(秒)
        :param peer_times:     同行次数阈值(次)
        :param place:         选择视频源，以列表的形式可传入多个
        :param select_lib:    选择库
        :param exclude_lib:   排除库
        :param case_num:      案件编号
        :param remark:        备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('同行人分析'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.driver.ele_click(self.tactics_ele.by_file_id_select)
        self.wid.wid_drop_down('档案ID', trig_wid=self.tactics_ele.ID_dropdown_el)
        self.driver.ele_input(self.tactics_ele.file_ip_input_fr, file_id)
        self.select_date_time(start_datetime=start_datetime, end_datetime=end_datetime,
                              widget_ele=self.tactics_ele.time_widget_input)
        self.wide_pub.wid_slt_date(start_datetime, end_datetime, module="tactics_time")
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('前后同行时间(秒)'), peer_time)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('同行次数阈值(次)'), peer_times)
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def create_accurate_peer(self, task_name=None, file_id=None, start_datetime=None, end_datetime=None,
                             place=None, peer_time=None, peer_times=None, select_lib=None,
                             exclude_lib=None, case_num=None, remark=None):
        """
        精准同行分析
        :param task_name:
        :param file_id:          选择档案编号
        :param start_datetime:   起始时间
        :param end_datetime:     结束时间
        :param peer_time:        前后同行时间(秒)
        :param peer_times:       同行次数阈值(次)
        :param place:            选择视频源，以列表的形式可传入多个
        :param select_lib:       选择库
        :param exclude_lib:      排除库
        :param case_num:         案件编号
        :param remark:           备注
        :return:
        """
        try_ele = self.driver.ele_exist(self.tactics_ele.level_second_menu.format('精准同行分析'))
        self.driver.ele_click(try_ele) if try_ele else None
        self.driver.ele_click(self.tactics_ele.create_task)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件名称'), task_name)
        self.driver.ele_click(self.tactics_ele.by_file_id_select)
        self.wid.wid_drop_down('档案ID', trig_wid=self.tactics_ele.ID_dropdown_el)
        self.driver.ele_input(self.tactics_ele.file_ip_input_fr, file_id)
        self.select_date_time(start_datetime=start_datetime, end_datetime=end_datetime,
                              widget_ele=self.tactics_ele.time_widget_input)
        self.wide_pub.wid_slt_date(start_datetime, end_datetime, module="tactics_time")
        self.select_video(camera_lst=place, trig_wid=self.tactics_ele.create_task_select_frame.format('地点'))
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('前后同行时间(秒)'), peer_time)
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('同行次数阈值(次)'), peer_times)
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('选择库'),
                                       select_lib) if select_lib else None
        self.wide_pub.wid_dep_tree_win(self.tactics_ele.create_task_select_frame.format('排除'),
                                       exclude_lib) if exclude_lib else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('案件编号'), case_num) if case_num else None
        self.driver.ele_input(self.tactics_ele.create_task_input_frame.format('备注'), remark) if remark else None
        self.driver.ele_click(self.tactics_ele.start_analyze)
        alter_msg = self.wide_pub.wid_get_alert_label(return_msg=True)
        assert "新建成功" == alter_msg, "弹窗提示不正确"

    def find_tactics_task(self, case_name=None, creator=None, case_num=None):
        """
        查询技战法任务
        :param case_name:
        :param creator:
        :param case_num:
        :return:
        """
        if case_name:
            self.wide_pub.wid_drop_down(val='案件名称', trig_wid=self.tactics_ele.search_type_list)
            self.driver.ele_input(self.tactics_ele.case_search_input, case_name, enter=True)
            if not self.driver.ele_exist(ele=self.tactics_ele.case_frame_detail.format(1, 1)):
                return False
            value = self.driver.ele_get_val(ele=self.tactics_ele.case_frame_detail.format(1, 1))
            if case_name in value:
                return value
            else:
                return False

        elif creator:
            self.wide_pub.wid_drop_down(val='创建人', trig_wid=self.tactics_ele.search_type_list)
            self.driver.ele_input(creator, self.tactics_ele.case_search_input, enter=True)
            value = self.driver.ele_get_val(ele=self.tactics_ele.case_frame_detail.format(1, 3))
            if creator in value:
                return value
            else:
                return False
        elif case_num:
            self.wide_pub.wid_drop_down(val='案件编号', trig_wid=self.tactics_ele.search_type_list)
            self.driver.ele_input(case_num, self.tactics_ele.case_search_input, enter=True)
            value = self.driver.ele_get_val(ele=self.tactics_ele.case_frame_detail.format(1, 2))
            if case_num in value:
                return value
            else:
                return False

    def view_result_detail(self, by_file_id=None, by_sort_num=None):
        """
        查看结果详情
        :param by_file_id:档案Id
        :param by_sort_num:排序序号
        :return:
        """
        if by_file_id:
            pass
        elif by_sort_num:
            self.driver.ele_move(self.tactics_ele.CaseDetail.detail_result_card.format(by_sort_num))
            time.sleep(0.5)
            self.driver.ele_click(self.tactics_ele.CaseDetail.result_detail.format(by_sort_num))
            val_msg = self.driver.ele_get_val(self.tactics_ele.CaseDetail.ResultDetail.result_detail_text,
                                              chk_visit=True)
            assert "结果详情" in val_msg, '进入结果详情失败'

    def view_file_detail(self, by_file_id=None, by_sort_num=None):
        """
        查看结果详情
        :param by_file_id:档案Id
        :param by_sort_num:排序序号
        :return:
        """
        if by_file_id:
            pass
        elif by_sort_num:
            self.driver.ele_move(self.tactics_ele.CaseDetail.detail_result_card.format(by_sort_num))
            time.sleep(0.5)
            self.driver.ele_click(self.tactics_ele.CaseDetail.file_detail.format(by_sort_num))
            time.sleep(5)
            self.driver.select_window(window_num=2)
            time.sleep(5)
            val_msg = self.driver.ele_get_val(self.tactics_ele.CaseDetail.FileDetail.file_detail_text, chk_visit=True)
            assert "档案详情" in val_msg, '进入档案详情失败'

    def pre_tactics_task(self, tactic_type="通用技战法", task_type=None, if_new_task=False):
        task_name = "UI{}_{}预置任务{}".format(tactic_type, task_type, get_random_name())
        error_msg = "技战法预置任务：{}，结果为空，预置失败".format(task_name)
        success_msg = "技战法预置任务：{}，预置成功".format(task_name)
        start_datetime = get_delta_time(days=-7)
        end_datetime = get_delta_time()
        remark = '我是备注'
        case_num = '12345678'
        video_list = list(self.df_cam.generate_camera_info(camera_type='rtsp-pre', fake=False).keys())
        time_space_list = [{'video_list': [video_list[0]], "start_time": start_datetime, "end_time": end_datetime},
                           {'video_list': [video_list[1]], "start_time": start_datetime, "end_time": end_datetime},
                           {'video_list': [video_list[2]], "start_time": start_datetime, "end_time": end_datetime},
                           ]
        column_list = {'时空档案过滤': 8}
        my_column = column_list.get(task_type) if column_list.get(task_type) else "last()"
        self.into_second_page(menu_name=tactic_type)
        self.into_third_page(menu_name=task_type)
        result = self.find_tactics_task(case_name=task_name)
        if result:
            self.view_task_result(task_name=task_name, column=my_column)
            ele_list = self.driver.ele_list(ele=self.tactics_ele.CaseDetail.detail_result_list)
            assert ele_list, error_msg
        else:
            if task_type == "频繁过人":
                self.create_often_pass_task(task_name=task_name, start_datetime=start_datetime,
                                            end_datetime=end_datetime,
                                            place=video_list, appear_times=2, select_lib=None, exclude_lib=None,
                                            case_num=case_num, remark=remark)
            elif task_type == '时空档案过滤':
                self.create_space_time_filter_case_task(task_name=task_name, start_datetime=start_datetime,
                                                        end_datetime=end_datetime, place=video_list, select_lib=None,
                                                        exclude_lib=None, case_num=case_num, remark=remark)
            elif task_type == '连续出现':
                self.create_continue_appear(task_name=task_name, start_datetime=start_datetime,
                                            end_datetime=end_datetime,
                                            continue_days=1, place=video_list, select_lib=None,
                                            exclude_lib=None, case_num=case_num, remark=remark)
            elif task_type == '昼伏夜出':
                self.create_day_hide_night_out(task_name=task_name, start_datetime=start_datetime,
                                               end_datetime=end_datetime,
                                               place=video_list, appear_days=1, night_start_time='22:00',
                                               night_end_time='06:00',
                                               select_lib=None, exclude_lib=None, case_num=case_num, remark=remark)
            elif task_type == '首次出现':
                self.create_first_appear(task_name=task_name, first_appear_time=start_datetime, not_appear_time='一个月',
                                         place=video_list, select_lib=None, exclude_lib=None, case_num=case_num,
                                         remark=remark)
            elif task_type == '感知离开':
                self.create_identify_leave(task_name=task_name, start_datetime=start_datetime,
                                           end_datetime=end_datetime,
                                           miss_days=2, place=video_list, select_lib=None, exclude_lib=None,
                                           case_num=case_num, remark=remark)
            elif task_type == '时空碰撞':
                self.create_time_space_crash(task_name=task_name, time_space_list=time_space_list, crash_times=2,
                                             select_lib=None, exclude_lib=None, case_num=case_num, remark=remark)
            elif task_type == '同行人分析':
                self.create_peer_analyze(task_name=task_name, file_id=17, start_datetime=start_datetime,
                                         end_datetime=end_datetime, place=video_list, peer_time=30, peer_times=3,
                                         select_lib=None,
                                         exclude_lib=None, case_num=case_num, remark=remark)
            elif task_type == '精准同行分析':
                self.create_accurate_peer(task_name=task_name, file_id=17, start_datetime=start_datetime,
                                          end_datetime=end_datetime, place=video_list, peer_time=30, peer_times=3,
                                          select_lib=None,
                                          exclude_lib=None, case_num=case_num, remark=remark)
            for _ in range(20):
                self.view_task_result(task_name=task_name, column=my_column)
                ele_list = self.driver.ele_list(ele=self.tactics_ele.CaseDetail.detail_result_list)
                if ele_list:
                    break
                else:
                    self.driver.ele_click(self.tactics_ele.go_back)
                    time.sleep(30)
            else:
                raise Exception(error_msg)
        self.driver.ele_click(self.tactics_ele.go_back)
        self.driver.ele_click(self.tactics_ele.go_back)
        return {'task_name': task_name, 'case_num': case_num, 'remark': remark}


if __name__ == '__main__':
    a = CameraDefine._pre_fixed_rtsp_videos
    for i in a.keys():
        print(i)

