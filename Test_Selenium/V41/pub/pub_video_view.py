#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from common import common_func
from sc_common.sc_define import define_camera
from common.common_func import shadow
from v43.pub.pub_base import PublicClass
import time
from v43.ele_set.page_video_view import ViedoViewPageEle


class ViedoViewAction(PublicClass):
    """卡口"""

    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = ViedoViewPageEle
        self.df = define_camera

    @shadow("卡口检查视频源是否能播放")
    def check_video_play(self):
        time.sleep(2)
        return True if self.driver.ele_exist(self.el.video_playing) else False

    @shadow("卡口检查视频源的抓拍列表或抓拍详情")
    def check_snap(self, snap_details=False, colose=False, sleep=15):
        time.sleep(sleep)
        if not self.driver.ele_exist(self.el.image_list):
            self.log.error("未产生抓拍推送，fail")
            return False
        if snap_details:
            self.driver.ele_click(self.el.new_snap)
        if colose:
            self.driver.ele_click(self.el.snap_details_close)
        return True

    @shadow("卡口检查告警列表")
    def check_alarm(self, sleep=15):
        time.sleep(sleep)
        if not self.driver.ele_exist(self.el.first_alarm):
            self.log.error("经过{}秒后，还未产生告警，fail".format(sleep))
            return False
        else:
            self.log.info("已产生告警推送，pass")
            return True

    @shadow("卡口进入全部告警页")
    def into_all_alarm(self, sleep=15):
        time.sleep(sleep)
        if self.driver.ele_exist(self.el.all_alarm_button):
            self.driver.ele_click(self.el.all_alarm_button)
            if self.driver.ele_exist(self.el.all_alarm_list):
                self.log.info("进入全部告警页面成功，pass")
                return True
            else:
                self.log.error("进入全部告警页面失败，请检查环境，fail")
                return False
        else:
            self.log.error("经过{}秒后，还未产生告警推送，fail".format(sleep))
            return False

    @shadow("卡口搜索视频源")
    def video_source_search(self, camera_lst):
        camera_lst = common_func.convert_to_array(camera_lst)
        if not camera_lst:
            return None
        for camera_ in camera_lst:
            self.driver.ele_input(self.el.camera_slt_cate_txt, input_value=camera_, enter=True)
            self.driver.chk_loading()
        return True

    @shadow("卡口开启人脸检测")
    def start_face_detection(self):
        self.driver.ele_click(self.el.one_switch)
        self.driver.ele_click(self.el.face_detection_start)
        return True


class ViedoViewPage(ViedoViewAction):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)

    @shadow("卡口视频源播放")
    def videoplay(self, camera_lst, split_screen=False, user_many_video=1):
        """

        :param camera_lst:
        :param split_screen:
        :param user_many_video:
        :return:
        """
        camera_lst = common_func.convert_to_array(camera_lst)
        if not camera_lst:
            return None
        if not self.video_source_search(camera_lst):
            return False
        if not split_screen:
            self.driver.ele_click(self.el.choose_video)
        else:
            self.driver.chk_loading()
            self.driver.ele_click(self.el.four_split_screen, move=True)
            self.driver.chk_loading()
            user_many_video_list = common_func.convert_to_array(user_many_video)
            if not user_many_video_list:
                return
            for camera_, video in zip(camera_lst, user_many_video_list):
                self.driver.ele_input(self.el.camera_slt_cate_txt, input_value=camera_, enter=True)
                self.driver.chk_loading()
                self.driver.drag(camera_, self.el.four_screen.format(video))

    @shadow("卡口检查一分屏/四分屏各种功能")
    def split_screen(self, camera_lst, one_screen=True, start_check=False, face=False, check_video_paly=False,
                     all_screen=False,
                     check_snap=False,
                     snap_details=False,
                     check_alarm=False, check_all_alarm=False):
        """

        :param camera_lst:
        :param one_screen:是否一分屏
        :param check_video_paly:检查视频源播放
        :param all_screen:检查全屏
        :param check_snap:检查抓拍
        :param snap_details:检查抓拍详情
        :param check_alarm:检查告警
        :param check_all_alarm:进入全部告警
        :return:
        """
        # 切换成四分屏
        self.wid.wid_chk_loading()
        if not one_screen:
            self.driver.ele_click(self.el.four_split_screen, move=True)
        search_res = self.video_source_search(camera_lst)
        if not search_res:
            return False
        self.driver.ele_click(self.el.choose_video, wait_time=5, load=True)
        if start_check:
            if face:
                self.driver.ele_click(self.el.one_switch)
                self.wid.wid_chk_loading()
                self.driver.ele_click(self.el.face_detection_start)
        if check_video_paly:
            search_res = self.check_video_play()
            if not search_res:
                self.log.error("视频源无法播放，fail")
                return False
        if all_screen:
            pass
        if check_snap:
            snap_res = self.check_snap()
            if not snap_res:
                return False
        if check_alarm:
            snap_res = self.check_alarm(sleep=10)
            if not snap_res:
                return False
        if snap_details:
            snap_res = self.check_snap(snap_details=True, colose=True)
            if not snap_res:
                return False
        if check_all_alarm:
            snap_res = self.into_all_alarm(sleep=10)
            if not snap_res:
                return False
        return True


if __name__ == "__main__":
    from common.w_driver import WDriver
    from v43.pub.pub_menu import MainPage

    driver = WDriver()
    driver.open_url("http://10.111.32.80:10219/#/surveillance")
    MainPage.login_in(driver, 'qjh', 'admin1234')
    test = ViedoViewPage(driver, log=driver.log, local_mod="卡口")
    test.split_screen("UI_pre_face_rtsp_1", check_video_paly=False, all_screen=False, check_snap=False,
                      snap_details=False,
                      check_alarm=False, check_all_alarm=False)