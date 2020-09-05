#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# __author__ = 'csf'
# 此部分用于放置视频源 事件和方法

import operator
import time
import random
from common.common_func import shadow, fail_ip_port
from sc_common.sc_define import define
from sc_common.sc_define import define_camera
from v43.ele_set.page_camera import CameraPageEle
from v43.pub.pub_base import PublicClass
from common import common_func as CF


class CameraAction(PublicClass):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.kwargs = kwargs
        self.dft_top_dep = define_camera.camera_top_dep
        self.el = CameraPageEle.Camera
        self.df_cam = define_camera()

    def slt_more_menu(self, need_menu):
        """
        部门... 更多子菜单
        :param need_menu:
        :return:
        """
        for per_ in self.driver.ele_list("{}>li".format(self.el.group_more_menu)):
            if self.driver.ele_get_val(per_) == need_menu:
                return self.driver.ele_click(per_)

    def key_search_camera(self, value):
        self.driver.ele_input(self.el.search_camera_ele, value, enter=True)

    def key_search_group(self, value):
        self.driver.ele_input(self.el.search_group_ele, value, enter=True)

    def chk_dep(self, dep_name, key_search=True):
        """
        检查部门是否存在 并返回 名字，数量，更多三个元素的元组
        :param dep_name:
        :param key_search:
        :return:
        """
        camera_dep_void = "css=.rz-tree__empty-text|#部门树"
        if key_search:
            self.driver.ele_input(self.el.search_group_ele, dep_name, enter=True)
            time.sleep(1)
        else:
            self.refresh_grp_tree(cln=True)
        if self.driver.ele_exist(camera_dep_void):
            return None
        else:
            ele_lst = self.wid.wid_tree(need_dep=dep_name)
            return ele_lst

    def goto_camera_dep_detail(self, dep_name):
        res = self.chk_dep(dep_name=dep_name)
        if not res:
            raise Exception("不存在此父级分组[{}]，请检查".format(dep_name))
        name_el, num_el, more_el = res
        # self.driver.ele_move(num_el)
        # self.driver.ele_click(more_el)
        # self.slt_more_menu("详情")

        self._clk_more_act(name_ele=name_el, more_ele=more_el, clk_more="详情")

    def goto_camera_dep_edit(self, dep_name):
        res = self.chk_dep(dep_name=dep_name)
        if not res:
            raise Exception("不存在此父级分组[{}]，请检查".format(dep_name))
        name_el, num_el, more_el = res
        # self.driver.ele_click(more_el)
        # self.slt_more_menu("编辑设置")
        self._clk_more_act(name_ele=name_el, more_ele=more_el, clk_more="编辑设置")

    def act_chk_dep(self, dep_name=None):
        """进入三大一级分组"""
        if "未分组" in dep_name:
            camera_group_name = self.df_cam.camera_no_dep
        elif "已删除" in dep_name:
            camera_group_name = self.df_cam.camera_del_dep
        else:
            camera_group_name = self.df_cam.camera_top_dep
        self.driver.refresh_driver()
        ele_lst = self.wid.wid_tree(need_dep=camera_group_name)
        return ele_lst

    def act_del_dep(self, name_ele, more_ele, wait_alert=False):
        """
        对指定视频源分组 元素删除动作
        :param name_ele:
        :param more_ele:
        :return:
        """
        self.wid.wid_chk_loading()
        self._clk_more_act(name_ele=name_ele, more_ele=more_ele, clk_more="删除")
        time.sleep(0.3)
        msg = self.driver.ele_get_val(self.el.del_group_confirm_tip)
        if self.el.del_group_confirm_msg not in msg:
            self.log.error("删除分组失败, 请检查 " + 'x' * 20)
            return False
        self.driver.ele_click(self.el.del_group_confirm_btn, move=True)
        return self.wid.wid_get_alert_label(wait_miss=wait_alert)

    def slt_camera_type(self, type1=None, type2="RTSP协议"):
        """
        视频源新建时 视频源 类型选取
        :param type1:
        :param type2:
        :return:
        """
        self.driver.ele_click(self.el.new_camera_type)
        time.sleep(0.5)
        if not type1:
            for cam_type in ["直连摄像机", "平台接入抓拍机", "平台接入摄像机", "直连抓拍机"]:
                self.driver.ele_click(self.el.new_camera_type_.format(cam_type))
                time.sleep(0.5)
                type2_ele = self.el.new_camera_type_.format(type2)
                if self.driver.ele_exist(type2_ele):
                    self.driver.ele_click(type2_ele)
                    break
            else:
                raise Exception("未发现[{}]规格的视频源,请仔细检查".format(type2))
        else:
            self.driver.ele_click(self.el.new_camera_type_.format(type1))
            self.driver.ele_click(self.el.new_camera_type_.format(type2))

    def chk_camera(self, camera_name):
        """
        获取视频源 所在行元素
        :param camera_name:
        :return:
        """
        self.driver.ele_input(self.el.search_camera_ele, camera_name, enter=True)
        self.wid.wid_chk_loading()
        if self.driver.ele_exist(self.el.camera_all_lst):
            tr_lst = self.driver.ele_list(self.el.camera_all_lst)
            for tr_num in range(len(tr_lst)):
                tr_el = '{}>tr:nth-of-type({})'.format(self.el.camera_table, tr_num + 1)
                name_el = self.el.camera_name_ele.format(tr_el)
                if self.driver.ele_get_val(name_el) == camera_name:
                    return tr_el
            else:
                self.log.warning("未找到视频源[{}]".format(camera_name))
                return 0
        else:
            self.log.warning("未发现任何视频源")
            return -1

    def goto_camera_detail(self, camera_name):
        """
        进到 视频源详情页面
        :param camera_name:
        :return:
        """
        tr_el = self.chk_camera(camera_name=camera_name)
        self.driver.ele_click(self.el.camera_detail_ele.format(tr_el))
        self.wid.wid_chk_loading()

    def goto_camera_edit(self, camera_name):
        """
        进到 视频源编辑页面
        :param camera_name:
        :return:
        """
        tr_el = self.chk_camera(camera_name=camera_name)
        self.driver.ele_click(self.el.camera_edit_ele.format(tr_el))

    def goto_camera_new(self, dep_name):
        """
        进到 视频源新建页面
        :param dep_name:
        :return:
        """
        self.chk_dep(dep_name)
        self.driver.ele_click(self.el.new_camera_btn, load=True)

    def get_cnt_camera_status(self):
        """
        获取视频源各统计 数量
        :return:
        """
        status_cnt = {}
        for el_n in range(len(self.driver.ele_list(self.el.camera_status_cnt_))):
            name_el = '{}>.text'.format(self.el.camera_status_cnt_)
            cnt_el = '{}>.count'.format(self.el.camera_status_cnt_)
            status_cnt[self.driver.ele_get_val(name_el)] = self.driver.ele_get_val(cnt_el)
        return status_cnt

    def refresh_grp_tree(self, cln=False):
        """
        对页面的视频源列表刷新操作
        :return:
        """
        if cln:
            self.driver.ele_input(self.el.search_group_ele, '', cln=1, enter=True)
        else:
            self.driver.ele_click(self.el.search_group_icon_ele)
        self.wid.wid_chk_loading()

    def refresh_camera_tbl(self, cln=False):
        """
        对页面的视频源列表刷新操作
        :return:
        """
        if cln:
            self.driver.ele_input(self.el.search_camera_ele, '', cln=1, enter=True)
        else:
            self.driver.ele_click(self.el.camera_tbl_refresh)
        self.wid.wid_chk_loading()

    def act_bat_edit(self, cancel=False):
        jude_str = 'btn-cancel'
        now_status = self.driver.ele_get_val(self.el.bat_edit_status, 'class')
        if (not cancel and (jude_str not in now_status)) or (cancel and jude_str in now_status):
            self.driver.ele_click(self.el.bat_edit_btn)
            time.sleep(0.5)

    def act_bat_slt_all(self, cancel=False):
        jude_str = 'is-checked'
        now_status = self.driver.ele_get_val(self.el.bat_edit_all_ele, 'class')
        if (not cancel and (jude_str not in now_status)) or (cancel and jude_str in now_status):
            self.driver.ele_click(self.el.bat_edit_all_ele)
            time.sleep(0.5)

    def _clk_more_act(self, name_ele, more_ele, clk_more=None):
        for _ in range(3):
            self.driver.ele_move(name_ele)
            if isinstance(self.driver.ele_get_val(more_ele), str):
                if clk_more:
                    self.driver.ele_click(more_ele)
                    isinstance(clk_more, str) and self.slt_more_menu(clk_more)
                break
            time.sleep(0.5)
        else:
            self.log.error('等待三次未能点击 部门后 的 more 控件')


