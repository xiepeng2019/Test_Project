#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


import time
from selenium.webdriver.common.by import By

from sc_common.sc_define import define
from v43.ele_set.page_menu import MenuPageEle, LoginPageEle


class MainPage:

    @staticmethod
    def into_settings(driver, menu_name):
        # driver.click_class("rz-button map rz-button--primary rz-button--small is-round")
        driver.move_over_to_element((By.XPATH, "//span[text()='系统设置']"))
        driver.click_xpath("//li[text()='" + menu_name + "'][@class='rz-dropdown-menu__item item']")
        # driver.action.move_by_offset(200, 200).perform()

    @staticmethod
    def into_menu_v1(driver, menu_name):
        """
        菜单导航 目前支持大部分菜单
        :param driver:
        :param menu_name:
        :return:
        """
        if not menu_name:
            return
        move_flag = False
        if menu_name == "数据汇智" or menu_name == "操作导航":
            driver.ele_move(MenuPageEle.left_menu_ele.format("首页"))
            driver.ele_click(MenuPageEle.sub_menu_ele.format(menu_name), move=move_flag)
        elif "检索" in menu_name or "时空过滤" in menu_name:
            driver.ele_move(MenuPageEle.left_menu_ele.format("检索"))
            driver.ele_click(MenuPageEle.sub_menu_ele.format(menu_name), move=True)
        elif "布控" in menu_name or "人群分析" in menu_name or "卡口" in menu_name or "解析管理" in menu_name or "技战法" in menu_name:
            # print(MenuPageEle.left_menu_ele.format(menu_name))
            driver.ele_click(MenuPageEle.left_menu_ele.format(menu_name), move=move_flag)
        elif "区域碰撞" in menu_name or "照片一比一" in menu_name or "入库助手" in menu_name or "查重" in menu_name:
            # print(MenuPageEle.left_menu_ele.format(menu_name))
            driver.ele_click(MenuPageEle.left_menu_ele.format("视图工具"), move=move_flag)
            time.sleep(1)
            driver.ele_click(MenuPageEle.view_tool_op.format(typo=menu_name), move=True)
        elif "退出地图中心" in menu_name:
            while True:
                now_title_num = len(driver.ele_list(MenuPageEle.map_load_finish_ele))
                if now_title_num > 5:
                    break
                time.sleep(1)
            driver.ele_click(MenuPageEle.map_center_ele, move=move_flag)
        elif "地图中心" in menu_name:
            driver.ele_click(MenuPageEle.map_menu_ele)
        elif "个人中心" in menu_name or "退出" in menu_name:
            # driver.ele_move(MenuPageEle.top_person_menu)
            # sub_menu_ele = MenuPageEle.top_sub_menu_logout if '退出' in menu_name else MenuPageEle.top_sub_menu.format(menu_name)
            # driver.ele_click(sub_menu_ele, wait_time=2)
            if '退出' in menu_name:
                driver.ele_click(MenuPageEle.top_sub_menu_logout, move=MenuPageEle.top_person_menu, wait_time=2)
                return True
            else:
                driver.ele_click(MenuPageEle.top_sub_menu.format(menu_name), move=MenuPageEle.top_person_menu,
                                 wait_time=2)
        elif "管理" in menu_name or "操作日志" in menu_name or "系统设置" in menu_name or "设备智检" in menu_name:
            for _ in range(2):
                try:
                    # driver.ele_move(MenuPageEle.top_system_menu)
                    menu_ele = driver.ele_exist(MenuPageEle.top_sub_menu.format(menu_name))
                    tmp_video_lst = ["视图源管理", "设备智检"]
                    if menu_name in tmp_video_lst:
                        if not menu_ele:
                            tmp_video_lst.remove(menu_name)
                            menu_name = tmp_video_lst[0]
                            menu_ele = driver.ele_exist(MenuPageEle.top_sub_menu.format(menu_name))
                            driver.ele_click(menu_ele, move=MenuPageEle.top_system_menu, wait_time=2)
                        driver.ele_click(menu_ele, move=MenuPageEle.top_system_menu, wait_time=2)
                        if menu_name == "设备智检":
                            driver.ele_click(MenuPageEle.top_sub_menu_video_menu)  # 设备智检时点管理
                    else:
                        driver.ele_click(menu_ele, move=MenuPageEle.top_system_menu, wait_time=2)
                    break
                except Exception as e:
                    continue
            else:
                raise Exception("菜单[{}]点击异常".format(menu_name))
        elif "告警中心" in menu_name:
            driver.ele_click(MenuPageEle.top_alarm_menu, move=move_flag)
        elif "任务中心" in menu_name:
            driver.ele_click(MenuPageEle.top_task_menu, move=move_flag)
        elif "技战法" in menu_name:
            driver.ele_click(MenuPageEle.left_menu_ele.format("技战法"))
        elif "消息提醒" in menu_name:
            driver.ele_click(MenuPageEle.top_message_menu, move=move_flag)
        else:
            raise Exception("导航菜单名[{}]不正确".format(menu_name))
        driver.chk_loading()

    @staticmethod
    def login_in(driver, username, password, judge=True):
        """
        csf 首页登录，需要传入参数：用户名, 密码
        username:用户名
        password:用户密码
        """
        driver.ele_input(LoginPageEle.login_user, username)
        driver.ele_input(LoginPageEle.login_pwd, password)
        driver.ele_click(LoginPageEle.login_btn, wait_time=5)
        # alert_msg = driver.get_alert_label()
        # if alert_msg:
        #     return alert_msg
        if judge and driver.ele_exist(LoginPageEle.success_ele):
            return False
        return True

    @staticmethod
    def login_out(driver):
        """
        csf 注销
        :param driver:
        :return:
        """
        # if not driver.ele_exist(LoginPageEle.login_user, timeout=1):
        driver.refresh_driver()
        MainPage.into_menu(driver, "退出")
        return driver.ele_exist(LoginPageEle.login_user, timeout=1)

    @staticmethod
    def login_first_act(driver, user, dft_pwd='88888888', new_pwd='admin1234'):
        """
        csf 新用户首次登录 修改密码
        :param driver:
        :param user:
        :param dft_pwd:
        :param new_pwd:
        :return:
        """
        MainPage.login_in(driver, username=user, password=dft_pwd, judge=False)
        # driver.chk_loading(loading_to=1)
        if driver.ele_exist(LoginPageEle.modify_ele, timeout=2):
            driver.ele_input(LoginPageEle.pwd_ipt, new_pwd)
            driver.ele_input(LoginPageEle.re_pwd_ipt, new_pwd)
            driver.ele_click(LoginPageEle.confirm_btn)
            return driver.get_alert_label(wait_miss=True)
        raise Exception("首次登录时密码错误或者其它异常，Pls chk")

    @staticmethod
    def judge_current_page(driver, mod_name):
        now_page = driver.get_url()
        mod_page_dict = define.ModDefine.page_url_dict
        if mod_name not in mod_page_dict:  # 无此menu的对应url 时返回False
            return -1
        # if mod_page_dict[mod_name] in now_page:
        if now_page.endswith(mod_page_dict[mod_name]):
            return True

    @staticmethod
    def into_menu(driver, menu_name=None):  # 各属性模块的导航
        mod_page_dict = define.ModDefine.page_url_dict
        if menu_name not in mod_page_dict:  # 无此menu的对应url 时返回False
            MainPage.into_menu_v1(driver, menu_name)
        else:
            into_retry = 3
            while into_retry:
                now_page = driver.get_url()
                if not now_page.endswith(mod_page_dict[menu_name]):
                    if mod_page_dict[menu_name] in now_page and now_page.endswith('esult'):
                        # if mod_page_dict[menu_name] in now_page:
                        break
                    if into_retry != 3:
                        print('retry')
                    MainPage.into_menu_v1(driver, menu_name)
                    into_retry -= 1
                else:
                    break
