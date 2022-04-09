# -*- coding: utf-8 -*-

"""
前言：
加密都是针对二进制进行的，对应到python当中就是Bytes
加密操作的时候必须确保数据是Bytes
字符串和Bytes互相转换用的是encode() / decode()

两位十六进制常常用来显示一个二进制字节

"""

# 不填写默认utf-8
a = '中国欢迎你'.encode()
print(a)
b = a.decode()
print(b)

