#!/usr/bin/env python  
""" 
@author:Administrator 
@file: ddt_demo.py 
@time: 2018/01/07 
"""  
#!/usr/bin/env python
# author: samren
import unittest

import ddt
L=[['1','2','3'],['a','b','c']]

def 遍历(var,*B):
    print(var)
    print(type(B))
    for i in B:
        print(i)


# 装饰器，接受一个对象，最后返回一个对象
@ddt.ddt
class demo_ddt(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.unpack
    @ddt.data(*L)   # * 是不定长参数的意思
    def test_aaaa(self, a, b, c):
        print(a, b, c)

if __name__ == "__main__":
    unittest.main()