#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait
from common.common_func import get_random_name, shadow
from selenium.webdriver.remote.webdriver import WebElement
from common.log import get_simple_log
from common import common_func as CF


class WDriver:

    # 初始化driver
    def __init__(self, browser="chrome", log=None, time_out=20, test_desired=None, hub_url=None, **kwargs):
        """
        :param browser: 浏览器名称（小写）
        :param log: 日志句柄
        :param time_out: 超时时间（秒）
        :param hub_url: 远程分布式hub服务地址，有则代表是远程执行
        """
        self.time_out = time_out
        self.interval_time = 1

        def browser_option(browser_option):
            browser_option.add_argument('--ignore-certificate-errors')
            return browser_option

        if hub_url:
            if browser == "chrome":
                desired_capabilities = DesiredCapabilities.CHROME
            elif browser == "firefox":
                desired_capabilities = DesiredCapabilities.FIREFOX
            else:
                browser = "chrome"
                desired_capabilities = DesiredCapabilities.CHROME
            if test_desired:
                desired_capabilities.update(test_desired)
            if kwargs.get('name'):
                desired_capabilities.update({'name': kwargs.get('name')})
            else:
                desired_capabilities.update({"name": browser + str(time.time())})
            desired_capabilities.update({
                # 时区
                'tz': 'Asia/Shanghai',
                # 视频文件名称
                'testFileNameTemplate': kwargs.get('file_name'),
            })
            self.driver = webdriver.Remote(command_executor=hub_url,
                                           desired_capabilities=desired_capabilities,
                                           options=browser_option(webdriver.ChromeOptions())
                                           )
        else:
            driver_pkg = os.path.join(os.path.dirname(__file__), "..", "driver_pkg")
            if browser == "firefox":
                self.driver = webdriver.Firefox(os.path.join(driver_pkg, "geckodriver.exe"),
                                                firefox_options=browser_option(webdriver.FirefoxOptions())
                                                )
            else:
                self.driver = webdriver.Chrome(os.path.join(driver_pkg, "chromedriver.exe"),
                                               chrome_options=browser_option(webdriver.ChromeOptions())
                                               )
        from datetime import datetime
        # self.driver.implicitly_wait(time_out)
        self.action = ActionChains(self.driver)
        self.w_wait = WebDriverWait(self.driver, self.time_out, self.interval_time)
        if log:
            self.log = log
        else:
            log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
            os.mkdir(log_path) if not os.path.exists(log_path) else log_path
            self.log = get_simple_log(file_name=get_random_name(), path=log_path)
        self.log.info("浏览器最大化{}".format((datetime.now()).strftime('%Y-%m-%d %H:%M:%S %f')))
        self.driver.maximize_window()

    @staticmethod
    def pause(seconds):
        """
        操作上暂停指定时间（秒）
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    def open_url(self, url):
        """
        打开指定url
        :param url:
        :return:
        """
        self.log.info("打开URL:{}".format(url))
        self.driver.get(url)

    def get_element(self, element, wait_time=1):
        """
        等待并获取元素
        :param element:
        :param wait_time:
        :return:
        """
        return self.exist_element(element=element, wait_time=wait_time)

    def exist_element(self, element, wait_time=5):
        """
        检查元素是否存在
        :param element:
        :param wait_time:
        :return:
        """
        if isinstance(element, WebElement):
            try:
                _ = element.text
            except StaleElementReferenceException as e:
                return False
            else:
                return element
        else:
            try:
                el = WebDriverWait(self.driver, wait_time).until(
                    expected_conditions.presence_of_element_located(element))
                # el = WebDriverWait(self.driver, wait_time).until(PresenceElementLocated(element))
            except:
                return False
            else:
                return el

    def click_element(self, element):
        """
        通用点击方法
        :param element:
        :return:
        """
        self.log.info("点击元素:{}".format(element))
        element = self.get_element(element)
        element.click()

    def input_element(self, element, text):
        """
        通用输入方法
        :param element:
        :param text:
        :return:
        """
        element = self.get_element(element)
        element.clear()
        element.send_keys(text)

    def click_id(self, value):
        """
        点击目标id，需要提供id值
        :param value:
        :return:
        """
        self.get_element((By.ID, value)).click()

    def click_xpath(self, value):
        """
        点击目标xpath，需要提供xpath值
        :param value:
        :return:
        """
        self.get_element((By.XPATH, value)).click()

    def click_class(self, value):
        """
        点击目标class，需要提供class值
        :param value:
        :return:
        """
        self.get_element((By.XPATH, "//*[@class='{}']".format(value))).click()

    def click_text(self, text):
        """
        点击目标文本，需要提供文本值
        :param text:
        :return:
        """
        self.get_element((By.XPATH, "//*[text()='{}']".format(text))).click()

    def input_id(self, value, text):
        """
        根据目标id进行输入文本，需要提供id值和文本值
        :param value:
        :param text:
        :return:
        """
        self.input_element((By.ID, value), text)

    def input_xpath(self, value, text):
        """
        根据目标xpath进行输入文本，需要提供xpath值和文本值
        :param value:
        :param text:
        :return:
        """
        self.input_element((By.XPATH, value), text)

    def input_class(self, value, text):
        """
        根据目标class进行输入文本，需要提供class值和文本值
        :param value:
        :param text:
        :return:
        """
        self.input_element((By.CLASS_NAME, value), text)

    def get_attribute(self, element, attr):
        """
        获取目标元素的属性
        :param element:
        :param attr:
        :return:
        """
        return self.get_element(element).get_attribute(attr)

    def get_location(self, element):
        return self.get_element(element).location

    def select_last_window(self):
        """
        选择最后打开的窗口
        """
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def select_window(self, title=None, window_num=None):
        """
        根据窗口或标签页title进行切换，需要提供title值
        :param title:
        :param window_num:  窗口号
        :return:
        """
        windows = self.driver.window_handles
        if title:
            for window in windows:
                self.driver.switch_to.window(window)
                if self.driver.title == title:
                    break
        elif window_num:
            self.driver.switch_to.window(windows[window_num - 1])

    def into_frame(self, value):
        """
        进入frame
        :param value:
        :return:
        """
        self.driver.switch_to.frame(value)

    def into_parent_frame(self):
        """
        进入父frame
        :return:
        """
        self.driver.switch_to.parent_frame()

    def out_frame(self):
        """
        退出frame
        :return:
        """
        self.driver.switch_to.default_content()

    def double_click(self, by, value):
        """
        双击元素
        :param by:
        :param value:
        :return:
        """
        if not isinstance(by, By):
            if by == "id":
                by = By.ID
            elif by == "class":
                by = By.XPATH
                value = "//*[@class='{}']".format(value)
            else:
                by = By.XPATH
        self.action.double_click(self.driver.find_element(by, value)).perform()

    def move_over_to_element(self, element):
        """
        鼠标移动到指定元素上面
        :param element:
        :return:
        """
        self.action.move_to_element(self.get_element(element)).perform()

    def drag(self, source_element, target_element):
        """
        拖拽元素
        :param source_element:
        :param target_element:
        :return:
        """
        e1 = self.get_element(source_element)
        e2 = self.get_element(target_element)
        self.action.drag_and_drop(e1, e2).perform()

    def click_enter_key(self):
        """
        点击回车键
        :return:
        """
        self.action.send_keys(Keys.ENTER).perform()

    def assert_text(self, text):
        """
        断言文本
        :param text:
        :return:
        """
        self.get_element((By.XPATH, "//*[text()='{}']".format(text)))

    def assert_element_text(self, element, text):
        """
        断言某元素文本
        :param element:
        :param text:
        :return:
        """
        attr_text = self.ele_get_val(element)
        assert attr_text == text, '{}跟{}不相同'.format(attr_text, text)

    def quit(self):
        """
        退出selenium driver
        :return:
        """
        self.driver.quit()

    # class CommonDriver(WDriver):
    """
    csf 延伸扩展， 适配SC
    """

    @staticmethod
    def _split_mark(ele):
        ele_mark = None
        split_char = '|#'
        if isinstance(ele, str) and ele.count(split_char):
            ele, ele_mark = ele.split(split_char)
        return ele, ele_mark

    @staticmethod
    def _split_ele(ele):
        """
        拆解 控件元素组合
        :param ele:
        :return:
        """
        if isinstance(ele, WebElement):
            return ele
        ele, _ = WDriver._split_mark(ele)
        if isinstance(ele, str) and (ele.startswith('//') or ele.startswith('/html')):
            identity_ = By.XPATH
            ele_value = ele
        elif isinstance(ele, str) and (ele.startswith('.') or ele.startswith('#')):
            identity_ = By.CSS_SELECTOR
            ele_value = ele
        else:
            split_char = ele.index('=')
            ele_identity, ele_value = ele[:split_char], ele[split_char + 1:]
            ele_identity = ele_identity.strip('= ')
            ele_value = ele_value.strip('= ')
            if ele_identity.lower() == 'id':
                identity_ = By.ID
            elif ele_identity.lower() == 'name':
                identity_ = By.NAME
            elif ele_identity.lower() == 'class':
                identity_ = By.CLASS_NAME
            elif ele_identity.lower() == 'tag':
                identity_ = By.TAG_NAME
            elif ele_identity.lower() == 'css':
                identity_ = By.CSS_SELECTOR
            elif ele_identity.lower() == 'xpath':
                identity_ = By.XPATH
            elif ele_identity.lower() == 'link':
                identity_ = By.LINK_TEXT
            elif ele_identity.lower() == 'plink':
                identity_ = By.PARTIAL_LINK_TEXT
            else:
                raise Exception("元素书写格式错误, 未知识别符[{}]，元素[{}]".format(ele_identity, ele))
        ele_value = ele_value.split('|')[0]
        return identity_, ele_value

    def ele_assert_text(self, ele, text):
        actual_text = self.ele_get_val(ele)
        assert actual_text == text, '{}跟{}不相同'.format(actual_text, text)

    def ele_move(self, ele, timeout=2):
        """
        移动鼠标到某个控件处
        :param ele:
        :param timeout:
        :return:
        """
        # el = self.ele_visibility(ele, timeout=timeout)
        el = self.get_element(self._split_ele(ele), wait_time=timeout)
        webdriver.ActionChains(self.driver).move_to_element(el).perform()
        return el

    def exec_js(self, cmd=None):
        """
        执行js命令
        :param cmd: js/jquery命令
        :return:
        """
        if not cmd:
            cmd = "document.readyState"
        return self.driver.execute_script("return {}".format(cmd))

    def ele_get_(self, ele):
        """
        获取元素
        :param ele:控件元素组合
        :return: 元素
        """
        return self.get_element(self._split_ele(ele))

    def ele_get_val(self, ele, attr_name=None, all_flag=False, chk_visit=True, timeout=2):
        """
        获取控件值 或 某个属性
        :param ele:控件元素组合
        :param attr_name:属性名
        :param all_flag: 控件值和属性值都需要
        :param chk_visit: 判定 是否是可见元素，默认False不检查
        :return: 控件值 或 属性值
        """
        tmp_, ele_mark = self._split_mark(ele)
        if chk_visit:
            ele = self.ele_visibility(ele, timeout=timeout)
        else:
            ele = self.get_element(self._split_ele(ele), wait_time=timeout)  # 获取元素，不考虑是否可见
        if not ele:
            self.log.error("控件[{}]:元素[{}]不可见，获取值或属性失败".format(ele_mark, tmp_))
            return None
        if all_flag:
            if self.exist_element(ele):
                widget_value = ele.text or time.sleep(0.1) or ele.text or time.sleep(0.1) or ele.text
                attribute_value = ele.get_attribute(attr_name)
                return widget_value, attribute_value
            return None, None
        if attr_name:
            ele_attr = None
            if self.exist_element(ele):
                try:
                    ele_attr = ele.get_attribute(attr_name)
                except Exception:
                    ...
            return ele_attr
        else:
            widget_value = ele.text or time.sleep(0.1) or ele.text or time.sleep(0.1) or ele.text
            return widget_value

    def ele_input_base(self, ele, input_value=None, cln=0, enter=False, return_flag=True, **kwargs):
        """
        对控件 输入
        :param ele: 控件元素组合
        :param input_value: 输入值
        :param cln: 覆盖输入 或者  清理输入，默认覆盖输入
        :param enter: 输入完成回车
        :param return_flag: 是否返回输入值，默认返回
        :return: 返回当前控件的值
        """
        # tmp_ele = self.get_element(self._split_ele(ele))
        tmp_ele = self.ele_visibility(ele, timeout=3) if cln in [1, 0] else self.ele_exist(ele, timeout=3)
        if cln == 1:
            tmp_ele.send_keys(Keys.CONTROL, 'a')
            tmp_ele.send_keys(Keys.BACKSPACE)
        elif cln == 3:
            tmp_ele.send_keys(Keys.CONTROL, 'a')
        elif cln == 0:
            tmp_ele.clear()
        tmp_ele.send_keys(input_value)
        if enter:
            tmp_ele.send_keys(Keys.ENTER)
        if return_flag:
            return self.ele_get_val(ele, attr_name="value")

    def ele_list(self, ele, timeout=2):
        """
        获取同类型值列表
        :param ele: 控件元素组合
        :param timeout: 等待时间
        :return: 控件列表
        """
        tmp_, ele_mark = self._split_mark(ele)
        ele_type, ele_val = self._split_ele(ele)
        if self.ele_exist(ele, timeout=timeout):
            return self.driver.find_elements(ele_type, ele_val)
        else:
            self.log.warning("控件[{}]:[{}]无列表".format(ele_mark, tmp_))
            return None

    @shadow("判定元素是否存在")
    def ele_exist(self, ele, timeout=2, miss=False):
        """
        重写元素是否存在  exist_element
        :param ele:
        :param timeout:
        :param miss:
        :return:
        """
        tmp_, ele_mark = self._split_mark(ele)
        t_start = time.time()
        if miss:
            chk_ex = lambda: not self.exist_element(self._split_ele(ele), wait_time=timeout)
            value = ele if CF.loop_chk(expression=chk_ex, return_bool=True) else False
        else:
            # return ele if self.exist_element(self._split_ele(ele), wait_time=timeout) else False
            value = self.exist_element(self._split_ele(ele), wait_time=timeout)
        cost_time = time.time() - t_start
        print('judge element exist cost {}s, 控件[{}]:[{}]'.format(round(cost_time, 2), ele_mark, tmp_))
        # print('judge element exist cost {}'.format(time.time()-t_start))
        return value

    def ele_click_or_not(self, ele, timeout=2):
        """
        判定元素是否可以点击
        :param ele:
        :param timeout:
        :return:
        """
        tmp_, ele_mark = self._split_mark(ele)
        try:
            click_result = WebDriverWait(self.driver, timeout).until(ClickAbleEle(self._split_ele(ele)))
        except TimeoutException:
            click_result = False
            self.log.warning("控件[{}]:元素[{}]不可点击".format(tmp_, ele_mark))
        return click_result

    def ele_visibility(self, ele, timeout=2):
        try:
            result = WebDriverWait(self.driver, timeout).until(VisibilityEle(self._split_ele(ele)))
        except TimeoutException:
            result = False
        return result

    def scroll_page(self, ele, action='down'):
        """
        图片页，过多时，向下，向上滚动(请求数据)
        :param ele:
        :param action:
        :return:
        """
        if action == 'down':
            self.ele_input(ele, Keys.PAGE_DOWN, cln=2)
        elif action == 'up':
            self.ele_input(ele, Keys.PAGE_UP, cln=2)
        elif action == 'end':
            self.ele_input(ele, Keys.END, cln=2)
        elif action == 'home':
            self.ele_input(ele, Keys.HOME, cln=2)
        else:
            raise Exception("暂不支持此动作[{}]".format(action))

    def ele_wait(self, to=5):
        self.driver.implicitly_wait(to)

    def get_url(self):
        return self.driver.current_url

    # class WDriver(WDriver_BK):
    """
    csf 适配 SC
    """

    # def __init__(self, browser="chrome", log=None, time_out=10, test_desired=None, hub_url=None, **kwargs):
    #     super().__init__(browser=browser, log=log, time_out=time_out, test_desired=test_desired, hub_url=hub_url, **kwargs)

    def ele_upload(self, img_path, ele="css=.rz-upload__input[name=file]"):
        """
        图片上传，适用于当前页面只有一个上传入口 ，多个时不可以(如1:1)
        :param img_path:
        :param ele:
        :return:
        """
        self.ele_input(ele, img_path, cln=-1, return_flag=False)

    def get_alert_label(self, wait_miss=False, return_msg=False):
        """
        获取 成功/失败的弹出标签，如新建用户成功 etc
        :return:
        """
        time.sleep(0.3)
        alert_ele = "css=.rz-message"
        alert_el = self.ele_exist(alert_ele)
        if not alert_el:
            return False
        msg = self.ele_get_val(alert_el) or self.ele_get_val(alert_el)
        msg_status = self.ele_get_val(alert_el, attr_name='class')
        if wait_miss:
            self.ele_exist(alert_ele, miss=True)
        if 'error' in msg_status:
            self.log.warning("异常信息:{}".format(msg))
            return False if not return_msg else msg
        else:
            self.log.warning("正常信息:{}".format(msg))
            return msg

    def chk_loading(self, loading_to=3, loading_el=None):
        """
        检测 加载圈
        :param loading_to: 加载超时 默认5s
        :return:
        """
        loading_el = loading_el or "css=div.rz-loading-mask|#加载圈"
        t_start = time.time()
        # time.sleep(1)
        load_success_flag = -1
        load_flag = False
        # print("=====> loading")
        # if not (self.ele_exist(loading_el) and self.ele_exist(loading_el)):
        #     return
        load_lst = self.ele_list(loading_el)
        success_flag = False
        if not load_lst:
            # print("不存在")
            return False
        # new_load_lst = [x for x in load_lst if 'none' not in self.ele_get_val(x, 'style', chk_visit=False)]
        # print('has {} load circle'.format(len(load_lst)))
        for load_sub in load_lst:
            # print('>>'*5)
            while time.time() - t_start < loading_to:
                loading_attr = self.ele_get_val(load_sub, 'style', chk_visit=False)
                if loading_attr is None and load_flag:
                    # print('元素已不存在，可判定成功跳出')
                    success_flag = True
                    break
                elif isinstance(loading_attr, str) and 'none' in loading_attr:
                    if load_flag:
                        # print('状态为加载完成')
                        success_flag = True
                        break
                    else:
                        # print('状态为未加载')
                        break
                else:  # 状态为加载中
                    # print('状态为加载中')
                    load_flag = True
                    time.sleep(0.3)
            else:
                self.log.warning("发现有状态还在Loading中，已超过[{}]s".format(int(loading_to)))
            if success_flag:
                # print("加载检测完成，===成功返回")
                break
        print('\tTotal:{}s, load check {}'.format(round(time.time() - t_start, 2), success_flag))
        time.sleep(1)
        return load_success_flag

    def wid_drop_down(self, val, drop_down_ele=None):
        """
        针对SC的下拉框进行点击操作
        :param val: 下拉框值
        :param drop_down_ele: 点击可弹出下拉框的控件
        :return:
        """
        if drop_down_ele:
            self.ele_click(drop_down_ele)
        wid_ = "css=body>div:last-child li"
        for ele_ in self.ele_list(wid_):
            if val == self.ele_get_val(ele_):
                self.ele_click(ele_)
                return True
        else:
            return False

    def refresh_driver(self):
        """
        刷新当面页
        :return:
        """
        self.driver.refresh()
        self.chk_loading()
        time.sleep(0.2)

    def ele_click(self, ele, move=False, wait_time=2, load=False, **kwargs):
        """
        点击 控件元素组合
        :param ele:控件
        :param move: 是否需要移动鼠标
        :param wait_time:等待时间
        :param load:是否加载
        :return:
        """
        tmp_, ele_mark = self._split_mark(ele)
        retry_time = 0
        while retry_time < 2:
            retry_time += 1
            try:
                if move and not isinstance(move, bool):  # 关联型 需移动到move元素，ele才可以显示
                    move_ele = self.ele_exist(move, timeout=wait_time)
                    element = self.ele_exist(ele, timeout=wait_time)
                    # webdriver.ActionChains(self.driver).click(move_ele).move_to_element(element).click(element).perform()
                    webdriver.ActionChains(self.driver).move_to_element(move_ele).perform()
                    time.sleep(0.3)
                    element.click()
                    load and self.chk_loading()
                    return
                else:
                    element = self.ele_click_or_not(ele, timeout=wait_time)
                    # print(element)
                    if element and isinstance(element, WebElement):
                        if move:
                            webdriver.ActionChains(self.driver).move_to_element(element).click(element).perform()
                        else:
                            element.click()
                        load and self.chk_loading(loading_to=load if isinstance(load, int) else 2)
                        return element
                    else:
                        if not retry_time:
                            raise Exception("控件[{}]:元素[{}]不可点击".format(ele_mark, tmp_))
            except:
                # return False
                if not retry_time:
                    raise Exception("控件[{}]:元素[{}]点击{}次异常".format(ele_mark, tmp_, retry_time))
            time.sleep(1)
            print('Click fail, retry ..')
        else:
            raise Exception("控件[{}]:元素[{}]点击{}次异常".format(ele_mark, tmp_, retry_time))

    def ele_input(self, ele, input_value, cln=0, enter=False, load=False, return_flag=True, **kwargs):
        """
        对控件 输入
        :param ele: 控件元素组合
        :param input_value: 输入值
        :param cln: 1: 清理当前输入框，清理输入值时使用 3：覆盖当前输入框并输入 0：webDriver的覆盖输入
        :param enter: 输入完成回车
        :param load: 检测加载圈
        :param return_flag: 是否返回输入的值，默认返回
        :return: 返回当前控件的值
        """
        tmp_, ele_mark = self._split_mark(ele)
        rtn_el = None
        tmp_ele = self.ele_visibility(ele, timeout=3) if cln in [1, 0] else self.ele_exist(ele, timeout=3)
        if not tmp_ele:
            raise Exception("控件[{}]:元素[{}]不可以见".format(ele_mark, tmp_))
        if cln == 1:
            tmp_ele.send_keys(Keys.CONTROL, 'a')
            tmp_ele.send_keys(Keys.BACKSPACE)
        elif cln == 3:
            tmp_ele.send_keys(Keys.CONTROL, 'a')
        elif cln == 0:
            tmp_ele.clear()
        tmp_ele.send_keys(input_value)
        if enter:
            tmp_ele.send_keys(Keys.ENTER)
        if return_flag:
            rtn_el = self.ele_get_val(ele, attr_name="value")
        load and self.chk_loading(loading_to=load if isinstance(load, int) else 2)
        return rtn_el


from selenium.webdriver.support.expected_conditions import _element_if_visible, _find_element, \
    StaleElementReferenceException


class ClickAbleEle(object):
    """ An Expectation for checking an element is visible and enabled such that
    you can click it."""

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = VisibilityEle(self.locator)(driver)
        if element and element.is_enabled():
            return element
        else:
            return False


class VisibilityEle(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            if isinstance(self.locator, WebElement):
                return _element_if_visible(self.locator)
            return _element_if_visible(_find_element(driver, self.locator))
        except StaleElementReferenceException:
            return False


class PresenceElementLocated(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        # return _find_element(driver, self.locator)
        try:
            # if isinstance(self.locator, WebElement):
            #     return _element_if_visible(self.locator)
            return _find_element(driver, self.locator)
        except:
            return False
