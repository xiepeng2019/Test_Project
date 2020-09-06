#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from v43.pub.pub_base import PublicClass
from common.common_func import shadow, get_ip_in_str
from sc_common.sc_define import ResDefine
import time, paramiko, json


class IntoLibPageEle:
    add_into_lib_task = "xpath=//*[@class='rz-button create-task rz-button--primary']/span[text()='新建任务']"  # 新建入库任务按钮
    task_name_input = "xpath=//*[@class='name input rz-input']/input"  # 任务名称新增
    select_lib_type = "xpath=//*[@class='rz-input rz-input--suffix']/input[@placeholder='请输入']"  # 选择库类型下拉框
    select_lib = "xpath=//*[@class='input rz-input rz-input-group rz-input-group--prepend rz-input--suffix rz-popover__reference']/input"  # 人像库列表下拉框
    lib_input = "xpath=(//*[@class='rz-input rz-input--suffix']/input[@placeholder='请输入库名/备注'])[2]"  # 库名或备注搜索框
    lib_name = "xpath=//*[@class='tarLibName']"  # 选中搜索出来的库
    file_type = "xpath=//*[@class='rz-form-item__content']/label[{typo}]"  # 传入数字，1.压缩包类型，2.图片文件夹
    add_file = "xpath=//*[@class='add-file-btn']/button"  # 新增文件按钮
    file_input = "xpath=//*[@class='rz-table__body']//input"  # 图片文件夹路径输入框
    file_input_ensure = "xpath=//*[@class='icon iconfont icon-by']"  # 图片文件夹路径输入确定按钮
    remark_input = "xpath=//*[@class='remark input rz-textarea rz-input--suffix']/textarea"  # 备注文本框
    next_steps = "xpath=//*[@class='control']/div/button[3]"  # 下一步
    # 参数设置页
    text_input = "xpath=//*[@class='configuration-contain']//form[@class='rz-form']/div[{typo}]//input"  # 传入数字 参数配置文本框 1.遍历文件夹图片线程,2.同步图片线程,3.图片质量分数 4.文件命名规则
    file_name_rules = "xpath=//*[@class='rz-scrollbar__view rz-select-dropdown__list']/li[1]/span[text()='姓名']"  # 文件命名规则
    file_name_set_button = "xpath=//*[@class='rz-button btn rz-button--text is-primary-text']"  # 文件命名规则设置
    add_file_name_rule = "xpath=//*[@class='rz-button rz-button--primary']/span[text()='添加文件命名规则']"  # 添加文件名命名规则
    add_file_name_ensure = "xpath=/html/body/div/div/div[3]/button[2]"  # 添加文件名命名规则确定按钮
    add_file_name_rule_close_btn = '//span[text()="文件命名规则设置"]/following-sibling::button'  # 规则右上角关闭按钮

    add_into_lib_task_ensure = "xpath=//*[@class='control']//button[3]"  # 新建入库任务确定按钮
    msg_close = "xpath=//*[@class='rz-button rz-button--primary']/span[text()='知道了']"  # 消息弹窗关闭
    # 入库助手页
    typo_drop_down = "xpath=//*[@class='filter-conditions']/div[{typo}]/div"  # 传入数字，入库助手页下拉框 2.人像库类型,3.状态
    task_input = "xpath=//*[@class='rz-input rz-input--suffix']/input"  # 任务名文本框
    into_lib_status = "xpath=//*[@class='rz-table__row']/td[5]//span[1][text()='{typo}']"  # 任务的状态
    task_op_button = "xpath=//*[@class='rz-button view-button rz-button--text']/span[text()='{typo}']"  # 终止，删除任务 按钮
    stop_or_delete_button_ensure = "xpath=//*[@class='rz-button rz-button--primary']/span[text()='{typo}']"  # 终止，删除确定按钮


ssh_info = {"user": "admin", "pwd": "88stIVA#2017", "host": "10.111.32.91", "remote_path": "/home/admin",
            "folder": "/ui_test_file", "file_name": "11.jpg"}


