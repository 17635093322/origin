# -*- encoding: utf-8 -*-
import os

"""

一.文件备份基础思路
    读取文件
    写入新文件
    
二.文件备份进阶思路
    读取文件
    
    考虑指定保存位置
        指定的是文件  ---- 直接写入
            or
        指定的是目录  ---- 构建新名称 --- 拼接保存路径 --- 写入数据


三.文件备份 完整思路

    # 注意指定你自己存在的文件路径，包括指定的目录也是
    
    Backup类
        方法1： 初始化 --- __init__
                    原文件路径 path -必备参数
                    保存路径 new_path -默认参数
                  
                  
        方法2： 读取文件      ---- read_data方法
        方法3： 写入文件数据   ---- write_data方法
        
        方法4： 构建新的保存名 ---- new_name方法 (构建保存路径及文件名)
                    1.获取原文件名（根据self.path）
                    2.根据文件名的 '.'进行切割 得到 文件名 及 文件后缀名
                    3.重新构造 拼接文件名
                    4.判断 self.new_path 是否 是否有数据 （注意：None在判断中其布尔值形为False, 非空字符串在判断中其布尔值形为True）
                         存在数据就拼接路径并返回
                         不存在就直接返回新的文件名 
                            
                
        
        方法5： 写入文件逻辑   ---- write_file方法
                    1.判断是否指定了保存路径
                       指定了：
                           判断指定目录/文件是否存在 -- 不存在就提示并结束
                           判断指定的是否是文件
                               指定的是文件 --- 无需处理
                               指定的是目录 --- 调用new_name方法构建保存路径及文件名，并重新赋值给self.new_path
                       没有指定：
                           调用new_name方法构建保存文件名，并重新赋值给self.new_path       
                               
                    2. 写入数据（write_data方法）           
        
        
        方法6： 启动方法      ---- run方法
                    读取数据（read_data方法）
                    写入文件（write_file方法）


"""


class Backup():
    def __init__(self, path, new_path=None):
        # 原文件路径
        self.path = path
        # 保存路径
        self.new_path = new_path
        # 文件数据
        self.file_data = None

    def read_data(self):
        """
            读取文件数据
        :return: 无返回值
        """
        # 判断文件/目录 是否存在
        if not os.path.exists(self.path):
            print('文件找不到， 请检查路径是否正确')
            return None
        # 读取文件
        with open(self.path, 'r', encoding='utf-8') as f:
            self.file_data = f.readlines()

    def write_data(self, file_path):
        """
            将数据写入文件
        :param file_path: 指定写入的文件
        :return:
        """
        # 判断文件/目录 是否存在
        if not os.path.exists(self.path):
            print('文件找不到， 请检查路径是否正确')
            return None
        with open(file_path, 'w', encoding='utf-8') as f1:
            f1.writelines(self.file_data)

    def new_name(self):
        """
            根据 文件名 构建 新的文件名
        :return:
        """
        # 获取原文件名
        old_name = os.path.basename(self.path)
        # 构建新名
        # 切割字符串
        name_list = old_name.split('.')
        # 构建新名称
        new_name = name_list[0] + '【备份】.' + name_list[-1]
        # 判断是否指定了路径
        if self.new_path:
            # 指定了就构建新路径
            return os.path.join(self.new_path, new_name)
        else:
            # 没指定就直接返回新名称
            return new_name

    def write_file(self):
        """
            写入数据
        :return:
        """
        # 判断是否指定了保存位置
        if self.new_path:
            # 指定了保存位置
            # 判断文件/目录 是否存在
            if not os.path.exists(self.new_path):
                print('保存路径指定有误，请检测后重新操作')
                return None
            # 判断是否 是 文件
            if not os.path.isfile(self.new_path):
                # 不是文件，那么就是文件夹（目录）
                # 重构名称，构建新名
                self.new_path = self.new_name()
        else:
            # 没指定 就 默认 当前位置 同级位置保存
            self.new_path = self.new_name()

        # 写入备份数据
        self.write_data(self.new_path)

    def run(self):
        # 读取数据
        self.read_data()
        # 写入文件数据
        self.write_file()


if __name__ == '__main__':
    # 注意指定你自己存在的文件路径，包括指定的目录也是
    backup = Backup('../study/demo1/stupython.py')
    # backup = Backup('../study/demo1/stupython.py', 'DF')
    backup.run()


