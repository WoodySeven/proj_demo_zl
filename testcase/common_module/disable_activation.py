#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import logging
from lib.utils import capture_screen


class DisableActivation(unittest.TestCase):
    """
    测试禁用、激活成员页面
    """

    def setUp(self):
        """开始打开谷歌浏览器"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/ranzhi/www/sys/admin/"
        driver = self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭浏览器成功")

    def test_disable_activation(self):
        """禁用成员、激活成员测试用例"""
        logging.info("test_create_member start....")
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        ##点击后台管理
        driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
        time.sleep(3)
        ##进入ifarme
        driver.switch_to.frame('iframe-superadmin')
        time.sleep(5)
        ##点击添加成员
        driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()
        ##选择研发部门
        driver.find_element_by_xpath('//*[@id="category5"]').click()
        ###禁用成员
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[2]').click()
        time.sleep(5)
        ###激活成员
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[2]').click()
        time.sleep(5)
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_MemberConfiguration_test end....")


if __name__ == '__main__':
    unittest.main()