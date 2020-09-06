#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# __author__ == 'huangyongchang'

from common.common_func import *
from sc_common.sc_define import define
from v43.ele_set.page_user import UserPageEle
from v43.pub.pub_base import PublicClass
from v43.pub.pub_role import RoleModule
from common import common_func as CF


class UserAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = UserPageEle
        self.df = define()

    @shadow('分配部门')
    def slt_dep_create_user(self, dep_name=None):
        if dep_name:
            self.driver.ele_click(self.el.new_user_dep, load=1)
            self.driver.ele_input(self.el.new_user_dep_srh, dep_name, enter=True, load=1)
            self.wid.wid_tree_slt_camera_group2(need_dep=dep_name,
                                                root_e='css=body>div:last-child .rz-tree>.rz-tree-node:nth-of-type(1)')

    @shadow('选择角色')
    def slt_role_user(self, new_role=None, add_role=None):
        role_name = new_role or add_role
        if role_name:
            role_name = convert_to_array(role_name)
            self.driver.ele_click(self.el.new_user_slt_role, load=1)
            # self.wid.wid_chk_loading()
            new_role and self.driver.ele_click(self.el.new_user_role_cancel_btn)  # and time.sleep(0.5)
            for i in role_name:
                self.driver.ele_click(self.el.new_user_slt_role_.format(i))
            self.driver.ele_click(self.el.new_user_role_save_btn)

    @shadow('分配视频源')
    def slt_assign_camera(self, new_camera=None, add_camera=None):
        camera_lst = new_camera or add_camera
        if camera_lst:
            self.driver.ele_click(self.el.new_user_slt_camera_input, load=1)
            # self.wid.wid_chk_loading()
            new_camera and self.driver.ele_click(self.el.new_user_slt_camera_cancel_btn)  # and time.sleep(0.5)
            if isinstance(camera_lst, str) and camera_lst.lower() == 'all':
                camera_list = ['一级部门（可修改名称）']
            else:
                camera_list = convert_to_array(camera_lst)
            if not self.wid.wid_new_user_camera_tree2(dep_list=camera_list):
                raise Exception("新建分组时勾选视频源分组异常")
            self.driver.ele_click(self.el.new_user_slt_camera_save_btn)

    @shadow('分配人像库')
    def slt_assign_lib(self, new_lib=None, add_lib=None):
        lib_lst = new_lib or add_lib
        if lib_lst:
            self.driver.ele_click(self.el.new_user_slt_lib_input)
            if isinstance(lib_lst, str) and lib_lst.lower() == 'all':
                lib_lst = ['全选', '全选']
            for lib_ in range(2):
                if lib_ == 1:
                    self.driver.ele_click(self.el.new_user_slt_lib_slt_alert_lib, load=1)
                if '暂无数据' not in self.driver.ele_get_val(self.el.lib_content):
                    new_lib and self.driver.ele_click(self.el.new_user_lst_lib_cancel_ele, load=2)  # 清空当前角色
                    # self.wid.wid_chk_loading()
                    lst_root = 'css=.selectable-libraries>div'
                    for per_ in range(len(self.driver.ele_list(lst_root))):
                        # cb_ele = lst_root + ':nth-of-type({}) label>span:first-child'.format(per_ + 1)
                        name_ele = lst_root + ':nth-of-type({}) label>span:last-child'.format(per_ + 1)
                        name = self.driver.ele_get_val(name_ele)
                        print('=={}'.format(name))
                        if name in lib_lst:
                            self.driver.ele_click(name_ele, move=True)
                            lib_lst.remove(name)
                            if not lib_lst or name == "全选":
                                break
                if not lib_lst:
                    break
            if lib_lst:
                self.log.warning("选择的人像库未选择完全，还剩余{}".format(lib_lst))
                # return False
            self.driver.ele_click(self.el.new_user_lst_lib_save_ele)
            return True

    @shadow('选择用户')
    def chk_user(self, user_name=None, role='不限', state='不限', return_tbl=False):
        self.driver.refresh_driver()
        now_role = self.driver.ele_get_val(self.el.filter_role_ipt, 'value')
        now_state = self.driver.ele_get_val(self.el.filter_status_ipt, 'value')
        if role != now_role:
            self.wid.wid_drop_down(role, self.el.filter_role_ipt)
            self.wid.wid_chk_loading()
        if state != now_state:
            self.wid.wid_drop_down(state, self.el.filter_status_ipt)
            self.wid.wid_chk_loading()
        if user_name:
            self.driver.ele_input(self.el.srh_input, user_name, enter=True, load=True)
        if return_tbl:
            time.sleep(1)
            if self.driver.ele_exist(self.el.tbl_tr):
                all_txt = self.driver.ele_get_val(self.el.tbl)
                # return [x.split('\n')[:4] for x in all_txt.split('禁用\n')]
                # return {k: x.split('\n') for k, x in enumerate(re.split('\n查| 禁用\n| 启用\n', all_txt)[::2]) if x}
                result = {x.split('\n')[0]: x.split('\n')[1:] for x in re.split('编辑启用\n|编辑禁用\n', all_txt) if x}
                return result
        else:
            tr_el = self.el.tbl_tr
            for tr_ in range(len(self.driver.ele_list(tr_el))):
                tr_el = tr_el + ':nth-of-type({})'.format(tr_ + 1)
                name = self.driver.ele_get_val(self.el.tbl_name.format(tr_el))
                if name == user_name:
                    return tr_el

    def goto_user_detail(self, user_name):
        tr_el = self.chk_user(user_name=user_name)
        self.driver.ele_click(self.el.tbl_detail.format(tr_el))

    def goto_user_edit(self, user_name):
        tr_el = self.chk_user(user_name=user_name)
        self.driver.ele_click(self.el.tbl_edit.format(tr_el))

    def slt_more_menu(self, need_menu):
        li_lst_ele = 'css=.mark-ul>li'
        for per_ in self.driver.ele_list(li_lst_ele):
            if self.driver.ele_get_val(per_) == need_menu:
                return self.driver.ele_click(per_)

    @shadow("新建部门")
    def new_dep(self, dep_name=None, root_dep=None):
        dep_name = dep_name or CF.get_random_name(self.df.name_prefix)
        el_lst = self.chk_dep(dep_name=root_dep)
        self.driver.ele_click(el_lst[-1], move=el_lst[0])
        self.slt_more_menu(need_menu="创建下级")
        self.wid.wid_chk_loading()
        self.driver.ele_input(self.el.new_dep_input, dep_name)
        self.driver.ele_click(self.el.new_dep_confirm_btn)
        # time.sleep(0.5)
        res = self.wid.wid_get_alert_label()
        if res:
            self.collect_resource(self.df.key_dep, dep_name)
            return dep_name

    def del_dep(self, dep_name):
        self.wid.wid_chk_loading()
        print('del')
        el_lst = self.chk_dep(dep_name=dep_name)
        self.driver.ele_click(el_lst[-1], wait_time=2)
        self.slt_more_menu(need_menu="删除")
        self.driver.ele_click(self.el.del_dep_confirm_btn)
        if self.wid.wid_get_alert_label():
            self.collect_resource(self.df.key_dep, remove_value=dep_name)
            return True

    def chk_dep(self, dep_name=None):
        if not dep_name:
            dep_name = self.df.top_dep
        el_lst = self.wid.wid_dep_tree2(need_dep=dep_name)
        if not el_lst:
            self.log.error("未找到此分组[{}]".format(dep_name))
            return False
        return el_lst

    @shadow("修改部门信息")
    def edit_dep(self, dep_name, new_dep_name):
        el_lst = self.chk_dep(dep_name=dep_name)
        self.driver.ele_click(el_lst[-1])
        self.slt_more_menu(need_menu="编辑设置")
        self.driver.ele_input(self.el.new_dep_input, new_dep_name)
        self.driver.ele_click(self.el.new_dep_confirm_btn)
        if self.wid.wid_get_alert_label():
            self.collect_resource(self.df.key_dep, resource_value=new_dep_name, remove_value=dep_name)
            time.sleep(1)
            return True

    def goto_dep_detail(self, dep_name):
        el_lst = self.chk_dep(dep_name=dep_name)
        self.driver.ele_click(el_lst[-1])
        self.slt_more_menu(need_menu="查看设置")

    def get_current_user_num(self):
        return get_num_from_str(self.driver.ele_get_val(self.el.total_user_num_ele))

    def get_del_user_num(self):
        return get_num_from_str(self.driver.ele_get_val(self.el.del_user_num))

    @shadow("获取已删除用户列表")
    def get_del_user(self):
        self.driver.ele_move(self.el.del_user_num)
        tbl_a = self.el.del_user_tbl
        user_lst_lst = []
        for tr in range(len(self.driver.ele_list((self.el.del_user_tbl + '>tr')))):
            user_name = self.driver.ele_get_val(tbl_a + '>tr:nth-of-type({})>td:nth-of-type(1)'.format(tr + 1))
            user_role = self.driver.ele_get_val(tbl_a + '>tr:nth-of-type({})>td:nth-of-type(2)'.format(tr + 1))
            user_dep = self.driver.ele_get_val(tbl_a + '>tr:nth-of-type({})>td:nth-of-type(3)'.format(tr + 1))
            user_phone = self.driver.ele_get_val(tbl_a + '>tr:nth-of-type({})>td:nth-of-type(4)'.format(tr + 1))
            tmp_lst = user_name, user_role, user_dep, user_phone
            tmp_lst and user_lst_lst.append(tmp_lst)
        return user_lst_lst


