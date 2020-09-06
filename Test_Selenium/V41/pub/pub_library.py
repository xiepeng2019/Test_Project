#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import inspect
import time
from functools import wraps
from v43.ele_set.page_library import LibraryPageEle
from v43.pub.pub_base import PublicClass
from v43.pub.pub_widget import WidPub
from sc_common.sc_define import ResDefine
from common.common_func import id_generator, get_random_name, convert_to_array


class CreateLibrary(PublicClass):
    def __init__(self, instance_obj, **kwargs):
        super().__init__(driver=instance_obj, **kwargs)
        self.instance_obj = instance_obj
        self.log = kwargs.get("log")
        self.lib_por = LibraryPageEle()
        self.text_dict = self.lib_por.text_dict
        self.pub_obj = WidPub(driver=instance_obj, log=instance_obj.log)

    def library_name_search(tag=False, inexistence=False, exist_type=None):
        def library_select(func):
            @wraps(func)
            def library_search(*args, **kwargs):
                self = args[0]
                library_name = kwargs.get("library_name")
                sense_type = kwargs.get("sense_type")
                if sense_type == 1:
                    library_type = self.text_dict.get("alert_button")
                else:
                    library_type = self.text_dict.get("static_button")
                if exist_type == "library_del":
                    self.instance_obj.refresh_driver()
                    self.into_menu()
                self.wid.wid_chk_loading()
                # time.sleep(4)
                lib_type_ele = self.lib_por.library_type_button.format(library_type)
                if 'active' not in self.instance_obj.ele_get_val(lib_type_ele, 'class'):
                    self.instance_obj.ele_click(lib_type_ele, load=True, wait_time=4)
                # self.instance_obj.ele_click(self.lib_por.library_type_button.format(library_type))
                # self.wid.wid_chk_loading()
                self.instance_obj.ele_input(
                    self.lib_por.library_portrait_name.format(self.text_dict.get("library_search")), library_name, enter=True, load=True)
                result = self.library_count_query(library_name=library_name, exist_type=exist_type)
                if result is 1:
                    if tag: return True
                else:
                    self.log.info("页面没有库名称: %s的库,成功" % library_name) if inexistence or tag else self.log.error(
                        "页面没有库名称: %s的库,失败" % library_name)
                    if tag:
                        pass
                    else:
                        return True if inexistence else False
                new_kwargs = dict()
                for key in inspect.getfullargspec(func).args:
                    if key in kwargs:
                        new_kwargs[key] = kwargs[key]
                if func.__name__ == "add_portrait":
                    new_kwargs = kwargs
                result = func(*args, **new_kwargs)
                if not result:
                    return False
                return result

            return library_search

        return library_select

    def library_count_query(self, library_name, exist_type):
        """
        查询页面是否有相同名称库
        :param library_name: 库名称
        :param exist_type: 库管理按钮: 人像管理、查看、编辑、删除
        :return:
        """
        # count_result = self.instance_obj.ele_click(self.lib_por.library_count_button, wait_time=3).text
        count_result = self.instance_obj.ele_get_val(self.lib_por.library_count_button, timeout=3)
        result = int(count_result.split(":")[1].strip())
        if result:
            lib_name_list = self.instance_obj.ele_list(self.lib_por.library_list_button)
            lib_manage_list = self.instance_obj.ele_list(
                self.lib_por.library_manage.format(self.text_dict.get(exist_type))) \
                if exist_type else ["1"] * len(lib_name_list)
            for i, k in zip(lib_name_list, lib_manage_list):
                if i.text == library_name:
                    self.log.info("页面有库名称: %s的库，成功" % library_name)
                    if exist_type == "library_del" and "UI_pre_" in library_name:
                        self.log.info("预置库不删")
                        return True
                    if exist_type: self.instance_obj.ele_click(k, wait_time=2)
                    return 1
        return True

    @library_name_search(tag=True, exist_type=None)
    def create_library(self, library_name=None, sense_type=1, attribute_info=None, del_attribute=False):
        """
        创建库
        :param library_name: 库名称
        :param sense_type: 库类型
        :param attribute_info: 库设置,type:dict , keys: lib_attribute, attribute_values
        :param del_attribute: True:删除属性
        :return:
        """
        if sense_type == 1:
            button_text = self.text_dict.get("library_alert")
            button_library_name = self.text_dict.get("library_alert_name")
            resource_type = ResDefine.key_lib
            mas = "布控库"
        elif sense_type == 2:
            button_text = self.text_dict.get("library_static")
            button_library_name = self.text_dict.get("library_static_name")
            resource_type = ResDefine.key_static_lib
            mas = "静态库"
        else:
            raise Exception("传入sense_type值不对")
        self.instance_obj.ele_click(self.lib_por.create_library_button.format(button_text))
        self.instance_obj.ele_input(self.lib_por.library_portrait_name.format(button_library_name), library_name)
        self.instance_obj.ele_click(self.lib_por.library_assist_button.format(self.text_dict.get("library_next_step")))
        self.instance_obj.ele_click(self.lib_por.library_assist_button.format(self.text_dict.get("library_next_step")))
        if attribute_info:
            self.create_attribute(attribute_info=attribute_info, del_attribute=del_attribute)
            time.sleep(1)
        self.instance_obj.ele_click(self.lib_por.library_assist_button.format(self.text_dict.get("library_confirm")))
        super().collect_resource(resource_type=resource_type, resource_value=library_name)
        time.sleep(1)
        wid_result = self.pub_obj.wid_get_alert_label()
        if "成功" in wid_result:
            self.log.info("新建%s,成功" % mas)
            return {"library_name": library_name}
        self.log.error("新建%s, 失败" % mas)
        return False

    def create_attribute(self, attribute_info=None, del_attribute=False):
        """
        创建自定义属性
        :param attribute_info: 库设置,type:dict , keys: lib_attribute, attribute_values
        :param del_attribute: True:删除属性
        :return:
        """
        attribute_info = convert_to_array(attribute_info)
        self.instance_obj.ele_click(self.lib_por.library_attribute, wait_time=1.5)
        for i, k in enumerate(attribute_info):
            if i >= 1:
                self.instance_obj.ele_click(self.lib_por.library_create_attribute, wait_time=1.5)
            self.instance_obj.ele_input(self.lib_por.library_portrait_name.format(self.text_dict.get("attribute_name")),
                                        k.get("lib_attribute"))
            self.instance_obj.ele_input(self.lib_por.library_portrait_name.format(self.text_dict.get("attribute_info")),
                                        k.get("attribute_values"))
        if len(attribute_info) > 1 and del_attribute:
            attribute_del_list = self.instance_obj.ele_list(self.lib_por.library_attribute_del)
            self.instance_obj.ele_click(attribute_del_list[-1], wait_time=1.5)
            self.instance_obj.ele_click(self.lib_por.library_del_confirm, wait_time=1.5)
        return True

    @library_name_search(exist_type="library_update")
    def update_library(self, sense_type=1, update_name=None, remark=None):
        """
        编辑库
        :param sense_type: 库类型
        :param update_name: 库名称
        :param remark: 备注
        :return:
        """
        if sense_type == 1:
            button_library_name = self.text_dict.get("library_alert_name")
        elif sense_type == 2:
            button_library_name = self.text_dict.get("library_static_name")
        else:
            raise Exception("传入sense_type值不对")
        if update_name:
            self.instance_obj.ele_input(self.lib_por.library_portrait_name.format(button_library_name), update_name)
            self.log.info("将库名称编辑为:%s" % update_name)
        if remark:
            self.instance_obj.ele_input(self.lib_por.library_remark, remark)
            self.log.info("备注为:%s" % update_name)
        self.instance_obj.ele_click(self.lib_por.library_assist_button.format(self.text_dict.get("save")),
                                    wait_time=1.5)
        wid_result = self.pub_obj.wid_get_alert_label()
        if "成功" in wid_result:
            return {"update_name": update_name, "remark": remark}
        self.log.error("库编辑失败")
        return False

    @library_name_search(inexistence=True, exist_type="library_del")
    def delete_library(self):
        """
        删除库
        :return:
        """
        self.instance_obj.ele_click(self.lib_por.library_assist_button.format(self.text_dict.get("library_del")))
        # time.sleep(1.5)
        wid_result = self.pub_obj.wid_get_alert_label(wait_miss=True)
        if "成功" in wid_result:
            return True
        self.log.error("库删除失败")
        return False

    @library_name_search(exist_type="library_manage")
    def add_portrait(self, portrait_name=None, image_=None, sense_type=1, identity=None, pre_por=False, back=False,
                     **kwargs):
        """
        添加人像
        :param portrait_name: 人像名称
        :param image_: 人像名称
        :param sense_type: 库类型
        :param identity: 身份证
        :param pre_por: 预置用
        :param back: True: 返回页面
        :param kwargs: por_remark: 备注， por_gender:性别， por_address:地址， por_area: 区域
        :return:
        """
        if pre_por:
            por_sum = self.portrait_sum
            if por_sum: return True
        image_ = image_ or ResDefine.ImgDef.face2_1
        self.instance_obj.ele_click(self.lib_por.portrait_add_button, wait_time=1.5)
        self.instance_obj.ele_input(self.lib_por.library_portrait_name.format(self.text_dict.get("portrait_name")),
                                    portrait_name)
        image_path = ResDefine.get_file(image_)
        self.pub_obj.wid_upload(img_path=image_path)
        if sense_type == 2:
            identity = identity or id_generator()
        info_result = self.portrait_info(identity=identity, **kwargs)
        if not info_result:
            return False
        self.instance_obj.ele_click(self.lib_por.library_assist_button.format(self.text_dict.get("library_confirm")),
                                    wait_time=3)
        self.wid.wid_chk_loading()
        if back:
            self.instance_obj.ele_click(self.lib_por.portrait_back_button, wait_time=2)
        self.log.info("人像添加，成功")
        return {"portrait_name": portrait_name, "identity": identity}

    @library_name_search(exist_type="library_manage")
    def import_portrait(self, import_name=None, pre_por=False, result_verify=False, sum=65):
        """
        人像导入
        :param import_name: 导入名称
        :param pre_por: 预置库
        :param result_verify: 校验图片数量
        :return:
        """
        if pre_por:
            por_sum = self.portrait_sum
            if por_sum >= sum:
                self.log.info("人像数量是%s张，成功" % por_sum)
                return True
            else:
                if result_verify:
                    self.log.error("人像数量是%s张，失败" % por_sum)
                    return False
        import_name = import_name or ResDefine.ImgDef.Lz_65_zip
        self.instance_obj.ele_click(self.lib_por.portrait_import_button, wait_time=1.5)
        import_path = ResDefine.get_file(import_name)
        self.pub_obj.wid_upload(img_path=import_path)
        for i in range(5):
            por_sum = self.portrait_sum
            if por_sum >= sum:
                break
            time.sleep(2)
        else:
            self.log.error("人像导入，失败")
            return False
        return True

    def portrait_name_query(self, portrait_name=None, sense_type=1, result=True):
        """
        判断人像是否存在
        :param portrait_name: 人像名称
        :param result: True:一定有结果
        :param sense_type: 库类型
        :return:
        """
        if sense_type == 1:
            count_result = self.instance_obj.ele_click(self.lib_por.portrait_count_button).text
        elif sense_type == 2:
            count_result = self.instance_obj.ele_click(self.lib_por.portrait_static_count).text
        else:
            return False
        por_sum = int(count_result.split("到")[1].split("个")[0].strip())
        if por_sum:
            portrait_list = self.instance_obj.ele_list(self.lib_por.portrait_list_button)
            for i in portrait_list:
                if i.text == portrait_name:
                    self.log.info("页面有人像名称:%s的人像，成功" % portrait_name)
                    self.instance_obj.ele_click(i, wait_time=1.5)
                    return True
        self.log.error("页面没有人像名称:%s的人像，失败" % portrait_name) if result else \
            self.log.info("页面没有人像名称:%s的人像，成功" % portrait_name)
        return False if result else 1

    @property
    def portrait_sum(self):
        """
        查询人像总数
        :return:
        """
        count_result = self.instance_obj.ele_click(self.lib_por.portrait_sum_button, wait_time=1.5, load=True).text
        por_sum = int(count_result)
        self.log.info("页面有人像，成功") if por_sum else self.log.info("页面没有人像，需要上传，成功")
        return por_sum

    def portrait_search(self, portrait_name=None, identity=None, por_remark=None, sense_type=1, result=True, tag=False):
        """
        通过人像名称或者备注或者id、搜索人像
        :param portrait_name: 人像名称
        :param identity: 身份证号
        :param por_remark: 备注
        :param sense_type: 库类型
        :param result: True:一定有结果
        :param tag: True: 备注搜索
        :return:
        # """
        time.sleep(4)
        self.instance_obj.ele_click(self.lib_por.portrait_id_down, wait_time=1)
        time.sleep(2)
        if por_remark and tag:
            self.instance_obj.ele_click(self.lib_por.portrait_id_remark.format(self.text_dict.get("remark")),
                                        wait_time=1.5)
            self.instance_obj.ele_input(
                self.lib_por.library_portrait_name.format(self.text_dict.get("input_remark")), por_remark)
            mes = "备注"
        elif identity:
            self.instance_obj.ele_click(self.lib_por.portrait_id_remark.format(self.text_dict.get("identity")),
                                        wait_time=1.5)
            self.instance_obj.ele_input(
                self.lib_por.library_portrait_name.format(self.text_dict.get("portrait_search")), identity)
            mes = "身份证号"
        elif portrait_name:
            self.instance_obj.ele_click(self.lib_por.portrait_id_remark.format(self.text_dict.get("identity")),
                                        wait_time=1.5)
            self.instance_obj.ele_input(
                self.lib_por.library_portrait_name.format(self.text_dict.get("portrait_search")), portrait_name)
            mes = "人像名称"
        else:
            return False
        self.instance_obj.ele_click(self.lib_por.library_search_button, wait_time=1.5)
        time.sleep(3)
        search_result = self.portrait_name_query(portrait_name, sense_type=sense_type, result=result)
        if not search_result:
            self.log.error("选择%s过滤，人像不符或者没有人像，失败" % mes)
            return False
        return True if result else search_result

    def portrait_info(self, identity=None, por_input=True, **kwargs):
        """
        填写人像信息
        :param identity: 身份证
        :param kwargs: por_remark: 备注， por_gender:性别， por_address:地址， por_area: 区域
        :param por_input: True:输入信息
        :return:
        """
        por_remark = kwargs.get("por_remark")
        por_gender = kwargs.get("por_gender")
        por_address = kwargs.get("por_address")
        por_area = kwargs.get("por_area")
        por_name = kwargs.get("por_name")
        if por_name:
            self.instance_obj.ele_input(self.lib_por.library_portrait_name.format(self.text_dict.get("portrait_name")),
                                        por_name)
        if identity:
            self.instance_obj.ele_input(
                self.lib_por.library_portrait_name.format(self.text_dict.get("portrait_identity_id")),
                identity)
        if por_remark:
            self.instance_obj.ele_input(
                self.lib_por.library_portrait_name.format(self.text_dict.get("por_remark")), por_remark)
        if identity: return True
        if por_gender:
            if por_input:
                self.instance_obj.ele_click(
                    self.lib_por.library_portrait_name.format(self.text_dict.get("portrait_gender")))
            time.sleep(2)
            gender_list = self.instance_obj.ele_list(self.lib_por.portrait_gender)
            for i in gender_list:
                if i.text == por_gender:
                    self.log.info("人像选择性别:%s，成功" % por_gender)
                    self.instance_obj.ele_click(i, wait_time=1.5)
                    break
            else:
                self.log.error("列表中没有性别:%s，失败" % por_gender)
                return False
        if por_address and por_area:
            if por_input:
                self.instance_obj.ele_click(self.lib_por.portrait_census)
            time.sleep(2)
            address_list = self.instance_obj.ele_list(self.lib_por.portrait_address)
            for i in address_list:
                if i.text == por_address:
                    self.log.info("人像选择地址:%s，成功" % por_address)
                    self.instance_obj.ele_click(i, wait_time=1.5)
                    break
            else:
                self.log.error("列表中没有地址:%s，失败" % por_address)
                return False
            time.sleep(2)
            area_list = self.instance_obj.ele_list(self.lib_por.portrait_area)
            for i in area_list:
                if i.text == por_area:
                    self.log.info("人像选择区域:%s，成功" % por_area)
                    self.instance_obj.ele_click(i, wait_time=1.5)
                    break
            else:
                self.log.error("列表中没有区域:%s，失败" % por_area)
                return False
        return True

    def update_portrait(self, portrait_name=None, identity=None, por_remark=None, update_id=None, tag=False,
                        sense_type=1,
                        **update_kwargs):
        """
        编辑人像信息
        :param portrait_name:  人像名称
        :param identity:  身份证
        :param por_remark:  备注
        :param update_id:  新身份证id
        :param sense_type:  库类型
        :param update_kwargs:  update_remark: 备注， update_gender:性别， update_address:地址， update_area: 区域, por_name: 人像名称
        :param tag: True: 备注搜索
        :return:
        """
        new_kwargs = dict()
        new_kwargs.update(
            {"por_remark": update_kwargs.get("update_remark"), "por_gender": update_kwargs.get("update_gender"),
             "por_address": update_kwargs.get("update_address"), "por_area": update_kwargs.get("update_area"),
             "por_name": update_kwargs.get("update_name")})
        search_result = self.portrait_search(portrait_name=portrait_name, identity=identity, por_remark=por_remark,
                                             tag=tag,
                                             sense_type=sense_type)
        if not search_result:
            return False
        self.instance_obj.ele_click(self.lib_por.portrait_update_button, wait_time=1.5)
        update_result = self.portrait_info(identity=update_id, **new_kwargs)
        if not update_result:
            return False
        self.instance_obj.ele_click(self.lib_por.library_assist_button.format(self.text_dict.get("library_confirm")),
                                    wait_time=1.5)
        self.instance_obj.ele_click(self.lib_por.portrait_x_button, wait_time=1.5)
        return True

    def delete_portrait(self, portrait_name=None, identity=None, por_remark=None, sense_type=1):
        """
        删除人像
        :param portrait_name: 人像名称
        :param identity: 身份证
        :param por_remark: 备注
        :param sense_type: 库类型
        :return:
        """
        search_result = self.portrait_search(portrait_name=portrait_name, identity=identity, por_remark=por_remark,
                                             sense_type=sense_type, result=False, tag=True)
        if not search_result:
            return False
        if search_result is 1:
            return True
        self.instance_obj.ele_click(self.lib_por.portrait_del_button, wait_time=1.5)
        self.instance_obj.ele_click(self.lib_por.portrait_confirm_del, wait_time=1.5)
        self.log.info("人像删除，成功")
        return True

    def portrait_select(self, gender=None, age=None, por_address=None, por_area=None):
        """
        人像性别、年龄、户籍筛查
        :param gender: 性别
        :param age: 年龄
        :param por_address: 地址
        :param por_area: 区域
        :return:
        """
        self.instance_obj.refresh_driver()
        mes = ""
        if gender:
            mes = "性别"
            gender_type = self.text_dict.get("por_gender")
            self.instance_obj.ele_click(self.lib_por.portrait_select_button.format(gender_type), wait_time=1)
            select_result = self.portrait_info(por_gender=gender, por_input=False)
            if not select_result:
                return False
        if age:
            mes = mes + "年龄"
            age_type = self.text_dict.get("por_age")
            self.instance_obj.ele_click(self.lib_por.portrait_select_button.format(age_type), wait_time=1)
        if por_address and por_area:
            mes = mes + "户籍"
            self.instance_obj.ele_click(self.lib_por.portrait_census_select, wait_time=1)
            select_result = self.portrait_info(por_address=por_address, por_area=por_area, por_input=False)
            if not select_result:
                return False

        self.instance_obj.ele_click(self.lib_por.portrait_select_confirm)
        por_sum = self.portrait_sum
        if por_sum:
            portrait_list = self.instance_obj.ele_list(self.lib_por.portrait_list_button)
            for i in portrait_list:
                self.instance_obj.ele_click(i, wait_time=1.5)
                if gender:
                    click_value = self.instance_obj.ele_click(self.lib_por.portrait_select_verify.format(gender_type),
                                                              wait_time=1).text
                    if click_value != gender:
                        self.log.error("性别过滤出来值与实际不符，失败")
                        return False
                if por_address and por_area:
                    census_type = self.text_dict.get("por_census")
                    click_value = self.instance_obj.ele_click(self.lib_por.portrait_select_verify.format(census_type),
                                                              wait_time=1).text
                    if click_value != "{0}/{1}".format(por_address, por_area):
                        self.log.error("性别过滤出来值与实际不符，失败")
                        return False
            self.log.info("选择%s过滤有结果，校验成功" % mes)
            return True
        else:
            self.log.error("选择%s过滤没有结果，失败" % mes)
            return False

    def sort_result(self, sort_obj=2, sense_type=1):
        """
        排序
        :param sort_obj: 2:人像数， 3:创建时间, 4:更新时间
        :param sense_type: 1:布控库， 2:静态库
        :return:
        """
        if sense_type == 1:
            library_type = self.text_dict.get("alert_button")
        else:
            library_type = self.text_dict.get("static_button")
        self.instance_obj.ele_click(self.lib_por.library_type_button.format(library_type), wait_time=3)
        time.sleep(4)
        if sort_obj == 2:
            sort_type = self.text_dict.get("por_sort")
            mes = "人像数"
        elif sort_obj == 4:
            sort_type = self.text_dict.get("create_time_sort")
            mes = "创建时间"
        elif sort_obj == 6:
            sort_type = self.text_dict.get("update_time_sort")
            mes = "更新时间"
        else:
            return False
        self.instance_obj.ele_click(self.lib_por.library_sort_button.format(sort_type), wait_time=1.5)
        time.sleep(1.5)
        result_list = self.instance_obj.ele_list(self.lib_por.library_sort.format(sort_obj))
        if sort_obj == 2:
            result = [int(i.text) for i in result_list]
            sort_result = sorted(result, reverse=True)
        else:
            result = [int(time.mktime(time.strptime(i.text, "%Y-%m-%d %H:%M:%S"))) for i in result_list]
            sort_result = sorted(result, reverse=True)
        if result != sort_result:
            self.log.error("列表中%s没有倒序，失败" % mes)
            return False
        return True

    def page_back(self):
        self.wid.back_module_index()
        # self.instance_obj.ele_click(self.lib_por.portrait_back_button, wait_time=1.5)


