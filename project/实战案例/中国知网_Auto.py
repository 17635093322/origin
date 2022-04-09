import json
import sys
import time
from lxml import etree
from selenium import webdriver  # # 驱动浏览器
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载完毕，寻找某些元素
from selenium.webdriver.support import expected_conditions as EC  ##等待指定标签加载完毕
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import pymysql


class Spider:
    def __init__(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        self.db = pymysql.connect(
            user='root',password='admin',database='spider',charset='utf8'
        )
        self.cursor = self.db.cursor()

    def get_data(self):
        # 浏览器搜索
        self.browser.get('https://www.cnki.net/')
        # 等待加载浏览器搜索框
        wait = WebDriverWait(self.browser,200)
        wait.until(EC.presence_of_element_located((By.ID, 'txt_SearchText')))
        # # 搜索框输入
        text_input = self.browser.find_element(By.ID, 'txt_SearchText')
        text_input.clear()
        text_input.send_keys('CEO')
        text_input.send_keys(Keys.ENTER)
        # 点击登录
        time.sleep(2)
        print('准备登录')
        wait.until(EC.presence_of_element_located((By.ID, 'Ecp_top_login_show')))
        self.browser.find_element(By.XPATH, '//*[@id="Ecp_top_login_show"]').click()
        # 点击微信
        print('点击微信')
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Ecp_ThirdLogin"]/a[2]')))
        self.browser.find_element(By.XPATH, '//*[@id="Ecp_ThirdLogin"]/a[2]').click()
        # 等待加载
        wait = WebDriverWait(self.browser,200)
        wait.until(EC.presence_of_element_located((By.ID, 'txt_SearchText')))
        # # 搜索框输入
        time.sleep(2)
        text_input = self.browser.find_element(By.ID, 'txt_SearchText')
        text_input.clear()
        text_input.send_keys('CEO')
        text_input.send_keys(Keys.ENTER)
        # 点击报纸
        print('切换到报纸')
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/ul[1]/li[4]')))
        self.browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/ul[1]/li[4]').click()
        print('切换到报纸成功')
        # 两秒闲置等待加载
        time.sleep(6)
        # 获取后续页面源码
        print('页面加载完成')
        html_demo = self.browser.page_source
        print('调成50个结果')
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="perPageDiv"]/div')))
        self.browser.find_element(By.XPATH, '//*[@id="perPageDiv"]/div').click()
        print('展开50个结果，准备点击')
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="perPageDiv"]/ul/li[3]/a')))
        self.browser.find_element(By.XPATH, '//*[@id="perPageDiv"]/ul/li[3]/a').click()
        print('点击完成')
        time.sleep(1.5)
        # 调用解析
        print('开始解析')
        i = 1
        while True:
            print(f'当前是第{i}页')
            i += 1
            self.parse_data(html_demo)
            self.browser.find_element(By.XPATH, '//*[@id="PageNext"]').click()
            time.sleep(3)
            html_demo = self.browser.page_source

    def parse_data(self,ht):
        print('已经进入调用')
        # 链接点击，下载
        link_click = self.browser.find_elements(By.XPATH,'//td[@class="operat"]/a[@class="downloadlink icon-download"]')
        # 转换
        xm = etree.HTML(ht)
        # 刊物名称
        title_name= xm.xpath('//td[@class="source"]/a')
        # 题名
        name = xm.xpath('//td[@class="name"]/a')
        # 发表时间
        time_name = xm.xpath('//td[@class="date"]')
        # 链接
        link = xm.xpath('//td[@class="operat"]/a[@class="downloadlink icon-download"]/@href')
        for tn, na, ti, li, li_cl in zip(title_name, name, time_name, link, link_click):
            title_kan = tn.text.strip()
            print(tn.text.strip())
            title = na.xpath('string(.)')
            print(na.xpath('string(.)'))
            title_time = ti.text.strip()
            print(ti.text.strip())
            title_url = 'https://kns.cnki.net' + li
            print('https://kns.cnki.net' + li)
            # self.save_data(title_kan,title,title_time,title_url)
            # li_cl.click()
            time.sleep(2)
            print('='*60)

    def save_data(self,title_kan,title,title_time,title_url):
        sql = 'insert into zhiwang(title_kan,title,title_time,title_url) values(%s,%s,%s,%s)'
        self.cursor.execute(sql,[title_kan,title,title_time,title_url])
        self.db.commit()

if __name__ == '__main__':
    data = Spider()
    data.get_data()