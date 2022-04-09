# -*- coding: utf-8 -*-
"""
2、DES

 1)简介

DES算法为密码体制中的对称密码体制，又被称为美国数据加密标准。

DES是一个分组加密算法，典型的DES以64位为分组对数据加密，加密和解密用的是同一个算法。

DES算法的入口参数有三个：Key、Data、Mode。其中Key为7个字节共56位，是DES算法的工作密钥；Data为8个字节64位，是要被加密或被解密的数据；Mode为DES的工作方式,有两种:加密或解密。

密钥长64位，密钥事实上是56位参与DES运算（第8、16、24、32、40、48、56、64位是校验位，使得每个密钥都有奇数个1），分组后的明文组和56位的密钥按位替代或交换的方法形成密文组。

算法步骤
1）初始置换
其功能是把输入的64位数据块按位重新组合,并把输出分为L0、R0两部分,每部分各长3 2位,其置换规则为将输入的第58位换到第一位,第50位换到第2位……依此类推,最后一位是原来的第7位。L0、R0则是换位输出后的两部分，L0是输出的左32位,R0是右32位,例:设置换前的输入值为D1D2D3……D64,则经过初始置换后的结果为:L0=D58D50……D8;R0=D57D49……D7。
其置换规则见下表：
58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,
2）逆置换
经过16次迭代运算后,得到L16、R16,将此作为输入,进行逆置换,逆置换正好是初始置换的逆运算，由此即得到密文输出。
此算法是对称加密算法体系中的代表,在计算机网络系统中广泛使用.
————————————————
版权声明：本文为CSDN博主「阿紫_PP」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ruanxingzi123/article/details/83017575
"""
# -*- coding:UTF-8 -*-
__author__ = 'rxz'

# 导入DES模块
from Cryptodome.Cipher import DES
import binascii

# 这是密钥,此处需要将字符串转为字节
key = b'abcdefgh'


# 需要去生成一个DES对象
def pad(text):
    """
      # 加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
       :param text:
       :return:
    """
    while len(text) % 8 != 0:
        text += ' '
    return text


# 创建一个DES实例
des = DES.new(key, DES.MODE_ECB)
text = "I'm china!"
padded_text = pad(text)
print(padded_text)
# 加密
encrypted_text = des.encrypt(padded_text.encode("utf-8"))
print(encrypted_text)
# rstrip(' ')返回从字符串末尾删除所有字符串的字符串(默认空白字符)的副本

# 解密
plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')
print(plain_text)

"""
I'm china!      
b'\xc0`I\x15\x8bo\x00\x00\xb0\xe27\xfe)\xc3\xde,'
I'm china!
"""

# -*- coding:UTF-8 -*-


# 导入DES模块
from Cryptodome.Cipher import DES
import binascii

# 这是密钥
key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new(key, DES.MODE_ECB)
# 需要加密的数据
text = 'python spider!'
text = text + (8 - (len(text) % 8)) * '='
# 加密的过程
encrypto_text = des.encrypt(text.encode())
# 加密过后二进制转化为ASCII
encrypto_text = binascii.b2a_hex(encrypto_text)
print(encrypto_text)
# 解密需要ASCII 先转化为二进制 然后再进行解密
plaint = des.decrypt(binascii.a2b_hex(encrypto_text))
print(plaint)

"""
b'084725d8f5ffafc61814fae0796bfd2f'
b'python spider!=='
"""




