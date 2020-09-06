#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


from common.common_func import *
from sc_common.sc_define import define
from v43.ele_set.page_search import SearchPageEle
from v43.pub.pub_base import PublicClass
from v43.pub.pub_menu import MainPage


class SearchAction(PublicClass):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.CommonSearch
        self.df = define()

    # @shadow("进入检索页")
    # def into_menu(self, menu_name):
    #     """
    #     进入所在检索Page
    #     menu_name:菜单名称
    #     """
    #     MainPage.into_menu(self.driver, menu_name)

    @shadow("上传图片")
    def upload_pic(self, img_path):
        """
        上传图片
        file_path:
        """
        self.wid.wid_upload(img_path=img_path)

    def txt_search_input(self, txt, txt_type=None):
        self.driver.ele_click(self.el.f_txt_trig_ele)
        time.sleep(0.5)
        self.driver.ele_input(self.el.f_txt_input_ele, txt)
        if txt_type and isinstance(txt_type, str):
            if 'id' in txt_type or '身份' in txt_type:
                self.driver.ele_click(self.el.f_txt_id_checkbox.format('身份'))
            elif 'plate' in txt_type or '车牌' in txt_type:
                self.driver.ele_click(self.el.f_txt_id_checkbox.format('车牌'))
        self.driver.ele_click(self.el.f_search_button)

    def chg_threshold(self, threshold):
        self.driver.ele_input(self.el.left_menu_threshold_, threshold)

    @shadow("选择日期")
    def slt_date(self, start_time=None, end_time=None):
        self.wid.wid_slt_date(start_time=start_time, end_time=end_time)

    @shadow("选择视频源")
    def slt_camera(self, camera_lst=None):
        """
        选择视频源
        :param camera_lst:  视频源名字 支持一个或多个
        :return:
        """
        self.wid.wid_slt_camera(camera_lst=camera_lst)

    def back_search_index(self):
        return self.wid.back_module_index()

    def goto_history(self):
        self.driver.ele_click(self.el.history_btn)
        self.wid.wid_chk_loading()


