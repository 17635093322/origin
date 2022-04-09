# -*- coding: utf-8 -*-
import emoji
import pymysql
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import re


class Spider(object):
    def __init__(self):
        """
        警告，本文中所有的睡眠都是有必要的，根据自己的网络情况调整
        """
        # 自动化对象实例化
        ua = UserAgent().random
        options = Options()
        # 添加随机ua
        options.add_argument(f'user-agent={ua}')
        # 添加IP代理
        # options.add_argument('--proxy-server=http://IP地址')
        self.browser = webdriver.Chrome(options=options)
        # self.browser = webdriver.Edge(options=options)
        self.db = pymysql.connect(user='root', password='admin', database='spider', charset='utf8')
        self.cursor = self.db.cursor()

    def login(self):
        # 基本页
        self.browser.get('https://huodong.ctrip.com/things-to-do/list?')
        time.sleep(5)
        # 点击登录
        # self.browser.find_element(By.XPATH, '//*[@id="nav-bar-set-login-person-text"]/span').click()
        # time.sleep(5)
        # 点击勾选协议
        # self.browser.find_element(By.XPATH, '//*[@id="normalview"]/p/input').click()
        # time.sleep(10)
        # 点击登录微信 ---------------------------------------------------------------------------------------------需要扫码
        # self.browser.find_element(By.XPATH, '//*[@id="loginbanner"]/div[2]/a[5]').click()
        # time.sleep(10)
        # 切换地方
        self.browser.find_element(By.XPATH, '//*[@id="act-10650038368-top-getcity-2-0"]').click()
        time.sleep(5)
        # 点击地方
        self.browser.find_element(By.XPATH, '//*[@id="ottd-smart-platform"]/section/div/div[2]/div[2]/div/div[2]/div/div/div/div[4]/div/div[1]/div/div[2]/div[1]/span').click()
        # 睡眠5秒
        time.sleep(5)
        i = 1
        # ======================================================进入翻页死循环============================================================
        while True:
            # ======================================================异常捕捉======================================================
            try:
                print(f'正在下载第{i}页的景点')
                html_data = self.browser.page_source
                xml_data = etree.HTML(html_data)
                # 提取页面元素
                for page_total in xml_data.xpath('//div[@class="m_productcard_container"]//a/@href'):
                    page = 'https:' + page_total
                    # 对页面景点源码进行解析
                    self.get_data(page)
                    # 解析完成提示语
                    # print('景点加载完毕')
                    time.sleep(2)
                    # print('==' * 60)
                # 进行翻页
                time.sleep(5)
                self.browser.find_element(By.XPATH, '//*[@id="ottd-smart-platform"]/section/div/div[3]/div[2]/div[2]/div/div[8]/i').click()
                # 睡眠5秒
                time.sleep(5)
                i += 1
            except:
                # 翻页循环异常后结束循环
                print('所有信息加载完毕')
                break

    def get_data(self, page_url):
        # 景点基本页
        self.browser.get(page_url)
        # 输出景点地址，方便校验
        print(self.browser.current_url)
        i = 1
        # ======================================================进入循环======================================================
        while True:
            # 捕捉页面源码
            html_data = self.browser.page_source
            # 转换页面源码格式
            xml_data = etree.HTML(html_data)
            # 提示信息
            print(f'正在打印评论第{i}页')
            # 遍历打印评论
            for page in xml_data.xpath('//div[@class="commentList"]/div[@class="commentItem"]//div[@class="commentDetail"]'):
                print(page.xpath('normalize-space(.)'))
                time.sleep(2)
                discuss = page.xpath('normalize-space(.)')
                # 准备保存
                print('执行保存操作')
                time.sleep(2)
                self.save(discuss)
            # 评论翻页
            button = self.browser.find_element(By.XPATH, '//li[@class=" ant-pagination-next"]').get_attribute('aria-disabled')
            if button == 'false':
                self.browser.find_element(By.XPATH, '//li[@class=" ant-pagination-next"]').click()
            elif button == 'true':
                break
            # 睡眠5秒
            time.sleep(5)
            i += 1


    def save(self, discuss):

        # emoji_pattern = r'/[x{1F601}-x{1F64F}]/u'
        discusses = re.sub(emoji.get_emoji_regexp(), r'', discuss)
        sql = 'insert into ctrip(discuss) values(%s)'
        self.cursor.execute(sql, [discusses])
        self.db.commit()


if __name__ == '__main__':
    a = Spider()
    a.login()
