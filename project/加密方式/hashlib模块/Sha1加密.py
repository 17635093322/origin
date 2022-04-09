# -*- coding: utf-8 -*-
"""
7、sha1 加密

SHA1的全称是Secure Hash Algorithm(安全哈希算法) 。SHA1基于MD5，加密后的数据长度更长，

它对长度小于264的输入，产生长度为160bit的散列值。比MD5多32位。

因此，比MD5更加安全，但SHA1的运算速度就比MD5要慢了。
————————————————
版权声明：本文为CSDN博主「阿紫_PP」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ruanxingzi123/article/details/83017575
"""
import hashlib


a = hashlib.sha1('中国你好'.encode()).hexdigest()
print(a)