class input_ssh:
    def __init__(self, host):
        self.ssh = None
        self.t = None
        self.host = host

    def put_file(self, local_file):
        try:

            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.host, username=ssh_info.get("user"),
                             password=ssh_info.get("pwd"))
            message = get_ip_in_str(self.host)
            t = paramiko.Transport(message, 22)
            t.connect(username=ssh_info.get("user"), password=ssh_info.get("pwd"))
            self.sftp = paramiko.SFTPClient.from_transport(t)
            stdin, stdout, stderr = self.ssh.exec_command("find -name {}".format(ssh_info.get("folder")[1:]))
            file_name = stdout.read().decode('utf-8')
            if not file_name:
                self.ssh.exec_command("cd {}".format(ssh_info.get("remote_path")))
                self.ssh.exec_command("mkdir {}{}".format(ssh_info.get("remote_path"), ssh_info.get("folder")))
            time.sleep(1)
            self.sftp.put(local_file, "{}{}/{}".format(ssh_info.get("remote_path"), ssh_info.get("folder"),
                                                       ssh_info.get("file_name")))
        except Exception as e:
            print(e)
        finally:
            if self.ssh:
                self.ssh.close()
            if self.t:
                self.t.close()


class IntoLibAction(PublicClass):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)
        self.el = IntoLibPageEle
        self.kw = kwargs

    @shadow("入库助手-创建任务基本信息页")
    def add_into_lib_task_base_info(self, task_name, lib_name, import_name, remark="", file_type=1, lib_type=1):
        """

        :param task_name:
        :param lib_name:
        :param import_name:
        :param remark:
        :param file_type:
        :param lib_type:
        :return:
        """
        self.driver.ele_click(self.el.add_into_lib_task)
        self.driver.ele_input(self.el.task_name_input, task_name)
        if lib_type == 1:
            self.driver.ele_click(self.el.select_lib_type)
            self.wid.wid_drop_down("布控库")
        if lib_type == 2:
            self.driver.ele_click(self.el.select_lib_type)
            self.wid.wid_drop_down("静态库")
        time.sleep(3)
        self.driver.ele_click(self.el.select_lib)
        time.sleep(3)
        self.driver.ele_input(self.el.lib_input, lib_name, enter=True)
        time.sleep(3)
        self.wid.wid_chk_loading()
        self.driver.ele_click(self.el.lib_name)
        self.driver.ele_click(self.el.file_type.format(typo=file_type))

        if file_type == 1:
            import_path = ResDefine.get_file(import_name)
            self.wid.wid_upload(img_path=import_path, ele="css=input[type='file']")
        if file_type == 2:
            loc_path = ResDefine.get_file("{}".format(ssh_info.get("file_name")), version_path="v40")
            message = get_ip_in_str(self.kw.get("host"))
            data = input_ssh(message)
            data.put_file(loc_path)
            self.driver.ele_click(self.el.add_file)
            self.driver.ele_input(self.el.file_input,
                                  "{}{}".format(ssh_info.get("remote_path"), ssh_info.get("folder")))
            self.driver.ele_click(self.el.file_input_ensure)
        if remark:
            self.driver.ele_input(self.el.remark_input, remark)
        self.driver.ele_click(self.el.next_steps)
        self.collect_resource(resource_type=ResDefine.key_into_lib_task, resource_value=task_name)
        return True

    @shadow("入库助手-创建任务参数配置页")
    def add_into_lib_task_setting(self, traverse_image, synchronous_image, quality_image, file_type=1):
        """

        :param traverse_image:
        :param synchronous_image:
        :param quality_image:
        :return:
        """
        self.driver.ele_input(self.el.text_input.format(typo="1"), traverse_image)
        self.driver.ele_input(self.el.text_input.format(typo="2"), synchronous_image)
        self.driver.ele_input(self.el.text_input.format(typo="3"), quality_image)
        self.driver.ele_click(self.el.text_input.format(typo=" 4"))
        if not self.driver.ele_exist(self.el.file_name_rules):
            self.log.warning("没有规则命名，文件命名规则设置")
            self.driver.ele_click(self.el.file_name_set_button)
            self.driver.ele_click(self.el.add_file_name_rule)
            self.driver.ele_click(self.el.add_file_name_ensure)
            self.driver.ele_click(self.el.add_file_name_rule_close_btn)
            self.driver.ele_click(self.wid.el.input_tip_el.format("文件命名规则"))
        self.driver.ele_click(self.el.file_name_rules)
        self.driver.ele_click(self.el.add_into_lib_task_ensure)
        self.wid.wid_chk_loading()
        time.sleep(1)
        if file_type == 1:
            self.driver.ele_click(self.el.msg_close)
        return True

    @shadow("入库助手-过滤搜索入库任务")
    def search_into_lib__task(self, lib_type=None, staus=None, search_info=None):
        """

        :param lib_type:
        :param staus:
        :param search_info:
        :return:
        """
        if lib_type:
            self.driver.ele_click(self.el.typo_drop_down.format(typo=2))
            self.driver.chk_loading()
            if lib_type not in ["不限", "布控库", "静态库"]:
                self.log.error("请输入正确的库类型：不限，布控库，静态库")
                return False
            self.wid.wid_drop_down(lib_type)

        if staus:
            self.driver.ele_click(self.el.typo_drop_down.format(typo=3))
            self.driver.chk_loading()
            if staus not in ["不限", "同步中", "等待中", "上传中", "已完成", "已终止"]:
                self.log.error("请输入正确的任务状态：不限，同步中，等待中，上传中，已完成，已终止")
                return False
            self.wid.wid_drop_down(staus)
        if search_info:
            self.driver.chk_loading()
            self.driver.ele_input(self.el.task_input, search_info, enter=True)
        return True

    @shadow("入库助手-获取相应状态的入库任务")
    def get_into_lib_status(self, name, status=None, count=30, time_sleep=3):
        self.search_into_lib__task(lib_type="不限", staus=None, search_info=name)
        if status == "上传中":
            status_el = self.el.into_lib_status.format(typo="上传中")
        elif status == "同步中":
            status_el = self.el.into_lib_status.format(typo="同步中")
        elif status == "已完成":
            status_el = self.el.into_lib_status.format(typo="已完成")
        else:
            self.log.error("当前传入的状态为：{}，请输入正确的任务状态：".format(status))
            return False
        for j in range(count):
            self.wid.wid_chk_loading()
            time.sleep(time_sleep)
            if self.driver.ele_exist(status_el):
                self.log.info("入库任务已变成自己所需要的的任务状态：{}".format(status))
                return True
            else:
                self.driver.chk_loading()
                self.driver.ele_input(self.el.task_input, name, enter=True)
                continue
        else:
            self.log.error("查询次数达到最大次数，仍未获取到{}状态的入库任务，请检查环境！".format(status))
            return False

    @shadow("入库助手-删除入库任务")
    def delete_into_lib_task(self, name):
        self.driver.refresh_driver()
        self.wid.wid_chk_loading()
        self.into_menu("入库助手")
        self.wid.wid_chk_loading()
        self.search_into_lib__task(lib_type="不限", staus=None, search_info=name)
        if self.driver.ele_exist(self.el.task_op_button.format(typo='终止')):
            self.driver.ele_click(self.el.task_op_button.format(typo='终止'))
            self.driver.ele_click(self.el.stop_or_delete_button_ensure.format(typo="终止"))
        time.sleep(1)
        if self.driver.ele_exist(self.el.task_op_button.format(typo="删除")):
            self.driver.ele_click(self.el.task_op_button.format(typo="删除"))
            self.driver.ele_click(self.el.stop_or_delete_button_ensure.format(typo="删除"))
        time.sleep(0.5)
        return True


class IntoLibPage(IntoLibAction):
    def __init__(self, driver, **kwargs):
        super().__init__(driver, **kwargs)

    def add_into_lib_task_main(self, task_name, lib_name, import_name, traverse_image, synchronous_image,
                               quality_image, remark="", file_type=1, lib_type=1):
        """

        :param task_name:
        :param lib_name:
        :param import_name:
        :param traverse_image:
        :param synchronous_image:
        :param quality_image:
        :return:
        """
        res = self.add_into_lib_task_base_info(task_name, lib_name, import_name, remark=remark, file_type=file_type,
                                               lib_type=lib_type)
        if not res:
            return False
        res2 = self.add_into_lib_task_setting(traverse_image, synchronous_image, quality_image, file_type=file_type)
        if not res2:
            return False
        return True


if __name__ == "__main__":
    pass
