# -*- coding: utf-8 -*-

"""
四、MD5（信息-摘要算法）
1、简述

message-digest algorithm 5（信息-摘要算法）。经常说的“MD5加密”，就是它→信息-摘要算法。

md5，其实就是一种算法。可以将一个字符串，或文件，或压缩包，执行md5后，就可以生成一个固定长度为128bit的串。这个串，基本上是唯一的。

2、不可逆性

每个人都有不同的指纹，看到这个人，可以得出他的指纹等信息，并且唯一对应，但你只看一个指纹，是不可能看到或读到这个人的长相或身份等信息。

3、特点

压缩性：任意长度的数据，算出的MD5值长度都是固定的。
容易计算：从原数据计算出MD5值很容易。
抗修改性：对原数据进行任何改动，哪怕只修改1个字节，所得到的MD5值都有很大区别。
强抗碰撞：已知原数据和其MD5值，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。
举个栗子：世界上只有一个我，但是但是妞却是非常非常多的，以一个有限的我对几乎是无限的妞，所以可能能搞定非常多（100+）的妞，这个理论上的确是通的，可是实际情况下....
————————————————
版权声明：本文为CSDN博主「阿紫_PP」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ruanxingzi123/article/details/83017575
"""


"""
import hashlib
# 待加密信息
str = '中国你好'

# 创建md5对象，
# md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
hl = hashlib.md5()

# 要对哪个字符串进行加密，就放这里
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode())

print('MD5加密前为 ：' + str)
# hl.hexdigest()) #拿到加密字符串
print('MD5加密后为 ：' + hl.hexdigest())

"""

"""

hash3 = hashlib.md5(bytes('abd', encoding='utf-8'))
''' 
如果没有参数，所以md5遵守一个规则，生成同一个对应关系，如果加了参数，
就是在原先加密的基础上再加密一层，这样的话参数只有自己知道，防止被撞库，
因为别人永远拿不到这个参数
'''
hash3.update(bytes("admin", encoding="utf-8"))
print(hash3.hexdigest())  # 9aea3c0a6c51555c1a4d0a5e9b689ded
"""
import hashlib
hl = hashlib.md5()

hl.update('中国你好'.encode())
str_1 = hl.hexdigest()
print(str_1)

