#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib,sys
importlib.reload(sys)
"""
__title__ = ''
__author__ = '86188'
__mtime__ = '2021/12/24'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.

"""
"""这是第一个robot framework调用python脚本的demo"""
class mytool():
    def __init__(self):
        pass
    def whomax(self,a,b):
        if a>=b:
            return a
        else:
            return b

    def writeInTxt(self,filePathName,content,way):
        #写入文件，提供文件名称
        """
        :param ``filePathName``:提供文件路径和名称如（test.txt）
        :param ``content``:提供写入内容
        :param ``way``:提供保存方式，`w`写入之前清空文本内容，`a`追加写入
        """
        with open (filePathName,way) as file_n:
            file_n.write(content)
            file_n.close()
