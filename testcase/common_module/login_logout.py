#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import ddt
import logging
from lib.utils import capture_screen
from config import *
from lib.common_logic import get_driver, login_by_admin


@ddt.ddt
class Login(unittest.TestCase):
    """
    RanZhi 用户登陆
    """
    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    @ddt.unpack
    @ddt.data(*test_data)
    def test_user_login_test(self, admin, password, flag):
        """admin的登录的所有测试用例
        测试用例在讲一个故事：
        1.条件是什么？
        2.做了哪些操作？
        3.出现了什么结果？
        """
        logging.info("test_admin_login_test start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys(admin)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        self.assertIn(flag, driver.page_source)
        logging.info("test data is : {}, {}, {}".format(admin, password, flag))
        capture_screen(driver)
        logging.info("test_user_login_test end....")

    if __name__ == '__main__':
        unittest.main()