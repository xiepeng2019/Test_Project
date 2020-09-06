# -*- coding: utf-8 -*-
import time
import pytest
import allure
from allure_commons.types import AttachmentType
import shutil
import os, sys
# 告警中心
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterAlarmExport import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterAlarmSilenceSetting import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterCheckAlarmDetails import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterCheckAlarmMapModelPush import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterCheckAlarmPush import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterHistoryAlarmExport import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterHistoryAlarmFilter import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterHistoryCheckTargetAlarm import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterStartTargetAlarmFilterVideoTaskCheckAlarmPush import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterStartTargetAlarmShowExport import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterStartTargetViewExport import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterTaskSetPushRegion import *
from v43.scripts.Main_flow.main_alarm_center.AlarmCenterTaskTilterCheckAlarm import *
# 解析管理
from v43.scripts.Main_flow.main_analysis_manege.CreateAnalysisTaskCheckAnalysisInfo import *
from v43.scripts.Main_flow.main_analysis_manege.CreateAnalysisTaskCheckResults import *
from v43.scripts.Main_flow.main_analysis_manege.OperationAnalysisFile import *
from v43.scripts.Main_flow.main_analysis_manege.UploadCloudFileCheckInfo import *
# 视图源管理
from v43.scripts.Main_flow.main_camera.CameraBatEdit import *
from v43.scripts.Main_flow.main_camera.CameraBlock import *
from v43.scripts.Main_flow.main_camera.CameraBlockImportExport import *
from v43.scripts.Main_flow.main_camera.CameraBlockType import *
from v43.scripts.Main_flow.main_camera.CameraCheckAndEdit import *
from v43.scripts.Main_flow.main_camera.CameraFilter import *
from v43.scripts.Main_flow.main_camera.CameraGroupCheckEdit import *
from v43.scripts.Main_flow.main_camera.CameraGroupDelSearch import *
from v43.scripts.Main_flow.main_camera.CameraGroupNew import *
from v43.scripts.Main_flow.main_camera.CameraImport import *
from v43.scripts.Main_flow.main_camera.CameraNew import *
from v43.scripts.Main_flow.main_camera.CameraRecovery import *
# 查重
from v43.scripts.Main_flow.main_check_repeat.CreateCheckRepeatTaskCheckResults import *
from v43.scripts.Main_flow.main_check_repeat.CreateCompareBetweenByLibsCheckResults import *
from v43.scripts.Main_flow.main_check_repeat.FilterCheckRepeatTask import *
from v43.scripts.Main_flow.main_check_repeat.FilterTaskResult import *
from v43.scripts.Main_flow.main_check_repeat.RebootDeleteCheckRepeatTask import *
from v43.scripts.Main_flow.main_check_repeat.ViewCheckRepeatTaskDetail import *
# 人群分析
from v43.scripts.Main_flow.main_crowd_analyze.CheckCrowdAlarmDetailWeb import *
from v43.scripts.Main_flow.main_crowd_analyze.CheckCrowdAnalyzeWeb import *
from v43.scripts.Main_flow.main_crowd_analyze.CrowdAlarmCard import *
from v43.scripts.Main_flow.main_crowd_analyze.CrowdAlarmDetailRelatedOperation import *
from v43.scripts.Main_flow.main_crowd_analyze.CrowdSettingAllTypeTask import *
from v43.scripts.Main_flow.main_crowd_analyze.ExportCrowdAlarmRecord import *
from v43.scripts.Main_flow.main_crowd_analyze.FilterCrowdAlarmRecord import *
from v43.scripts.Main_flow.main_crowd_analyze.FilterCrowdTask import *
from v43.scripts.Main_flow.main_crowd_analyze.ModifyCrowdTaskStatus import *
# 入库助手
from v43.scripts.Main_flow.main_into_lib_assistant.IntoStaticLib import *
from v43.scripts.Main_flow.main_into_lib_assistant.IntoStaticLibFolderTask import *
from v43.scripts.Main_flow.main_into_lib_assistant.IntoTargetFolderLib import *
from v43.scripts.Main_flow.main_into_lib_assistant.IntoTargetLibTask import *
# 人像库管理
from v43.scripts.Main_flow.main_library.LibAlertPortraitSearchFilter import *
from v43.scripts.Main_flow.main_library.LibAlertPortraitUpdateDel import *
from v43.scripts.Main_flow.main_library.LibraryAlertCreateSort import *
from v43.scripts.Main_flow.main_library.LibraryStaticCreateSort import *
from v43.scripts.Main_flow.main_library.LibraryUpdateDel import *
from v43.scripts.Main_flow.main_library.LibStaticPortraitSearchFilter import *
from v43.scripts.Main_flow.main_library.LibStaticPortraitUpdateDel import *
# 退出
from v43.scripts.Main_flow.main_login.Logout import *
# 个人中心
from v43.scripts.Main_flow.main_personal_center.AdminEditorPersonalInfo import *
from v43.scripts.Main_flow.main_personal_center.ApplyNoPassRepeatEdit import *
from v43.scripts.Main_flow.main_personal_center.ApplyTaskProcess import *
from v43.scripts.Main_flow.main_personal_center.ApprovePermissionCreateTask import *
from v43.scripts.Main_flow.main_personal_center.CheckPermissionCreateTaskProcess import *
from v43.scripts.Main_flow.main_personal_center.FilterSearchEvent import *
from v43.scripts.Main_flow.main_personal_center.PersonFaceSearch import *
from v43.scripts.Main_flow.main_personal_center.PersonIntSearch import *
from v43.scripts.Main_flow.main_personal_center.PersonLibSearch import *
from v43.scripts.Main_flow.main_personal_center.PersonPedSearch import *
from v43.scripts.Main_flow.main_personal_center.PersonVehSearch import *
from v43.scripts.Main_flow.main_personal_center.view_apply_task_detail import *
# 区域碰撞
from v43.scripts.Main_flow.main_region_collision.AddCollisionTaskCheckResults import *
from v43.scripts.Main_flow.main_region_collision.CheckSearchCollisionTask import *
from v43.scripts.Main_flow.main_region_collision.StopCollisionTask import *
# 智能检索
from v43.scripts.Main_flow.main_search.compose_search.ComImgSearch import *
from v43.scripts.Main_flow.main_search.compose_search.ComImgSearchFavorite import *
from v43.scripts.Main_flow.main_search.compose_search.ComImgSearchHistory import *
from v43.scripts.Main_flow.main_search.compose_search.ComImgSearchSelect import *
from v43.scripts.Main_flow.main_search.compose_search.ComImgSearchTrace import *
from v43.scripts.Main_flow.main_search.compose_search.ComImgSearchTraceDupTarget import *
from v43.scripts.Main_flow.main_search.compose_search.ComTxtIDSearch import *
from v43.scripts.Main_flow.main_search.compose_search.ComTxtPlateSearch import *
# 时空过滤
from v43.scripts.Main_flow.main_search.timespace.TimespaceSearchExport import *
# 系统设置
from v43.scripts.Main_flow.main_setting.MainSetting import *
# 卡口
from v43.scripts.Main_flow.main_surveillance.AdminFourSplitScreenFunction import *
from v43.scripts.Main_flow.main_surveillance.AdminOneFourSplitScreen import *
from v43.scripts.Main_flow.main_surveillance.AdminOneSplitScreenFunction import *
# 技战法
from v43.scripts.Main_flow.main_tactics.ViewContinueAppearTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewContinueAppearTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewDayHideNightOutTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewDayHideNightOutTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewFirstAppearTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewFirstAppearTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewIdentifyLeaveTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewIdentifyLeaveTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewOftenPassTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewOftenPassTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewPeerAnalyzeTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewPeerAnalyzeTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewTSCrashTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewTSCrashTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewTSFileFilterTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewTSFileFilterTaskResultDetailFileDetail import *
from v43.scripts.Main_flow.main_tactics.ViewAccuratePeerAnalyzeTaskDetail import *
from v43.scripts.Main_flow.main_tactics.ViewAccuratePeerAnalyzeTaskResultDetailFileDetail import *
# 布控
from v43.scripts.Main_flow.main_task.AdminAddTask import *
from v43.scripts.Main_flow.main_task.AdminAlarmScreen import *
from v43.scripts.Main_flow.main_task.AdminCheckAlarmDetails import *
from v43.scripts.Main_flow.main_task.AdminCheckAlarmHistory import *
from v43.scripts.Main_flow.main_task.AdminCheckAlarmTrack import *
from v43.scripts.Main_flow.main_task.AdminCheckEditorStopCloneTask import *
from v43.scripts.Main_flow.main_task.AdminCheckMessage import *
from v43.scripts.Main_flow.main_task.AdminCheckTaskVideoDetails import *
from v43.scripts.Main_flow.main_task.AdminExportAlarm import *
from v43.scripts.Main_flow.main_task.AdminQueryTask import *
from v43.scripts.Main_flow.main_task.AdminSetAlarmPushMethod import *
from v43.scripts.Main_flow.main_task.AdminSetSilenceTarget import *
from v43.scripts.Main_flow.main_task.AdminTaskCheckMap import *
# 任务中心
from v43.scripts.Main_flow.main_task_center.AdminSearchTaskOpTask import *
# 角色管理
from v43.scripts.Main_flow.main_user_role.RoleCRUD import *
from v43.scripts.Main_flow.main_user_role.RoleSearch import *
from v43.scripts.Main_flow.main_user_role.UserCRUD import *
from v43.scripts.Main_flow.main_user_role.UserDep import *
from v43.scripts.Main_flow.main_user_role.UserSearch import *
# 照片一比一
from v43.scripts.Main_flow.main_video_tool.one_to_one.LibImgPk import *
from v43.scripts.Main_flow.main_video_tool.one_to_one.UploadImgPk import *

