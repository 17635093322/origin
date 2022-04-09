# -*- coding: utf-8 -*-
"""
# b2a类似于编码 / a2b类似于解码

binascii.a2b_uu(string)

binascii.b2a_uu(data)

binascii.a2b_base64(string)

binascii.b2a_base64(data)

binascii.a2b_qp(string[, header])

binascii.b2a_qp(data[, quotetabs, istext, header])

binascii.a2b_hqx(string)

binascii.rledecode_hqx(data)

binascii.rlecode_hqx(data)

binascii.b2a_hqx(data)

binascii.crc_hqx(data, crc)

binascii.crc32(data[, crc])

binascii.b2a_hex(data)

binascii.b2a_hex(data)

binascii.hexlify(data)

binascii.a2b_hex(hexstr)

binascii.unhexlify(hexstr)

异常有：

exception binascii.Error

exception binascii.Incomplete

"""
import binascii


# binascii模块 --- binascii模块包含很多在二进制和ASCII编码的二进制表示转换的方法
# 通常情况不会直接使用这些功能，而是使用像UU，base64编码，或BinHex封装模块。
a = binascii.b2a_hex('中国欢迎你'.encode())
print(a)

b = binascii.a2b_hex(a)
print(b)
print(b.decode())