class CommonSearchModule(SearchAction):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.search_cate = kwargs.get('search')

    def history_get_all(self):
        self.goto_history()
        his_el_lst = self.driver.ele_list(self.el.his_cap_lst)
        if not his_el_lst:
            return dict()
        his_lst = [self.driver.ele_get_val(x) for x in his_el_lst]
        if self.driver.ele_exist(self.el.his_page_btn):
            btn_lst = self.driver.ele_list(self.el.his_page_btn)
            for btn in btn_lst[1:]:
                self.driver.ele_click(btn, load=True)
                now_his_lst = [self.driver.ele_get_val(x) for x in self.driver.ele_list(self.el.his_cap_lst)]
                his_lst.extend(now_his_lst)
        return his_lst

    def get_all_capture_lib(self, img_mix=False, need_num=False, id_search=False):
        self.wid.scroll_loading_all()
        t_start = time.time()
        all_cap_dict = {}
        all_captures = self.driver.ele_list(self.el.all_lib_capture_ele)
        per_ = 0
        for per_ in range(len(all_captures)):
            slt_status = (not id_search) and 'is-checked' in self.driver.ele_get_val(
                self.el.cap_slt_status_ele.format(per_ + 1), 'class', chk_visit=False)
            threshold = (not id_search) and self.driver.ele_get_val(self.el.per_lib_cap_threshold_ele.format(per_ + 1))
            name = self.driver.ele_get_val(self.el.per_lib_cap_name_ele.format(per_ + 1))
            cap_id = self.driver.ele_get_val(self.el.per_lib_cap_id_ele.format(per_ + 1))
            cap_lib = self.driver.ele_get_val(self.el.per_lib_cap_lib_ele.format(per_ + 1))
            if img_mix:
                more_ele = self.el.per_lib_cap_more_lib_ele.format(per_ + 1)
                if self.driver.ele_exist(more_ele):
                    self.driver.ele_move(more_ele)
                    time.sleep(0.3)
                    ele_lst = self.driver.ele_list(self.el.per_lib_cap_more_lib_lst)
                    other_lib_lst = [x.text for x in ele_lst if
                                     'display' not in self.driver.ele_get_val(x, 'style', chk_visit=False)]
                    cap_lib = [cap_lib]
                    cap_lib.extend(other_lib_lst)
            if id_search:
                all_cap_dict[per_] = [name, cap_id, cap_lib]
            else:
                all_cap_dict[per_] = [slt_status, threshold, name, cap_id, cap_lib]
            if need_num and per_ > need_num:
                break
        t_end = time.time() - t_start
        self.driver.ele_move(self.el.per_lib_cap_name_ele.format(per_ + 1))
        self.log.info("获取[{}]个数据， 耗时[{}]".format(len(all_cap_dict), t_end))
        return all_cap_dict

    def get_all_capture(self, need_slt=False, veh_flag=False, **kwargs):
        """
        获取当前检索页面，所有检索抓抓捕图，返回 dict # TODO 暂无法适配车辆检索结果的时间排序
        :param need_slt:
        :param veh_flag:
        :return:
        """
        if not kwargs.get('not_load'):
            self.wid.scroll_loading_all(**kwargs)
        t_start = time.time()
        all_slt_wid = self.driver.ele_list(self.el.all_capture_lst_slt_ele)
        if not all_slt_wid:
            return False
        slt_status_lst = ['is-checked' in x.get_attribute('class') for x in
                          self.driver.ele_list(self.el.all_capture_lst_slt_ele)]
        all_cap_dict = {}
        # 1 500抓拍获取 10s以内,但未适配所有检索页
        if not veh_flag:
            now_page_val = self.driver.ele_get_val(self.el.all_capture_data_ele)
            # split_val = '比中\n%\n' if '比中' in now_page_val else '%\n'
            cap_info_lst = [x.strip('\n').split('\n') for x in re.split('比中\n%\n|%', now_page_val) if x]
            for i, per_wid in enumerate(cap_info_lst):
                per_wid.insert(0, slt_status_lst[i])
                per_wid[1] = float(per_wid[1])
                all_cap_dict[i] = per_wid
        else:
            plate_no_lst = [x.text for x in self.driver.ele_list(self.el.all_capture_plate_no)]
            img_info_lst = [x.text for x in self.driver.ele_list(self.el.all_capture_img_info_no)]
            for i in range(len(slt_status_lst)):
                camera, cap_date = img_info_lst[i].split('\n')
                all_cap_dict[i] = [slt_status_lst[i], plate_no_lst[i * 2], camera,
                                   cap_date]  # mx 2020.8.21 获取车牌号，会有2条记录。原：all_cap_dict[i] = [slt_status_lst[i], plate_no_lst[i], camera, cap_date]
        t_end = time.time() - t_start
        self.log.info("获取[{}]个数据， 耗时[{}]".format(len(all_slt_wid), t_end))
        return all_cap_dict

    def filter_slt_camera(self, need_dep=None, search=False):
        """
        检索抓拍过滤时 依视频源过滤时的 视频源树结构
        :return:
        """
        if not need_dep or isinstance(need_dep, int):
            camera_lst = []
        if need_dep and isinstance(need_dep, str) and search:
            self.driver.ele_input(self.el.left_search_camera_ipt, need_dep, enter=True)

        def slt_camera_tree(root_e=None):
            root_e = root_e or "css=.root-tree"
            all_root_ele = self.driver.ele_list(root_e + '>.rz-big-data-tree-node')
            # print(len(all_root_ele))
            tmp_set = []
            for i in range(len(all_root_ele)):
                root_node = root_e + '>div:nth-of-type({})'.format(i + 1)
                root_node_1 = root_node + '>div:nth-of-type(1)'
                expand_ele = root_node_1 + '>*:nth-child(1)'
                name_ele = root_node_1 + '>*:nth-child(2)'
                num_ele = root_node_1 + '>*:last-child'
                now_name = self.driver.ele_get_val(name_ele)
                # print(now_name)
                if need_dep != now_name:
                    tmp_val = self.driver.ele_get_val(expand_ele, attr_name='class')
                    if 'rz-icon-caret-right' in tmp_val and 'icon-video' not in tmp_val:
                        tmp_set.append(root_node)
                    if 'icon-video' in tmp_val:
                        if not need_dep or isinstance(need_dep, int):
                            camera_lst.append(num_ele)
                            if isinstance(need_dep, int) and len(camera_lst) >= need_dep:
                                return camera_lst
                else:
                    # print("=" * 80)
                    self.driver.ele_click(num_ele, move=True, load=True)
                    if not need_dep or isinstance(need_dep, int):
                        camera_lst.append(num_ele)
                        if isinstance(need_dep, int) and len(camera_lst) >= need_dep:
                            return camera_lst
                    else:
                        return name_ele, num_ele
            for j in tmp_set:
                expand_el = j + '>div:nth-of-type(1)>*:nth-child(1)'
                if 'expanded' not in self.driver.ele_get_val(expand_el, 'class'):
                    self.driver.ele_click(expand_el)
                    time.sleep(0.5)
                return_val = slt_camera_tree(j + '>div:nth-of-type(2)')
                if return_val:
                    return return_val

        if not need_dep:
            slt_camera_tree()
            return camera_lst
        else:
            return slt_camera_tree() or camera_lst

    def filter_capture_property(self, face_property=None):
        self.driver.ele_click(self.el.flt_face_trig)
        for k, v in face_property.items():
            if '性别' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_sex_input)
            if '年龄' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_age_input)
            if '眼镜' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_glass_input)
            if '胡' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_beard_input)
            if '口罩' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_mask_input)
            if '帽子' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_cat_input)
        self.driver.ele_click(self.el.flt_confirm_btn)

    def filter_capture(self, camera=None, face_property=None, sort=None, select=False):
        """
        过滤条件
        :param camera:  视频源/视频源分组, 单字符串
        :param face_property: {'性别':'', '年龄':'','眼镜':'','胡型':'','口罩':'','帽子':''} 组合dict
        :param sort: 时间(默认)，视频源， 相似度
        :param select: 只看比中
        :return:
        """
        if camera:
            self.driver.ele_click(self.el.flt_camera_trig_el)
            self.filter_slt_camera(need_dep=camera)
        if face_property:
            self.filter_capture_property(face_property=face_property)
        sort and self.wid.wid_drop_down(val=sort, trig_wid=self.el.flt_sort_trig_el) and self.wid.wid_chk_loading()
        self.slt_show_slt_only_act(show=select)
        return self.get_all_capture()

    def slt_show_slt_only_act(self, show=True):
        """
        是否开启 仅显示比中，
        :param show:
        :return:
        """
        if ('is-check' not in self.driver.ele_get_val(self.el.only_show_el, 'class') and show) \
                or ('is-check' in self.driver.ele_get_val(self.el.only_show_el, 'class') and not show):
            self.driver.ele_click(self.el.only_show_slt_el, wait_time=3, load=True)
            self.wid.wid_chk_loading()

    def get_slt_number(self):
        """
        获取 当前页的 比中数量
        :return:
        """
        return get_num_from_str(self.driver.ele_get_val(self.el.only_show_slt_num_el))

    def chg_intel_slt(self, intel_slt=True, current_page=None):
        """
        修改智能比中的 状态
        :param intel_slt:
        :param current_page:
        :return:
        """
        # if isinstance(current_page, str):
        #     if current_page == 'main':
        #         btn_ = self.el.intel_slt_btn_main
        #     else:
        #         btn_ = self.el.intel_slt_btn_sub
        # else:
        btn_ = self.el.intel_slt_btn

        judge_val = 'is-checked'
        now_status = self.driver.ele_get_val(btn_, 'class', chk_visit=False)
        if judge_val in now_status and not intel_slt or judge_val not in now_status and intel_slt:
            self.driver.ele_click(btn_)
            self.wid.wid_chk_loading()
        return judge_val in now_status and intel_slt or judge_val not in now_status and not intel_slt

    def chg_intel_slt_threshold(self, new_threshold):
        """
        修改智能比中的 阈值
        :param new_threshold:
        :return:
        """
        now_threshold = self.driver.ele_get_val(self.el.intel_slt_threshold_ele).strip('%')
        # self.log.error(now_threshold)
        if now_threshold != new_threshold:
            self.driver.ele_click(self.el.intel_slt_threshold_ele, wait_time=4)
            self.driver.ele_input(self.el.intel_threshold_ipt, new_threshold)
            self.driver.ele_click(self.el.intel_confirm_btn, load=True)

    def slt_cap_act(self, slt_num=10, region=None, veh_flag=False):
        """
        检索结果页，比中结果，支持两种，slt_num 和region     # TODO 暂无法适配车辆检索结果的时间排序
        :param slt_num: 一个一个比中，默认从第一个开始
        :param region: 拖划式比中，1为一排
        :return:
        """
        # if not veh_flag:
        if slt_num and not region:
            # all_captures_len = len(self.driver.ele_list(self.el.all_capture_ele))
            # slt_num = all_captures_len if all_captures_len < slt_num else slt_num
            # for per_ in range(slt_num):
            #     self.driver.ele_move(self.el.per_cap_ele.format(per_ + 1))
            #     self.driver.ele_click(self.el.cap_slt_cbox.format(per_ + 1))

            all_captures_wid = self.driver.ele_list(self.el.all_capture_lst_ele)
            all_captures_slt_wid = self.driver.ele_list(self.el.all_capture_lst_slt_ele)
            now_img_num = len(all_captures_wid)
            self.log.warning('共有图片{}, 现在比中{}'.format(now_img_num, slt_num))
            if slt_num > now_img_num:
                slt_num = now_img_num
            for i in range(slt_num):
                self.driver.ele_move(all_captures_wid[i])
                time.sleep(0.4)
                self.driver.ele_click(all_captures_slt_wid[i], wait_time=2)
        if region:
            all_cap = self.driver.ele_list(self.el.all_cap_ele)
            start_el = all_cap[0]
            width = 1380
            height = region * 215 - 20
            time.sleep(5)
            self.wid.move_to_ele_near(start_el, -15, 0).click_and_hold().move_to_element_with_offset(start_el, width,
                                                                                                     height).release().perform()
            time.sleep(1)

        all_cap = self.get_all_capture(need_slt=True, not_load=True, veh_flag=veh_flag)
        slt_num = len([x for x in all_cap.values() if x[0]])
        return slt_num

    def base_search(self, img_path=None, need_all=False, slt=False, threshold=None, txt_=None, close_int_slt=False,
                    click=False, txt_type="全部", **kwargs):
        """
        图片/文本检索
        :param img_path:    图片检索 所使用的图片
        :param need_all:    是否需要加载 所有抓拍，默认只有一页，一页最大150张
        :param slt:         是否手动选中一些抓拍图
        :param threshold:   阈值
        :param txt_:        文本检索
        :param close_int_slt:   是否关闭智能检索，默认False不关闭
        :param click:       针对多重检索(融合/智能) 需要确认图片点击检索按钮
        :param txt_type:       智能检索时 文本的类别
        :return:
        """
        if img_path and not txt_:  # 图片检索
            self.upload_pic(img_path)
        elif not img_path and txt_:  # 文本检索(暂适配了车辆/库的文本)
            self.txt_search_input(txt=txt_, txt_type=txt_type)
        else:
            self.driver.ele_click(self.el.f_search_button)
        if click:  # 智能/融合检索 需图片确认后 点击检索按钮
            time.sleep(1)
            self.driver.ele_click(self.el.f_search_button, wait_time=2)
        self.driver.chk_loading()
        judge_veh_ele = self.el.filter_com_el.format("车辆属性")
        if self.driver.ele_exist(judge_veh_ele, timeout=1):
            self.driver.ele_click(judge_veh_ele)
            self.driver.ele_click(self.el.filter_com_btn.format("重置"), load=True)
        if threshold:
            self.chg_threshold(threshold)
            self.driver.ele_click(self.el.left_menu_srh_btn)
            self.wid.wid_chk_loading()
        need_all and self.wid.scroll_loading_all(**kwargs)
        if (slt or close_int_slt) and self.driver.ele_exist(self.el.intel_slt_btn):  # 如有智能比中，暂时关闭
            more_lst = self.driver.ele_list(self.el.result_more)  # 自动为智能检索 点击 人脸抓拍的更多
            if more_lst:
                self.driver.ele_click(more_lst[1], load=True)
            self.chg_intel_slt(intel_slt=False)
        if slt:  # 手动比中3行 抓拍图
            self.slt_cap_act(region=3, veh_flag=kwargs.get('veh_flag'))
            time.sleep(1)

    # @shadow("图片检索 B目标")
    # def img_search_b(self, img_path=None, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False):
    #     """
    #     第二个目标检索
    #     :param img_path:
    #     :param start_time:
    #     :param end_time:
    #     :param camera_lst:
    #     :param need_all:
    #     :param slt:
    #     :return:
    #     """
    #     self.driver.ele_click(self.el.s_new_target_ele)
    #     self.img_search(img_path=img_path, start_time=start_time, end_time=end_time, camera_lst=camera_lst, need_all=need_all, slt=slt)

    def get_slt_num(self):
        """
        获取当前检索页 比中数量
        :return:
        """
        return int(self.driver.ele_get_val(self.el.slt_num_ele))

    def chk_favourite_status(self):
        now_slt_status = self.driver.ele_get_val(self.el.fav_search_status_ele, 'class')
        return 'disable' not in now_slt_status

    def favourite_search_act(self):
        """
        在当前检索页 点击 收藏 动作
        :return:
        """
        self.driver.ele_click(self.el.fav_search_ele)  # , load=True)
        fav_res = self.wid.wid_get_alert_label(wait_miss=True)
        return '收藏比中成功' in fav_res

    def export_search_act(self):
        """
        在当前检索页，点击 导出检索 动作
        :return:
        """
        self.driver.ele_click(self.el.export_search_ele)
        return self.wid.wid_task_tip(wait_miss=True)

    def goto_trace_act(self):
        """
        在当前检索页 点击 查看轨迹 动作
        :return:
        """
        self.driver.ele_click(self.el.trace_ele)

    def trace_sort_act(self, sort='视频'):
        """
        在轨迹页面，点击 轨迹排序 动作
        :param sort:    排序 有 视频源 和 时间两种
        :return:
        """
        now_sort = self.driver.ele_get_val(self.el.trace_sort_trig)
        if sort not in now_sort:
            self.wid.wid_drop_down(sort, self.el.trace_sort_trig)
            self.wid.wid_chk_loading()

    def trace_filter_time(self, time_=None):
        if time_:
            time_lst = []
            now_time_wid_lst = self.trace_get_date_lst_act(trig_wid='过滤')
            self.driver.ele_click(self.el.trace_filter_all)  # 点击全选，取消所有日期，便于点击所需日期
            if isinstance(time_, list):
                for per_ in now_time_wid_lst:
                    if self.driver.ele_get_val(per_) in time_:
                        date_val = self.driver.ele_get_val(per_)
                        self.driver.ele_click(per_)
                        time_.remove(date_val)
                        time_lst.append(date_val)
                    if not time_:
                        break
            elif isinstance(time_, int):
                for per_ in now_time_wid_lst:
                    if time_:
                        self.driver.ele_click(per_)
                        time_ -= 1
                        time_lst.append(self.driver.ele_get_val(per_))
                    else:
                        break
            else:
                self.driver.ele_click(now_time_wid_lst[0])
            self.driver.ele_click(self.el.trace_filter_confirm_btn, load=True)
            return time_lst

    def trace_dot_(self):
        """
        在轨迹页面 点击轨迹
        :return:
        """
        self.driver.ele_click(self.el.trace_companion_ele)

    def trace_dot_capture_act(self, el):
        """
        轨迹页面 左边比中结果处，点击比中图后， 地图中点位的 视频源 点击动作
        :param el:
        :return:
        """
        self.driver.ele_click(el, load=True)

    def trace_dot_capture_get_total(self):
        """
        轨迹页面 左边比中结果处，点击比中图后， 地图中点位的 视频源 抓拍记录页面 全部抓拍数
        :return:
        """
        return int(self.driver.ele_get_val(self.el.trace_dot_capture_num)) or time.sleep(1) or int(
            self.driver.ele_get_val(
                self.el.trace_dot_capture_num))

    def trace_dot_camera_act(self):
        """
        轨迹页面 左边比中结果处，点击比中图后， 地图中点位的 点位点击，并获取此点位的比中数量
        :return:
        """
        now_num = get_num_from_str(self.driver.ele_get_val(self.el.trace_dot_ele))
        plus_el = self.el.trace_map_plus
        for i in range(10):
            self.driver.ele_click(plus_el)
            if i > 4 and try_catch(self.driver.ele_click, ele=self.el.trace_dot_ele, wait_time=1, judge=True):
                break
        return now_num

    def trace_dot_captures_act(self):
        """
        轨迹页面 左边比中结果处，点击比中图后， 地图中点位的 视频源列表获取
        :return:
        """
        return self.driver.ele_list(self.el.trace_dot_camera_lst)

    def trace_companions_act(self):
        """
        轨迹页面 点击同行人 动作
        :return:
        """
        return self.driver.ele_click(self.el.trace_companion_ele, load=True)

    def trace_get_date_lst_act(self, trig_wid=None, rtn_val=False):
        """
        轨迹页面 左边比中结果处，点击日期过滤后，获取所有日期控件列表
        :return:
        """
        if '过滤' in trig_wid:
            self.driver.ele_click(self.el.trace_filter_trig)
        elif '显示' in trig_wid:
            self.driver.ele_click(self.el.trace_dis_ele)
        elif '播放' in trig_wid:
            self.driver.ele_click(self.el.trace_play_ele)
        wid_lst = self.driver.ele_list(self.el.trace_filter_date)
        if not rtn_val:
            return wid_lst
        else:
            return [self.driver.ele_get_val(x) for x in wid_lst]

    def trace_get_page_capture_act(self):
        """
        轨迹页面 左边比中结果处，获取当前页面(未滚动) 所有抓拍元素
        :return:
        """
        return self.driver.ele_list(self.el.trace_sort_per_cap_ele)

    def trace_get_all_capture(self):
        """
        轨迹页面 左边比中结果处，获取所有的比中抓拍图(会自动滚动页面)
        :return:
        """
        x_len = -90
        self.wid.wid_chk_loading()
        now_ele_lst = self.trace_get_page_capture_act()
        cnt = 0
        self.wid.scroll_page_act(self.el.trace_sort_per_cap_ele, x=x_len, trace=True)
        while cnt < 12 and len(now_ele_lst) < len(self.trace_get_page_capture_act()):
            # self.wid.scroll_page_act(now_ele_lst[0], x=-18, y=0)
            self.wid.scroll_page_act(self.el.trace_sort_per_cap_ele, x=x_len)
            cnt += 1
        all_cap_ele = self.driver.ele_list(self.el.trace_sort_per_cap_ele)
        all_cap = dict(zip(range(len(all_cap_ele)), (self.driver.ele_get_val(x).split('\n') for x in all_cap_ele)))
        return all_cap

    # 公共 判定，
    def judge_trace_dot_capture_record(self):
        """
        点位详情-抓拍记录
        :return:
        """
        page_cap = self.trace_get_page_capture_act()
        self.driver.ele_click(page_cap[0], load=True)
        trace_page_dot_num = self.trace_dot_camera_act()
        self.wid.wid_chk_loading()
        if not self.driver.ele_exist(self.el.trace_dot_camera_lst):  # 判定当前点位 是否有多个视频源
            dot_cap_num = self.trace_dot_capture_get_total()
        else:
            cap_lst = self.trace_dot_captures_act()
            dot_cap_num = 0
            for cap_ in cap_lst:
                self.trace_dot_capture_act(cap_)
                time.sleep(1)
                dot_cap_num += self.trace_dot_capture_get_total()
                self.back_search_index()
        self.log.warning('轨迹页显示数:{}, 点位总数{}'.format(trace_page_dot_num, dot_cap_num))
        return trace_page_dot_num == dot_cap_num

    def judge_trace_page_ele(self, double_target=False, slt_val=None, search_type='face'):
        page_title = self.driver.ele_get_val(self.el.page_title_ele)
        if double_target and not slt_val:
            slt_val = '目标A+目标B轨迹'
        elif not slt_val:
            slt_val = '比中结果'
        if double_target:
            judge_widget = self.driver.ele_exist(self.el.trace_slt_wid_ele) and \
                           self.driver.ele_exist(self.el.trace_active_wid_ele) and self.driver.ele_exist(
                self.el.trace_dis_ele) and \
                           slt_val in self.driver.ele_get_val(self.el.trace_slt_wid_ele)
        else:
            judge_widget = self.driver.ele_exist(self.el.trace_slt_wid_ele) and \
                           self.driver.ele_exist(self.el.trace_active_wid_ele) \
                           and self.driver.ele_exist(self.el.trace_play_ele) and self.driver.ele_exist(
                self.el.trace_dis_ele) and slt_val in self.driver.ele_get_val(self.el.trace_slt_wid_ele)
            if search_type == 'face':
                judge_widget = judge_widget and self.driver.ele_exist(self.el.trace_companion_ele)
        return judge_widget and '查看轨迹' in page_title

    def judge_trace_sort_cap(self):
        self.trace_sort_act('时间')
        time_all_cap = self.trace_get_all_capture()
        time_all_cap_time = [x[-1] for x in time_all_cap.values()]
        tmp_val_1 = time_all_cap_time
        tmp_val_1.sort()
        tmp_val_1.reverse()
        self.trace_sort_act('视频')
        cam_all_cap = self.trace_get_all_capture()
        cam_all_cap_camera = [x[-2] for x in cam_all_cap.values()]
        tmp_val_2 = cam_all_cap_camera
        tmp_val_2.sort()
        tmp_val_2.reverse()
        return tmp_val_2 == cam_all_cap_camera and tmp_val_1 == time_all_cap_time

    def judge_trace_filter_time_cap(self, double_target=False):
        set_date_lst = self.trace_filter_time(time_=1)
        time.sleep(1)
        dis_date_lst = self.trace_get_date_lst_act(trig_wid='显示', rtn_val=True)
        self.driver.ele_click(self.el.trace_dis_ele)
        if not double_target:
            play_date_lst = self.trace_get_date_lst_act(trig_wid='播放', rtn_val=True)
            return set_date_lst == play_date_lst == dis_date_lst
        else:
            return set_date_lst == dis_date_lst

    def judge_trace_double_target_switch(self):
        trace_type_lst = ['目标A轨迹', '目标B轨迹', '目标A+目标B轨迹']
        for trace_type in trace_type_lst:
            self.wid.wid_drop_down(val=trace_type, trig_wid=self.el.trace_double_modify_btn, exact=True)
            self.wid.wid_chk_loading()
            time.sleep(1)
            judge_val = True
            if '+' in trace_type:
                judge_val = self.driver.ele_exist(self.el.trace_double_judge_card) and self.driver.ele_exist(
                    self.el.trace_double_judge_card_img) and \
                            len(self.driver.ele_list(self.el.trace_double_judge_card_img)) > len(
                    self.driver.ele_list(self.el.trace_double_judge_card))
            if not (self.judge_trace_page_ele(double_target=True, slt_val=trace_type) and judge_val):
                return False
        else:
            return True

    def judge_favourite_search(self):
        if self.chk_favourite_status():
            return False
        else:
            self.slt_cap_act(region=3)
            if not self.chk_favourite_status():
                return False
            self.favourite_search_act()
            return self.get_slt_number()

    @shadow("视频源检索-图片检索")
    def img_search(self, img_path=None, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False,
                   close_int_slt=False, **kwargs):
        """
        图片检索
        :param img_path:    图片
        :param start_time:  检索视频源的开始时间
        :param end_time:    检索视频源的结束时间
        :param camera_lst:  检索视频源列表
        :param need_all:    是否需要加载所有抓拍， 默认False 不加载
        :param slt:         是否手动选中一些抓拍图  默认False, 不比中
        :param close_int_slt:   是否关闭智能比中    默认False, 不关闭智能比中
        :param kwargs:      自定义个性参数，目前 有int_search, 融合检索专用(因为融合检索抓拍图宽270)
        :return:
        """
        img_path = self.df.get_file(img_path or self.df.ImgDef.face2_1)
        self.slt_camera(camera_lst=camera_lst)
        self.slt_date(start_time=start_time, end_time=end_time)
        self.base_search(img_path=img_path, need_all=need_all, slt=slt, threshold=None, txt_=None,
                         close_int_slt=close_int_slt, **kwargs)

    def judge_history(self):
        before_his_lst = self.history_get_all()
        self.back_search_index()
        t_start = time.time()
        self.img_search()
        # 框选比中
        self.back_search_index()
        now_his_lst = self.history_get_all()
        now_new_cap_date = re.findall(r'(\d{4}-\d{2}-\d{2} .+)', now_his_lst[0])[0].strip('\r\n')
        date_delta = self.cf.convert_format_time_to_timestamp(now_new_cap_date) / 1000 - t_start
        self.log.warning('检索后{}, 检索前{}， 时差{}'.format(len(now_his_lst), len(before_his_lst), date_delta))
        if not (len(now_his_lst) == len(before_his_lst) + 1 and 0 < date_delta < 10):
            self.log.error("历史检索数量不符，或者最近一次时间不符")
            return False
        return True

    def judge_favourite_export(self, person_instance, search_type="人脸检索", region_num=3, fav_type=None, search=True,
                               export=True):
        search and self.img_search(close_int_slt=True)
        # 框选比中
        veh_flag = False
        if search_type in ['人脸检索', '融合检索']:
            self.chg_intel_slt(intel_slt=False)  # 取消智能比中
        slt_num = 5
        fav_type = fav_type or search_type
        if '智能检索' in search_type:
            if fav_type == "车辆检索":
                tab_num = 3
                slt_num = 2
            else:
                tab_num = 1
                slt_num = 0
            # self.driver.ele_click(self.driver.ele_list(self.el.result_more)[tab_num], load=True) #mx 2020.8.20 注释掉该步骤
        if search_type == "车辆检索":  # or fav_type == '车辆检索':
            self.slt_cap_act(slt_num=slt_num, veh_flag=True)  # 勾选比中
            veh_flag = True
        else:
            self.slt_cap_act(region=region_num)  # 框选比中
        time.sleep(1)
        # now_slt_num = len(self.get_all_capture(not_load=True, veh_flag=veh_flag))     # tmp csf
        now_slt_num = self.get_slt_number()
        fav_time = time.time()
        if not self.favourite_search_act():
            self.log.error("收藏失败")
            return False
        person_instance.into_menu()
        time.sleep(1)
        person_instance.into_my_collection(collection_type=fav_type)
        self.wid.wid_chk_loading()
        img_lst = self.driver.ele_list(person_instance.el.collection_image_info)
        fav_val = self.driver.ele_get_val(img_lst[0])
        slt_num, slt_date = fav_val.split('\n')
        slt_num_ = self.cf.get_num_from_str(slt_num)
        date_delta = self.cf.convert_format_time_to_timestamp(slt_date.strip('\r\n')) / 1000 - fav_time
        if not (slt_num_ == now_slt_num and 0 < date_delta < 10):
            self.log.error("收藏的 比中图片数量 和时间不符")
            self.log.error("比中数量{}, 收藏中显示数量{}".format(now_slt_num, slt_num))
            return False
        # 导出比中
        if export:
            self.into_menu()
            if not self.export_search_act():
                self.log.error("导出检索时失败")
                return False
        return True


