#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from v43.ele_set.page_task import TaskPageEle
from common import common_func
from sc_common.sc_define import TaskDefine, define_camera
from common.common_func import shadow, get_num_from_str
from v43.pub.pub_base import PublicClass
import time
from sc_common.sc_define import ResDefine
from v43.pub.pub_sys_setting import SettingModule


class TaskAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = TaskPageEle
        self.of = TaskDefine
        self.df = define_camera
        # self.stop_alarm_message()
        del kwargs['local_mod']
        self.set_module = SettingModule(driver, **kwargs)
        self.set_sys_task()

    @shadow("进入布控任务")
    def into_task_center(self):
        """
        进入布控任务
        :return:
        """
        self.driver.click_xpath(self.el.task_main)

    @shadow("预置设置系统布控任务阈值下限")
    def set_sys_task(self, ):
        try:

            self.into_menu("系统设置")
            self.set_module.click_left_menu(type_num=2)
            now_tsk_threshold = get_num_from_str(self.driver.ele_get_val(self.el.setting_lbl_el.format("阈值下限")))
            if str(now_tsk_threshold) != self.of.pre_threshold_value:
                self.driver.ele_click(self.el.camera_confirm_btn)
                self.driver.ele_click(self.el.all_push)
                time.sleep(1)
                self.driver.ele_input(self.el.setting_ipt_el.format("阈值下限"), self.of.pre_threshold_value)
                self.driver.ele_input(self.el.setting_ipt_ele.format("智能布控"),self.of.task_time_value)
                self.driver.ele_input(self.el.setting_ipt_elc.format("检索范围"), self.of.search_scsope_value)
                # self.driver.ele_input(self.el.setting_ipt_el.format("人体检索时间间隔"), "5")
                time.sleep(1)
                # if self.driver.ele_exist(self.el.next_add_task):
                #     self.driver.ele_click(self.el.next_add_task)
                confirm_btn_ele = self.driver.ele_get_val(self.el.camera_confirm_btn, attr_name="class")
                if "is-disabled" not in confirm_btn_ele:
                    self.driver.ele_click(self.el.camera_confirm_btn)
                else:
                    self.driver.ele_click(self.el.camera_cancel_btn)
        except Exception as e:
            self.log.info("")

    def stop_alarm_message(self):
        """
        执行测试前，关闭告警消息提醒
        :return:
        """
        self.driver.click_xpath(self.el.small_bell)
        self.wid.wid_chk_loading()
        if self.driver.ele_exist("xpath=" + self.el.stop_push_message):
            self.driver.click_xpath(self.el.stop_push_message)
        self.driver.click_xpath(self.el.small_bell)
        return True

    @shadow("新建任务（基本信息）")
    def task_info_long_time(self, name, precise_num, vague_num="", remark=""):
        """
        新建任务（基本信息）
        :param name: 任务名称
        :param a_type: 布控任务类型
        :param precise_num: 精准告警阈值
        :param vague_num: 模糊模糊告警阈值,不输默认不设置模糊阈值
        :return:
        """
        self.driver.click_xpath(self.el.add_task)
        time.sleep(1)
        self.driver.input_xpath(self.el.task_name_input, name)
        # self.driver.click_text(a_type)
        self.driver.input_xpath(self.el.alarm_input, precise_num)
        time.sleep(1)
        self.driver.click_enter_key()
        if vague_num:
            self.driver.click_xpath(self.el.switch_fuzzy)
            self.driver.input_xpath(self.el.fuzzy_alarm_input, vague_num)
            self.driver.click_enter_key()
        if remark:
            self.driver.input_xpath(self.el.remark_input, remark)
        self.driver.click_xpath(self.el.next_add_task)
        return True

    @shadow("新建任务（选择布控对象），填写选人像库内容")
    def task_select_face_db(self, db_names):
        """
        新建任务（选择布控对象），填写选人像库内容
        :param db_names:list类型
        :return:
        """
        self.driver.ele_click(self.el.add_monitor_lib)
        self.wid.wid_chk_loading()
        for db in db_names:
            self.wid.wid_chk_loading()
            self.driver.ele_input(self.el.lib_search_input, db)
            self.driver.ele_click(self.el.other)
            self.driver.ele_click(self.el.lib_search_button, load=True)
            self.driver.ele_click(self.el.all_choose, wait_time=3)
        self.wid.wid_chk_loading()
        self.driver.ele_click(self.el.ensure_lib, load=True)
        self.driver.ele_click(self.el.next_add_task, load=True)
        return True

    @shadow("新建照片布控")
    def add_photo_task(self, images_path, name, id=""):
        """
        新建照片布控
        :param images_path:
        :param name:
        :param id:
        :return:
        """
        self.driver.click_xpath(self.el.photo_task)
        self.driver.click_xpath(self.el.switch_task)
        if isinstance(images_path, list):
            for i in images_path:
                self.driver.ele_upload(i, self.el.upload_image)
            self.driver.input_xpath(self.el.image_name_input, name)
            if id:
                self.driver.input_xpath(self.el.image_id_input, id)
            self.driver.click_xpath(self.el.save_photo)
        return True

    @shadow("新建任务选择视频源")
    def task_select_add_source(self, camera_lst, trig_wid=None):
        """
        新建任务选择视频源
        :param camera_lst:
        :param trig_wid:
        :return:
        """
        camera_lst = common_func.convert_to_array(camera_lst)
        if not camera_lst:
            return
        if trig_wid:
            self.driver.ele_click(trig_wid)
        # else:
        #     self.driver.ele_click(self.el.camera_ele)
        #     pass
        # self.driver.ele_click(self.el.camera_page_cam_tree)
        self.wid.wid_chk_loading()
        # self.wid.wid_drop_down("视频源", self.el.camera_slt_cate_ele)
        for camera_ in camera_lst:
            self.driver.ele_input(self.el.camera_slt_cate_txt, input_value=camera_, enter=True)
            time.sleep(2)
            self.driver.ele_click(self.el.camera_slt_cate_search_check_box)     # 点1
            # print([self.driver.ele_click(x) for x in self.driver.ele_list(self.el.camera_slt_cate_search_check_box)]) # 点所有
        self.driver.ele_click(self.el.camera_confirm_btn)
        return True

    @shadow("新建布控权限分配")
    def assign_permissions(self, user_list=None, dep_list=None):
        self.wid.wid_power_assign(user_list=user_list, dep_list=dep_list)

    @shadow("布控任务详情")
    def task_details(self, name, typo=1):
        """
        布控任务详情
        :param name:
        :param typo:
        :return:
        """
        self.driver.input_xpath(self.el.task_search, name)
        self.driver.click_xpath(self.el.task_search_button)
        self.driver.click_xpath(self.el.task_info)
        if typo != 1:
            self.driver.click_xpath(self.el.task_base_info.format(typo=typo))
        return True

    @shadow("根据输入条件获取布控任务列表")
    def switch_task_list(self, task_status=None, task_source=None, search_info=None):
        """
        根据输入条件获取布控任务列表
        :param task_status: 运行中/等待中/已终止
        :param task_source: 不限/我创建的任务/分配给我的任务
        :param search_info:
        :return:
        """
        self.wid.wid_chk_loading()
        if task_status:
            # self.driver.click_xpath(self.el.task_staus)
            # self.driver.chk_loading()
            self.driver.ele_click(self.el.task_staus, load=True)
            self.driver.ele_click(self.el.status_com_.format(task_status))
            # if task_status == "运行中":
            #     self.driver.click_xpath(self.el.run)
            # elif task_status == "等待中":
            #     self.driver.click_xpath(self.el.wait)
            # elif task_status == "已终止":
            #     self.driver.click_xpath(self.el.stop)
        if task_source:
            # self.driver.click_xpath(self.el.task_source)
            # self.driver.chk_loading()
            self.driver.ele_click(self.el.task_source, load=True)
            self.driver.ele_click(self.el.task_src_com.format(task_source))
            # if task_source == "不限":
            #     self.driver.click_xpath(self.el.infinite)
            # elif task_source == "我创建的任务":
            #     self.driver.click_xpath(self.el.icreate)
            # elif task_source == "分配给我的任务":
            #     self.driver.click_xpath(self.el.distribution)
        if search_info:
            self.driver.chk_loading()
            self.driver.ele_input(self.el.task_search, search_info)
            self.driver.ele_click(self.el.task_search_button)
        return True

    @shadow("布控列表-终止布控任务")
    def stop_task(self, name, task_status="运行中"):
        """
        终止布控任务
        :param name:
        :param task_status:
        :return:
        """
        # if name in [self.of.preset_accurate_fuzzy_task_name, self.of.preset_task_name]:
        #     self.log.info("预置的布控任务，不做清理")
        #     return True
        self.driver.refresh_driver()
        self.into_menu("布控")
        self.switch_task_list(task_status=task_status)
        self.driver.input_xpath(self.el.task_search, name)
        self.driver.click_xpath(self.el.task_search_button)
        self.wid.wid_chk_loading()
        if not self.driver.ele_exist(self.el.more):
            self.log.info("布控任务：{}或已被终止，无需终止！".format(name))
            return True
        self.driver.ele_click(self.el.more)
        self.wid.wid_chk_loading()
        self.driver.click_xpath(self.el.stop_task_button)
        self.driver.click_xpath(self.el.ensure_stop_task)
        result = self.wid.wid_get_alert_label()
        if "终止任务成功" in result:
            self.log.info("布控任务：{}，终止成功！".format(name))
            return True

    @shadow("布控列表-重启布控任务")
    def restart_task(self, name, task_status="已终止"):
        """
        布控列表-重启布控任务
        :param name:
        :return:
        """
        self.switch_task_list(task_status=task_status)
        self.driver.input_xpath(self.el.task_search, name)
        self.driver.click_xpath(self.el.task_search_button)
        self.driver.click_xpath(self.el.restart_task_ele)
        self.driver.click_xpath(self.el.ensure_restart_task)
        result = self.driver.exist_element(self.el.restart_task_success)
        if not result:
            return False
        self.driver.click_xpath(self.el.restart_task_success_button)
        return True

    @shadow("布控列表-克隆布控任务")
    def clone_task(self, name, task_status="运行中"):
        """
        布控列表-克隆布控任务
        :param name:
        :param task_status:
        :return:
        """
        self.switch_task_list(task_status=task_status)
        self.driver.input_xpath(self.el.task_search, name)
        self.driver.click_xpath(self.el.task_search_button)
        self.driver.ele_click(self.el.more)
        self.driver.click_xpath(self.el.clone_task_button)
        self.wid.wid_chk_loading()
        if self.driver.ele_exist(self.el.first_editor):
            self.driver.ele_click(self.el.first_editor)
        # self.driver.click_xpath(self.el.next_add_task)
        return True

    @shadow("布控列表-编辑布控任务")
    def editor_task(self, name, task_status="运行中"):
        """
        编辑布控任务
        :param name:
        :param task_status:
        :return:
        """
        # TODO
        self.switch_task_list(task_status=task_status)
        self.driver.input_xpath(self.el.task_search, name)
        self.driver.click_xpath(self.el.task_search_button)
        self.driver.click_xpath(self.el.editor_task)
        self.wid.wid_chk_loading()
        if self.driver.ele_exist(self.el.first_editor):
            self.driver.ele_click(self.el.first_editor)
        return True

    @shadow("布控列表-进入告警列表页")
    def into_alarm_list(self, name, task_status="运行中", map=False, heat=False):
        """
        布控列表-进入告警列表页
        :param name:
        :param task_status:
        :param map:是否进入地图模式
        :param heat:是否进入地图模式中的热力图模式
        :return:
        """
        self.wid.wid_chk_loading()
        if self.driver.ele_exist(self.el.check_push_config):
            self.log.info("当前页面已在告警列表页中，无需再次进入")
            return True
        self.switch_task_list(task_status=task_status)
        self.wid.wid_chk_loading()
        self.driver.input_xpath(self.el.task_search, name)
        self.wid.wid_chk_loading()
        self.driver.click_xpath(self.el.task_search_button)
        self.wid.wid_chk_loading()
        self.driver.click_xpath(self.el.alarm_info)
        self.wid.wid_chk_loading()
        if map:
            self.driver.ele_click(self.el.alarm_list_map)
            if heat:
                self.driver.ele_click(self.el.heat_map)
        return True

    @shadow("告警列表-检查是否产生告警")
    def get_alarm(self, count=12*7, time_sleep=5, than_in_the_alarm=False):
        """
        告警列表-检查是否产生告警
        :param count:
        :param time_sleep:
        :return:
        """
        for j in range(count):
            self.wid.wid_chk_loading()
            if self.driver.ele_exist(self.el.first_alarm):
                if than_in_the_alarm:
                    self.wid.wid_chk_loading()
                    if self.driver.ele_exist(self.el.first_than_in_the_alarm):
                        self.log.info("布控已产生精准告警！")
                        return True
                    if (count - 1) == j:
                        self.log.error("查询次数达到最大次数，仍未产生精准告警")
                        return False
                    else:
                        self.driver.refresh_driver()
                        time.sleep(time_sleep)
                        continue
                self.log.info("布控已产生告警！")
                return True
            else:
                self.driver.refresh_driver()
                time.sleep(time_sleep)
                continue
        else:
            self.log.error("查询次数达到最大次数，仍未产生告警，请检查环境！")
            return False

    @shadow("告警目标详情-设置沉默时间")
    def silence_setting(self, start_time=None, end_time=None, reason="test"):
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
        return True

    @shadow("告警列表-查看沉默人员")
    def check_silence_personnel(self, move_target=False, ed_taeget=False, start_time=None, end_time=None, reason=None):
        """
        告警列表-查看沉默人员
        :param move_target: 移除沉默人员
        :param ed_taeget: 编辑沉默人员时间
        :param start_time: 沉默人员开始时间 与ed_taeget配合使用
        :param end_time: 沉默人员结束时间 与ed_taeget配合使用
        :param reason: 沉默原因 与ed_taeget配合使用
        :return:
        """
        self.driver.click_xpath(self.el.silence_personnel)
        if ed_taeget:
            self.driver.click_xpath(self.el.ed_silence_target)
            self.wid.wid_slt_date(start_time=start_time, end_time=end_time, module="silence")
            if reason:
                self.driver.input_xpath(self.el.silence_reason_input, reason)
            self.driver.click_xpath(self.el.silence_ensure)
        if move_target:
            self.driver.click_xpath(self.el.move_silence_target)
            self.driver.click_xpath(self.el.move_silence_ensure)
        return True

    @shadow("告警列表-告警推送方式设置")
    def alarm_push_setting(self, videos=None, sound=True):
        """
        告警列表-告警推送方式设置
        :param videos:
        :param sound:
        :return:
        """
        self.driver.click_xpath(self.el.alarm_push_set)
        self.wid.wid_chk_loading()
        if sound:
            self.driver.click_xpath(self.el.sound_open)
        else:
            self.driver.click_xpath(self.el.sound_close)
        if videos:
            self.driver.click_xpath(self.el.alarm_push_select_video)
            self.wid.wid_chk_loading()
            camera_lst = common_func.convert_to_array(videos)
            if not camera_lst:
                return
            self.driver.ele_click(self.el.alarm_video_all_choose)
            for camera_ in camera_lst:
                self.driver.ele_input(self.el.video_input, input_value=camera_, enter=True)
                self.driver.chk_loading()
                self.driver.ele_click(self.el.alarm_video_all_choose)
            self.driver.chk_loading()
            self.driver.ele_click(self.el.alarm_push_select_video_button)
            self.driver.click_xpath(self.el.alarm_push_ensure)
        return True

    @shadow("告警列表-查看告警推送区域与推送声音提示状态")
    def check_alarm_push(self, status="已开启", videos=None):
        """
        告警列表-查看告警推送区域与推送声音提示状态
        :return:
        """
        sound_status = self.driver.ele_get_val(self.el.sound_status)    #, 'class', chk_visit=False)
        # if status == "已开启" and 'is-check' not in sound_status:
        #     # self.driver.ele_exist(self.el.sound_status.format("已开启"))
        #     self.log.error("查询的声音状态不正确")
        #     return False
        # if status == "已关闭" and 'is-check' in sound_status:
            # if not self.driver.ele_exist(self.el.sound_status.format("已关闭")):
        if status != sound_status:
                self.log.error("查询的声音状态不正确")
                return False
        self.driver.ele_click(self.el.check_push_config)
        return True

    @shadow("根据输入条件获取布控告警列表")
    def switch_alarm_list(self, videos=None, librarys=None, similar_number=None, identity_attribute=False, gender=None,
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
        if videos:
            camera_lst = common_func.convert_to_array(videos)
            if not camera_lst:
                return
            self.driver.click_xpath(self.el.video_list)
            self.wid.wid_chk_loading()
            self.driver.ele_click(self.el.alarm_video_all_choose)
            for camera_ in camera_lst:
                self.driver.ele_input(self.el.video_input, input_value=camera_, enter=True)
                self.driver.chk_loading()
                self.driver.ele_click(self.el.alarm_video_all_choose)
            self.driver.ele_click(self.el.video_button)
        if librarys:
            librarys = common_func.convert_to_array(librarys)
            if not librarys:
                return
            self.driver.click_xpath(self.el.lib_list)
            self.driver.chk_loading()
            self.driver.click_xpath(self.el.lib_cansel_selected)
            self.driver.chk_loading()
            for lib in librarys:
                self.driver.input_xpath(self.el.lib_input, lib)
                self.driver.click_xpath(self.el.lib_other)
                self.driver.click_xpath(self.el.lib_button)
                self.driver.chk_loading()
                self.driver.click_xpath(self.el.lib_cansel_selected)
            self.driver.click_xpath(self.el.lib_save)
        if similar_number:
            self.driver.chk_loading()
            self.driver.ele_click(self.el.similar)
            self.driver.chk_loading()
            self.driver.ele_input(self.el.similar_input, similar_number)
            self.driver.click_enter_key()
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
        if search_info:
            self.driver.chk_loading()
            self.driver.input_xpath(self.el.target_input, search_info)
            self.driver.click_enter_key()
        if only_pitch:
            self.driver.chk_loading()
            self.driver.click_xpath(self.el.only_check_than_in_the)
        return True

    @shadow("进入告警详情页")
    def alarm_details(self, remark="", judge=False, all_alarm=False, track=False):
        """
        进入告警详情页
        :param name:
        :param task_status:
        :param remark:
        :param judge:
        :param all_alarm:
        :param track:
        :return:
        """
        self.wid.wid_chk_loading()
        self.driver.ele_click(self.el.first_alarm)
        self.wid.wid_chk_loading()
        if remark:
            self.driver.input_xpath(self.el.alarm_remark, remark)
            self.driver.click_xpath(self.el.alarm_remark_commit)
        if judge:
            self.wid.wid_chk_loading()
            self.driver.click_xpath(self.el.target_judge)
        if all_alarm:
            self.wid.wid_chk_loading()
            self.driver.click_xpath(self.el.all_alarm)
        self.wid.wid_chk_loading()
        if track:
            time.sleep(3)
            self.driver.click_xpath(self.el.check_track)
        return True

    @shadow("获取布控任务列表数据")
    def get_task_list(self):
        """
        :return:
        """
        task_dict = dict()
        tr_list = self.driver.ele_list(self.el.task_list_table_tr)
        for item in tr_list:
            all_txt = self.driver.ele_get_val(item)
            if all_txt:
                task_dict.update(dict([[y.split('\n')[0],
                                        [y.split('\n')[1], y.split('\n')[2], y.split('\n')[3], y.split('\n')[4],
                                         y.split('\n')[5],
                                         y.split('\n')[6]
                                            , y.split('\n')[7]]]
                                       for y in all_txt.split('删除\n')]))
        return task_dict


class TaskPage(TaskAction):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)

    def add_libtask_or_phototask(self, name, precise_num, camera_lst, db_names=None,
                                 images_path=None, id="", vague_num="",
                                 remark="", trig_wid=None, task_type=0, get_alarm=False, than_in_the_alarm=False,
                                 count=40, time_sleep=3):
        """
        新建任务（完整流程）
        :param name: 任务名称
        :param task_type: 布控任务类型:0为人像库布控，1为照片布控
        :param precise_num: 精准告警阈值
        :param is_vague: 是否勾选模糊告警阈值
        :param vague_num: 模糊模糊告警阈值
        :return:
        #TODO
        """
        self.task_info_long_time(name, precise_num, vague_num=vague_num, remark=remark)
        if task_type == 0:
            self.task_select_face_db(db_names)
        if task_type == 1:
            self.add_photo_task(images_path, name, id=id)
        self.task_select_add_source(camera_lst, trig_wid=trig_wid)
        self.driver.ele_click(self.el.next_add_task)
        time.sleep(0.3)
        if self.driver.ele_exist(self.el.submit_task_confirm):
            self.cf.try_catch(self.driver.ele_click, ele=self.el.submit_task_confirm, judge=True)
        if name not in [self.of.preset_accurate_fuzzy_task_name, self.of.preset_task_name]:
            self.collect_resource(resource_type=ResDefine.key_task, resource_value=name)
        self.wid.wid_chk_loading()
        if get_alarm:
            self.into_alarm_list(name, task_status="运行中")
            alarm_data = self.get_alarm(count=count, time_sleep=time_sleep, than_in_the_alarm=than_in_the_alarm)
            self.driver.ele_click(self.el.go_back)
            if alarm_data:
                self.log.info("布控产生了告警，正确")
                return name
            else:
                return False
        else:
            return name

    def pre_lib_task(self, accurate_fuzzy=True, task_status="运行中", get_alarm=False, than_in_the_alarm=False, count=20,
                     time_sleep=3):
        """
        新建精准阈值的预置布控或精准阈值模糊阈值的预置布控
        :param accurate_fuzzy:是否新建有模糊阈值的预置布控
        :return:
        """
        video_name_lst = list(self.df_cam.generate_camera_info(camera_type='rtsp-pre', fake=False).keys())
        self.switch_task_list(task_status=task_status)
        if accurate_fuzzy:
            task_name = self.of.preset_accurate_fuzzy_task_name
        else:
            task_name = self.of.preset_task_name
        self.driver.input_xpath(self.el.task_search, task_name)
        self.driver.click_xpath(self.el.task_search_button)
        self.wid.wid_chk_loading()
        if not self.driver.ele_exist("xpath=" + self.el.task_info):
            if accurate_fuzzy:
                self.log.info("预置布控任务----{}---不存在或已终止，正在新建新的预置任务".format(self.of.preset_accurate_fuzzy_task_name))
                self.add_libtask_or_phototask(self.of.preset_accurate_fuzzy_task_name,
                                              self.of.preset_accurate_alarm_threshold, video_name_lst,
                                              db_names=["UI_pre_65_por"],
                                              vague_num=self.of.preset_threshold)
            else:
                self.log.info("预置布控任务----{}---不存在或已终止，正在新建新的预置任务".format(self.of.preset_task_name))
                self.add_libtask_or_phototask(self.of.preset_task_name,
                                              self.of.preset_accurate_alarm_threshold, video_name_lst,
                                              db_names=["UI_pre_65_por"])
            self.wid.wid_chk_loading()
            if get_alarm:
                self.into_alarm_list(task_name, task_status="运行中")
                alarm_data = self.get_alarm(count=count, time_sleep=time_sleep, than_in_the_alarm=than_in_the_alarm)
                self.driver.ele_click(self.el.go_back)
                if alarm_data:
                    self.log.info("布控产生了告警，正确")
                    return task_name
                else:
                    return False
            else:
                return task_name
        else:
            if accurate_fuzzy:
                task_name = self.of.preset_accurate_fuzzy_task_name
                self.log.info("预置布控任务----{}---已存在，无需再次新建".format(task_name))
            else:
                task_name = self.of.preset_task_name
                self.log.info("预置布控任务----{}---已存在，无需再次新建".format(task_name))
            if get_alarm:
                self.into_alarm_list(task_name, task_status="运行中")
                alarm_data = self.get_alarm(count=count, time_sleep=time_sleep, than_in_the_alarm=than_in_the_alarm)
                self.driver.ele_click(self.el.go_back)
                if alarm_data:
                    self.log.info("布控产生了告警，正确")
                    return task_name
                else:
                    return False
            else:
                return task_name


if __name__ == "__main__":
    from common.w_driver import WDriver
    from v43.pub.pub_menu import MainPage

    driver = WDriver()
    driver.open_url("http://10.111.32.91:10219/#/control-tasks")
    #
    MainPage.login_in(driver, 'qjh', 'admin1234')
    test = TaskPage(driver)
    # test.add_libtask_or_phototask("test", 80, ["pre_face_rtsp_3"], db_names=["33"])
    test.into_alarm_list("抓孔明")
    # test.get_task_list()
    test.export_alarm(num="1")
