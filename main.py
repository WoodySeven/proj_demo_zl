#!/usr/bin/env python  
""" 
@author:Administrator 
@file: main.py 
@time: 2018/01/07 
"""
import HTMLTestRunner
import unittest
import logging
import time
import traceback
from lib.Logger import Logger
from testcase.cases_login_logout.admin_login_logout import BugFree管理员登录退出


if __name__ == "__main__":
    logger = Logger('./log/logger.log', logging.INFO)
    logging.info("本次测试开始执行，以下是详细日志:")
    try:
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(BugFree管理员登录退出))
        # suite.addTest(loader.loadTestsFromTestCase(BugFree管理员登录退出))
        # suite.addTest(loader.loadTestsFromTestCase(BugFree管理员登录退出))

        #unittest.TextTestRunner(verbosity=2).run(suite)
        fp = open('reports/report_bugfree_{0}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")), 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Bugfree的测试报告',
            description='Bugfree的所有测试用例执行细节'
        )
        runner.run(suite)
        logging.info("测试顺利结束！")
    except Exception:
        """traceback模块是为了获取详细的异常信息，
        print_exc() 把异常输出到屏幕上，而format_exc() 把异常返回成字符串"""
        traceback.print_exc()
        logging.error(traceback.format_exc())
        logging.error("测试异常终止")
    finally:
        if fp is not None:
            fp.close()