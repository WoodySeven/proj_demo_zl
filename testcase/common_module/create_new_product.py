#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import ddt
import logging
from lib.utils import capture_screen


class CreateNewProduct(unittest.TestCase):
    """
    测试新增产品页面
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

    def test_create_new_products(self):
        """新建产品测试用例"""
        logging.info("test_create_new_products start....")
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
        ##进入ifarme
        driver.switch_to.frame('iframe-1')
        time.sleep(5)
        ##新增产品
        driver.find_element_by_link_text("产品").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()##点击新增产品
        driver.find_element_by_id("name").send_keys(random.randint(1000, 9999))##输入名称
        time.sleep(3)
        ##输入产品
        driver.find_element_by_id("code").send_keys( "{0}{1}".format(random.choice('abcdefghjklqwertyuiomnbvcxz'), random.randint(1000, 9999)))
        time.sleep(3)
        driver.find_element_by_id("line").click()##选择产品线
        time.sleep(3)
        driver.find_element_by_id("type").click()##选择类型
        driver.find_element_by_xpath('//*[@id="type"]/option[2]').click()
        driver.find_element_by_id("status").click()##选择状态
        driver.find_element_by_xpath('//*[@id="status"]/option[2]').click()
        driver.find_element_by_id('submit').click()##点击保存
        time.sleep(3)
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_create_new_products end....")

if __name__ == '__main__':
    unittest.main()
