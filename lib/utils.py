#!/usr/bin/env python  
""" 
@author:Administrator 
@file: utils.py.py 
@time: 2018/01/07 
"""  
import os
import shutil
import time

def copy_file(src, dest):
    """拷贝文件到指定目录，src拷贝到dest"""
    if not os.path.exists(src):
        raise OSError
    shutil.copyfile(src, dest)

def capture_screen(driver,file_name=None):
    """对浏览器内部截图
    file_name是图片名
    如果成功，返回路径，如果不成功，返回None
    """
    pic_path = "./screenshots/mypic_{}.png".format(time.strftime("%Y-%m-%d %H-%M-%S"))
    if file_name is None:
        driver.get_screenshot_as_file(pic_path)
    else:
        driver.get_screenshot_as_file(file_name)
        pic_path = file_name
    if os.path.exists(pic_path):
        return pic_path