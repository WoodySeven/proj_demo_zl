#!/usr/bin/env python
import unittest
import time
from selenium import webdriver
import random
import logging
from lib.utils import capture_screen


class CashIncome(unittest.TestCase):
    """
    测试现金记账收入页面
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

    def test_cash_income(self):
        """现金记账收入测试用例"""
        logging.info("test_cash_income start....")
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
        ##点击收入
        driver.find_element_by_xpath('//*[@id="mainNavbar"]/div[2]/ul/li[3]/a').click()
        time.sleep(5)
        ##点击记收入
        driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
        driver.find_element_by_id('depositor').click()##选择账号
        driver.find_element_by_xpath('//*[@id="depositor"]/option[2]').click()
        driver.find_element_by_id('category').click()##选择科目
        driver.find_element_by_xpath('//*[@id="category"]/option[2]').click()##选择客户
        driver.find_element_by_xpath('//*[@id="trader_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="trader_chosen"]/div/ul/li[1]').click()##选择合同
        time.sleep(2)
        driver.find_element_by_id('money').send_keys(random.randint(3213,4455))##输入金额
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()##选择经手人
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/a').click()##选择产品
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li[1]').click()
        time.sleep(5)
        driver.find_element_by_id('date').click()##选择时间
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/thead/tr[1]/th[2]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/table/thead/tr/th[1]/i').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/table/tbody/tr/td/span[5]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[3]/td[4]').click()
        time.sleep(5)
        driver.find_element_by_id('desc').send_keys('白日依山尽，黄河入海流')##输入说明
        time.sleep(2)
        #driver.find_element_by_name('files[]').click()
        driver.find_element_by_id('submit').click()##保存
        logging.info("test data is : {},{}".format('admin', '123456'))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_cash_income end....")
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()