class CameraSearch(CommonSearchModule):

    @shadow("图片检索 B目标")
    def img_search_b(self, img_path=None, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False,
                     **kwargs):
        """
        第二个目标检索
        :param img_path:
        :param start_time:
        :param end_time:
        :param camera_lst:
        :param need_all:
        :param slt:
        :return:
        """
        self.driver.ele_click(self.el.s_new_target_ele)
        self.img_search(img_path=img_path, start_time=start_time, end_time=end_time, camera_lst=camera_lst,
                        need_all=need_all, slt=slt, **kwargs)

    def judge_filter_camera(self, int_search=False, com_search=False):
        fail_flag = False
        time.sleep(3)
        com_search and time.sleep(2)
        # t_start = time.time()
        # while not self.driver.ele_exist(self.el.f_camera_slt_cate_txt) and time.time()-t_start < 5:
        self.driver.ele_click(self.el.flt_camera_trig_el, load=True)
        time.sleep(1)
        tst_cam_lst = self.filter_slt_camera(need_dep=3)
        for camera_ in tst_cam_lst:
            self.driver.ele_click(camera_, load=True)
            now_capture = self.get_all_capture(int_search=int_search)
            left_menu_total = self.cf.get_num_from_str(self.driver.ele_get_val(camera_))
            actual_capture_num = len(now_capture)
            if left_menu_total != actual_capture_num:
                self.log.error("此视频源下抓拍数统计与实际不符")
                self.log.error("左侧显示{}, 实际抓拍图有{}".format(left_menu_total, actual_capture_num))
                fail_flag += 1
                break
        self.driver.ele_click(self.el.flt_camera_close_el, load=True)
        return not fail_flag

    def judge_filter_slt(self, int_search=False):
        fail_flag = False
        self.slt_show_slt_only_act()
        slt_num = self.get_slt_number()
        now_capture = self.get_all_capture(int_search=int_search)
        if slt_num != len(now_capture):
            self.log.warning("比中过滤异常")
            self.log.error("比中的数量为{}, 现在实际显示比中的数量为{}".format(slt_num, len(now_capture)))
            fail_flag += 1
        self.slt_show_slt_only_act(show=False)
        return not fail_flag


