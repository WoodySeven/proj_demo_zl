#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import logging
from lib.utils import capture_screen


class CreateMember(unittest.TestCase):
    """
    测试新增成员页面
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

    def test_create_member(self):
        """添加成员测试用例"""
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
        ##用户名
        driver.find_element_by_id('account').send_keys("{0}{1}".format(random.choice('abcdefghjklqwertyuiomnbvcxz'),random.randint(1000,9999)))
        ##真实姓名
        driver.find_element_by_id('realname').send_keys(random.choice('abcdefghjklqwertyuiomnbvcxz'))
        driver.find_element_by_id('gender2').click()##选择性别
        driver.find_element_by_id('dept').click()##选择部门
        driver.find_element_by_xpath('//*[@id="dept"]/option[2]').click()
        driver.find_element_by_id('role').click()##选择角色
        driver.find_element_by_xpath('//*[@id="role"]/option[3]').click()
        driver.find_element_by_id('password1').send_keys('123456')##输入密码
        driver.find_element_by_id('password2').send_keys('123456')##再一次输入密码
        ##输入邮箱
        driver.find_element_by_id('email').send_keys("{}@qq.com".format(random.randint(1000,9999)))
        driver.find_element_by_id('submit').click()##点击保存
        time.sleep(6)
        ##删除成员信息
        # driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[11]/a[3]').click()
        # time.sleep(2)
        # alert = self.driver.switch_to.alert##获取警示框
        # alert.accept()##点击确认
        # time.sleep(3)
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_create_member end....")


if __name__ == '__main__':
    unittest.main()
