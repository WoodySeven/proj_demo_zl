#!/usr/bin/env python  
""" 
@author:Administrator 
@file: main.py 
@time: 2018/01/07 
"""
import HTMLTestRunner
import unittest

import time

from testcase.cases_login_logout.admin_login_logout import BugFree管理员登录退出


if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(BugFree管理员登录退出))
    #unittest.TextTestRunner(verbosity=2).run(suite)
    fp = open('reports/report_bugfree_{0}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Bugfree的测试报告',
        description='Bugfree的所有测试用例执行细节'
    )
    runner.run(suite)
    fp.close()