class CreateLibPor(CreateLibrary):
    def __init__(self, instance_obj, **kwargs):
        super().__init__(instance_obj=instance_obj, **kwargs)

    def create_lib_add_por(self, library_name=None, portrait_name=None, sense_type=1, image_=None, import_name=None,
                           identity=None, back=False, upload_=True, import_=False, attribute_info=None,
                           del_attribute=False, **kwargs):
        """
        创建库已经上传人像
        :param library_name: 库名
        :param portrait_name: 人像名称
        :param sense_type: 类型，1:布控库，2：静态库
        :param image_: 图片名称
        :param import_name: 导入名称
        :param identity: 身份证号
        :param upload_: 上传
        :param import_: 导入
        :param attribute_info: 库设置,type:dict , keys: lib_attribute, attribute_values
        :param del_attribute: True:删除属性
        :param kwargs: por_remark: 备注， por_gender:性别， por_address:地址， por_area: 区域
        :param back:
        :return:
        """
        portrait_result = None
        library_name = library_name or get_random_name(name_prefix=ResDefine.name_prefix)
        portrait_name = portrait_name or get_random_name(name_prefix="por_")
        library_result = super().create_library(library_name=library_name, sense_type=sense_type,
                                                attribute_info=attribute_info, del_attribute=del_attribute)
        if not library_result or not isinstance(library_result, dict):
            return False
        if upload_:
            portrait_result = super().add_portrait(library_name=library_name, sense_type=sense_type,
                                                   portrait_name=portrait_name, image_=image_, identity=identity,
                                                   **kwargs)
        if upload_ and import_ and sense_type == 1:
            self.instance_obj.ele_click(self.lib_por.portrait_back_button, wait_time=1.5)
        if import_ and sense_type == 1:
            portrait_result = self.import_portrait(library_name=library_name, sense_type=sense_type,
                                                   import_name=import_name)
        self.wid.wid_chk_loading()
        if not portrait_result:
            return False
        if back:
            self.page_back()
        if upload_:
            library_result.update(portrait_result)
        return library_result

    def pre_lib_por(self, sense_type=1, number=1):
        """
        预置库和人像
        :param sense_type: 类型，1:布控库，2：静态库
        :param number: 人像数量，1:一张人像，65: 65张人像
        :return:
        """
        upload_ = import_ = portrait_result = portrait_name = None
        if number == 1:
            library_name = self.df.pre_lib_alert_1 if sense_type == 1 else self.df.pre_lib_static_1
            portrait_name = "one_por"
            upload_ = True
        elif sense_type == 1 and number == 65:
            library_name = self.df.pre_lib_alert_65
            import_ = True
        else:
            return False
        library_result = super().create_library(library_name=library_name, sense_type=sense_type)
        if not library_result:
            return False
        if upload_:
            portrait_result = super().add_portrait(library_name=library_name, sense_type=sense_type,
                                                   portrait_name=portrait_name, pre_por=True)
        if import_:
            #
            # lib_type_ele = self.lib_por.library_type_button.format("alert_button" if sense_type == 1 else 'static_button')
            # if 'active' not in self.instance_obj.ele_get_val(lib_type_ele, 'class'):
            #     self.instance_obj.ele_click(lib_type_ele, load=True)
            # self.instance_obj.ele_input(
            #     self.lib_por.library_portrait_name.format(self.text_dict.get("library_search")), library_name, enter=True, load=True)
            lib_ele_lst = self.instance_obj.ele_list('css=tbody>tr')
            for per_lib in lib_ele_lst:
                lib_name, lib_num = self.instance_obj.ele_get_val(per_lib).split('\n')[:2]
                if lib_name == library_name and self.cf.get_num_from_str(lib_num) == 65:
                    return {"library_name": library_name, "portrait_name": portrait_name}
            else:
                portrait_result = self.import_portrait(library_name=library_name, sense_type=sense_type, pre_por=True)
        if not portrait_result:
            return False
        self.instance_obj.ele_click(self.lib_por.portrait_back_button, wait_time=1.5)
        self.wid.wid_chk_loading()
        return {"library_name": library_name, "portrait_name": portrait_name}

    def library_update(self, library_name=None, sense_type=1, update_name=None, remark=None):
        """
        创库、编辑
        :param library_name: 库名
        :param sense_type: 类型，1:布控库，2：静态库
        :param update_name: 编辑库名称
        :param remark: 库备注
        :return:
        """
        library_name = library_name or get_random_name(name_prefix=ResDefine.name_prefix)
        library_result = super().create_library(library_name=library_name, sense_type=sense_type)
        if not library_result or not isinstance(library_result, dict):
            return False
        portrait_result = super().update_library(library_name=library_name, sense_type=sense_type,
                                                 update_name=update_name, remark=remark)
        if not portrait_result or not isinstance(portrait_result, dict):
            return False
        library_result.update(portrait_result)
        return library_result

    def portrait_update(self, library_name=None, portrait_name=None, sense_type=1, image_=None, import_name=None,
                        identity=None, update_id=None, upload_=True, import_=False, tag=False, **kwargs):
        """
        创库、添加人像、编辑
        :param library_name: 库名
        :param portrait_name: 人像名称
        :param sense_type: 类型，1:布控库，2：静态库
        :param image_: 上传人像名称
        :param import_name: 导入名称
        :param identity: 身份证号
        :param update_id: 编辑身份证号
        :param upload_: True: 上传
        :param import_: True: 导入
        :param tag: True: 人像备注搜索
        :param kwargs: por_remark: 备注， por_gender:性别， por_address:地址， por_area: 区域,
                       update_remark: 备注， update_gender:性别， update_address:地址， update_area: 区域， update_name: 人像名称
        :return:
        """
        library_name = library_name or get_random_name(name_prefix=ResDefine.name_prefix)
        portrait_name = portrait_name or get_random_name(name_prefix="por_")
        por_result = self.create_lib_add_por(library_name=library_name, portrait_name=portrait_name,
                                             sense_type=sense_type, image_=image_, import_name=import_name,
                                             identity=identity, upload_=upload_, import_=import_, **kwargs)
        if not por_result:
            return False
        result = self.update_portrait(portrait_name=portrait_name, identity=identity, update_id=update_id, tag=tag,
                                      sense_type=sense_type, **kwargs)
        if not result:
            return False
        por_result.update({"update_name": kwargs.get("update_name")})
        return por_result


if __name__ == "__main__":
    from common.w_driver import WDriver
    from v43.pub.pub_menu import MainPage

    driver = WDriver()
    driver.open_url("http://10.111.32.91:10219/#/users")
    #
    MainPage.login_in(driver, 'pj', 'admin1234')
    # MainPage.into_menu(driver, menu_name="人像库管理")
    attribute_info = [{"lib_attribute": "头发", "attribute_values": "黑色"},
                      {"lib_attribute": "衣服", "attribute_values": "白色"}]
    sb = CreateLibPor(instance_obj=driver, log=driver.log, local_mod="人像库管理", mod_NO1="人像库管理")
    print(sb.portrait_select(gender="男", por_address="北京市", por_area="东城区"))
    # sb.delete_portrait(por_remark="dd")
    # sb.library_update(library_name="9", update_name="888", remark="808", sense_type=1)
    # sb.delete_library(library_name="999",sense_type=1)
    # print(sb.portrait_update(por_remark="999", por_gender="男", update_gender="女", update_remark="2222",por_address="北京市", por_area="东城区"))