class FaceSearchModule(CameraSearch):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.FS

    def judge_face_filter(self, search=True, com_search=False, **kwargs):
        search and self.img_search(slt=True)
        if not self.judge_filter_camera(com_search=com_search):
            return False
        # 比中筛选
        time.sleep(2)
        if not search and self.driver.ele_exist(self.el.intel_slt_btn):
            more_lst = self.driver.ele_list(self.el.result_more)
            # self.driver.ele_click(more_lst[1], load=True) #mx 2020.8.20 注释掉该步骤
            self.chg_intel_slt(intel_slt=False)
            self.slt_cap_act(region=3)
            time.sleep(1)
        self.slt_show_slt_only_act()
        slt_num = self.get_slt_number()
        now_capture = self.get_all_capture(**kwargs)
        if slt_num != len(now_capture):
            self.log.error("比中数统计与实际不符")
            return False
        self.slt_show_slt_only_act(show=False)
        # 人脸属性过滤
        fake_data = {
            "性别": ['男', '女', '不限'],
            "年龄": ['老年人', '成年人', '小孩', '不限'],
            "眼镜": ['无眼镜', '太阳镜', '透明色', '不限'],
            "胡型": ['无胡子', '络腮胡', '不限'],
            "口罩": ['有', '无', '不限'],
            "帽子": ['无帽子', '鸭舌帽', '不限'],
        }
        time.sleep(2)
        loading_ele = 'css=.retrieval-result-row-list:nth-of-type(2) div.rz-loading-mask' if com_search else None
        for k, v in fake_data.items():
            for value in v:
                self.filter_capture_property(face_property={k: value})
                if not self.wid.wid_chk_loading(loading_el=loading_ele):
                    self.log.error("过滤条件后，未有加载")
                    return False
        # 排序
        for sort_ in ["时间", "视频源", "相似度"]:
            self.wid.wid_drop_down(val=sort_, trig_wid=self.el.flt_sort_trig_el)
            if not self.wid.wid_chk_loading(loading_el=loading_ele):
                self.log.error("排序后，未有加载")
                return False
        return True


