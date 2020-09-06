#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = "huangyongchang"

from v43.ele_set.page_crowd_analyze import CrowdAnalyzeEle
from v43.pub.pub_menu import MainPage
from v43.pub.pub_base import PublicClass
from common.common_func import *
from v43.pub.pub_widget import WidPub
from v43.pub.pub_camera import CameraModule


class CrowAnalyzeCommon(PublicClass):
    def __init__(self, web_driver, **kwargs):
        super(CrowAnalyzeCommon, self).__init__(web_driver, **kwargs)
        self.wide_pub = WidPub(web_driver, **kwargs)
        self.crowd_ele = CrowdAnalyzeEle
        self.video_obj = CameraModule(web_driver=web_driver, **kwargs)

    def pre_crowd(self):
        """
        人群预置：预置视频源，预置人群事件任务
        :return:
        """
        my_setting_events = []
        # setting_events = ["越线事件", "徘徊事件", "过密事件", "入侵事件", "逆行事件"]
        setting_events = ["越线", "徘徊", "过密", "入侵", "逆行"]
        video_name = 'UI_pre_crowd_rtsp_1'
        video_name = \
        list(self.df_cam.generate_camera_info(camera_type='rtsp-pre', camera_use='crowd', fake=False).keys())[0]
        for i in setting_events:
            if not self.filter_crowd_task(video_name=video_name, alarm_type=i):
                my_setting_events.append(i)
        if my_setting_events:
            self.into_menu("人群分析")
            self.create_crowd_event_task(video_name=video_name, events=my_setting_events)
        return {"video_name": video_name}

    @shadow("进入人群分析页面")
    def into_crowd_analyze(self):
        """
        进入人群分析页面
        :return:
        """
        MainPage.into_menu("人群分析")

    @shadow("查找指定视频源")
    def __find_video(self, video_name):
        self.driver.ele_input(self.crowd_ele.TaskConfig.search_video, video_name, enter=True)
        assert self.driver.ele_get_val(self.crowd_ele.TaskConfig.video_name.format(video_name)) == video_name

    def into_config(self, video_name):
        # 指定视频源进入配置
        self.__find_video(video_name)
        # self.driver.ele_click(self.crowd_ele.TaskConfig.config.format(video_name)) # mx 2020.8.27 注释掉

    def into_list_model(self):
        # 进入列表模式
        self.driver.ele_click(self.crowd_ele.list_model)

    def into_map_model(self):
        # 进入地图模式
        self.driver.ele_click(self.crowd_ele.map_model)

    def into_alarm_manage(self):
        # 进入告警管理页面
        self.driver.ele_click(self.crowd_ele.alarm_manage)

    def into_task_config(self):
        # 进入任务配置
        self.driver.ele_click(self.crowd_ele.task_config)

    @shadow("预览视频源")
    def preview_video(self, video_name):
        self.__find_video(video_name)
        self.driver.ele_click(self.crowd_ele.TaskConfig.video_preview)

    @shadow("点击任务详情")
    def task_detail(self, video_name):
        self.__find_video(video_name)
        self.driver.ele_click(self.crowd_ele.TaskConfig.task_detail)

    @shadow("任务配置")
    def config(self, video_name):
        self.__find_video(video_name)
        self.driver.ele_click(self.crowd_ele.TaskConfig.config)

    @shadow("暂停或重启任务")
    def pause_or_reboot(self, video_name, ope_name="暂停"):
        self.__find_video(video_name)
        self.driver.ele_click(self.crowd_ele.TaskConfig.pause_reboot.format(video_name, ope_name))
        self.driver.ele_click(self.crowd_ele.TaskConfig.modify_task_status_confirm)

    def terminate(self, video_name):
        self.into_menu(menu_name='人群分析')
        self.into_task_config()
        self.__find_video(video_name)
        self.driver.ele_click(self.crowd_ele.TaskConfig.terminate.format(video_name))
        self.driver.ele_click(self.crowd_ele.TaskConfig.modify_task_status_confirm)
        return True

    def create_crowd_event_task(self, video_name, events):
        """
        创建人群事件任务
        :param video_name:  视频源名称
        :param events:  需要创建任务的事件类型
        :return:
        """
        self.into_task_config()
        for event in events:
            time.sleep(2)
            self.into_config(video_name=video_name)
            self.driver.ele_click(self.crowd_ele.TaskConfig.config.format(video_name))
            if event == "越线":
                self.driver.ele_click(self.crowd_ele.TaskConfig.cross_line_event)  # 点击左侧越线事件菜单
                if "已启用" in self.driver.ele_get_val(self.crowd_ele.TaskConfig.event_switch):  # 判断页面是否是开启状态，有则跳过
                    self.driver.ele_click(self.crowd_ele.TaskConfig.save)  # 点击保存
                    continue
                self._setting_cross_line_event()
                self.collect_resource(self.df.key_crowd_task, video_name)
            elif event == "徘徊":
                self.driver.ele_click(self.crowd_ele.TaskConfig.hover_event)  # 点击左侧徘徊事件菜单
                if "已启用" in self.driver.ele_get_val(self.crowd_ele.TaskConfig.event_switch):
                    self.driver.ele_click(self.crowd_ele.TaskConfig.save)  # 点击保存
                    continue
                self._setting_hover_event()
                self.collect_resource(self.df.key_crowd_task, video_name)
            elif event == "过密":
                self.driver.ele_click(self.crowd_ele.TaskConfig.to_much_event)
                if "已启用" in self.driver.ele_get_val(self.crowd_ele.TaskConfig.event_switch):
                    self.driver.ele_click(self.crowd_ele.TaskConfig.save)
                    continue
                self._setting_to_much_event()
                self.collect_resource(self.df.key_crowd_task, video_name)
            elif event == "滞留":
                self.driver.ele_click(self.crowd_ele.TaskConfig.retention_event)
                if "已启用" in self.driver.ele_get_val(self.crowd_ele.TaskConfig.event_switch):
                    self.driver.ele_click(self.crowd_ele.TaskConfig.save)
                    continue
                self._setting_retention_event()
                self.collect_resource(self.df.key_crowd_task, video_name)
            elif event == "入侵":
                self.driver.ele_click(self.crowd_ele.TaskConfig.invade_event)
                if "已启用" in self.driver.ele_get_val(self.crowd_ele.TaskConfig.event_switch):
                    self.driver.ele_click(self.crowd_ele.TaskConfig.save)
                    continue
                self._setting_invade_event()
                self.collect_resource(self.df.key_crowd_task, video_name)
            elif event == "逆行":
                self.driver.ele_click(self.crowd_ele.TaskConfig.converse_event)
                if "已启用" in self.driver.ele_get_val(self.crowd_ele.TaskConfig.event_switch):
                    self.driver.ele_click(self.crowd_ele.TaskConfig.save)
                    continue
                self._setting_converse_event()
                self.collect_resource(self.df.key_crowd_task, video_name)
        self.collect_resource(self.df.key_crowd_task, video_name)

    @shadow("设置越线事件")
    def _setting_cross_line_event(self):
        """
        设置越线事件
        :return:
        """
        self.driver.ele_click(self.crowd_ele.TaskConfig.cross_line_event)
        self.driver.ele_click(self.crowd_ele.TaskConfig.event_switch)
        self.driver.ele_click(self.crowd_ele.TaskConfig.video_play)
        time.sleep(5)
        self.driver.ele_click(self.crowd_ele.TaskConfig.screen_capture)
        self.driver.ele_click(self.crowd_ele.TaskConfig.draw_direction)
        time.sleep(0.5)
        self.wide_pub.draw_line(self.crowd_ele.TaskConfig.check_region, src_x=60, src_y=350, width=850, height=0,
                                slt_direction='up')
        time.sleep(0.5)
        self.driver.ele_click(self.crowd_ele.TaskConfig.save)

    @shadow("设置徘徊事件")
    def _setting_hover_event(self):
        """
        设置徘徊事件
        :return:
        """
        self.driver.ele_click(self.crowd_ele.TaskConfig.hover_event)
        self.driver.ele_click(self.crowd_ele.TaskConfig.event_switch)
        self.driver.ele_click(self.crowd_ele.TaskConfig.video_play)
        time.sleep(1.5)
        self.driver.ele_click(self.crowd_ele.TaskConfig.screen_capture)
        self.driver.ele_click(self.crowd_ele.TaskConfig.draw_direction)
        time.sleep(0.5)
        self.wide_pub.win_draw_close()
        self.driver.ele_click(self.crowd_ele.TaskConfig.save)

    @shadow("设置过密事件")
    def _setting_to_much_event(self):
        """
        设置过密事件
        :return:
        """
        self.driver.ele_click(self.crowd_ele.TaskConfig.to_much_event)
        self.driver.ele_click(self.crowd_ele.TaskConfig.event_switch)
        self.driver.ele_click(self.crowd_ele.TaskConfig.video_play)
        time.sleep(1.5)
        self.driver.ele_click(self.crowd_ele.TaskConfig.screen_capture)
        self.driver.ele_click(self.crowd_ele.TaskConfig.draw_direction)
        time.sleep(0.5)
        self.wide_pub.win_draw_close()
        self.driver.ele_click(self.crowd_ele.TaskConfig.save)

    @shadow("设置滞留事件")
    def _setting_retention_event(self):
        """
        设置滞留事件
        :return:
        """
        if self.driver.ele_exist(self.crowd_ele.TaskConfig.retention_event):
            self.driver.ele_click(self.crowd_ele.TaskConfig.retention_event)
            self.driver.ele_click(self.crowd_ele.TaskConfig.event_switch)
            self.driver.ele_click(self.crowd_ele.TaskConfig.video_play)
            time.sleep(3)
            self.driver.ele_click(self.crowd_ele.TaskConfig.screen_capture)
            # self.driver.ele_click(self.crowd_ele.TaskConfig.draw_direction)
            self.driver.ele_click(self.crowd_ele.TaskConfig.box_to_body)
            time.sleep(0.5)
            self.wide_pub.wid_draw_rectangle(self.crowd_ele.TaskConfig.check_region, 170, 125, 105, 400,
                                             bool_isclick=True)
            time.sleep(0.5)
            self.wide_pub.wid_draw_rectangle(self.crowd_ele.TaskConfig.check_region, 400, 140, 105, 400,
                                             bool_isclick=True)
            time.sleep(0.5)
            self.wide_pub.wid_draw_rectangle(self.crowd_ele.TaskConfig.check_region, 575, 160, 105, 400,
                                             bool_isclick=True)
            self.driver.ele_click(self.crowd_ele.TaskConfig.save)
        else:
            pass

    @shadow("设置入侵事件")
    def _setting_invade_event(self):
        """
        设置入侵事件
        :return:
        """
        self.driver.ele_click(self.crowd_ele.TaskConfig.invade_event)
        self.driver.ele_click(self.crowd_ele.TaskConfig.event_switch)
        self.driver.ele_click(self.crowd_ele.TaskConfig.video_play)
        time.sleep(1.5)
        self.driver.ele_click(self.crowd_ele.TaskConfig.screen_capture)
        self.driver.ele_click(self.crowd_ele.TaskConfig.draw_direction)
        time.sleep(0.5)
        self.wide_pub.win_draw_close()
        self.driver.ele_click(self.crowd_ele.TaskConfig.save)

    @shadow("设置逆行事件")
    def _setting_converse_event(self):
        """
        设置逆行事件
        :return:
        """
        self.driver.ele_click(self.crowd_ele.TaskConfig.converse_event)
        self.driver.ele_click(self.crowd_ele.TaskConfig.event_switch)
        self.driver.ele_click(self.crowd_ele.TaskConfig.video_play)
        time.sleep(1.5)
        self.driver.ele_click(self.crowd_ele.TaskConfig.screen_capture)
        self.driver.ele_click(self.crowd_ele.TaskConfig.draw_direction)
        time.sleep(0.5)
        self.wide_pub.draw_line(self.crowd_ele.TaskConfig.check_region, src_x=60, src_y=350, width=850, height=0,
                                slt_direction='up')
        self.driver.ele_click(self.crowd_ele.TaskConfig.save)

    def check_alarm_detail_web(self):
        assert "告警详情" == self.driver.ele_get_val(self.crowd_ele.alarm_detail)
        assert "事件时段统计" in self.driver.ele_get_val(self.crowd_ele.event_time_total)
        assert "研判" == self.driver.ele_get_val(self.crowd_ele.judge_text)
        assert "告警点位" == self.driver.ele_get_val(self.crowd_ele.alarm_point_text)
        assert "事件类型" == self.driver.ele_get_val(self.crowd_ele.event_type_text)
        assert "告警时间" == self.driver.ele_get_val(self.crowd_ele.alarm_time_text)

    def filter_crowd_alarm_record(self, video_list=[], start_time="2020-03-10", end_time="2021-01-01",
                                  in_7_days=False, in_15_days=False, event_type="不限", event_level="不限",
                                  judge_status="不限"):
        """

        :param video_list:    需要筛选的视频源，列表形式传入，可传多个
        :param start_time:    起始时间
        :param end_time:      结束时间
        :param in_7_days:     近7天
        :param in_15_days:    近15天
        :param event_type:    事件类型
        :param event_level:   事件等级
        :param judge_status:  研判状态
        :return:
        """
        if video_list:
            self.wide_pub.wid_slt_camera(camera_lst=video_list, trig_wid=self.crowd_ele.AlarmManage.video_select_widget,
                                         click_confirm=False)
        if in_7_days or in_15_days:
            pass
        else:
            self.wide_pub.wid_slt_date(start_time, end_time)
        self.wide_pub.wid_drop_down(event_type, self.crowd_ele.AlarmManage.event_type, exact=True)
        self.wide_pub.wid_drop_down(event_type, self.crowd_ele.AlarmManage.event_type, exact=True)
        self.wide_pub.wid_drop_down(event_level, self.crowd_ele.AlarmManage.event_level, exact=True)
        self.wide_pub.wid_drop_down(judge_status, self.crowd_ele.AlarmManage.judge_status, exact=True)
        self.wid.wid_chk_loading()
        ele_list = self.driver.ele_list(self.crowd_ele.AlarmManage.crowd_alarm_list)
        for goal_ele in ele_list:
            text = self.driver.ele_get_val(goal_ele)
            if event_type != "不限" and event_type not in text:
                raise ValueError("过滤结果，事件类型不正确，选项类型为{}， 结果为{}".format(event_type, text.split("\n")[0]))
            if not video_list and text.split("\n")[1] not in video_list:
                raise ValueError("过滤结果，视频源不正确，目标视频源为{}， 结果为{}".format(video_list, text.split("\n")[0]))
        return ele_list

    def export_crowd_alarm_record(self, start_num=1, end_num=2):
        """
        导出人群告警记录
        :param start_num: 起始编号
        :param end_num: 结束编号
        :return:
        """
        self.driver.ele_click(self.crowd_ele.AlarmManage.export)
        self.driver.ele_input(self.crowd_ele.AlarmManage.export_start_num, start_num)
        self.driver.ele_input(self.crowd_ele.AlarmManage.export_end_num, end_num)
        self.driver.ele_click(self.crowd_ele.AlarmManage.export_confirm)
        msg = self.wide_pub.wid_task_tip(wait_miss=True)
        if msg != "导出告警记录-人群分析任务已完成":
            raise Exception("导出失败：{}".format(msg))

    def filter_crowd_task(self, video_name=None, equipment_status=None, config_status=None, alarm_type=None,
                          task_status=None):
        """
        筛选人群任务
        :param equipment_status:
        :param config_status:
        :param alarm_type:
        :param task_status:
        :return:
        """
        self.into_task_config()
        if equipment_status is not None:
            self.wide_pub.wid_drop_down(equipment_status, self.crowd_ele.TaskConfig.equip_status_list, exact=True)
        if config_status is not None:
            self.wide_pub.wid_drop_down(config_status, self.crowd_ele.TaskConfig.config_status_list, exact=True)
        if alarm_type is not None:
            self.wide_pub.wid_drop_down(alarm_type, self.crowd_ele.TaskConfig.alarm_type_list, exact=True)
        if task_status is not None:
            self.wide_pub.wid_drop_down(task_status, self.crowd_ele.TaskConfig.task_status_list, exact=True)
        if video_name is not None:
            self.driver.ele_input(self.crowd_ele.TaskConfig.search_video, video_name, enter=True)
        ele_list = self.driver.ele_list(self.crowd_ele.TaskConfig.crowd_list_ele)
        if ele_list:
            for goal_ele in ele_list:
                text = self.driver.ele_get_val(goal_ele)
                if config_status and config_status != "不限":
                    assert config_status == text.split("\n")[2], "配置状态筛选为{}，结果为{}".format(config_status,
                                                                                          text.split("\n")[2])
                if alarm_type and alarm_type != "不限":
                    if alarm_type not in text.split("\n")[3] and "..." not in text.split("\n")[3]:
                        return False
                        # raise Exception("告警类型筛选为：{}, 结果为{}".format(alarm_type, text.split("\n")[3]))
                if task_status and task_status != "不限":
                    assert task_status == text.split("\n")[4], "任务状态筛选为{}，结果为{}".format(task_status,
                                                                                        text.split("\n")[4])
            return ele_list
        else:
            return False


# class CrowdAnalyzeModule(CrowAnalyzeCommon):
#     def __init__(self, web_driver, **kwargs):
#         super(CrowdAnalyzeModule, self).__init__(web_driver, **kwargs)


if __name__ == '__main__':
    pass
