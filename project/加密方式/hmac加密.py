# -*- coding: utf-8 -*-
import hmac

"""
python中还有一个hmac模块，它对我们创建key和内容再进行处理然后再加密

该模块加密是先把数据存储到字典中，然后再进行加密，方法与上述方法类似。
"""


# hm = hmac.new(b'abc')
hm = hmac.new('中国你好'.encode(encoding='utf-8'),b'bads')
print(hm.digest())
print(hm.hexdigest())