class PedSearchModule(CameraSearch):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.PS

    def img_search(self, img_path=None, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False,
                   **kwargs):
        img_path = self.df.get_file(img_path or self.df.ImgDef.body_1)
        super().img_search(img_path=img_path, start_time=start_time, end_time=end_time, camera_lst=camera_lst,
                           need_all=need_all, slt=slt)

    def judge_ped_search_filter(self, search=True):
        # 视频源过滤
        search and self.img_search()
        if not self.judge_filter_camera():
            return False
        # # 比中筛选
        # self.slt_show_slt_only_act()
        # slt_num = self.get_slt_number()
        # now_capture = self.get_all_capture()
        # if slt_num != len(now_capture):
        #     self.log.error("比中数统计与实际不符")
        # self.slt_show_slt_only_act(show=False)
        # 人体属性过滤
        # 排序
        for sort_ in ["相似度", "时间", "视频源"]:
            self.wid.wid_drop_down(val=sort_, trig_wid=self.el.flt_sort_trig_el)
            if not self.wid.wid_chk_loading():
                self.log.error("排序后，未有加载")
                return False
        return True


class IntSearchModule(CameraSearch):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.IS

    def img_search(self, img_path=None, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False,
                   **kwargs):
        """
        图片检索
        :param img_path:
        :param start_time:
        :param end_time:
        :param camera_lst:
        :param need_all:
        :param slt:
        :return:
        """
        img_path = self.df.get_file(img_path or self.df.ImgDef.face2_1)
        super().img_search(img_path=img_path,
                           start_time=start_time,
                           end_time=end_time,
                           camera_lst=camera_lst,
                           need_all=need_all,
                           slt=slt,
                           click=True,
                           int_search=True,
                           **kwargs)

    def get_all_capture(self, **kwargs):
        return super().get_all_capture(x=280, page_num=40, **kwargs)

    def judge_int_search_filter(self, search=True, com_search=False):
        search and self.img_search(slt=True)
        # 视频源过滤
        if not self.judge_filter_camera(int_search=True):
            self.log.error("视频源过滤抓拍 异常")
            return False
        # 比中筛选
        self.slt_cap_act(region=3)
        time.sleep(1)
        if not self.judge_filter_slt(int_search=True):
            self.log.error("比中过滤抓拍异常")
            return False
            # 人脸属性过滤
        if not com_search:
            fake_data = {
                "性别": ['男', '女', '不限'],
                "年龄": ['老年人', '成年人', '小孩', '不限'],
                "眼镜": ['无眼镜', '太阳镜', '透明色', '不限'],
                "胡型": ['无胡子', '络腮胡', '不限'],
                "口罩": ['有', '无', '不限'],
                "帽子": ['无帽子', '鸭舌帽', '不限'],
            }
            for k, v in fake_data.items():
                for value in v:
                    self.filter_capture_property(face_property={k: value})
                    chk_res = self.wid.wid_chk_loading()
                    if not chk_res:
                        self.log.error("过滤条件后，未有加载")
                        return False
            # 优先排序
            priority_lst = ['人脸', '人体']
            for priority_ in priority_lst:
                self.wid.wid_drop_down(priority_, self.el.filter_priority_ele)
                if not self.wid.wid_chk_loading():
                    self.log.error("排序后，未有加载")
                    return False
        # 排序
        for sort_ in ["相似度", "时间", "视频源"]:
            self.wid.wid_drop_down(val=sort_, trig_wid=self.el.flt_sort_trig_el)
            if not self.wid.wid_chk_loading():
                self.log.error("排序后，未有加载")
                return False
        return True


