#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import ddt
import logging
from lib.utils import capture_screen
from lib.common_logic import get_driver, login_by_admin
from config import *


class CreateNewClients(unittest.TestCase):
    """
    测试新增客户页面
    """
    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = get_driver()
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_create_new_clients(self):
        """新建客户测试用例"""
        logging.info("test_create_new_clients start....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        time.sleep(3)

        time.sleep(5)
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_create_new_clients end....")

if __name__ == '__main__':
    unittest.main()