import logging
from common.log import log_config
from v43.base_class import dft_conf
import time, threading
from datetime import datetime
from PIL import ImageGrab
from cv2 import *
import numpy as np

# from pynput import keyboard

tst_cfg = dft_conf()
tst_cfg['log'] = log_config(f_level=logging.INFO, c_level=logging.INFO, out_path='.',
                            filename='tmp', fix=True)[0]


@allure.feature('主流程')  # feature定义功能
class TestMain_flow():
    boo_isVideo = False  # 是否开启视频录制

    def setup(self):
        if self.boo_isVideo:  # 是否开启视频录制
            self.flag = True  # 录制视频开始标识
            th = threading.Thread(target=self.video_record)  # 创建一个线程
            th.start()  # 启动线程

    def teardown(self):
        if self.boo_isVideo:  # 是否开启视频录制
            self.flag = True  # 结束录制
            time.sleep(1)  # 等待视频释放过后
            # # allue添加视频
            file = open("执行视频.mp4", 'rb').read()  # 临时视频，新用例运行结果会覆盖
            allure.attach(file, '执行视频', allure.attachment_type.MP4)

    #
    # @allure.story('告警中心')
    # def test_AlarmCenterAlarmExport(self): assert not AlarmCenterAlarmExport(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterAlarmSilenceSetting(self): assert not AlarmCenterAlarmSilenceSetting(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterCheckAlarmDetails(self): assert not AlarmCenterCheckAlarmDetails(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterCheckAlarmMapModelPush(self): assert not AlarmCenterCheckAlarmMapModelPush(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterCheckAlarmPush(self): assert not AlarmCenterCheckAlarmPush(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterHistoryAlarmExport(self): assert not AlarmCenterHistoryAlarmExport(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterHistoryAlarmFilter(self): assert not AlarmCenterHistoryAlarmFilter(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterHistoryCheckTargetAlarm(self): assert not AlarmCenterHistoryCheckTargetAlarm(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterStartTargetAlarmFilterVideoTaskCheckAlarmPush(self): assert not AlarmCenterStartTargetAlarmFilterVideoTaskCheckAlarmPush(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterStartTargetAlarmShowExport(self): assert not AlarmCenterStartTargetAlarmShowExport(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterStartTargetViewExport(self): assert not AlarmCenterStartTargetViewExport(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterTaskSetPushRegion(self): assert not AlarmCenterTaskSetPushRegion(config=tst_cfg).run(True)['test_error'];
    # @allure.story('告警中心')
    # def test_AlarmCenterTaskTilterCheckAlarm(self): assert not AlarmCenterTaskTilterCheckAlarm(config=tst_cfg).run(True)['test_error'];
    #
    # @allure.story('解析管理')
    # def test_CreateAnalysisTaskCheckAnalysisInfo(self): assert not CreateAnalysisTaskCheckAnalysisInfo(config=tst_cfg).run(True)['test_error']
    # @allure.story('解析管理')
    # def test_CreateAnalysisTaskCheckResults(self): assert not CreateAnalysisTaskCheckResults(config=tst_cfg).run(True)['test_error']
    # @allure.story('解析管理')
    # def test_OperationAnalysisFile(self): assert not OperationAnalysisFile(config=tst_cfg).run(True)['test_error']
    # @allure.story('解析管理')
    # def test_UploadCloudFileCheckInfo(self): assert not UploadCloudFileCheckInfo(config=tst_cfg).run(True)['test_error']
    #
    # @allure.story('视图源管理')
    # def test_CameraBatEdit(self): assert not CameraBatEdit(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraBlock(self): assert not CameraBlock(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraBlockImportExport(self): assert not CameraBlockImportExport(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraBlockType(self): assert not CameraBlockType(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraCheckAndEdit(self): assert not CameraCheckAndEdit(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraFilter(self): assert not CameraFilter(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraGroupCheckEdit(self): assert not CameraGroupCheckEdit(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraGroupDelSearch(self): assert not CameraGroupDelSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraGroupNew(self): assert not CameraGroupNew(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraImport(self): assert not CameraImport(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraNew(self): assert not CameraNew(config=tst_cfg).run(True)['test_error']
    # @allure.story('视图源管理')
    # def test_CameraRecovery(self): assert not CameraRecovery(config=tst_cfg).run(True)['test_error']
    #
    # @allure.story('查重')
    # def test_CreateCheckRepeatTaskCheckResults(self): assert not CreateCheckRepeatTaskCheckResults(config=tst_cfg).run(True)['test_error']
    # @allure.story('查重')
    # def test_CreateCompareBetweenByLibsCheckResults(self): assert not CreateCompareBetweenByLibsCheckResults(config=tst_cfg).run(True)['test_error']
    # @allure.story('查重')
    # def test_FilterCheckRepeatTask(self): assert not FilterCheckRepeatTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('查重')
    # def test_FilterTaskResult(self): assert not FilterTaskResult(config=tst_cfg).run(True)['test_error']
    # @allure.story('查重')
    # def test_RebootDeleteCheckRepeatTask(self): assert not RebootDeleteCheckRepeatTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('查重')
    # def test_ViewCheckRepeatTaskDetail(self): assert not ViewCheckRepeatTaskDetail(config=tst_cfg).run(True)['test_error']
    #
    # @allure.story('人群分析')
    # def test_CheckCrowdAlarmDetailWeb(self): assert not CheckCrowdAlarmDetailWeb(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_CheckCrowdAnalyzeWeb(self): assert not CheckCrowdAnalyzeWeb(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_crowd_alarm_card(self): assert not CrowdAlarmCard(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_crowd_alarm_detail_related_operation(self): assert not CrowdAlarmDetailRelatedOperation(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_CrowdSettingAllTypeTask(self): assert not CrowdSettingAllTypeTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_ExportCrowdAlarmRecord(self): assert not ExportCrowdAlarmRecord(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_FilterCrowdAlarmRecord(self): assert not FilterCrowdAlarmRecord(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_FilterCrowdTask(self): assert not FilterCrowdTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('人群分析')
    # def test_ModifyCrowdTaskStatus(self): assert not ModifyCrowdTaskStatus(config=tst_cfg).run(True)['test_error']
    #
    # @allure.story('入库助手')
    # def test_into_static_lib_task(self): assert not IntoStaticLib(config=tst_cfg).run(True)['test_error']
    # @allure.story('入库助手')
    # def test_into_target_lib_folder_task(self): assert not IntoStaticLibFolderTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('入库助手')
    # def test_into_target_lib_task(self): assert not IntoTargetFolderLib(config=tst_cfg).run(True)['test_error']
    # @allure.story('入库助手')
    # def test_IntoStaticLibFolderTask(self): assert not IntoTargetLibTask(config=tst_cfg).run(True)['test_error']
    #
    # @allure.story('人像库管理')
    # def test_LibAlertPortraitSearchFilter(self): assert not LibAlertPortraitSearchFilter(config=tst_cfg).run(True)['test_error']
    # @allure.story('人像库管理')
    # def test_LibAlertPortraitUpdateDel(self): assert not LibAlertPortraitUpdateDel(config=tst_cfg).run(True)['test_error']
    # @allure.story('人像库管理')
    # def test_LibraryAlertCreateSort(self): assert not LibraryAlertCreateSort(config=tst_cfg).run(True)['test_error']
    # @allure.story('人像库管理')
    # def test_LibraryStaticCreateSort(self): assert not LibraryStaticCreateSort(config=tst_cfg).run(True)['test_error']
    # @allure.story('人像库管理')
    # def test_LibraryUpdateDel(self): assert not LibraryUpdateDel(config=tst_cfg).run(True)['test_error']
    # @allure.story('人像库管理')
    # def test_LibStaticPortraitSearchFilter(self): assert not LibStaticPortraitSearchFilter(config=tst_cfg).run(True)['test_error']
    # @allure.story('人像库管理')
    # def test_LibStaticPortraitUpdateDel(self): assert not LibStaticPortraitUpdateDel(config=tst_cfg).run(True)['test_error']
    #
    # @allure.story('退出')
    # def test_Logout(self):assert not Logout(config=tst_cfg).run(True)['test_error']
    #
    # @allure.story('个人中心')
    # def test_AdminEditorPersonalInfo(self): assert not AdminEditorPersonalInfo(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_ApplyNoPassRepeatEdit(self): assert not ApplyNoPassRepeatEdit(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_ApplyTaskProcess(self): assert not ApplyTaskProcess(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_ApprovePermissionCreateTask(self): assert not ApprovePermissionCreateTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_CheckPermissionCreateTaskProcess(self): assert not CheckPermissionCreateTaskProcess(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_FilterSearchEvent(self): assert not FilterSearchEvent(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_PersonFaceSearch(self): assert not PersonFaceSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_PersonIntSearch(self): assert not PersonIntSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_PersonLibSearch(self): assert not PersonLibSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_PersonPedSearch(self): assert not PersonPedSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_PersonVehSearch(self): assert not PersonVehSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('个人中心')
    # def test_ViewApplyTaskDetail(self): assert not ViewApplyTaskDetail(config=tst_cfg).run(True)['test_error']
    # #
    # @allure.story('区域碰撞')
    # def test_AddCollisionTaskCheckResults(self): assert not AddCollisionTaskCheckResults(config=tst_cfg).run(True)['test_error']
    # @allure.story('区域碰撞')
    # def test_CheckSearchCollisionTask(self): assert not CheckSearchCollisionTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('区域碰撞')
    # def test_StopCollisionTask(self): assert not StopCollisionTask(config=tst_cfg).run(True)['test_error']

    # @allure.story('任务中心')
    # def test_AdminSearchTaskOpTask(self): assert not AdminSearchTaskOpTask(config=tst_cfg).run(True)['test_error']
    # #
    # @allure.story('智能检索')
    # def test_ComImgSearch(self): assert not ComImgSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('智能检索')
    # def test_ComImgSearchFavorite(self): assert not ComImgSearchFavorite(config=tst_cfg).run(True)['test_error']
    # @allure.story('智能检索')
    # def test_ComImgSearchHistory(self): assert not ComImgSearchHistory(config=tst_cfg).run(True)['test_error']
    # @allure.story('智能检索')
    # def test_ComImgSearchSelect(self): assert not ComImgSearchSelect(config=tst_cfg).run(True)['test_error']
    # @allure.story('智能检索')
    # def test_ComImgSearchTrace(self): assert not ComImgSearchTrace(config=tst_cfg).run(True)['test_error']
    # @allure.story('智能检索')
    # def test_ComImgSearchTraceDupTarget(self): assert not ComImgSearchTraceDupTarget(config=tst_cfg).run(True)['test_error']
    # @allure.story('智能检索')
    # def test_ComTxtIDSearch(self): assert not ComTxtIDSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('智能检索')
    # def test_ComTxtPlateSearch(self): assert not ComTxtPlateSearch(config=tst_cfg).run(True)['test_error']
    # #
    # @allure.story('时空过滤')
    # def test_TimespaceSearchExport(self): assert not TimespaceSearchExport(config=tst_cfg).run(True)['test_error']
    # #
    # @allure.story('系统设置')
    # def test_MainSetting(self): assert not MainSetting(config=tst_cfg).run(True)['test_error']
    # #
    # @allure.story('卡口')
    # def test_AdminFourSplitScreenFunction(self): assert not AdminFourSplitScreenFunction(config=tst_cfg).run(True)['test_error']
    # @allure.story('卡口')
    # def test_AdminOneFourSplitScreen(self): assert not AdminOneFourSplitScreen(config=tst_cfg).run(True)['test_error']
    # @allure.story('卡口')
    # def test_AdminFourSplitScreenFunction(self): assert not CheckSplitScreenFunction(config=tst_cfg).run(True)['test_error']
    #
    @allure.story('技战法')
    def test_ViewContinueAppearTaskDetail(self):
        assert not ViewContinueAppearTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewContinueAppearTaskResultDetailFileDetail(self):
        assert not ViewContinueAppearTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewDayHideNightOutTaskDetail(self):
        assert not ViewDayHideNightOutTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewDayHideNightOutTaskResultDetailFileDetail(self):
        assert not ViewDayHideNightOutTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewFirstAppearTaskDetail(self):
        assert not ViewFirstAppearTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewFirstAppearTaskResultDetailFileDetail(self):
        assert not ViewFirstAppearTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewIdentifyLeaveTaskDetail(self):
        assert not ViewIdentifyLeaveTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewIdentifyLeaveTaskResultDetailFileDetail(self):
        assert not ViewIdentifyLeaveTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewOftenPassTaskDetail(self):
        assert not ViewOftenPassTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewOftenPassTaskResultDetailFileDetail(self):
        assert not ViewOftenPassTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewPeerAnalyzeTaskDetail(self):
        assert not ViewPeerAnalyzeTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewPeerAnalyzeTaskResultDetailFileDetail(self):
        assert not ViewPeerAnalyzeTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewTSCrashTaskDetail(self):
        assert not ViewTSCrashTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewTSCrashTaskResultDetailFileDetail(self):
        assert not ViewTSCrashTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewTSFileFilterTaskDetail(self):
        assert not ViewTSFileFilterTaskDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewTSFileFilterTaskResultDetailFileDetail(self):
        assert not ViewTSFileFilterTaskResultDetailFileDetail(config=tst_cfg).run(True)['test_error']

    @allure.story('技战法')
    def test_ViewAccuratePeerAnalyzeTaskDetail(self):
        assert not ViewAccuratePeerAnalyzeTaskDetail(config=tst_cfg).run(True)["test_error"]

    # @allure.story('布控')
    # def test_AdminAddTask(self): assert not AdminAddTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminAlarmScreen(self): assert not AdminAlarmScreen(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminCheckAlarmDetails(self): assert not AdminCheckAlarmDetails(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminCheckAlarmHistory(self): assert not AdminCheckAlarmHistory(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminCheckAlarmTrack(self): assert not AdminCheckAlarmTrack(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminCheckEditorStopCloneTask(self): assert not AdminCheckEditorStopCloneTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminCheckMessage(self): assert not AdminCheckMessage(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminCheckTaskVideoDetails(self): assert not AdminCheckTaskVideoDetails(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminExportAlarm(self): assert not AdminExportAlarm(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminQueryTask(self): assert not AdminQueryTask(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminSetAlarmPushMethod(self): assert not AdminSetAlarmPushMethod(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminSetSilenceTarget(self): assert not AdminSetSilenceTarget(config=tst_cfg).run(True)['test_error']
    # @allure.story('布控')
    # def test_AdminTaskCheckMap(self): assert not AdminTaskCheckMap(config=tst_cfg).run(True)['test_error']
    # #
    # #
    # @allure.story('角色管理')
    # def test_RoleCRUD(self): assert not RoleCRUD(config=tst_cfg).run(True)['test_error']
    # @allure.story('角色管理')
    # def test_RoleSearch(self): assert not RoleSearch(config=tst_cfg).run(True)['test_error']
    # @allure.story('角色管理')
    # def test_UserCRUD(self): assert not UserCRUD(config=tst_cfg).run(True)['test_error']
    # @allure.story('角色管理')
    # def test_UserDep(self): assert not UserDep(config=tst_cfg).run(True)['test_error']
    # @allure.story('角色管理')
    # def test_UserSearch(self): assert not UserSearch(config=tst_cfg).run(True)['test_error']
    # #
    # @allure.story('照片一比一')
    # def test_LibImgPk(self): assert not LibImgPk(config=tst_cfg).run(True)['test_error']
    # @allure.story('照片一比一')
    # def test_UploadImgPk(self): assert not UploadImgPk(config=tst_cfg).run(True)['test_error']

    def video_record(self, name=None):  # 录入视频
        # name = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # 当前的时间（当文件名）
        name = "执行视频"  # 视频名称
        screen = ImageGrab.grab()  # 获取当前屏幕
        width, high = screen.size  # 获取当前屏幕的大小
        fourcc = VideoWriter_fourcc('X', 'V', 'I', 'D')  # MPEG-4编码,文件后缀可为.avi .asf .mov等
        video = VideoWriter('%s.mp4' % name, fourcc, 15, (width, high))  # （文件名，编码器，帧率，视频宽高）
        # print('3秒后开始录制----')  # 可选
        # time.sleep(3)
        print('开始录制!')
        global start_time
        start_time = time.time()
        while True:
            if self.flag:
                print("录制结束！")
                global final_time
                final_time = time.time()
                video.release()  # 释放
                break
            im = ImageGrab.grab()  # 图片为RGB模式
            imm = cvtColor(np.array(im), COLOR_RGB2BGR)  # 转为opencv的BGR模式
            video.write(imm)  # 写入
            # time.sleep(5) # 等待5秒再次循环


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    if os.path.exists(filepath):
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


if __name__ == '__main__':
    print(11111)
    del_file("report/temp")  # 删除默认的路径的报告数据
    allurePath = "D:/allure-2.13.5/"  # allure安装路径
    reportData = 'report/temp/xml'  # 成报告数据路径
    moduleName = "report/告警中心/html"  # 生成报告数据路径

    # 生成配置信息 "-s 代表可以将执行成功的案例日志打印出来 ; -q+文件执行路径 代表只需要执行的文件"
    # pytest.main(['-s','-q', 'UItest.py', '--alluredir', reportData]) # 执行用例，并生成报告数据
    pytest.main(['-s', '--lf', '-q', 'UItest.py', '--alluredir', reportData])  # 如果要重新运行失败用例，用改行执行脚本。
    print(time.ctime())
    # os.system(allurePath + "bin/allure.bat " # allure安装路径
    # "generate " #命令参数
    # + reportData + #报告数据路径
    # " -o "  #命令参数
    # + moduleName + " --clean") # 报告数据生成HTML路径