class VehSearchModule(CameraSearch):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.VS

    def img_search(self, img_path=None, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False,
                   **kwargs):
        img_path = self.df.get_file(img_path or self.df.ImgDef.car_12)
        super().img_search(img_path=img_path,
                           start_time=start_time,
                           end_time=end_time,
                           camera_lst=camera_lst,
                           need_all=need_all,
                           slt=slt,
                           **kwargs)

    def txt_search(self, plate_no=None, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False):
        self.slt_camera(camera_lst=camera_lst)
        self.slt_date(start_time=start_time, end_time=end_time)
        self.base_search(txt_=plate_no, need_all=need_all, slt=slt)

    def judge_veh_search_filter(self, search=True):
        search and self.img_search()
        # 视频源过滤
        # if not self.judge_filter_camera():
        #     return False
        # 比中筛选
        tst_slt_num = 2
        self.slt_cap_act(slt_num=tst_slt_num, veh_flag=True)
        self.slt_show_slt_only_act()
        slt_num = self.get_slt_number()
        now_capture = self.get_all_capture(veh_flag=True)
        if slt_num != len(now_capture):
            self.log.error("比中数统计与实际不符")
            return False
        self.slt_show_slt_only_act(show=False)
        # 车辆属性过滤
        fake_data = {
            # "性别": ['男', '女', '不限'],
            # "年龄": ['老年人', '成年人', '小孩', '不限'],
            # "眼镜": ['无眼镜', '太阳镜', '透明色', '不限'],
            # "胡型": ['无胡子', '络腮胡', '不限'],
            # "口罩": ['有', '无', '不限'],
            # "帽子": ['无帽子', '鸭舌帽', '不限'],
        }
        for k, v in fake_data.items():
            for value in v:
                self.filter_capture_property(face_property={k: value})
                if not self.wid.wid_chk_loading():
                    self.log.error("过滤条件后，未有加载")
                    return False
        return True


