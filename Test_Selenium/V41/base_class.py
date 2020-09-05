#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import traceback

import sys
import re

import requests
from selenium.common.exceptions import WebDriverException

from common import common_func
from common.w_driver import WDriver
from common.common_func import *
from sc_common.sc_define import define, define_camera
from v43.pub.pub_camera import CameraModule
from v43.pub.pub_library import CreateLibPor
from v43.pub.pub_menu import MainPage
from v43.pub.pub_personal_center import PersonalCenterPage
from v43.pub.pub_role import RoleModule
from v43.pub.pub_search import *
from v43.pub.pub_sys_setting import SettingModule
from v43.pub.pub_task import TaskPage
from v43.pub.pub_user_manage import UserModule
from v43.pub.pub_video_tool import VideoToolModule
from v43.pub.pub_video_view import ViedoViewPage
from v43.pub.pub_alarm_center import AlarmCenterAction
from v43.pub.pub_personal_center import PersonalCenterPage
from v43.pub.pub_region_collision import RegionCollisionAction
from v43.pub.pub_task_center import TaskCenterPage
from v43.pub.pub_crowd_analyze import CrowAnalyzeCommon
from v43.pub.pub_into_lib_assistant import IntoLibPage
from v43.pub.pub_tactics import TacticsCommonMethod
from v43.pub.pub_analysis_manage import AnalysisAction
from v43.pub.pub_check_repeat import CheckRepeatAction
from common.log import log_define


