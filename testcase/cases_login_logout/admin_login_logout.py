#!/usr/bin/env python  
""" 
@author:Administrator 
@file: admin_login_logout.py.py 
@time: 2018/01/07 
"""  
import unittest
import time
import ddt
from selenium import webdriver

test_data = [['admin', '123456', '退出'],
             ['invalid', '123455', '用户名不存在'],
             ['', '123456', '不可为空白']]


@ddt.ddt
class BugFree管理员登录退出(unittest.TestCase):
    """
    演示的是Bugfree的登录和退出
    数据驱动，相同逻辑使用不同的数据去运行
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.2.87"
        driver = self.driver

    def tearDown(self):
        pass

    @ddt.unpack
    @ddt.data(*test_data)
    def test_admin_login_test(self, admin, password, flag):
        """admin的登录的所有测试用例"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys(admin)
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys(password)
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.assertIn(flag, driver.page_source)