class LibSearchModule(CommonSearchModule):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.LS

    def slt_lib(self, lib_type='布控'):
        self.wid.wid_drop_down(val=lib_type, trig_wid=self.el.slt_lib_trig)

    @shadow("身份检索-图片检索")
    def img_search(self, img_path=None, lib_type='布控库', need_all=False, slt=False, threshold=None):
        img_path = self.df.get_file(img_path or self.df.ImgDef.face2_1)
        self.slt_lib(lib_type=lib_type)
        self.base_search(img_path=img_path, need_all=need_all, slt=slt, threshold=threshold)

    def txt_search(self, txt_=None, lib_type='布控库', need_all=False, slt=False):
        self.slt_lib(lib_type=lib_type)
        self.base_search(txt_=txt_, need_all=need_all, slt=slt)

    def filter_lib_tag(self, el):
        self.driver.ele_click(self.el.lib_tag_ele)
        # self.driver.ele_click(self.el.lib_tag_reset_btn)
        now_slt_status = self.driver.ele_get_val(self.el.lib_tag_slt_all, 'aria-checked')
        if now_slt_status and 'true' in now_slt_status:
            self.driver.ele_click(self.el.lib_tag_slt_all)
        if now_slt_status and 'mix' in now_slt_status:
            self.driver.ele_click(self.el.lib_tag_slt_all)
            self.driver.ele_click(self.el.lib_tag_slt_all)
        self.driver.ele_click(el)
        tag_lib_name = self.driver.ele_get_val(el)
        self.driver.ele_click(self.el.lib_tag_confirm_btn)
        load_rtn = self.wid.wid_chk_loading()
        if not load_rtn:
            return False
        return tag_lib_name

    def filter_lib_property(self, lib_property):
        self.driver.ele_click(self.el.lib_property_ele)
        for k, v in lib_property.items():
            if '性别' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_sex_input)
            if '年龄' in k:
                self.wid.wid_drop_down(v, trig_wid=self.el.flt_age_input)
            if '户籍' in k:
                self.driver.ele_input(self.el.lib_property_hometown_ele, v)
            if '备注' in k:
                self.driver.ele_input(self.el.lib_property_ps_ele, v)
        self.driver.ele_click(self.el.flt_confirm_btn)

    def judge_lib_filter(self, search=True):
        search and self.img_search()
        self.driver.ele_click(self.el.lib_tag_ele)
        time.sleep(1)
        tag_lst = self.driver.ele_list(self.el.lib_tag_lst)
        self.driver.ele_click(self.el.lib_tag_ele)
        for tag_ in tag_lst:
            now_tag_name = self.filter_lib_tag(tag_)
            if not now_tag_name:
                self.log.error("点击标签后 加载失败")
                return False
            # now_cap_all = self.get_all_capture_lib(img_mix=True)
            # now_cap_tag_lst = [x[-1] for x in now_cap_all.values()]
            # for per_ in now_cap_tag_lst:
            #     if isinstance(per_, str) and per_ != now_tag_name or isinstance(per_, list) and now_tag_name not in per_:
            #         return False
        # 身份属性 过滤
        fake_data = {
            "性别": ['男', '女', '不限'],
            "年龄": ['老年', '中年', '青年', '儿童', '不限'],
        }
        for k, v in fake_data.items():
            for value in v:
                self.filter_lib_property(lib_property={k: value})
                if not self.wid.wid_chk_loading():
                    self.log.error("过滤条件后，未有加载")
                    return False
        return True


