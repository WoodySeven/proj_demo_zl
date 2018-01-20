#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import logging
from lib.utils import capture_screen

class CashExpenditure(unittest.TestCase):
    """
    测试现金记账支出页面
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

    def test_cash_expenditure(self):
        """现金记账支出测试用例"""
        logging.info("test_cash_expenditure start....")
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        ##现金记账
        driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="s-applist-3"]/a').click()
        time.sleep(5)
        ##进入ifarme
        driver.switch_to.frame("iframe-3")
        time.sleep(5)
        ##点击支出
        driver.find_element_by_xpath('//*[@id="mainNavbar"]/div[2]/ul/li[4]/a').click()
        ##点击记支出
        driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
        time.sleep(3)
        driver.find_element_by_id('depositor').click()##选择账号
        driver.find_element_by_xpath('//*[@id="depositor"]/option[2]').click()
        driver.find_element_by_id('category').click()##选择科目
        driver.find_element_by_xpath('//*[@id="category"]/option[2]').click()
        driver.find_element_by_id('objectType2').click()##选择订单支出
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="order_chosen"]/a').click()##选择订单
        driver.find_element_by_xpath('//*[@id="order_chosen"]/div/ul/li[1]').click()
        time.sleep(2)
        driver.find_element_by_id('money').clear()##清空金额
        driver.find_element_by_id('money').send_keys(random.randint(3211,5462))##输入金额
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()##选择经手人
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
        driver.find_element_by_id('desc').send_keys('我们我们啊哈哈')##输入说明
        driver.find_element_by_id('submit').click()##保存
        time.sleep(3)
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_cash_expenditure end....")
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()