class CameraModule(CameraAction):

    def filter_camera(self, camera_type=None, camera_status=None, camera_acs=None, camera_task=None):
        if camera_type or camera_status or camera_task or camera_acs:
            self.driver.ele_click(self.el.bat_filter_com_btn.format("重置"))  # 重置
            self.wid.wid_chk_loading()
        if camera_type:
            self.driver.ele_click(self.el.bat_type_ele)
            self.wid.wid_drop_down(camera_type)
        if camera_status:
            self.driver.ele_click(self.el.bat_status_ele)
            self.wid.wid_drop_down(camera_status)
        if camera_task:
            self.driver.ele_click(self.el.bat_task_ele)
            self.wid.wid_drop_down(camera_task)
        if camera_acs:
            # query_dict = self.el.bat_acs_pub_wid_dict
            self.driver.ele_click(self.el.bat_acs_ele)
            for k, v in camera_acs.items():
                self.driver.ele_click(self.el.bat_acs_common_wid.format(k, v))
            self.driver.ele_click(self.el.bat_acs_common_btn.format("保存"))
        if camera_type or camera_status or camera_task or camera_acs:
            self.driver.ele_click(self.el.bat_filter_com_btn.format("确定"))  # 确认
            self.wid.wid_chk_loading()

    @shadow("预置视频源创建")
    def pre_camera(self, camera_use='face', pre_all=False):
        """
        预置视频源的创建
        :param camera_use:  face ped face_ped crow alarm search car 7种
        :param pre_all:  默认每类 3个
        :return:
        """
        acs_lst = []
        cam_dict = self.df_cam.generate_camera_info(camera_type='rtsp-pre', camera_use=camera_use, fake=False)
        # cam_dict_lst = dict([[x, cam_dict[x]] for x in list(cam_dict.keys())[:3]])
        cam_dict_lst = {x: cam_dict[x] for x in list(cam_dict.keys())[:3]}
        if 'face' in camera_use or 'alarm' in camera_use or 'search' in camera_use:
            acs_lst.append('face')
        if 'ped' in camera_use or 'search' in camera_use:
            acs_lst.append('ped')
        if 'face_ped' in camera_use:
            acs_lst.append('face_ped')
        # if 'crow' in camera_use:  # TODO 待环境确认
        #     acs_lst.append('crow')
        for cam_name, cam_path in cam_dict_lst.items():
            self.new_camera(camera_name=cam_name, camera_info=cam_path, acs_lst=acs_lst, recovery=True)

    @shadow("新建视频源")
    def new_camera(self, camera_name=None, camera_type=None, camera_use='face', camera_info=None, fake=True,
                   acs_lst=None, dep_name=None,
                   recovery=False, **kwargs):
        """
        新建视频湖泊
        :param camera_name: 视频名字，不传为随机新建
        :param camera_type: 视频源 类型，rtsp-op gb 1400 海康/hk ali/aliyun onv
        :param camera_use:  视频源用途，rtsp及gb时需使用此参数，有face ped car only None 5个,前两个为gb使用，后3个为rtsp，
        :param camera_info: camera信息，与define保持一致
        :param fake:        是否为假数据
        :param acs_lst:      是否接入
        :param dep_name:      所属分组
        :param recovery:      所属分组
        :param kwargs:      扩展参数
        :return:
        """

        def new_camera_func():
            camera_name_new = camera_name or CF.get_random_name(self.df_cam.name_test)
            if dep_name:
                # 1
                # ele_lst = self.wid.wid_tree(need_dep=dep_name)
                # if ele_lst:
                #     self.driver.ele_click(ele_lst[0])
                # 2
                if not self.chk_dep(dep_name=dep_name):  # 检测部门是否存在，不存在 创建一个
                    self.new_dep(dep_name=dep_name, root_dep=kwargs.get('root_dep'))
                    self.chk_dep(dep_name=dep_name)
            self.driver.ele_click(self.el.new_camera_btn)
            self.driver.chk_loading()
            camera_type_new = camera_type or 'rtsp-op'
            camera_type_new = camera_type_new.lower()
            drop_res = None  # 为1400和gb 回放平台 的下拉检查 赋初值
            if 'rtsp' in camera_type_new:  # RTSP
                self.slt_camera_type(type1="直连摄像机", type2="RTSP协议")
                if 'pre' in camera_name_new:
                    rtsp_path = self.df_cam.generate_camera_info(camera_type=camera_type_new, camera_use=camera_use,
                                                                 fake=fake)
                else:
                    rtsp_path = fail_ip_port(True)
                rtsp_path = camera_info or rtsp_path
                self.driver.ele_input(self.el.new_camera_ipt.format("网络地址"), rtsp_path)
            elif 'gb' in camera_type_new or "国标" in camera_type_new:  # 国标
                self.slt_camera_type(type1="平台接入摄像机", type2="标准28181平台")
                gb_param = camera_info or self.df_cam.generate_camera_info(camera_type='gb', fake=fake)
                self.driver.ele_input(self.el.new_camera_ipt.format("设备ID"), gb_param['deviceCode'])
                drop_res = self.wid.wid_drop_down(True, trig_wid=self.el.new_camera_ipt.format('接入平台'), judge=True)
                drop_res = drop_res and self.wid.wid_drop_down(True, trig_wid=self.el.new_camera_ipt.format('回放平台'),
                                                               judge=True)  # 4.2
            # elif 'haikang' in camera_type_new or 'capture' in camera_type_new or "海康" in camera_type_new or "hk" in camera_type_new:
            elif "海康" in camera_type_new or "hk" in camera_type_new:
                self.slt_camera_type(type1="直连抓拍机", type2="海康抓拍机")
                cap_param = camera_info or self.df_cam.generate_camera_info(camera_type='海康', fake=fake)
                self.driver.ele_input(self.el.new_camera_ipt.format("ip地址"), cap_param['host'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入端口号"), cap_param['port'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入用户名"), cap_param['userName'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入密码"), cap_param['password'])
            elif '1400' in camera_type_new:
                self.slt_camera_type(type1="平台接入抓拍机", type2="GAT1400平台")
                cap_param = camera_info or self.df_cam.generate_camera_info(camera_type='1400', fake=fake)
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入设备ID"), cap_param['deviceCode'])
                drop_res = self.wid.wid_drop_down(True, trig_wid=self.el.new_camera_ipt.format('请选择接入平台'), judge=True)
            elif 'ali' in camera_type_new:
                self.slt_camera_type(type1="平台接入摄像机", type2="阿里云平台")
                cap_param = camera_info or self.df_cam.generate_camera_info(camera_type='ali', fake=fake)
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入设备ID"), cap_param['deviceCode'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入下级平台地址"), cap_param['host'])
                self.driver.ele_input(self.el.new_camera_ipt.format("输入下级平台端口"), cap_param['port'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入下级平台用户名"), cap_param['userName'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入下级平台密码"), cap_param['password'])
            elif 'onv' in camera_type_new:
                self.slt_camera_type(type1="直连摄像机", type2="ONVIF协议")
                cap_param = camera_info or self.df_cam.generate_camera_info(camera_type='onv', fake=fake)
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入ip地址"), cap_param['host'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入端口号"), cap_param['port'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入下级平台用户名"), cap_param['userName'])
                self.driver.ele_input(self.el.new_camera_ipt.format("请输入下级平台密码"), cap_param['password'])
            else:  # 其它规格 需填与页面相同规格名   # TODO 待扩展
                self.slt_camera_type(type2=camera_type_new)
            # 添加一个回放平台 确认:
            if isinstance(drop_res, int) and drop_res == -1:
                self.driver.refresh_driver()
                self.into_menu("系统设置")
                from v43.pub.pub_sys_setting import SettingModule
                if 'gb' in camera_type_new or "国标" in camera_type_new:
                    SettingModule(self.driver, **self.kwargs).new_gb_platform()
                else:
                    SettingModule(self.driver, **self.kwargs).new_1400_platform()
                self.into_menu()
                return new_camera_func()
            # 输入名字，坐标，点击确认
            self.driver.ele_input(self.el.new_camera_ipt.format("请输入视频源名称"), camera_name_new)
            x = kwargs.get('x')
            y = kwargs.get('y')
            x and self.driver.ele_input(self.el.new_camera_longitude, x)
            y and self.driver.ele_input(self.el.new_camera_latitude, y)
            self.driver.ele_input(self.el.new_camera_remark, "This is a {} video".format(camera_type_new))
            self.driver.ele_click(self.el.camera_btn_com.format("确定"))
            # self.wid.wid_chk_loading()
            time.sleep(2)
            alert_info = self.wid.wid_get_alert_label(return_msg=True)
            if alert_info and '异常' in alert_info:
                self.driver.ele_click(self.el.camera_btn_com.format("取消"))
                if recovery and '重复' in alert_info:
                    self.recovery_camera(camera_name_new, dest_dep=dep_name)
                else:
                    return False
            self.collect_resource(self.df.key_camera, camera_name_new)
            if acs_lst:
                time.sleep(0.5)
                acs_lst_new = CF.convert_to_array(acs_lst)
                if not self.chg_acs(camera_name=camera_name_new, acs_lst=acs_lst_new):
                    raise Exception("修改接入状态异常")
            return camera_name_new

        return new_camera_func()

    def edit_camera(self, camera_name, new_camera_name=None, new_path=None, new_dep=None, verify=True):
        self.goto_camera_edit(camera_name)
        time.sleep(1)
        new_camera_name and self.driver.ele_input(self.el.new_camera_name, new_camera_name)
        new_path and self.driver.ele_input(self.el.new_camera_add, new_path)
        if new_dep:
            self.driver.ele_click(self.el.new_camera_group)
            time.sleep(0.5)
            self.driver.ele_input(self.el.slt_grp_srh, new_dep, enter=True)
            # self.wid.wid_tree_slt_camera_group(need_dep=new_dep, root_e=self.el.slt_grp_tree)
            self.driver.ele_click('//span[text()="{}"]'.format(new_dep))
        self.driver.ele_click(self.el.camera_edit_save_btn, load=True)
        time.sleep(1)
        # 保存后,在详情页面进行检测是否为新的值
        # 4.2需要再次点击 详情查看
        if not verify:
            return True
        page_camera_name = self.driver.ele_get_val(self.el.camera_det_name)
        page_camera_path = self.driver.ele_get_val(self.el.camera_det_path)
        page_camera_group = self.driver.ele_get_val(self.el.camera_det_group)
        if (new_camera_name and new_camera_name != page_camera_name) or (new_path and new_path != page_camera_path) \
                or (new_dep and new_dep != page_camera_group):
            self.log.warning("新输入值 与期待值 不符")
            return False
        self.driver.ele_click(self.el.camera_detail_close)  # 关闭详情框
        self.collect_resource(self.df.key_camera, new_camera_name, remove_value=camera_name)
        return True

    def __resolve_name_dup(self, camera_name):
        camera_name_lst = CF.convert_to_array(camera_name)
        for camera_name in camera_name_lst:
            # 1
            self.chk_dep(dep_name=self.df_cam.camera_top_dep)
            tmp = self.chk_camera(camera_name=camera_name)
            if isinstance(tmp, str):
                if not self.edit_camera(camera_name=camera_name,
                                        new_camera_name=CF.get_random_name(self.df.name_prefix + 'cam_'), verify=False):
                    break
                else:
                    continue
            # 2
            self.act_chk_dep("已删除")
            tr = self.chk_camera(camera_name=camera_name)
            if isinstance(tr, str):
                self.driver.ele_click(self.el.camera_recovery_ele.format(tr))
                self.driver.ele_click(self.el.camera_recovery_confirm_ele)
            self.chk_dep(dep_name=self.df_cam.camera_no_dep)
            self.wid.wid_chk_loading()
            trs = self.chk_camera(camera_name=camera_name)
            if isinstance(trs, str):
                if not self.edit_camera(camera_name=camera_name,
                                        new_camera_name=CF.get_random_name(self.df.name_prefix + 'cam_'), verify=False):
                    break
        else:
            return True

    def import_camera(self, dep_name=None):
        xls_ = self.df.get_file(self.df.ImgDef.rtsp_xls)
        xls_dict = CF.get_xls_content(xls_, 'RTSP')
        lst_key = list(xls_dict.keys())
        self.__resolve_name_dup(lst_key)
        if not dep_name:
            dep_name = self.new_dep()
        self.chk_dep(dep_name=dep_name)
        self.driver.ele_click(self.el.import_icon)
        self.driver.ele_input(self.el.import_file_ele, xls_, cln=2)
        time.sleep(1)
        msg = self.wid.wid_task_tip()
        if not msg:
            self.log.error("导入视频源未捕获到导入提示, 出错")
            return False
        self.refresh_camera_tbl(cln=True)
        if list(self.get_tbl().keys()) == lst_key:
            # self.collect_resource(self.df.key_camera, lst_key)
            return True

    @shadow("新建视频源分组及视频源")
    def new_camera_dep(self, camera_name=None, acs_lst=None, camera_path=None, dep_name=None, camera_type=None,
                       fake=True, **kwargs):
        """
        建视频源，默认RTSP
        :param camera_name:
        :param acs_lst:
        :param camera_path:
        :param dep_name:
        :param camera_type:
        :param fake:
        :param acs_lst:
        :return:
        """
        acs_lst = CF.convert_to_array(acs_lst)
        dep_name = dep_name or CF.get_random_name(self.df_cam.name_test)
        if not self.chk_dep(dep_name):
            self.new_dep(dep_name=dep_name)
            self.chk_dep(dep_name)
        # 新建
        new_res = self.new_camera(camera_name=camera_name, camera_info=camera_path, camera_type=camera_type,
                                  acs_lst=acs_lst, fake=fake, **kwargs)
        return dep_name, new_res

    @shadow("编辑视频源分组")
    def edit_camera_group(self, dep_name, new_dep_name=None):
        new_dep_name = new_dep_name or CF.get_random_name(self.df_cam.name_test)
        self.goto_camera_dep_edit(dep_name)
        self.wid.wid_chk_loading()
        self.driver.ele_input(self.el.new_group_name, new_dep_name, cln=1)
        self.driver.ele_click(self.el.camera_grp_edit_btn)
        if self.wid.wid_get_alert_label():
            self.collect_resource(self.df.key_camera_group, new_dep_name, remove_value=dep_name)
            return True
        else:
            return False

    @shadow("删除单个视频源")
    def del_camera(self, camera_name):
        """
        删除视频源, 会做取消接入操作
        :param camera_name:
        :return:
        """
        tbl_tr = self.chg_acs(camera_name)
        if tbl_tr:
            self.driver.ele_click(self.el.camera_del_ele.format(tbl_tr))
            time.sleep(0.5)
            self.driver.ele_click(self.el.camera_del_confirm_ele)
            if self.wid.wid_get_alert_label():
                self.collect_resource(self.df.key_camera, remove_value=camera_name)
                self.refresh_camera_tbl(cln=True)
                return True
            return False

    @shadow("检查视频源接入状态")
    def chk_acs(self, camera_name, acs_lst="未接入", rtn_tbl=False):
        """
        检查 视频源接入状态，
        :param camera_name:
        :param acs_lst: 目前支持 face ped face_ped,三种参数组合的列表
        :param rtn_tbl: 是否返回表格所在tr元素, 默认不返回
        :return:
        """
        acs_lst = CF.convert_to_array(acs_lst)
        tbl_tr = self.chk_camera(camera_name)
        if isinstance(tbl_tr, str):
            now_status = self.driver.ele_get_val(self.el.camera_acs_status.format(tbl_tr))
            status_lst = now_status.split(',')
            if operator.eq(acs_lst, status_lst):
                self.log.warning("目前状态于要求状态相符，都为[{}]".format(acs_lst))
                return tbl_tr
            else:
                return False if not rtn_tbl else False, tbl_tr

    @shadow("修改视频源的接入状态")
    def chg_acs(self, camera_name, acs_lst=None):
        """
        修改 视频源接入状态
        :param camera_name:
        :param acs_lst: 目前支持 face ped face_ped, crowd,四种参数组合的列表
        :return:
        """
        acs_lst = CF.convert_to_array(acs_lst)
        if isinstance(acs_lst, list):
            if '人群' in acs_lst:  # 针对 状态显示和 接入界面显示不一致
                acs_lst[acs_lst.index('人群')] = '人群分析'
            if self.kwargs.get('fairy') and '人脸' in acs_lst:
                acs_lst[acs_lst.index('人脸')] = '人脸人体联合'
        if not acs_lst:
            acs_lst = "未接入"
        rtn_val = self.chk_acs(camera_name, acs_lst=acs_lst)
        if isinstance(rtn_val, tuple):
            tbl_tr = rtn_val[1]
            self.driver.ele_click(self.el.camera_detail_ele.format(tbl_tr))
            self.wid.wid_chk_loading()
            time.sleep(1)
            face_acs = self.driver.ele_get_val(self.el.camera_face_status, attr_name='class')
            ped_acs = self.driver.ele_get_val(self.el.camera_ped_status, attr_name='class')
            face_ped_acs = self.driver.ele_get_val(self.el.camera_face_ped_status, attr_name='class')
            crowd_acs = self.driver.ele_get_val(self.el.camera_crowd_status, attr_name='class') or ""
            if (('face' in acs_lst or '人脸' in acs_lst) and 'is-checked' not in face_acs) or (
                    ('face' not in acs_lst and '人脸' not in acs_lst) and 'is-checked' in face_acs):
                self.driver.ele_click(self.el.camera_face_status)
                self.wid.wid_chk_loading()
                assert "接入成功" in self.wid.wid_get_alert_label(wait_miss=True), "修改人脸接入状态失败"
            if (('ped' in acs_lst or '人体' in acs_lst or '结构化' in acs_lst) and 'is-checked' not in ped_acs) or \
                    ((
                             'ped' not in acs_lst and '人体' not in acs_lst and '结构化' not in acs_lst) and 'is-checked' in ped_acs):
                self.driver.ele_click(self.el.camera_ped_status)
                self.wid.wid_chk_loading()
                assert "接入成功" in self.wid.wid_get_alert_label(wait_miss=True), "修改人体接入状态失败"
            if (('face_ped' in acs_lst or '人脸人体联合' in acs_lst) and 'is-checked' not in face_ped_acs) or (
                    ('face_ped' not in acs_lst and '人脸人体联合' not in acs_lst) and 'is-checked' in face_ped_acs):
                self.driver.ele_click(self.el.camera_face_ped_status)
                self.wid.wid_chk_loading()
                assert "成功" in self.wid.wid_get_alert_label(wait_miss=True), "修改人脸人体联合接入状态失败"
            if (('crowd' in acs_lst or '人群分析' in acs_lst) and 'is-checked' not in crowd_acs) or (
                    ('crowd' not in acs_lst and '人群分析' not in acs_lst) and 'is-checked' in crowd_acs):
                self.driver.ele_click(self.el.camera_crowd_status)
                self.wid.wid_chk_loading()
                assert "成功" in self.wid.wid_get_alert_label(wait_miss=True), "修改人群分析接入状态失败"

            self.driver.ele_click(self.el.camera_detail_close)
            rtn_val = tbl_tr
        return rtn_val

    @shadow("批量移动视频源分组")
    def bat_move_camera(self, dest_dep, keyword='', root_dep=None):
        if not root_dep:
            root_dep = self.dft_top_dep
            self.chk_dep(dep_name=root_dep)
        if self.chk_camera(camera_name=keyword) == -1:
            return False
        self.act_bat_edit()
        self.act_bat_slt_all()
        self.driver.ele_click(self.el.bat_edit_move, load=True)
        self.wid.wid_tree_slt_camera_group(need_dep=dest_dep)
        self.driver.ele_click(self.el.bat_edit_del_confirm)  # 确定按钮
        return True

    @shadow("批量修改视频源的接入状态")
    def bat_edit_camera_acs(self, keyword='', root_dep=None, acs=None):
        """
        批量 编辑视频源的 接入状态
        :param keyword:  名称/编号/IP地址 ，置空为所有
        :param root_dep: 所在分组，不填写为一级部门
        :param acs:
        :return:
        """
        # 批量接入/取消接入
        acs = CF.convert_to_array(acs)
        # if not root_dep:
        #     root_dep = self.dft_top_dep
        #     self.chk_dep(dep_name=root_dep)
        if self.chk_camera(camera_name=keyword) == -1:
            return False

        # self.driver.ele_input(self.el.search_camera_ele, input_value=keyword, enter=True)
        # self.wid.wid_chk_loading()
        # 批量查询状态
        now_acs_lst = list(set([v[2] for v in self.get_tbl().values()]))
        if len(now_acs_lst) == 1:  # 说明所有视频源接入状态为一种
            now_acs_status_lst = now_acs_lst[0].split(',')
            if operator.eq(acs, now_acs_status_lst) or (
                    not acs and len(now_acs_status_lst) == 1 and now_acs_status_lst[0] == "未接入"):
                self.log.warning("批量编辑时，状态相符，退出")
                return
        if not acs:
            new_dict = {
                "人脸": "接入",
                "结构化": '接入',
                "人脸人体联合": '接入',
            }
        else:
            new_dict = {}
            if "人脸" in acs or 'face' in acs:
                new_dict["人脸"] = "未接入"
            if "结构化" in acs or '人体' in acs or 'ped' in acs:
                new_dict["结构化"] = "未接入"
            if "人脸人体联合" in acs or 'face_ped' in acs:
                new_dict["人脸人体联合"] = "未接入"
        if new_dict:
            self.act_bat_edit(cancel=False)
        for k, v in new_dict.items():
            self.filter_camera(camera_acs={k: v})
            if self.driver.ele_exist(self.el.camera_all_lst):
                self.act_bat_slt_all()
                ele_ = self.el.bat_edit_acs_cancel if not acs else self.el.bat_edit_acs
                self.wid.wid_drop_down(val=k, trig_wid=ele_)
                self.driver.ele_click(self.el.bat_edit_confirm_btn)
                if self.driver.ele_exist(self.el.bat_edit_confirm_no_skip_btn):
                    self.driver.ele_click(self.el.bat_edit_confirm_no_skip_btn)
                self.wid.wid_chk_loading()
        self.act_bat_edit(cancel=True)
        self.driver.ele_click(self.el.bat_filter_com_btn.format("重置"))  # 重置筛选

    @shadow("批量删除视频源")
    def bat_del_camera(self, keyword='', root_dep=None, chk_acs=True):
        """
        批量删除视频源
        :param keyword: 名称/编号/IP地址 ，置空为所有
        :param root_dep: 所在分组，不填写为一级部门
        :param chk_acs: 是否检查接入状态，默认不检查
        :return:
        """
        # root_dep = root_dep or self.dft_top_dep
        ele_lst = self.chk_dep(dep_name=root_dep) if root_dep else None
        if not root_dep or ele_lst:
            if self.get_camera_nums():
                if chk_acs:
                    self.bat_edit_camera_acs(keyword=keyword, root_dep=root_dep)
                self.act_bat_edit()
                self.act_bat_slt_all()
                self.driver.ele_click(self.el.bat_edit_del)
                self.driver.ele_click(self.el.bat_edit_del_confirm)
                if not self.wid.wid_get_alert_label():
                    return False
            # return '成功' in self.wid.wid_get_alert_label()
            else:
                self.log.warning("此分组[{}]下未发现视频源".format(root_dep))
            return ele_lst
        else:
            self.log.warning("未发现此分组[{}]".format(root_dep))
        return False

    @shadow("新建视频源分组")
    def new_dep(self, dep_name=None, root_dep=None, pwr_user_list=None, pwr_dep_list=None, new_type="新建下级"):
        """
        新建部门
        :param dep_name:
        :param root_dep:    所在分组，不填写为一级部门
        :param pwr_user_list: 分配权限，按用户
        :param pwr_dep_list:    分配权限，按部门
        :param new_type:    两种 新建下级和 新建同级
        :return:
        """
        dep_name = dep_name or CF.get_random_name(self.df_cam.name_test)
        root_dep = root_dep or self.dft_top_dep
        res = self.chk_dep(dep_name=root_dep)
        if not res:
            raise Exception("不存在此父级分组[{}]，请检查".format(root_dep))
        name_el, num_el, more_el = res
        # self.driver.ele_click(more_el)
        # self.slt_more_menu(new_type)

        self._clk_more_act(name_ele=name_el, more_ele=more_el, clk_more=new_type)

        self.driver.ele_input(self.el.new_group_name, dep_name)
        ref_ele = self.driver.ele_click(self.el.new_group_rectangle)
        self.wid.wid_draw_circle(ref_ele)
        self.driver.ele_click(self.el.new_group_next_btn)
        time.sleep(1)
        self.driver.chk_loading()
        # self.wid.wid_power_assign(dep_list='pre_三级部门')
        # self.wid.wid_power_assign(dep_list='一级部门（可修改名称）')
        # self.wid.wid_power_assign(user_list='whale_无审核无审批权限普通用户')
        self.wid.wid_power_assign(user_list=pwr_user_list, dep_list=pwr_dep_list)
        self.driver.ele_click(self.el.new_group_next_btn)
        if not self.wid.wid_get_alert_label():
            return False
        self.collect_resource(self.df.key_camera_group, dep_name)
        return dep_name

    @shadow("删除视频源分组")
    def del_dep(self, dep_name, cln_camera=False):
        """
        删除部门
        :param dep_name:
        :param cln_camera:  是否清理此分组下的视频源
        :return:
        """
        return_val = self.chk_dep(dep_name=dep_name, key_search=True)
        if return_val:
            num = CF.get_num_from_str(self.driver.ele_get_val(return_val[1]))
            if num:
                self.log.warning('此分组下有视频源[{}]个'.format(num))
                if cln_camera:
                    self.bat_del_camera()
                # else:
                #     return 0
                # if self.act_del_dep(return_val[0], return_val[-1]):
                #     self.collect_resource(resource_type=self.df.key_camera_group, remove_value=dep_name)
                #     return True
                return self.del_dep(dep_name=dep_name)
            else:
                return self.act_del_dep(name_ele=return_val[0], more_ele=return_val[-1])
        else:
            self.log.warning('未发现此分组[{}], 不须删除'.format(dep_name))
            return -1

    def __del_all_dep(self, root_e=None, root_dep=None):
        """
        循环体,内使用,清理root_e 分组下的所有分组，慎用，前提是分组都为空分组
        :param root_e: 默认为 一级分组
        :return:
        """
        if not root_e:
            root_e = "css=.rz-tree>div:nth-of-type(2)"
        del_flag = False
        del_root = False
        this_expand_ele = root_e + '>div:nth-of-type(1)>span'  # 展开
        tmp_ele = self.driver.ele_get_(this_expand_ele)
        if 'expanded' not in self.driver.ele_get_val(tmp_ele, 'class'):
            self.driver.ele_click(this_expand_ele)
            time.sleep(0.5)
        all_root_ele = self.driver.ele_list(root_e + '>div:nth-of-type(2)' + '>.rz-tree-node')
        dep_len = len(all_root_ele)
        # print(dep_len)
        for i in range(dep_len, 0, -1):
            root_node = root_e + '>div:nth-of-type(2)' + '>div:nth-of-type({})'.format(i)  # 分支
            root_node_1 = root_node + '>div:nth-of-type(1)'  # 展开
            expand_ele = root_node_1 + '>span'
            grain_ele = root_node_1 + '>div'
            name_ele = grain_ele + '>div:nth-of-type(1)'
            num_ele = grain_ele + '>.count'
            more_ele = grain_ele + '>.more'
            now_name = self.driver.ele_get_val(name_ele)
            if now_name == "":
                time.sleep(1)
                now_name = self.driver.ele_get_val(name_ele)
            cam_num = CF.get_num_from_str(self.driver.ele_get_val(num_ele))
            tmp_val = self.driver.ele_get_val(expand_ele, attr_name='class', chk_visit=False)
            # print('{}={}='.format(now_name, cam_num))
            if now_name == root_dep:
                del_root = True
            if 'leaf' in tmp_val:
                del_flag = (cam_num == 0) and (not root_dep)
            if 'expand-icon' in tmp_val and 'expander' not in tmp_val and 'leaf' not in tmp_val:
                if del_root:
                    self.__del_all_dep(root_e=root_node)
                else:
                    self.__del_all_dep(root_e=root_node, root_dep=root_dep)
                del_flag = (cam_num == 0) and (not root_dep)
            if del_flag or del_root:
                self.act_del_dep(name_ele=name_ele, more_ele=more_ele)
                self.wid.wid_chk_loading()
                if del_root:
                    break
                expand_val = self.driver.ele_get_val(this_expand_ele, 'class', chk_visit=False)
                if expand_val and 'expanded' not in expand_val:
                    self.driver.ele_click(this_expand_ele)
                    time.sleep(0.5)

    @shadow("删除所有视频源分组(包括深层)")
    def del_all_dep(self, root_dep=None):
        """
        删除所有视频源 对外接口
        :param root_dep:
        :return:
        """
        self.driver.ele_input(self.el.search_group_ele, '', cln=1, enter=True)
        return self.__del_all_dep(root_dep=root_dep)

    @shadow("删除所有视频源分组(单个递归)+视频源(批量清理)")
    def del_all_camera_group(self, root_dep=None, camera_lst=None, cam_blk_lst=None):
        """
        慎用，清理一级部门下的所有视频源(取消接入删除)和分组
        :return:
        """
        # TMP
        self.driver.refresh_driver()
        self.into_menu()
        root_dep = CF.convert_to_array(root_dep)
        camera_lst = CF.convert_to_array(camera_lst)
        cam_blk_lst = CF.convert_to_array(cam_blk_lst)
        for camera_ in camera_lst:
            self.del_camera(camera_)
            self.log.warning("删除视频源[{}]".format(camera_))

        if camera_lst:
            self.driver.refresh_driver()
        for dep_ in root_dep:
            self.log.warning("清理分组[{}]下的视频源".format(dep_))
            self.del_dep(dep_name=dep_, cln_camera=True)
            # ele_lst = self.bat_del_camera(root_dep=dep_)
            # if ele_lst and isinstance(ele_lst, tuple):
            #     self.refresh_grp_tree()
            #     self.log.warning("删除分组[{}]".format(dep_))
            #     self.del_dep(dep_)
            # self.act_del_dep(name_ele=ele_lst[0], more_ele=ele_lst[-1])
            # self.del_all_dep(root_dep=dep_)
        for per_blk in cam_blk_lst:
            self.del_block_type(block_type=per_blk)
        return True

    @shadow("恢复视频源到指定分组")
    def recovery_camera(self, camera_name, dest_dep):
        """
        恢复视频源
        :param camera_name:
        :param dest_dep:
        :return:
        """
        self.act_chk_dep("已删除")
        cam_tr = self.chk_camera(camera_name=camera_name)
        if isinstance(cam_tr, str):
            self.driver.ele_click(self.el.camera_recovery_ele.format(cam_tr))
            self.driver.ele_click(self.el.camera_recovery_confirm_ele)
            self.wid.wid_chk_loading()
        #
        self.chk_dep(dep_name=self.df_cam.camera_no_dep)
        self.goto_camera_edit(camera_name=camera_name)
        self.driver.ele_click(self.el.new_camera_group)
        self.wid.wid_tree_slt_camera_group(need_dep=dest_dep, root_e=self.el.slt_grp_tree)
        self.wid.wid_chk_loading()
        self.driver.ele_click(self.el.camera_btn_com.format("保存"))
        # now_grp_name = dest_dep
        now_grp_name = self.driver.ele_get_val(self.el.camera_det_group)  # 4.2
        self.driver.ele_click(self.el.camera_detail_close)
        self.collect_resource(self.df.key_camera, resource_value=camera_name)
        self.driver.refresh_driver()
        self.log.warning("Now group name is [{}], expect group name is [{}]".format(now_grp_name, dest_dep))
        return now_grp_name == dest_dep

    @shadow("获取当前分组的视频源数量")
    def get_camera_nums(self):
        """
        获取当前 分组视频源数量
        :return:
        """
        if len(self.driver.ele_list(self.el.camera_judge_page_ele)) == 2:  # 多页时返回 分页器显示数量
            return CF.get_num_from_str(self.driver.ele_get_val(self.el.camera_total))
        elif self.driver.ele_exist(self.el.camera_all_lst):  # 单页有数据时 返回当前页的行数
            return len(self.driver.ele_list(self.el.camera_all_lst))
        else:  # 单页无列 返回0
            return 0

    @shadow("获取当前页视频源的所有信息")
    def get_tbl(self, dep_name=None):
        """
        获取当前页面 视频源表格的所有数据
        :param dep_name:
        :return:
        """
        if dep_name:
            self.chk_dep(dep_name)
        total_cam_num = self.get_camera_nums()
        if total_cam_num and total_cam_num < 30:  # 页面表格1页30，预置3*7份 21个,
            all_txt = self.driver.ele_get_val(self.el.camera_table)
            camera_dict = {y.split('\n')[0]: y.split('\n')[1:4] for y in all_txt.split('删除\n') if y}
            return camera_dict
        else:
            return {}

    @shadow("预置视频源分组+视频源")
    def pre_dep_camera(self, camera_use=None, fake=False):
        """
        预置 视频源分组 和视频源
        :param camera_use:
        :param fake:
        :return:
        """
        camera_use = camera_use or 'face'
        pre_root_grp = self.df_cam.pre_camera_group
        grp_lst = [
            self.df_cam.pre_camera_group_face,
            self.df_cam.pre_camera_group_ped,
            self.df_cam.pre_camera_group_face_ped,
            self.df_cam.pre_camera_group_car,
            self.df_cam.pre_camera_group_crowd,
            self.df_cam.pre_camera_group_alarm,
            self.df_cam.pre_camera_group_search,
        ]
        camera_use = CF.convert_to_array(camera_use)
        camera_use_lst = CF.convert_to_array(camera_use)
        # 1  临时替换 #2
        # ele_lst = self.wid.wid_tree(need_dep=pre_root_grp)
        # if ele_lst:
        #     self.driver.ele_click(ele_lst[0])
        #   2
        if self.chk_dep(pre_root_grp):
            self.log.warning("已经存在此分组[{}],不需创建".format(grp_lst))
            new_camera_dict = self.get_tbl()
            def_root_dep = self.df_cam.pre_camera_group
            if new_camera_dict:
                new_camera_dict = {k: v[2] for k, v in new_camera_dict.items()}  # 页面的数据
            camera_key_value_dict = self.df_cam.def_camera_dict
            if self.kwargs.get('fairy'):  # fairy no access face
                camera_key_value_dict['face'][0] = "人脸人体联合"
            for camera_use_ in camera_use_lst:
                need_camera_dict = self.df_cam.generate_camera_info(camera_type='rtsp-pre', camera_use=camera_use_,
                                                                    fake=False)
                need_camera_name = list(need_camera_dict.keys())
                need_camera_act_lst = CF.convert_to_array(camera_key_value_dict[camera_use_][0])
                camera_dep_name = camera_key_value_dict[camera_use_][1]
                for per_cam in need_camera_name:
                    if not new_camera_dict or per_cam not in new_camera_dict:
                        self.new_camera(camera_name=per_cam, camera_info=need_camera_dict[per_cam],
                                        acs_lst=need_camera_act_lst,
                                        dep_name=camera_dep_name, fake=fake, recovery=True, root_dep=def_root_dep)
                    elif per_cam in new_camera_dict and [x for x in need_camera_act_lst if
                                                         x not in new_camera_dict[per_cam]]:
                        self.chg_acs(camera_name=per_cam, acs_lst=need_camera_act_lst)
        else:
            self.new_dep(pre_root_grp)
            for grp_ in grp_lst:
                self.new_dep(dep_name=grp_, root_dep=pre_root_grp)
            camera_use_lst = CF.convert_to_array(camera_use)
            if 'face' in camera_use_lst:
                self.chk_dep(self.df_cam.pre_camera_group_face)
                self.pre_camera(camera_use='face')
            if 'ped' in camera_use_lst:
                self.chk_dep(self.df_cam.pre_camera_group_ped)
                self.pre_camera(camera_use='ped')
            if 'face_ped' in camera_use_lst:
                self.chk_dep(self.df_cam.pre_camera_group_face_ped)
                self.pre_camera(camera_use='face_ped')
            if 'crow' in camera_use_lst:
                self.chk_dep(self.df_cam.pre_camera_group_crowd)
                self.pre_camera(camera_use='crow')
            if 'car' in camera_use_lst:
                self.chk_dep(self.df_cam.pre_camera_group_car)
                self.pre_camera(camera_use='car')
            if 'alarm' in camera_use_lst:
                self.chk_dep(self.df_cam.pre_camera_group_alarm)
                self.pre_camera(camera_use='alarm')
            if 'search' in camera_use_lst:
                self.chk_dep(self.df_cam.pre_camera_group_search)
                self.pre_camera(camera_use='search')
        # self.driver.refresh_driver()

    # 区块相关
    def new_block_type(self, block_type=None):
        block_type = block_type or CF.get_random_name()
        self.driver.ele_click(self.el.search_camera_ele)
        self.driver.ele_click(self.el.block_type_new_btn, wait_time=5)
        self.driver.ele_input(self.el.block_type_new_name, block_type)
        self.driver.ele_click(self.el.block_type_new_confirm)
        self.collect_resource(self.df.key_camera_block, block_type)
        return block_type

    def display_block_type(self, block_type):
        t_start = time.time()
        while time.time() - t_start < 12:
            el = 'css=.icon-arrowR'
            if self.driver.ele_click_or_not(self.el.block_type_ele.format(block_type), timeout=1):
                return True
            if 'disable' in self.driver.ele_get_val(el, 'class'):
                break
            self.driver.ele_click(el)
        else:
            return False

    def chk_block_type(self, block_type):
        self.display_block_type(block_type)
        self.driver.ele_click(self.el.block_type_ele.format(block_type))

    def edit_block_type(self, block_type, new_block_type):
        self.driver.ele_move(self.el.block_type_ele.format(block_type))
        self.driver.ele_click(self.el.block_type_more_ele.format(block_type))
        self.driver.ele_click(self.el.block_type_more_edit)
        self.driver.ele_input(self.el.block_type_new_name, new_block_type)
        self.driver.ele_click(self.el.block_type_new_confirm)

    def del_block_type(self, block_type):
        self.chk_block_type(block_type=block_type)
        self.driver.ele_move(self.el.block_type_ele.format(block_type))
        self.driver.ele_click(self.el.block_type_more_ele.format(block_type))
        self.driver.ele_click(self.el.block_type_more_del)
        self.wid.wid_pop_win()
        if self.wid.wid_get_alert_label():
            self.collect_resource(self.df.key_camera_block, remove_value=block_type)
            return True
        else:
            self.log.error("删除区块类型失败[{}]".format(block_type))

    def new_block(self, block_name, dep_name, block_type=None, camera_lst=None):
        camera_lst = CF.convert_to_array(camera_lst)
        if not block_type:
            block_type = self.new_block_type()
        self.chk_block_type(block_type=block_type)
        res = self.chk_dep(dep_name=dep_name)
        if not res:
            raise Exception("不存在此父级分组[{}]，请检查".format(dep_name))
        name_el, num_el, more_el = res
        # self.driver.ele_click(more_el)
        # self.slt_more_menu("新建区块")

        self._clk_more_act(name_ele=name_el, more_ele=more_el, clk_more="新建区块")

        self.driver.ele_input(self.el.block_new_name, block_name)
        time.sleep(0.5)  # remote error add sleep  add by csf 20200427
        self.driver.ele_click(self.el.block_new_confirm)
        # 选择视频源
        camera_lst_page = self.driver.ele_list(self.el.block_new_camera_label)
        for per_ in camera_lst_page:
            if not camera_lst and self.driver.ele_get_val(per_) in camera_lst:
                self.driver.ele_click(per_)
        self.driver.ele_click(self.el.block_new_confirm)
        return self.wid.wid_get_alert_label()

    def chk_block(self, block_name):
        self.refresh_grp_tree(cln=True)
        ele_ = self.wid.wid_tree2(need_dep=block_name, return_lst=True)
        self._clk_more_act(name_ele=ele_[0], more_ele=ele_[-1])
        return ele_

    def goto_block_detail(self, block_name):
        ele_ = self.chk_block(block_name=block_name)
        # self.driver.ele_click(ele_[-1])
        # self.slt_more_menu("区块详情")

        self._clk_more_act(name_ele=ele_[0], more_ele=ele_[-1], clk_more="区块详情")

    def del_block(self, block_name):
        ele_ = self.chk_block(block_name=block_name)
        # self.driver.ele_click(ele_[-1])
        # self.slt_more_menu("删除")
        self._clk_more_act(name_ele=ele_[0], more_ele=ele_[-1], clk_more="删除")
        self.driver.ele_click(self.el.block_del_confirm_btn)
        return self.wid.wid_get_alert_label()

    def edit_block(self, block_name, new_block_name=None, new_cam_lst=None):
        new_cam_lst = CF.convert_to_array(new_cam_lst)
        ele_ = self.chk_block(block_name=block_name)
        # self.driver.ele_click(ele_[-1])
        # self.slt_more_menu("编辑区块")
        self._clk_more_act(name_ele=ele_[0], more_ele=ele_[-1], clk_more="编辑区块")
        new_block_name and self.driver.ele_input(self.el.block_new_name, new_block_name)
        self.driver.ele_click(self.el.block_edit_camera_info)
        # 选择视频源
        if new_cam_lst:
            camera_lst_page = self.driver.ele_list(self.el.block_new_camera_label)
            for per_ in camera_lst_page:
                now_status = self.driver.ele_get_val(per_, 'class')
                this_camera_name = self.driver.ele_get_val(per_)
                if (this_camera_name in new_cam_lst and 'is-check' not in now_status) or \
                        (this_camera_name not in new_cam_lst and 'is-check' in now_status):
                    self.driver.ele_click(per_)
        self.driver.ele_click(self.el.block_new_confirm)
        return self.wid.wid_get_alert_label()

    def export_block(self):
        self.driver.ele_click(self.el.block_export_btn)
        time.sleep(1)
        return self.wid.wid_task_tip(wait_miss=True)

    def import_block(self, import_file):
        self.driver.ele_click(self.el.block_import_btn)
        self.driver.ele_input(self.el.import_file_ele, import_file, cln=2)
        time.sleep(1)
        return self.wid.wid_task_tip()

    def main(self):
        # block_name = "Hello_world2"
        # block_type_name = self.new_block_type()
        # self.new_block(block_name, dep_name="whale_search", block_type=block_type_name)
        # self.del_block_type(block_name)

        # camera_name = 'AT_123'
        # self.new_camera(camera_name=camera_name, camera_path='rtsp://10.9.244.23:8554/lz1-1.264',dep_name="AT_20200310112141506445", acs_lst=["人脸", "人体"])
        # self.bat_edit_camera_acs(keyword='at', acs=['人脸','结构化', '人脸人体联合'])
        # self.bat_edit_camera_acs(keyword='at')
        # print(self.del_dep('AT_20200310112141506445', cln_camera=True))
        # print(self.del_dep('g_b19f68b3c1', cln_camera=True))
        # print(self.del_dep('g_bb4c2288d1', cln_camera=True))
        # self.bat_del_camera()
        # self.chk_dep('30w')
        # self.del_all_dep()
        # self.recovery_camera('at___12121', 'AT_20200310112707860368')
        # time.sleep(2)
        # self.bat_edit_camera_acs()
        # self.get_tbl(dep_name="sf_pre_group_1")
        # self.del_all_dep()

        # self.del_all_camera_group()
        self.del_all_dep()
        # print(self.wid.wid_tree(need_dep="abc"))
        # print(self.wid.wid_tree2(need_dep="UI_pre_crow"))
        # print(self.wid.wid_tree2(need_dep="UI_pre_crow"))
        # print(self.wid.wid_tree2(need_dep="2020年03月", del_grp=True))
        # self.pre_dep_camera(camera_use=['face', 'ped', 'face_ped', 'car', 'search', 'alarm',])

        pass