class UserModule(UserAction, RoleModule):

    @shadow("创建新用户")
    def new_user(self, user_name=None, real_name=None, dep=None, role=None, lib=None, camera=None, no=None, phone=None,
                 **kwargs):
        """
        新建用户
        :param user_name:  账号
        :param real_name:  姓名
        :param dep: 所属部门
        :param role:       角色
        :param lib:    分配人像库    默认为None, 全选用all, 多个视频源用列表存储
        :param camera:      分配视频源  默认为None, 全选用all, 多个视频源用列表存储
        :param no:     警号
        :param phone: 手机号码
        :return:
        """
        # 设置参数默认值
        dft_role_name = self.df.dft_role
        user_name = user_name or get_random_name(self.df.name_prefix)
        role = role or dft_role_name
        dep = dep or self.df.top_dep
        real_name = real_name or user_name
        # 格式化 参数
        role = convert_to_array(role)
        # 参数输入
        self.driver.ele_click(self.el.new_user_btn)
        self.wid.wid_chk_loading()
        self.driver.ele_input(self.el.new_user_user_name, user_name)
        self.driver.ele_input(self.el.new_user_real_name, real_name)
        self.slt_role_user(new_role=role)
        self.slt_dep_create_user(dep_name=dep)
        if dft_role_name not in role:
            if lib:
                self.slt_assign_lib(new_lib=lib)
            if camera:
                self.slt_assign_camera(new_camera=camera)
        if no:
            self.driver.ele_input(self.el.new_user_NO, no)
        if phone:
            self.driver.ele_input(self.el.new_user_phone, phone)
        self.driver.ele_click(self.el.new_user_save_btn)
        if not self.wid.wid_get_alert_label():
            return False
        self.collect_resource(self.df.key_user, user_name)
        if kwargs.get('disable') and not self.chg_user_status(user_name=user_name, enable=False):
            self.log.error("禁用用户失败")
            return False
        return user_name

    # new csf
    @shadow("启用/禁用用户状态")
    def chg_user_status(self, user_name, enable=True):
        tr_el = self.chk_user(user_name=user_name)
        now_status = self.driver.ele_get_val(self.el.tbl_status.format(tr_el))
        if ('启用' in now_status and not enable) or ('禁用' in now_status and enable):
            self.driver.ele_click(self.el.tbl_en_dis.format(tr_el))
            if '启用' in now_status and not enable:
                self.driver.ele_click(self.el.tbl_del_confirm_btn)
            return self.wid.wid_get_alert_label()
        return True

    @shadow("重置用户密码")
    def rst_user_pwd(self, user_name):
        tr_el = self.chk_user(user_name=user_name)
        self.driver.ele_click(self.el.tbl_more.format(tr_el))
        self.driver.ele_click(self.el.tbl_rst)
        self.driver.ele_click(self.el.tbl_del_confirm_btn)
        return self.wid.wid_get_alert_label()

    @shadow("获取部门信息")
    def get_dep_info(self, dep_name):
        self.goto_dep_detail(dep_name=dep_name)
        detail_ele_lst = self.driver.ele_list(self.el.dep_info_ele)
        info_lst = [self.driver.ele_get_val(x) for x in detail_ele_lst]
        self.driver.ele_click(self.el.dep_close_btn)
        return {
            'dep': info_lst[0],
            'creator': info_lst[1],
            'create_time': info_lst[2],
            'updater': info_lst[3],
            'update_time': info_lst[4],
        }

    @shadow("获取用户信息")
    def get_user_info(self, user_name):
        self.goto_user_detail(user_name=user_name)
        detail_ele_lst = self.driver.ele_list(self.el.detail_info_ele)
        info_lst = [self.driver.ele_get_val(x) for x in detail_ele_lst]
        self.driver.ele_click(self.el.detail_close_btn)
        return {
            'account': info_lst[0],
            'name': info_lst[1],
            'dep': info_lst[2],
            'role': info_lst[3],
            'lib': info_lst[4],
            'camera': info_lst[5],
            'no': info_lst[6],
            'phone': info_lst[7],
            'creator': info_lst[8],
            'create_time': info_lst[9],
            'updater': info_lst[10],
            'update_time': info_lst[11],
        }

    @shadow("Now modify user info")
    def edit_user(self, user_name, new_real_name=None, new_dep=None, new_role=None, add_role=None,
                  new_lib=None, add_lib=None, new_camera=None, add_camera=None, new_no=None, new_phone=None, **kwargs):

        # 参数输入
        self.goto_user_edit(user_name=user_name)
        self.wid.wid_chk_loading()
        new_real_name and self.driver.ele_input(self.el.new_user_real_name, new_real_name)
        self.slt_role_user(new_role=new_role, add_role=add_role)
        self.slt_dep_create_user(dep_name=new_dep)
        if self.df.dft_role not in self.driver.ele_get_val(self.el.new_user_slt_role, 'value'):
            if new_lib:
                self.slt_assign_lib(new_lib=new_lib, add_lib=add_lib)
            if new_camera:
                self.slt_assign_camera(new_camera=new_camera, add_camera=add_camera)
        if new_no:
            self.driver.ele_input(self.el.new_user_NO, new_no)
        if new_phone:
            self.driver.ele_input(self.el.new_user_phone, new_phone)
        self.driver.ele_click(self.el.new_user_save_btn)
        if not self.wid.wid_get_alert_label():
            return False
        new_real_name and self.collect_resource(self.df.key_user, resource_value=new_real_name, remove_value=user_name)
        return new_real_name or user_name

    @shadow("删除用户")
    def del_user(self, user_name):
        tr_el = self.chk_user(user_name=user_name)
        self.driver.ele_click(self.el.tbl_more.format(tr_el))
        self.driver.ele_click(self.el.tbl_del)
        self.driver.ele_click(self.el.tbl_del_confirm_btn)
        if self.wid.wid_get_alert_label():
            self.collect_resource(self.df.key_user, remove_value=user_name)
            return True

    @shadow("新建用户-角色-部门")
    def new_user_role_dep(self, user, role=None, dep=None, lib=None, camera=None, chg_right_dict='all', switch=False,
                          **kwargs):
        self.driver.ele_wait()
        self.into_menu(menu_name=self.df.ModDefine.mod_role)
        if not role or not self.chk_role(role_name=role):
            role = self.new_role(role_name=role, chg_right_dict=chg_right_dict)
        self.into_menu()
        if not dep or not self.chk_dep(dep_name=dep):
            dep = self.new_dep(dep_name=dep)
        if not self.new_user(user_name=user, dep=dep, role=role, lib=lib, camera=camera, **kwargs):
            self.log.error("创建用户[{}]异常".format(user))
            return False
        if switch:
            pass  # TODO csf
        return user

    @shadow("新建用户-角色-部门")
    def new_user_role_dep_v2(self, user, role=None, dep=None, lib=None, camera=None, only_right=None, remove_right=None
                             , switch=False, **kwargs):
        self.driver.ele_wait()
        self.into_menu(menu_name=self.df.ModDefine.mod_role)
        if not role or not self.chk_role(role_name=role):
            role = self.new_role_v2(role_name=role, only_right=only_right, remove_right=remove_right)
        self.into_menu()
        if not dep or not self.chk_dep(dep_name=dep):
            dep = self.new_dep(dep_name=dep, root_dep=kwargs.get('root_dep'))
        if not self.new_user(user_name=user, dep=dep, role=role, lib=lib, camera=camera, **kwargs):
            self.log.error("创建用户[{}]异常".format(user))
            return False
        if switch:
            pass  # TODO csf
        return user

    @shadow("删除用户-角色-部门")
    def del_user_role_dep(self, users, roles, deps):
        self.driver.refresh_driver()
        if users or deps:
            self.into_menu(menu_name=self.df.ModDefine.mod_user)
            for user in convert_to_array(users):
                self.del_user(user_name=user)
            for dep in convert_to_array(deps):
                self.del_dep(dep_name=dep)
        if roles:
            self.into_menu(menu_name=self.df.ModDefine.mod_role)
            for role in convert_to_array(roles):
                self.del_role(role_name=role)
        return True

    def pre_task_user(self):
        tbl = self.chk_user(user_name=self.df.pre_res, return_tbl=True)
        pre_dep = self.df.top_dep
        dep_2 = self.df.dep_2_
        dep_3 = self.df.dep_3_
        new_user_lst = []
        # 一级部门下的普通用户
        if not tbl or self.df.pre_com_user not in tbl:
            # 全权限 普通用户
            self.new_user_role_dep_v2(user=self.df.pre_com_user, role=self.df.pre_com_user,
                                      dep=pre_dep,
                                      chg_right_dict='all',
                                      lib='all',
                                      camera='all',
                                      )
            new_user_lst.append(self.df.pre_com_user)
        # 二级部门下的用户
        # if self.chk_dep(dep_name=dep_2):
        #     self.new_dep(dep_name=dep_2)
        # tbl = self.chk_user(user_name=self.df.pre_res, return_tbl=True)
        if not tbl or self.df.pre_com_2_user not in tbl:
            # 所有权限普通用户
            # tmp_dict = self.df.get_right_dict(remove_right=["布控-审核", '布控-审批'])
            self.new_user_role_dep_v2(user=self.df.pre_com_2_user, role=self.df.pre_com_2_user,
                                      dep=dep_2,
                                      root_dep=pre_dep,
                                      # remove_right=["布控-审核", '布控-审批'],
                                      lib='all',
                                      camera='all',
                                      )
            new_user_lst.append(self.df.pre_com_2_user)
        if not tbl or self.df.pre_com_2_no_app_user not in tbl:
            # 无审批权限用户
            # tmp_dict = self.df.get_right_dict(remove_right='布控-审批')
            self.new_user_role_dep_v2(user=self.df.pre_com_2_no_app_user, role=self.df.pre_com_2_no_app_user,
                                      dep=dep_2,
                                      root_dep=pre_dep,
                                      remove_right=["布控-审批"],
                                      lib='all',
                                      camera='all',
                                      )
            new_user_lst.append(self.df.pre_com_2_no_app_user)
        # 三级部门下的用户
        # if self.chk_dep(dep_name=dep_3):
        #     self.new_dep(dep_name=dep_3)
        # tbl = self.chk_user(user_name=self.df.pre_res, return_tbl=True)
        if not tbl or self.df.pre_com_3_user_no_edit not in tbl:
            # 无编辑审批审核权限用户
            tmp_dict = self.df.get_right_dict(remove_right=[])
            self.new_user_role_dep_v2(user=self.df.pre_com_3_user_no_edit, role=self.df.pre_com_3_user_no_edit,
                                      dep=dep_3,
                                      root_dep=dep_2,
                                      remove_right=["布控-审核", "布控-审批", "布控-编辑"],
                                      lib='all',
                                      camera='all',
                                      )
            new_user_lst.append(self.df.pre_com_3_user_no_edit)
        if not tbl or self.df.pre_com_3_user_no not in tbl:
            # 无审批和审核权限用户
            tmp_dict = self.df.get_right_dict(remove_right=[])
            self.new_user_role_dep_v2(user=self.df.pre_com_3_user_no, role=self.df.pre_com_3_user_no,
                                      dep=dep_3,
                                      root_dep=dep_2,
                                      # chg_right_dict=tmp_dict,
                                      remove_right=["布控-审核", "布控-审批"],
                                      lib='all',
                                      camera='all',
                                      )
            new_user_lst.append(self.df.pre_com_3_user_no)

        for pre_user in new_user_lst:
            self.switch_new_user(pre_user)
        if new_user_lst:
            self.switch_user(user=self.user, pwd=self.pwd)

    def main(self):
        # self.new_user_role_dep('hello_world333', role=None, dep=None, camera=['UI_pre_', 'sf_pre_group_1'],
        #                        lib=['预置布控库65onlyread', '预置布控库1onlyread', '人像库3347c09982'],
        #                        )
        # self.chk_user('a', role='不限', state="已启用", return_tbl=True)
        # # self.pre_task_user()
        # # self.get_del_user()
        # # self.into_menu("角色管理")
        # # self.get_role_power(role_name="UI_pre_普通用户")
        #
        # menu_list = [
        #     # "数据汇智",
        #     # "操作导航",
        #     # "人脸检索",
        #     # "融合检索",
        #     # "行人检索",
        #     # "车辆检索",
        #     # "智能检索",
        #     # "时空过滤",
        #     # "身份检索",
        #     # "离线检索",
        #     "布控",
        #     # "人群分析",
        #     "卡口",
        #     "视图工具",
        #     # "解析管理",
        #     "告警中心",
        #     "任务中心",
        #     "视图源管理",
        #     "人像库管理",
        #     "角色管理",
        #     "用户管理",
        #     "操作日志",
        #     "系统设置",
        #     "个人中心",
        #     # "消息提醒",
        #     # "地图中心",
        #     # "退出地图中心",
        #     "退出",
        # ]
        # # for menu_ in menu_list:
        # #     # print(menu_)
        # #     self.into_menu(menu_)
        # # time.sleep(2)
        #
        # self.into_menu('卡口')
        # self.driver.ele_click('css=.four-screen', move=True)
        # self.driver.ele_click('css=.four-screen', move=True)
        # self.driver.ele_click('css=.one-screen')
        # self.driver.ele_click('css=.four-screen')
        # self.driver.ele_click('css=.one-screen')
        # self.driver.ele_click('css=.four-screen')
        # time.sleep(2)

        # tbl = self.chk_user(user_name=self.df.pre_res, return_tbl=True)
        # pre_dep = self.df.top_dep
        # self.new_user_role_dep_v2(user="UI_tst_", role='UI_tst_',
        #                        dep=pre_dep,
        #                        only_right="布控-审批", need_right=None,
        #                        lib='all',
        #                        camera='all',
        #                        )

        self.pre_task_user()