class TimeSearchModule(CommonSearchModule):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.TS

    def search(self, start_time=None, end_time=None, camera_lst=None, need_all=False, slt=False):
        self.slt_camera(camera_lst=camera_lst)
        self.slt_date(start_time=start_time, end_time=end_time)
        self.base_search(need_all=need_all, slt=slt)

    def search_switch(self, tab_name='人脸'):
        tab_lst = self.driver.ele_list(self.el.search_tab_lst_ele)
        now_tab_el = [x for x in tab_lst if 'active' in self.driver.ele_get_val(x, 'class')][0]
        now_tab = self.driver.ele_get_val(now_tab_el).strip(' ')
        if now_tab != tab_name:
            need_tab_el = [x for x in tab_lst if tab_name == self.driver.ele_get_val(x)][0]
            self.driver.ele_click(need_tab_el)
            self.wid.wid_chk_loading()
            return 'active' in self.driver.ele_get_val(need_tab_el, 'class')
        return True


class OfflineSearchModule(CommonSearchModule):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.OS


class ComSearchModule(FaceSearchModule, LibSearchModule, VehSearchModule, IntSearchModule):
    def __init__(self, web_driver, **kwargs):
        super().__init__(web_driver, **kwargs)
        self.el = SearchPageEle.CS

    def img_search(self, img_path=None, start_time=None, end_time=None, camera_lst=None, **kwargs):
        """
        图片检索
        :param img_path:
        :param start_time:
        :param end_time:
        :param camera_lst:
        :return:
        """
        img_path = self.df.get_file(img_path or self.df.ImgDef.mix_img)
        FaceSearchModule.img_search(self, img_path=img_path,
                                    start_time=start_time,
                                    end_time=end_time,
                                    camera_lst=camera_lst,
                                    click=True, **kwargs)

    def txt_search(self, txt_=None, txt_type="全部", slt=False, **kwargs):
        LibSearchModule.base_search(self, txt_=txt_, slt=slt, txt_type=txt_type, **kwargs)
        time.sleep(3)

    def get_all_capture(self, **kwargs):
        return FaceSearchModule.get_all_capture(self, **kwargs)


if __name__ == "__main__":
    from common.w_driver import WDriver

    driver = WDriver()
    driver.open_url("http://10.111.32.91:10219/#/users")
    #
    MainPage.login_in(driver, 'chi', 'admin1234')
    menu_list = [
        # "数据汇智",
        # "操作导航",
        # "人脸检索",
        # "融合检索",
        # "行人检索",
        # "车辆检索",
        # "智能检索",
        # "时空过滤",
        # "身份检索",
        # "离线检索",
        # "布控",
        # "人群分析",
        # "卡口",
        # "视图工具",
        "解析管理",
        "告警中心",
        "任务中心",
        "视图源管理",
        "人像库管理",
        "角色管理",
        "系统设置",
        "用户管理",
        "操作日志",
        "个人中心",
        "消息提醒",
        "地图中心",
        "退出地图中心",
        "退出",
    ]
    for menu_ in menu_list:
        print("模块：{}，现在时间{}".format(menu_, time.time()), end='')
        MainPage.into_menu(driver, menu_)
    time.sleep(2)

    # MainPage.into_menu(driver, "人脸检索")
    # img_path = r"D:\GIT_\sf_scripts\material\SenseFace\API\v40\31.jpg"
    # driver.ele_input(SearchPageEle.FS.img_ele, r"D:\GIT_\sf_scripts\material\SenseFace\API\v40\31.jpg")
    # MainPage.into_menu(driver, "用户管理")
    # user_name = 'hyc123'

    # driver.ele_click("css=.filter-wrap>button")
    # driver.ele_input("css=input[placeholder=请输入账号]", user_name)
    # driver.ele_input("css=input[placeholder=请输入姓名]", user_name)
    # driver.ele_click("css=input[placeholder=请选择所属部门]")

    # driver.ele_click("css=body>div:last-child span[title='一级部门（可修改名称）']")
    # driver.ele_click("css=input[placeholder=请选择角色]")
    # driver.ele_click("css=body>div:last-child>div>div>label:last-of-type")
    # driver.ele_click("css=body>div:last-child>div:last-child button:last-child")
    # driver.ele_click("css=.rz-dialog__wrapper+.user-details .dialog-footer button:last-child")

    # print(driver.ele_get_val("css=.rz-message__content"))

    # dep_group_root_tree = "css=.grain"
    # sin_ele = "css=.rz-tree-node__expand-icon.rz-icon-caret-right"
    # abc = driver.ele_list(sin_ele)
    # for per_ in abc:
    #     if 'expander' not in per_.get_attribute('class') and 'leaf' not in per_.get_attribute('class'):
    #         per_.click()
    # need_dep = "34254"
    # need_dep = "二sddsd级"
    # need_dep = "傻大个问他rete"
    # tree_ele = "css=.rz-tree"
    #

    # # a = sub_func2("css=body>div:last-child>div:last-child")
    # driver.ele_click(a)
    # more_ele = a+"+div+div>span"
    # print(more_ele)
    # print(driver.ele_get_val(more_ele))
    # driver.ele_click(more_ele)
    # mark_ele = "css=.leaves>.book-mark .mark-li"
    # lst = driver.ele_list(mark_ele)
    # print(len(lst))
    # for j in lst:
    #     print(j.text)
    # lst[3].click()
    # time.sleep(10)
    # wid = WidPub(driver)
    # # MainPage.into_menu(driver, "用户管理")
    # MainPage.into_menu(driver, "角色管理")
    # driver.ele_click('css=.roles-module-top .rz-button--primary')
    # time.sleep(1)
    # # wid.wid_role_power_tree()
    #
    # wid.wid_role_power_tree(chg_dict={"卡口": {"使用": True},
    #                                 "1:1验证":  {"使用": True},
    #                                   })

    time.sleep(5)
    driver.quit()