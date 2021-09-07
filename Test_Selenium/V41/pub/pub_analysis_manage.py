#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from v43.pub.pub_base import PublicClass
from common.common_func import shadow
import time
from sc_common.sc_define import ResDefine


class AnalysisManagePageEle:
    access_situation_page = "xpath=//*[@x-placement='bottom-start']"  # 接入情况页
    access_situation_button = "xpath=//*[@class='general-btn btn-active']"  # 接入情况页按钮
    add_analysis_task_button = "xpath=//*[@class='rz-button rz-button--text']"  # 新增解析任务按钮

    analysis_task_name_input = "xpath=//*[@class='rz-form-item__content']//input"  # 解析任务名称文本框
    task_remark_input = "xpath=//*[@class='rz-form-item__content']//textarea"  # 解析任务备注
    task_button_typo = "xpath=//*[@class='footer-btns-wrap']//span[text()='{typo}']"  # 取消，下一步，上一步，提交
    task_name_input_serach = "xpath=//*[@class='rz-input rz-input--suffix']/input"  # 解析任务搜索框 云盘文件名搜索框
    task_list_first = "xpath=//*[@class='task-group-list']/li[1]"  # 任务列表首个
    task_op_button = "xpath=//*[@slot='reference'][1]"  # 任务列表操作按钮
    op_file = "xpath=//tbody/tr[1]//*[@class='primary'][text()='{typo}']"  # 解析文件操作：播放，编辑，删除，下载
    task_op_list = "xpath=//ul[@class='more-operation']/li[text()='{typo}']"  # 任务详情，任务编辑，删除任务
    edtior_task_base_info_page = "xpath=//*[@class='base-info-mode']//span[text()='保存并提交']"  # 编辑解析任务基本信息页的保存并提交按钮
    edtior_task_permissions_page = "xpath=//*[@class='set-authority']//span[text()='保存并提交']"  # 编辑解析任务权限分配页的保存并提交按钮
    filter_info = "xpath=//*[@class='filter-info']/div[{typo}]/div"  # 各个过滤信息的下拉框按钮 传入数字1,2,3 1.解析类型，2.解析对象，3.状态
    video_file_input = "xpath=//*[@class='rz-form-item filter-operatee rz-form-item--medium']//input"  # 视频文件搜索框
    video_op_button = "xpath=//*[@class='operate']/span[text()='{typo}']"  # 视频文件的各个操作：播放，编辑，删除，下载
    add_analysis_file_button = "xpath=//*[@class='rz-button rz-button--primary rz-button--medium rz-popover__reference']"  # 添加解析文件按钮
    file_list = "xpath=//*[@class='rz-scroller infinite-list']/span[@title='{file_name}']"  # 选择文件，传入文件名
    analysis_button = "xpath=//*[@class='rz-button rz-button--primary']/span[text()='{typo}']"  # 操作按钮：解析结果，云盘
    add_analysis_file_typo_list = "xpath=//*[@class='addProcess-pop']/p[text()='{typo}']"  # 新增解析文件类型：GB28281平台 (离线视频流)，云盘（离线文件）
    selected_file_button = "xpath=//*[@class='rz-dialog__wrapper select-dialog']//span[text()='{typo}']"  # 选择文件：确定，取消
    analysis_results_task_name_input = "xpath=//*[@class='rz-input rz-input--suffix']/input[@placeholder='请输入任务名称或任务备注']"  # 解析结果页，解析任务搜索框
    analysis_results = "xpath=//*[@class='type-content']/div[{typo}]"  # 传入数字，解析结果各个文件类型的结果：1.历史视频流，2.离线视频流，3.离线图片文件
    analysis_results_typo = "xpath=//*[@class='rz-radio-group radio-buttons']/label[{typo}]"  # 传入数字，解析结果各个类型的结果：1.人脸，2.人体，3.机动车，4.非机动车，5.骑手
    export_results_button = "xpath=//*[@class='export-comparison']"  # 导出结果按钮
    all_task_button = "xpath=//*[@class='all-task tree-item active']"  # 解析结果页全部任务下拉框按钮
    task_name_button = "xpath=//*[@class='task-item-wrap tree-item']"  # 解析结果页任务名下拉框按钮
    offline_file_button = "xpath=//*[@class='rz-tooltip item']/span[text()='离线视频文件']"  # 解析结果页离线视频源文件下拉框按钮
    results_file_name = "xpath=//*[@class='tree-item file-item']"  # 解析结果页离线视频源文件按钮
    delete_file_ensure = "xpath=//*[@class='rz-button rz-button--primary rz-button--primary ']"  # 删除解析文件确定
    analysis_task_info_body = "xpath=//*[@class='rz-form base-info-wrap base-info-detail']"  # 解析任务完整信息
    go_back = "xpath=//*[@class='rz-button flex-middle back-btn rz-button--text rz-button--medium']"  # 返回

    add_folder = "xpath=//*[@class='rz-button more-operation rz-button--primary is-plain']"  # 新建文件夹按钮
    add_folder_input = "xpath=//*[@class='rechristen rz-input']/input"  # 新建文件夹名称文本框
    add_folder_ensure = "xpath=//*[@class='rz-icon-check rz-icon-undefined']"  # 新建文件夹确定
    file_name_button = "xpath=//*[@class='span-icon rz-tooltip item'][text()='{name}']"  # 点击某一文件或文件夹
    cloud_file_op = "xpath=//*[@class='table-operation']//span[text()='{typo}']"  # 云盘文件操作功能
    delete_folder_ensure = "xpath=//*[@class='rz-button rz-button--primary']//span[text()='删除']"  # 云盘文件删除确定
    go_cloud_page = "xpath=//*[@class='crumbs-btn']//span[text()='返回上一页']"  # 在文件夹页中返回到云盘页
    upload_file_ensure_button = "xpath=//*[@class='rz-button rz-button--primary']/span[text()='确定']"  # 上传文件到云盘的提示弹窗的确定按钮
    analysis_task_input = "xpath=//*[@class='rz-select']"  # 解析任务下拉框
    analysis_file_ensure = "xpath=//*[@class='rz-button rz-button--primary rz-button--large']"  # 云盘中解析文件确定按钮
    analysis_name = "xpath=//li/span[text()='{name}']"  # 云盘中解析页中搜索出任务后的选中元素
    analysis_obj = "xpath=//*[@class='rz-checkbox-group']/label[{typo}]"  # 传入数字，1.取消人脸解析 2.取消结构化解析
    inner_type = "xpath=//*[@class='inner-type']"  # 人脸
    analysis_file_status = "xpath=//*[@class='plain']"  # 解析文件的状态
    not_analysis_info = "xpath=//*/p[text()='暂无解析内容']"
    analysis_results_first = "xpath=//*[@class='list']/div[1]"  # 解析结果首张图片
    analysis_results_list = "xpath=//*[@class='list']"  # 解析结果列表


class AnalysisAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = AnalysisManagePageEle

    @shadow("解析管理-新增解析任务")
    def add_analysis_task(self, task_name, remark=False):
        """

        :param task_name:
        :param remark:
        :return:
        """
        self.wid.wid_chk_loading()
        if self.driver.ele_exist(self.el.access_situation_page):
            self.driver.ele_click(self.el.access_situation_button)
        self.driver.ele_click(self.el.add_analysis_task_button)
        self.wid.wid_chk_loading()
        self.driver.ele_input(self.el.analysis_task_name_input, task_name)
        if remark:
            self.driver.ele_input(self.el.task_remark_input, remark)
        self.driver.ele_click(self.el.task_button_typo.format(typo='下一步'))
        self.wid.wid_chk_loading()
        self.driver.ele_click(self.el.task_button_typo.format(typo='提交'))
        alert_msg = self.wid.wid_get_alert_label()
        return alert_msg
        # if "成功" in self.wid.wid_get_alert_label():
        #     return True
        # else:
        #     return False

    @shadow("解析管理-搜索解析任务")
    def search_analysis_task(self, task_name):
        """

        :param task_name:
        :return:
        """
        self.wid.wid_chk_loading()
        self.driver.ele_input(self.el.task_name_input_serach, task_name, enter=True)
        self.wid.wid_chk_loading()
        return True

    @shadow("解析管理-解析任务的各个操作")
    def operate_analysis_task(self, typo="", task_name=""):
        """

        :param typo:
        :param task_name:
        :return:
        """
        if typo not in ["任务详情", "任务编辑", "删除任务"]:
            return False
        self.driver.ele_click(self.el.task_list_first, move=True)
        time.sleep(1)
        self.driver.ele_click(self.el.task_op_button)
        time.sleep(1)
        self.driver.ele_click(self.el.task_op_list.format(typo=typo))
        if typo == "任务编辑":
            if task_name:
                self.driver.ele_input(self.el.analysis_task_name_input, task_name)
                self.driver.ele_click(self.el.edtior_task_base_info_page)
        if typo == "删除任务":
            self.driver.ele_click(self.el.delete_file_ensure)
            if "删除成功" not in self.wid.wid_get_alert_label():
                return False

        return True

    @shadow("解析管理-上传文件到云盘")
    def add_cloud_file(self, file="", folder=""):
        """
        :param file:
        :param folder:
        :return:
        """
        self.driver.ele_click(self.el.analysis_button.format(typo="云盘"))
        if folder:
            self.driver.ele_click(self.el.add_folder)
            self.driver.ele_input(self.el.add_folder_input, folder)
            self.driver.ele_click(self.el.add_folder_ensure)
            time.sleep(1)
            if "新建文件夹成功" not in self.wid.wid_get_alert_label():
                return False
            time.sleep(4)
            self.driver.ele_click(self.el.file_name_button.format(name=folder))
        time.sleep(1)
        self.driver.chk_loading()
        self.driver.ele_input(self.el.task_name_input_serach, file, enter=True)
        if self.driver.ele_exist(self.el.file_name_button.format(name=file)):
            return True

        file = ResDefine.get_file(file)
        self.wid.wid_upload(img_path=file, ele="css=input[type='file']")

        time.sleep(2)
        if "成功" not in self.wid.wid_get_alert_label(wait_miss=True):
            return False
        return True

    @shadow("解析管理-云盘页中搜索文件")
    def search_cloud_file(self, search_info=""):
        """

        :param search_info:
        :return:
        """
        if search_info:
            self.driver.chk_loading()
            self.driver.ele_input(self.el.task_name_input_serach, search_info, enter=True)
        return True

    @shadow("解析管理-操作云盘文件")
    def operation_cloud_file(self, play=False, analysis_task="", analysis_obj="", modify_name="", delete=False,
                             download=False):
        """

        :param play:
        :param analysis:
        :param modify_name:
        :param delete:
        :param download:
        :return:
        """
        if play:
            self.driver.ele_click(self.el.cloud_file_op.format(typo="播放"))
        if modify_name:
            self.driver.ele_click(self.el.cloud_file_op.format(typo="重命名"))
            self.driver.ele_input(self.el.add_folder_input, modify_name)
            self.driver.ele_click(self.el.add_folder_ensure)
        if analysis_task:
            self.driver.ele_click(self.el.cloud_file_op.format(typo="解析"))
            time.sleep(1)
            self.driver.ele_click(self.el.analysis_task_input)
            time.sleep(1)
            self.driver.ele_input(self.el.task_name_input_serach, analysis_task, enter=True)
            time.sleep(1)
            self.driver.ele_click(self.el.analysis_name.format(name=analysis_task))
            if analysis_obj:
                self.driver.ele_click(self.el.analysis_obj.format(typo=analysis_obj))
            self.driver.ele_click(self.el.analysis_file_ensure)
        if download:
            self.driver.ele_click(self.el.cloud_file_op.format(typo="下载"))
        if delete:
            self.driver.ele_click(self.el.cloud_file_op.format(typo="删除"))
            self.driver.ele_click(self.el.delete_folder_ensure)
        return True

    @shadow("解析管理-添加解析文件")
    def add_analysis_file(self, analysis_file="cut.mp4", file_typo="云盘（离线文件）", analysis_obj="2"):
        """

        :param analysis_file:
        :param file_typo:
        :param analysis_obj:
        :return:
        """
        self.driver.ele_click(self.el.add_analysis_file_button)
        self.driver.ele_click(self.el.add_analysis_file_typo_list.format(typo=file_typo))
        if not self.driver.ele_exist(self.el.file_list.format(file_name=analysis_file)):
            self.log.error("你需要选择的文件：{} 不存在，请输入存在的视频文件".format(analysis_file))
            return False
        self.driver.ele_click(self.el.file_list.format(file_name=analysis_file))
        time.sleep(1)
        self.driver.ele_click(self.el.selected_file_button.format(typo="确定"))
        time.sleep(1)
        if analysis_obj:
            self.driver.ele_click(self.el.analysis_obj.format(typo=analysis_obj))
        time.sleep(0.5)
        self.driver.ele_click(self.el.task_button_typo.format(typo='提交'))
        msg = self.wid.wid_task_tip()
        if not msg:
            return False
        return True

    @shadow("解析管理-过滤解析文件")
    def filter_analysis_file(self, analysis_typo=None, analysis_obj=None, analysis_status=None, search_info=None):
        """

        :param analysis_typo:
        :param analysis_obj:
        :param analysis_status:
        :param search_info:
        :return:
        """
        if analysis_typo:
            self.driver.ele_click(self.el.filter_info.format(typo=1))
            self.driver.chk_loading()
            if analysis_typo not in ["不限", "历史视频流", "离线视频文件", "图片文件"]:
                self.log.error("请输入正确的库类型：不限，历史视频流，离线视频文件,图片文件")
                return False
            self.wid.wid_drop_down(analysis_typo)

        if analysis_obj:
            self.driver.ele_click(self.el.filter_info.format(typo=2))
            self.driver.chk_loading()
            if analysis_obj not in ["不限", "人脸", "结构化"]:
                self.log.error("请输入正确的库类型：不限，人脸，结构化")
                return False
            self.wid.wid_drop_down(analysis_obj)

        if analysis_status:
            self.driver.ele_click(self.el.filter_info.format(typo=3))
            self.driver.chk_loading()
            if analysis_status not in ["不限", "已终止", "排队中", "解析中", "解析失败", "已完成"]:
                self.log.error("请输入正确的任务状态：不限，已终止，排队中，解析中，解析失败，已完成")
                return False
            self.wid.wid_drop_down(analysis_status)
        if search_info:
            self.driver.chk_loading()
            self.driver.ele_input(self.el.video_file_input, search_info, enter=True)
        return True

    @shadow("解析管理-操作解析文件")
    def operate_analysis_file(self, op_typo="播放"):
        """

        :param op_typo:
        :return:
        """
        self.driver.ele_click(self.el.op_file.format(typo=op_typo))
        if op_typo == "删除":
            self.driver.ele_click(self.el.delete_file_ensure)

    @shadow("解析管理-解析结果操作")
    def operate_analysis_results(self, typo="解析结果", search_info="", results_typo=""):
        """

        :param typo:
        :param search_info:
        :param results_typo:
        :return:
        """
        self.driver.ele_click(self.el.analysis_button.format(typo=typo))
        if search_info:
            self.driver.chk_loading()
            self.driver.ele_input(self.el.analysis_results_task_name_input, search_info, enter=True)
            self.wid.wid_chk_loading()
            time.sleep(2)
            # self.driver.ele_click(self.el.all_task_button)
            self.driver.ele_click(self.el.task_name_button)
            self.wid.wid_chk_loading()
            time.sleep(1)
            self.driver.ele_click(self.el.offline_file_button)
            self.wid.wid_chk_loading()
            time.sleep(1)
            self.driver.ele_click(self.el.results_file_name)
            self.wid.wid_chk_loading()
        if results_typo:
            self.driver.ele_click(self.el.analysis_results_typo.format(typo=results_typo))
        return True

    @shadow("解析管理-预置解析任务")
    def pre_analysis_task(self):
        task_name = "UI_pre_analysis_task"
        file_name = "cut.mp4"
        self.wid.wid_chk_loading()
        if self.driver.ele_exist(self.el.access_situation_page):
            self.driver.ele_click(self.el.access_situation_button)
        else:
            self.search_analysis_task(task_name)
        if not self.driver.ele_exist(self.el.task_list_first):
            data = self.add_analysis_task(task_name, remark=False)
            if not data:
                return False
        self.driver.ele_click(self.el.task_list_first)
        time.sleep(1)
        if not self.driver.ele_exist(self.el.not_analysis_info):
            self.filter_analysis_file(analysis_obj="人脸")
        if not self.driver.ele_exist(self.el.inner_type):
            res = self.add_cloud_file(file=file_name)
            if not res:
                return False
            res2 = self.search_cloud_file(search_info=file_name)
            if not res2:
                return False
            res3 = self.operation_cloud_file(analysis_task=task_name, analysis_obj="2")
            if not res3:
                return False
            self.driver.ele_click(self.el.go_back)
        return True
