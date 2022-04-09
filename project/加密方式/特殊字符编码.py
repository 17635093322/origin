# -*- coding: utf-8 -*-

# 常见情况下，代码中，参数当中和URL当中可能会出现特殊字符
# 例如：
# 避免url中出现特殊字符（如汉字）的编码方式。其实就是将超出ASCII范围的字符转换成带%的十六进制格式。

from urllib import parse


a = parse.quote('中国欢迎你')
print(a)

b = parse.unquote(a)
print(b)
