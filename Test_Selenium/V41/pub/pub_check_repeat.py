#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from v43.pub.pub_base import PublicClass
from common.common_func import *
import time


class CheckRepeatEle:
    add_task_button = "xpath=//*[@class='rz-button create-task-btn rz-button--primary']"  # 新建任务按钮
    case_input = "xpath=//*[@class='rz-input']/input[@placeholder='{typo}']"  # 案件文本框：请输入案件名称，请输入案件编号
    lib_contrast = "xpath=//*[@class='rz-radio-group']/label[{typo}]"  # 传入数字 选中查重方式：1.聚类，2.库间比对
    threshold_value_input = "xpath=//*[@class='rz-input rz-input--small rz-input--suffix']/input"  # 阈值文本框
    check_repeat_source = "xpath=//*[@class='rz-input rz-input--suffix rz-popover__reference']"  # 查看来源
    choose_lib_typo = "xpath=//*[@class='tabs']/div[{typo}]"  # 选择库类型，传入数字，1.静态库，2.布控库
    lib_search_input = "xpath=//*[@class='rz-input rz-input--suffix']/input[@placeholder='请输入库名/备注']"  # 库名搜索框
    all_select = "xpath=//*[@class='rz-checkbox']/span/span"  # 全选按钮
    save_button = "xpath=//*[@class='rz-button rz-button--text is-primary-text']"  # 保存按钮
    remarks_input = "xpath=//*[@class='rz-textarea']/textarea"  # 备注文本框
    create_task_button = "xpath=//*[@class='rz-button rz-button--primary']"  # 创建任务按钮
    filter_drop_button = "xpath=//*[@class='left']/div[{typo}]//input"  # 传入数字，过滤下拉框按钮：1.任务状态，2.创建人
    search_button = "xpath=//*[@class='rz-input rz-input--suffix']/input"  # 任务搜索框
    task_frame_text = "css=.has-gutter>tr>th:nth-of-type({})>div"  # 1.任务名，2.案件编号，3.创建人，4.查重来源，5.查重方式，6.备注，7.状态，8.操作
    first_task_status = "xpath=//tr[1][@class='rz-table__row']/td[{}]"  # 首个任务的各个信息：1.任务名，2.案件编号，3.创建人，4.查重来源，5.查重方式，6.备注，7.状态，8.操作
    task_op_button = "xpath=//tr[1][@class='rz-table__row']/td[8]/div/button[{typo}]"  # 任务操作按钮，1.删除，2.查看结果
    termination_ensure = "xpath=//span[text()='终止']"  # 终止确认
    delete_ensure_button = "xpath=//*[@class='rz-button rz-button--primary rz-button--primary ']"  # 删除确定按钮
    first_similar_target = "xpath=//*[@class='list']/div[1]"  # 首组相似目标
    first_task_run_status = "xpath=//tr[1][@class='rz-table__row']/td[7]/div/div/span[text()='{typo}']"  # 任务的运行状态
    similar_por_detail_text = "css=.person-detail>div>.rz-dialog__title"  # 相似人像详情
    judge = "xpath=//button/span[text()='研判']"  # 研判
    judge_select = "css=.right-arae>div:nth-of-type(1)  .rz-radio__input"  # 研判选项，是否
    match_info = "css=.match-info>p"  # 匹配信息
    judge_confirm = "css=.rz-dialog__body .rz-button.rz-button--primary"  # 研判确定
    exclusion = "css=.rz-dialog__body .right-arae>div:nth-of-type(1) .exclusions-tag"  # 排除
    warning_info = "css=.rz-table__empty-text>p"  # 提示语
    reboot_confirm = "xpath=//span[text()='重启']"  # 重启确认建

    class TaskDetail:
        export = "css=.rz-button.export.rz-button--text>span"  # 导出
        result_list = "css=.check-result-list>div>div>div>div"  # 结果列表
        task_detail_text = "css=.crumbs-item.last-crumbs-item>span"  # 任务详情  （text）
        similar_pro_num = "css=.selectors>div:nth-of-type(3)>div>div>input"  # 相似人像数
        repeat_info = "css=.selectors>div:nth-of-type(4)>div>div>input"  # 重复情况
        repeat_source_input = "xpath=//span[text()='查重来源']/../div/input"  # 重复来源input
        similarity_input = "xpath=//span[text()='相似度']/../div/input"  # 相似度input
        similarity_input_frame = "css=.rz-input.rz-input--small.rz-input--suffix>input"  # 相似度输入框
        return_back = "css=.rz-icon-arrow-left"  # 返回


class CheckRepeatAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = CheckRepeatEle

    @shadow("查重-新建查重任务")
    def add_task(self, task_name=None, check_typo="1", similar=95, lib_list=None, case_num=None, remarks=None):
        """
        新建查重任务
        :param task_name:
        :param check_typo:  1、聚类， 2、库间比对
        :param similar:     相似度
        :param lib_list:    人像库名称，以列表形式传入 [{'lib_type':1, 'lib_name': '库名'}]，最多传两个库
        :param case_num:
        :param remarks:
        :return:
        """
        assert isinstance(lib_list, list), 'lib_list参数不为列表，入参格式不正确'
        self.driver.ele_click(self.el.add_task_button)
        self.driver.ele_input(self.el.case_input.format(typo="请输入案件名称"), task_name)
        if check_typo == "2":
            self.driver.ele_click(self.el.lib_contrast.format(typo=check_typo))
            self.driver.ele_input(self.el.threshold_value_input, similar, cln=1)
        self.driver.ele_click(self.el.check_repeat_source)
        self.wid.wid_chk_loading()
        time.sleep(1)
        for val in lib_list:
            lib_type = val['lib_type']
            lib_name = val['lib_name']
            self.driver.ele_click(self.el.choose_lib_typo.format(typo=lib_type))
            self.wid.wid_chk_loading()
            time.sleep(2)
            self.driver.ele_input(self.el.lib_search_input, lib_name, enter=True)
            self.wid.wid_chk_loading()
            time.sleep(1)
            self.driver.ele_click(self.el.all_select)
        if lib_list:
            self.driver.ele_click(self.el.save_button)
        if case_num:
            self.driver.ele_input(self.el.case_input.format(typo="请输入案件编号"), case_num)
        if remarks:
            self.driver.ele_input(self.el.remarks_input, remarks)
        self.driver.ele_click(self.el.create_task_button)
        tip_info = self.wid.wid_get_alert_label()
        if tip_info:
            self.collect_resource(self.df.key_check_repeat, task_name)
            return True

    @shadow("查重-过滤查重任务")
    def filter_check_repeat_task(self, task_status="不限", create_user="不限", search_info=None):
        """

        :param task_status:
        :param create_user:
        :param search_info:
        :return:
        """
        if task_status:
            self.driver.ele_click(self.el.filter_drop_button.format(typo=1))
            self.driver.chk_loading()
            if task_status not in ["不限", "排队中", "进行中", "存储中", "已完成", "失败", "已终止"]:
                self.log.error("请输入正确的任务状态：不限, 排队中, 进行中, 存储中, 已完成, 失败, 已终止")
                return False
            self.wid.wid_drop_down(task_status)

        if create_user:
            self.driver.ele_click(self.el.filter_drop_button.format(typo=2))
            self.driver.chk_loading()
            if create_user not in ["不限", "我的任务", "其他人的任务"]:
                self.log.error("请输入正确的创建人类型：不限，我的任务，其他人的任务")
                return False
            self.wid.wid_drop_down(create_user)

        if search_info:
            self.driver.ele_input(self.el.search_button, search_info, enter=True)
            self.driver.chk_loading()
            if not self.driver.ele_exist(self.el.first_task_status):
                return False
        return True

    @shadow("查重-操作查重任务")
    def operation_check_repeat_task(self, operation=None):
        """
        查重-操作查重任务
        :param operation:  1、删除、终止、重启、查看结果
        :return:
        """
        if operation in ['删除', '终止']:
            self.driver.ele_click(self.el.task_op_button.format(typo=1))
            self.driver.ele_click(self.el.delete_ensure_button)
            res = self.wid.wid_get_alert_label()
            if not res:
                return False
            return True if "任务已终止" in res or "任务已删除" in res or '重启任务成功' in res else False
        else:
            self.driver.ele_click(self.el.task_op_button.format(typo=2))
            if operation == '重启':
                time.sleep(1)
                self.driver.ele_click(self.el.reboot_confirm)
                res = self.wid.wid_get_alert_label()
                if not res:
                    return False
                return True if "任务已终止" in res or "任务已删除" in res or '重启任务成功' in res else False

    @shadow("查重-获取相应状态的查重任务")
    def get_check_repeat_status(self, task_name, status=None, count=20, time_sleep=10):
        self.filter_check_repeat_task(search_info=task_name)
        if status not in ["不限", "排队中", "进行中", "存储中", "已完成", "失败", "已终止"]:
            self.log.error("请输入正确的运行状态")
            return False
        status_el = self.el.first_task_run_status.format(typo=status)

        for j in range(count):
            self.wid.wid_chk_loading()
            time.sleep(time_sleep)
            if self.driver.ele_exist(status_el):
                self.log.info("查重任务已变成自己所需要的的任务状态：{}".format(status))
                return True
            else:
                self.driver.chk_loading()
                self.filter_check_repeat_task(search_info=task_name)
                continue
        else:
            self.log.error("查询次数达到最大次数，仍未获取到{}状态的查重任务，请检查环境！".format(status))
            return False

    @shadow("查重-查看结果详情")
    def view_task_result(self, task_name=None, index=None, judge=None):
        """
        :param task_name:
        :param index: 结果列表第几个详情, 不传不查看结果详情
        :param judge: 研判，True为是，False， 否
        :return:
        """
        self.filter_check_repeat_task(search_info=task_name)
        self.wid.wid_chk_loading()
        self.operation_check_repeat_task(operation='查看结果')
        result_list = self.driver.ele_list(self.el.TaskDetail.result_list)
        assert result_list, '查重任务结果为空'
        self.driver.ele_assert_text(self.el.TaskDetail.task_detail_text, '任务详情')
        self.driver.ele_assert_text(self.el.TaskDetail.export, '导出')
        if index:
            self.driver.ele_click(result_list[index - 1])
            self.driver.ele_assert_text(self.el.similar_por_detail_text, '相似人像详情')
            self.driver.ele_assert_text(self.el.match_info, '匹配信息')
            if judge is not None:
                self.driver.ele_click(self.el.judge)
                judge_list = self.driver.ele_list(self.el.judge_select)
                self.driver.ele_click(judge_list[0]) if judge else self.driver.ele_click(judge_list[1])
                self.driver.ele_click(self.el.judge_confirm)
                self.driver.ele_assert_text(self.el.exclusion, '排除')

    @shadow('查重-筛选任务结果')
    def filter_task_result(self, repeat_source=None, similar_pro_num=None, repeat_info=None, similarity=None):
        """
        查重-筛选任务结果
        :param repeat_source:    重复来源
        :param similar_pro_num:  相似人像数
        :param repeat_info:      重复情况
        :param similarity:       相似度
        :return:
        """
        if repeat_source:
            pass
        if similar_pro_num:
            self.wid.wid_drop_down(similar_pro_num, self.el.TaskDetail.similar_pro_num)
            self.wid.wid_chk_loading()
        if repeat_info:
            self.wid.wid_drop_down(similar_pro_num, self.el.TaskDetail.similar_pro_num)
            self.wid.wid_chk_loading()
        if similarity:
            self.driver.ele_click(self.el.TaskDetail.similarity_input)
            self.driver.ele_input(self.el.TaskDetail.similarity_input_frame, similarity, cln=1, enter=True)
            self.wid.wid_chk_loading()

    @shadow('查重-新建库聚类、新建库间比对预置任务')
    def pre_check_repeat_task(self):
        task_name_list = ['UI_pre_查重_库聚类任务']
        lib_info_list = [[{'lib_type': '2', 'lib_name': "UI_pre_65_por"}]
                         ]
        check_type_list = ['1']
        similar = 92
        for i in range(len(task_name_list)):
            if not self.filter_check_repeat_task(search_info=task_name_list[i]):
                self.add_task(task_name=task_name_list[i], check_typo=check_type_list[i], similar=similar,
                              lib_list=lib_info_list[i], remarks='我是备注', case_num=12345678)
                time.sleep(0.5)
                self.filter_check_repeat_task(task_status="进行中", create_user="不限", search_info=task_name_list[i])
                time.sleep(5 * 60)
                result = self.get_check_repeat_status(task_name=task_name_list[i], status="已完成", count=10,
                                                      time_sleep=30)
                assert result, '查重任务{}没有过了10分钟之后还完成'.format(task_name_list[i])
        return task_name_list[0]

    @shadow('删除查重任务')
    def delete_check_repeat_task(self, task_name):
        """
        :param task_name: 任务名称
        :return:
        """
        result = self.filter_check_repeat_task(task_status='进行中', search_info=task_name)
        if result:
            self.operation_check_repeat_task(operation='终止')
            self.operation_check_repeat_task(operation='删除')
        else:
            self.filter_check_repeat_task(search_info=task_name)
            self.operation_check_repeat_task(operation='删除')
        return True


