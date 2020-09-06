# -*- coding: utf-8 -*-
import time


class LoginPage:

    @staticmethod
    def login_password(driver, username, password):
        """
        首页登录，需要传入参数：用户名, 密码
        username:用户名
        password:用户密码
        """
        driver.click_class("rz-button rz-button--text type-button password")
        driver.input_xpath("//*[@class='login-item-input rz-input rz-input--suffix']/input[@class='rz-input__inner'][@type='text']", username)
        # driver.input_xpath("//input[@placeholder='请输入用户名']", username)
        driver.input_xpath("//*[@class='login-item-input rz-input rz-input--suffix']/input[@class='rz-input__inner'][@type='password']", password)
        # driver.input_xpath("//input[@placeholder='请输入密码']", username)
        driver.click_class("rz-button login-btn rz-button--primary")
