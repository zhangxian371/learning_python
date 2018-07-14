#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 指定源文件的编码格式是utf-8

# utf 是utf-8编码字符串
utf = 'hello, 冒险者，我是穆，请问你是？'
print utf

name = raw_input('请输入你的名字：')
print '%s你好，真是个不错的名字，欢迎来到%s' % (name, '法兰城')