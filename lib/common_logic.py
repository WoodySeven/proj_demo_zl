#!/usr/bin/env python
import time

from config import *
from selenium import webdriver


def get_driver():
    """获取driver对象"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    return driver


def login_by_admin(driver):
    """管理员登录"""
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(ADMIN_ACCOUNT['account'])
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(ADMIN_ACCOUNT['password'])
    driver.find_element_by_id("submit").click()


def click_all_apps(driver):
    """点击所有应用"""
    driver.find_element_by_xpath("//*[@id=\"s-menu-allapps\"]/button").click()
    time.sleep(3)


def click_crm_btn(driver):
    """点击客户管理"""
    driver.find_element_by_xpath("//*[@id=\"s-applist-1\"]/a/img").click()
    time.sleep(3)
    ##进入ifarme


def switch_to_frame(driver, frame_name = 'iframe-1'):
    driver.switch_to.frame('iframe-1')
    time.sleep(3)
    ##新增客户
    driver.find_element_by_link_text("客户").click()
    driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()  ##点击添加客户
    driver.find_element_by_id("name").send_keys(random.randint(1000, 9999))  ##输入名称
    driver.find_element_by_id("contact").send_keys(random.choice('abcdefghjklqwertyuiomnbvcxz'))  ##输入联系人
    driver.find_element_by_id("phone").send_keys(random.randint(10000000000, 99999999999))  ##输入电话
    driver.find_element_by_id("email").send_keys("{}@qq.com".format(random.randint(1000, 9999)))  ##输入邮箱
    driver.find_element_by_id("qq").send_keys(random.randint(1000, 9999))  ##输入qq
    driver.find_element_by_id("type").click()  ##选择类型
    driver.find_element_by_xpath('//*[@id="type"]/option[2]').click()
    time.sleep(5)
    driver.find_element_by_id("size").click()  ##选择规模
    driver.find_element_by_xpath('//*[@id="size"]/option[2]').click()
    driver.find_element_by_id("level").click()  ##选择级别
    driver.find_element_by_xpath('//*[@id="level"]/option[2]').click()
    driver.find_element_by_id('intension').send_keys("客户意向非常大")  ##购买意向输入
    driver.find_element_by_id("submit").click()  ##点击保存