class BaseWebCase(object):
    title = None
    project_name = "SenseCity"
    module = None
    author = None
    other_info = None
    #
    tst_title = None
    tst_case_no = None
    tst_step = None
    tst_expect = None

    def __init__(self, driver=None, config=None, **kwargs):
        # 框架相关
        # 初始参数
        self.remote_driver = None
        if config and not isinstance(config, dict):
            raise Exception("config 参数必须为 KV 形式.")
        if driver:
            self.driver = driver
            self.driver_outer = True
        else:
            if not config:  config = dft_conf()  # csf add for debug   20200428
            config and kwargs.update(config)
            kwargs['name'] = self.__class__.__name__  # self.tst_case_no
            if kwargs.get('hub_url'):
                driver_start_time = int(time.time())
                self.file_name = '{case_name}_{timestamp}'.format(case_name=kwargs.get('name'),
                                                                  timestamp=driver_start_time, )
                self.remote_driver = get_ip_in_str(kwargs.get('hub_url'))
                kwargs.update(file_name=self.file_name)
            self.driver = WDriver(**kwargs)
            self.driver_outer = False
        self.host = config and config.get('host') or kwargs.get('host')
        self.user = config and config.get('user') or kwargs.get('user')
        self.pwd = config and config.get('pwd') or kwargs.get('pwd')
        self.url = self.host
        #
        kwargs['host'] = self.host
        kwargs['user'] = self.user
        kwargs['pwd'] = self.pwd
        #
        self.log = config and config.get('log') or kwargs.get('log') or log_define(locals())
        self.cf = common_func
        # 定义
        self.test_start_time = time.time()
        self.config = config
        self.pass_flag = False
        self.error_info = None
        kwargs['log'] = self.log  # 将log装进底层
        # 业务相关 预置资源
        self.pre_camera = None  # 可能过指定参数来决定只建相关视频源 face ped face_ped car crow alarm search
        self.pre_lib = None
        self.pre_role = None
        self.pre_user = None
        self.pre_dep = None
        self.pre_task = None
        self.create_lib = None
        self.pre_check_repeat = None
        self.args_dict = kwargs
        self.into_tst_menu = True  # 默认实例后 进测试模块页
        self.pre_crowd = False  # crowd
        self.pre_crowd_video = []
        # 模块实例属性
        self.module_list = []  # 模块列表，由各用例改写
        # self.def_mod_lst = [x for x in dir(define) if x.startswith('mod')]
        self.df = define()  # 配置定义
        self.df_cam = define_camera()  # 配置定义
        self.cf = common_func  # 非业务相关 Public method
        self.mod_def = self.df.ModDefine  # 模块名列表
        self.login = True  # 是否登录，默认登录
        self.param = BaseWebCase.MethodParam
        # self.p_s_fs = self.p_s_ps = self.p_s_is = self.p_s_cs = self.p_s_ls = self.p_s_ts = self.p_s_vs = \
        #     self.p_s_ts = self.p_s_os = self.p_tsk = self.p_user = self.p_role = self.p_cam = self.p_lib = \
        #     self.p_per = self.p_home_da = self.p_home_op = self.p_op = self.p_sys = self.p_ala = None
        # self.e_s_fs = self.e_s_ps = self.e_s_is = self.e_s_cs = self.e_s_vs = self.e_s_ls = self.e_s_ts = \
        #     self.e_s_os = self.e_tsk = self.e_user = self.e_role = self.e_sys = self.e_op = self.e_home_da = \
        #     self.e_home_op = self.e_ala = self.e_cam = self.e_lib = self.e_per = None
        # self.pub_base = PublicClass(self.driver, **kwargs)

    def login_(self):
        self.host = re.findall(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', self.host)[0]
        self.url = "http://{}:{}".format(self.host, self.df.dft_url_ssh_port if self.host.startswith(
            'https') else self.df.dft_url_port)
        self.driver.open_url(self.url)
        if self.login:  # 是否登录
            login_res = MainPage.login_in(self.driver, self.user, self.pwd)
            if login_res:
                msg = "使用用户:[{}]密码:[{}]登录Web:[{}]异常".format(self.user, self.pwd, self.url)
                if isinstance(login_res, str):
                    self.log.error(login_res)
                    msg += "-异常原因:[{}]".format(login_res)
                self.set_fail(msg)
            self.log.info("Login success")

    def login_out(self):
        MainPage.login_out(driver=self.driver)

    def init_module(self, args_dict):
        mod_def = self.mod_def
        self.log.info("实例模块")
        m_list = convert_to_array(self.module_list)
        args_dict['mod_NO1'] = m_list[0]  # 将第一模块塞进底层
        if mod_def.mod_search_face in m_list:
            args_dict['local_mod'] = mod_def.mod_search_face
            self.p_s_fs = FaceSearchModule(self.driver, **args_dict)
            self.e_s_fs = self.p_s_fs.el
            self.pre_camera = 'face'
        if mod_def.mod_search_ped in m_list:
            args_dict['local_mod'] = mod_def.mod_search_ped
            self.p_s_ps = PedSearchModule(self.driver, **args_dict)
            self.e_s_ps = self.p_s_ps.el
            self.pre_camera = 'ped'
        if mod_def.mod_search_int in m_list:
            args_dict['local_mod'] = mod_def.mod_search_int
            self.p_s_is = IntSearchModule(self.driver, **args_dict)
            self.e_s_is = self.p_s_is.el
            self.pre_camera = ['face', 'ped']
        if mod_def.mod_search_com in m_list:
            args_dict['local_mod'] = mod_def.mod_search_com
            self.p_s_cs = ComSearchModule(self.driver, **args_dict)
            self.e_s_cs = self.p_s_cs.el
            self.pre_camera = ['face', 'ped']
        if mod_def.mod_search_veh in m_list:
            args_dict['local_mod'] = mod_def.mod_search_veh
            self.p_s_vs = VehSearchModule(self.driver, **args_dict)
            self.e_s_vs = self.p_s_vs.el
            self.pre_camera = 'car'
        if mod_def.mod_search_lib in m_list:
            args_dict['local_mod'] = mod_def.mod_search_lib
            self.p_s_ls = LibSearchModule(self.driver, **args_dict)
            self.e_s_ls = self.p_s_ls.el
            self.pre_lib = True
            self.param.sense_type = 1
            self.param.por_number = 65
        if mod_def.mod_search_ts in m_list:
            args_dict['local_mod'] = mod_def.mod_search_ts
            self.p_s_ts = TimeSearchModule(self.driver, **args_dict)
            self.e_s_ts = self.p_s_ts.el
            self.pre_camera = 'face'
        if mod_def.mod_search_off in m_list:
            args_dict['local_mod'] = mod_def.mod_search_off
            self.p_s_os = None
            self.e_s_os = self.p_s_os.el

        if mod_def.mod_user in m_list or mod_def.mod_role in m_list:
            args_dict['local_mod'] = mod_def.mod_user
            self.p_user = UserModule(self.driver, **args_dict)
            self.e_user = self.p_user.el
        if mod_def.mod_role in m_list or mod_def.mod_user in m_list:
            args_dict['local_mod'] = mod_def.mod_role
            self.p_role = RoleModule(self.driver, **args_dict)
            self.e_role = self.p_role.el
        if mod_def.mod_camera in m_list or mod_def.mod_task in m_list or mod_def.mod_search_face in m_list \
                or mod_def.mod_search_ped in m_list or mod_def.mod_search_int in m_list or mod_def.mod_search_com in m_list \
                or mod_def.mod_search_ts in m_list or mod_def.mod_search_veh in m_list or mod_def.mod_surveillance in m_list \
                or mod_def.mod_region in m_list or mod_def.mod_crowd in m_list or mod_def.mod_tactics in m_list:
            args_dict['local_mod'] = mod_def.mod_camera
            self.p_cam = CameraModule(self.driver, **args_dict)
            self.e_cam = self.p_cam.el
        if mod_def.mod_lib in m_list or mod_def.mod_search_lib in m_list or mod_def.mod_task in m_list or mod_def.mod_search_com in m_list:
            args_dict['local_mod'] = mod_def.mod_lib
            self.p_lib = CreateLibPor(self.driver, **args_dict)
            self.e_lib = self.p_lib.lib_por
        if mod_def.mod_person in m_list:
            args_dict['local_mod'] = mod_def.mod_person
            self.p_per = PersonalCenterPage(self.driver, **args_dict)
            self.e_per = self.p_per.el
        if mod_def.mod_home_data in m_list:
            args_dict['local_mod'] = mod_def.mod_home_data
            self.p_home_da = None
            self.e_home_da = self.p_home_da.el
        if mod_def.mod_home_op in m_list:
            args_dict['local_mod'] = mod_def.mod_home_op
            self.p_home_op = None
            self.e_home_op = self.p_home_op.el
        if mod_def.mod_op in m_list:
            args_dict['local_mod'] = mod_def.mod_op
            self.p_op = None
            self.e_op = self.p_op.el
        if mod_def.mod_system in m_list:
            args_dict['local_mod'] = mod_def.mod_system
            self.p_sys = SettingModule(self.driver, **args_dict)
            self.e_sys = self.p_sys.el
        if mod_def.mod_alarm in m_list:
            args_dict['local_mod'] = mod_def.mod_alarm
            self.p_ala = AlarmCenterAction(self.driver, **args_dict)
            self.e_ala = self.p_ala.el
        if mod_def.mod_task in m_list:
            args_dict['local_mod'] = mod_def.mod_task
            self.p_tsk = TaskPage(self.driver, **args_dict)
            self.e_tsk = self.p_tsk.el
            self.pre_camera = 'face'
        if mod_def.mod_surveillance in m_list:
            args_dict['local_mod'] = mod_def.mod_surveillance
            self.p_sl = ViedoViewPage(self.driver, **args_dict)
            self.e_sl = self.p_sl.el
            self.pre_camera = 'face'
        if mod_def.mod_view_tool in m_list:
            args_dict['local_mod'] = mod_def.mod_view_tool
            self.p_tool = VideoToolModule(self.driver, **args_dict)
            self.e_tool = self.p_tool.el
        if mod_def.mod_region in m_list:
            args_dict['local_mod'] = mod_def.mod_region
            self.p_reg = RegionCollisionAction(self.driver, **args_dict)
            self.e_reg = self.p_reg.el
            self.pre_camera = 'face'
        if mod_def.mod_task_center in m_list:
            args_dict['local_mod'] = mod_def.mod_task_center
            self.p_task_center = TaskCenterPage(self.driver, **args_dict)
            self.e_task_center = self.p_task_center.el
        if mod_def.mod_crowd in m_list:
            args_dict['local_mod'] = mod_def.mod_crowd
            self.p_crowd = CrowAnalyzeCommon(self.driver, **args_dict)
            self.e_crowd = self.p_crowd.crowd_ele
            self.pre_camera = []
            self.pre_camera.append('ped') if '结构化' in self.pre_crowd_video else None
            self.pre_camera.append('crowd') if '人群分析' in self.pre_crowd_video else None
        if mod_def.mod_into_lib in m_list:
            args_dict['local_mod'] = mod_def.mod_into_lib
            self.p_into_lib = IntoLibPage(self.driver, **args_dict)
            self.e_into_lib = self.p_into_lib.el
        if mod_def.mod_tactics in m_list:
            args_dict['local_mod'] = mod_def.mod_tactics
            self.p_tactics = TacticsCommonMethod(self.driver, **args_dict)
            self.e_tactics = self.p_tactics.tactics_ele
            self.pre_camera = 'face'
        if mod_def.mod_analysis in m_list:
            args_dict['local_mod'] = mod_def.mod_analysis
            self.p_analysis = AnalysisAction(self.driver, **args_dict)
            self.e_analysis = self.p_analysis.el
        if mod_def.mod_checkrepeat in m_list:
            args_dict['local_mod'] = mod_def.mod_checkrepeat
            self.p_checkrepeat = CheckRepeatAction(self.driver, **args_dict)
            self.e_checkrepeat = self.p_checkrepeat.el

    # 用例前置
    def pre_set(self):
        """
        预置资源
        :return:
        """
        # if not self.driver_outer:
        #     self.login_()
        self.login_()
        self.init_module(self.args_dict)
        # self.driver.refresh_driver()
        if self.pre_lib:
            self.p_lib.into_menu()
            for senset_type in convert_to_array(self.param.sense_type):
                pre_lib = self.p_lib.pre_lib_por(sense_type=senset_type, number=self.param.por_number)
                if not pre_lib:
                    raise Exception("预置库失败")
                self.pre_lib_name = pre_lib.get("library_name")
                self.pre_por_name = pre_lib.get("portrait_name")
        if self.create_lib:
            self.p_lib.into_menu()
            create_lib = self.p_lib.create_lib_add_por(library_name=self.param.library_name,
                                                       portrait_name=self.param.portrait_name,
                                                       sense_type=self.param.sense_type, image_=self.param.image_,
                                                       import_name=self.param.import_name, identity=self.param.identity,
                                                       por_remark=self.param.por_remark,
                                                       por_gender=self.param.por_gender,
                                                       por_address=self.param.por_address, por_area=self.param.por_area,
                                                       back=self.param.back, upload_=self.param.upload_,
                                                       import_=self.param.import_)
            if not create_lib or not isinstance(create_lib, dict):
                raise Exception("新增库失败")
            self.create_lib_name = create_lib.get("library_name")
            self.create_por_name = create_lib.get("portrait_name")
        if self.pre_camera:
            self.p_cam.into_menu()
            self.p_cam.pre_dep_camera(camera_use=self.pre_camera)
        if self.pre_dep:
            pass
        if self.pre_role:
            pass
        if self.pre_user:
            self.p_user.into_menu()
            self.p_user.pre_task_user()
            pass
        if self.pre_task:
            pass
        if self.pre_check_repeat:
            self.repeat_task_name = self.p_checkrepeat.into_menu('查重')
        if self.pre_crowd:
            self.p_crowd.into_menu()
            self.p_crowd.pre_crowd()
        if self.pre_check_repeat:
            self.p_checkrepeat.into_menu()
            self.p_checkrepeat.pre_check_repeat_task()
        # 进测试模块页
        if self.into_tst_menu:  # 默认为 进测试模块，个性化前置时可设为False
            MainPage.into_menu(self.driver, self.args_dict.get('mod_NO1'))  # 多模块时的第一导航

    def print_log(self, func_result, resource_name, *args, **kwargs):
        """
        csf 用于清理环境时 捕获异常，不影响其它资源的清理
        :param log:
        :param func_result:
        :param resource_name:
        :param args:
        :param kwargs:
        :return:
        """
        log_ = self.log
        try:
            if func_result(*args, **kwargs):
                log_.warning("清理-[{}]-数据完毕".format(resource_name))
            else:
                log_.error("清理-[{}]-数据出现 ERROR ....".format(resource_name))
        except WebDriverException as e:
            self.driver_offline(e)
            log_.error(str(traceback.format_exc()))
            log_.error("ERROR: 清理-[{}]-数据  公共方法出现异常，捕捉打印, 继续下一个清理 ....".format(resource_name))
        except:
            log_.error(str(traceback.format_exc()))
            log_.error("ERROR: 清理-[{}]-数据  公共方法出现异常，捕捉打印, 继续下一个清理 ....".format(resource_name))

    # 资源清理
    def clean_env(self):
        """
        各模块清理，模块间清理独立，互不影响
        :return:
        """
        log_ = self.log
        log_.warning("<====== 清理环境  Start ===========>")
        try:
            if not hasattr(log_, "bag"):
                return
            filter_src = lambda src_key: list(
                set([x for x in log_.bag[self.df.store_key][src_key] if not x.startswith(pre_flag)]))
            pre_flag = self.df.pre_res
            cam_lst = filter_src(self.df.key_camera)
            grp_lst = filter_src(self.df.key_camera_group)
            user_lst = filter_src(self.df.key_user)
            role_lst = filter_src(self.df.key_role)
            dep_lst = filter_src(self.df.key_dep)
            crowd_task_list = filter_src(self.df.key_crowd_task)
            check_repeat_list = filter_src(self.df.key_check_repeat)
            cam_blk_lst = filter_src(self.df.key_camera_block)
            lib_alert_list = filter_src(self.df.key_lib)
            lib_static_list = filter_src(self.df.key_static_lib)
            task_name_list = filter_src(self.df.key_task)
            # task_name_list.append("UI_")
            region_task_list = filter_src(self.df.key_region_task)
            into_lib_task_list = filter_src(self.df.key_into_lib_task)
            if task_name_list:
                for tak_name in task_name_list:
                    self.print_log(self.p_tsk.stop_task, "布控清理", tak_name)
            if crowd_task_list:
                for i in crowd_task_list:
                    self.print_log(self.p_crowd.terminate, "人群任务", video_name=i)
            if cam_lst or grp_lst or cam_blk_lst:
                self.print_log(self.p_cam.del_all_camera_group, "视频源及分组", root_dep=grp_lst, camera_lst=cam_lst,
                               cam_blk_lst=cam_blk_lst)

            for i in lib_alert_list:
                self.print_log(self.p_lib.delete_library, "布控库", library_name=i, sense_type=1)

            for i in lib_static_list:
                self.print_log(self.p_lib.delete_library, "静态库", library_name=i, sense_type=2)

            for i in region_task_list:
                self.print_log(self.p_reg.delete_region_task, "区域碰撞任务", name=i)
            for i in into_lib_task_list:
                self.print_log(self.p_into_lib.delete_into_lib_task, "入库任务", name=i)
            if check_repeat_list:
                for i in check_repeat_list:
                    self.print_log(self.p_checkrepeat.delete_check_repeat_task, '查重清理', task_name=i)
            if user_lst or role_lst or dep_lst:
                self.print_log(self.p_user.del_user_role_dep, "用户/部门/角色", users=user_lst, roles=role_lst, deps=dep_lst)

        except Exception as e:
            log_.error("<====== 清理数据 出现异常(不影响主测试体 测试结果), 请排查以上清理环境信息 ======>")
            log_.error(e)
        else:
            log_.warning("<====== 清理数据 End ======>")
        finally:
            try:
                if self.driver_outer:
                    self.driver.refresh_driver()
                    self.login_out()
                else:
                    self.driver.quit()
            except WebDriverException as e:
                self.driver_offline(e)

    class MethodParam:
        # 预置库参数
        sense_type = 1
        por_number = 1

        # 新增库参数
        library_name = get_random_name(name_prefix=define.name_prefix)
        portrait_name = get_random_name(name_prefix="por_")
        image_ = define.ImgDef.face2_1
        import_name = define.ImgDef.Lz_65_zip
        identity = None
        por_remark = None
        por_gender = None
        por_address = None
        por_area = None
        back = False
        upload_ = True
        import_ = False

    # 用例运行
    def run(self, local_exec=False):
        driver_online = True
        try:
            self.tst_start()
            self.pre_condition()
            self.try_catch("预置", self.pre_set)
            tst_return = self.try_catch("测试体", self.action)
        except WebDriverException as e:
            driver_online = False
            self.driver_offline(e)
            self.error_info = str(traceback.format_exc())
        except Exception:
            self.error_info = str(traceback.format_exc())
        else:
            if isinstance(tst_return, bool):
                tst_return and self.set_pass()
        finally:
            driver_online and self.try_catch("清理环境", self.clean_env)
            self.result = "Pass" if self.pass_flag else "Fail" if not self.error_info else "Error"
            self.tst_result()
            if not local_exec:
                return self.pass_flag
            result_dict = {
                'test_result': self.result,
                'test_case': self.tst_case_no,
                'test_name': self.title,
                'test_expect': self.tst_expect,
                'test_step': self.tst_step,
                'script_author': self.author,
                'test_error': self.error_info,
                'test_log': self.log.name
            }
            return result_dict

    # 用例动作
    def action(self):
        pass

    def pre_condition(self):
        """
        预置资源 标志位
        :return:
        """
        pass

    def set_fail(self, msg=None):
        if msg:
            self.log.error("Error: {}".format(msg))
        self.pass_flag = False
        error_msg = msg or "出现与预期不符情况,用例已经Fail"
        raise Exception(error_msg)

    def set_pass(self):
        self.pass_flag = True

    def tst_start(self):
        log_print = self.log.warning
        log_print('=' * 88)
        log_print('脚本为: {}'.format(self.__class__.__name__))
        log_print('作者为: {}'.format(self.author))
        log_print('环境为: {}'.format(self.url))
        log_print('用例为: {}'.format(self.title))
        log_print('用例ID为: {}'.format(self.tst_case_no))
        log_print('=' * 88)

    def tst_result(self):
        total_test_time = time.time() - self.test_start_time
        test_result = self.result
        video_path = self.remote_driver and "http://{}:4444/dashboard/{}.mp4".format(self.remote_driver, self.file_name)
        log_print = self.log.warning if self.pass_flag else self.log.error
        log_print('=' * 88)
        log_print('脚本为: {}'.format(self.__class__.__name__))
        log_print('环境为: {}'.format(self.url))
        log_print('用例为: {}'.format(self.title))
        log_print('用例ID为: {}'.format(self.tst_case_no))
        log_print('步骤为: {}'.format(self.tst_step))
        log_print('期望为: {}'.format(self.tst_expect))
        log_print('测试结果: {}'.format(test_result))
        log_print('测试耗时： [{}分{}秒{}毫秒]'.format(int(total_test_time / 60), int(total_test_time % 60),
                                              int(str(total_test_time).split('.')[1][:3])))
        video_path and log_print('测试视频: {}'.format(video_path))
        self.pass_flag or log_print(
            '测试失败原因: {}'.format("错误如下===\n" + (self.error_info or "测试点中异常(预料中)，请查看中途日志^^^^^")))
        log_print('=' * 88)

    def try_catch(self, test_step, func_result, *args, **kwargs):
        try:
            result = func_result(*args, **kwargs)
        # except WebDriverException as e:
        #     self.driver_offline(e)
        #     raise e
        except Exception as e:
            self.log.error("[{}] 出现异常,请检查.".format(test_step))
            raise e
        else:
            self.log.warning("[{}] 完成.".format(test_step))
            return result

    @staticmethod
    def main(script_instance, *args, **kwargs):
        """
        csf 用于本地 联跑执行
        :param script_instance:
        :param args:
        :param kwargs:
        :return:
        """
        main_class = script_instance(*args, **kwargs)
        return main_class.run(local_exec=True)

    def driver_offline(self, e):
        error_e = str(e).split('\n')[0]
        error_msg = "浏览器失联，可能原因是浏览器已关闭(远端可能为超时失联)==={}".format(error_e)
        self.log.error(error_msg)
        return error_msg


def dft_conf():
    local_file = 'd:\sf_ip.txt'
    if not os.path.exists(local_file):
        local_file = 'sf_ip.txt'
    with open(local_file, encoding='utf-8') as f:
        first_line = f.readline().strip('\r\n') or f.readline().strip('\r\n') or f.readline().strip('\r\n')
        host, user, pwd = first_line.split('\t')
        default_conf = {
            "host": host,  # "http://10.111.32.72",
            "user": user,  # "chi",
            "pwd": pwd,  # "admin1234",
            "hub_url": "http://10.9.242.37:4444/wd/hub",
            "browser": "chrome",
            'fairy': False,
        }
        return default_conf
