#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import ddt
import logging
from lib.utils import capture_screen


class CreateNewOrder(unittest.TestCase):
    """
    测试新增订单页面
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/ranzhi/www/sys/admin/"
        driver = self.driver

    def tearDown(self):
        self.driver.quit()

    def test_create_new_order(self):
        """新增订单测试用例"""
        logging.info("test_create_new_order start....")
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        ##点击所有应用，点击客户管理
        driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"s-applist-1\"]/a/img").click()
        time.sleep(3)
        ##进入iframe
        driver.switch_to.frame('iframe-1')
        time.sleep(5)
        ##新增订单
        driver.find_element_by_link_text("订单").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()##创建订单
        driver.find_element_by_xpath('//*[@id="customer_chosen"]/a').click()##选择客户
        driver.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/ul').click()##选择产品
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li[3]').click()
        driver.find_element_by_id('plan').send_keys(random.randint(2123,6454))##输入计划金额
        time.sleep(5)
        driver.find_element_by_id('submit').click()##点击保存
        time.sleep(5)
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("ttest_create_new_order end....")


if __name__ == '__main__':
    unittest.main()