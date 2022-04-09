# -*- coding: utf-8 -*-
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import workbook
from lxml import etree
import emoji
import time


class LingYing_Spider(object):
    def __init__(self):
        # GUI实例化，创建根窗口
        self.window = tk.Tk()
        # 根窗口添加标题
        self.window.title('领英自动化')
        # 根窗口固定大小
        self.window.geometry('700x400')
        # 创建一个下拉菜单
        self.menubar = tk.Menu(self.window)
        # 创建一个菜单项
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # 下拉菜单装到容器内部
        self.menubar.add_cascade(label='operation', menu=self.filemenu)
        # 添加退出按钮
        self.filemenu.add_command(label='Exit', command=self.window.destroy)
        # 配置菜单栏显示
        self.window.config(menu=self.menubar)
        # 总标题
        tk.Label(self.window, text='自动化程序', bg='red', fg='black', font=16).pack()

        # 页面区分
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack()
        # 子frame建立
        self.frame_left = tk.Frame(self.main_frame)
        self.frame_right = tk.Frame(self.main_frame)

        # 左 frame
        self.frame_left.pack(side='left')
        # 嵌套一个提示窗口
        self.text_hint_1 = tk.Label(self.frame_left, text='请输入查询的公司', bg='green', fg='white', font=12)
        self.text_hint_1.pack()
        # 嵌套一个输入窗口
        self.text_input_1 = tk.Entry(self.frame_left, font=12, show=None)
        self.text_input_1.pack()
        # 嵌套一个提示窗口
        self.text_hint_2 = tk.Label(self.frame_left, text='请输入你的账号', bg='green', fg='white', font=12)
        self.text_hint_2.pack()
        # 嵌套一个输入窗口
        self.text_input_2 = tk.Entry(self.frame_left, font=12, show=None)
        self.text_input_2.pack()
        # 嵌套一个提示窗口
        self.text_hint_3 = tk.Label(self.frame_left, text='请输入你的密码', bg='green', fg='white', font=12)
        self.text_hint_3.pack()
        # 嵌套一个输入窗口
        self.text_input_3 = tk.Entry(self.frame_left, font=12, show='*')
        self.text_input_3.pack()

        # 嵌套一个运行函数的按钮
        self.button = tk.Button(self.frame_left, text='点击运行', font=12, bg='red', fg='white', command=self.login_html)
        self.button.pack()

        # 右 frame
        self.frame_right.pack(side='right')
        # 嵌套一个提示窗口
        self.text_hint_4 = tk.Label(self.frame_right, text='登录时间：有验证时间就长点,没有就短点(默认1.5)', bg='green', fg='white', font=12)
        self.text_hint_4.pack()
        # 嵌套一个输入窗口
        self.text_time_4 = tk.Entry(self.frame_right, font=12, show=None)
        self.text_time_4.pack()
        # 嵌套一个提示窗口
        self.text_hint_5 = tk.Label(self.frame_right, text='点击posts是否完成,否就长点,完成就短点(默认1.5)', bg='green', fg='white', font=12)
        self.text_hint_5.pack()
        # 嵌套一个输入窗口
        self.text_time_5 = tk.Entry(self.frame_right, font=12, show=None)
        self.text_time_5.pack()
        # 嵌套一个提示窗口
        self.text_hint_6 = tk.Label(self.frame_right, text='comments需要加载的时间(默认5)', bg='green', fg='white', font=12)
        self.text_hint_6.pack()
        # 嵌套一个输入窗口
        self.text_time_6 = tk.Entry(self.frame_right, font=12, show=None)
        self.text_time_6.pack()

        # 创建一个数据表
        self.wb = workbook.Workbook()
        # 数据表的一个激活
        self.ws = self.wb.active
        # 添加一下数据表的表头
        # self.ws.append(['发布内容', '内容图片url', '点赞数', '转发数', '评论数', '评论内容'])
        # 根窗口循环
        self.window.mainloop()

    def login_html(self):
        # 创建一个变量接受输入窗口的值
        str_company = self.text_input_1.get()
        str_account = self.text_input_2.get()
        str_password = self.text_input_3.get()
        int_time_1 = self.text_time_4.get()
        int_time_2 = self.text_time_5.get()
        int_time_3 = self.text_time_6.get()
        # 隐藏自动化头
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 实例化自动化对象
        driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
        driver.get('https://www.linkedin.com/authwall?trk=ripf&trkInfo=AQED7qDsuPIMsgAAAX-5l4-AxlGf3Dw5x9hSclATswrbbkcwivzM6S2zWl1_IPtflN3Kiig76mHqmspc1Yv4y56TvYxw37LLA3VzFKg3hGMRIUn4oYXeAxBzy-JRuLwt3C40DXk=&originalReferer=&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fwhite-lodging%2Fposts%2F%3FfeedView%3Dall')
        # wait = WebDriverWait(driver, 20)
        # 点击登录按钮
        driver.find_element(By.XPATH, '//*[@id="main-content"]/div/form/p/button').click()
        # 输入账号 f'{str_account}'
        session_key = driver.find_element(By.XPATH, '//*[@id="session_key"]')
        session_key.send_keys(f'{str_account}')
        # 输入密码 f'{str_password}'
        session_password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
        session_password.send_keys(f'{str_password}')
        # 点击登录
        driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div/form/button').click()
        time.sleep(float(int_time_1))
        # 点击搜索
        driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').click()
        # f'{str_company}'
        driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').send_keys(f'{str_company}')
        driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').send_keys(Keys.ENTER)
        print('点击搜索了进入搜索界面')
        time.sleep(2)
        # 点击进入公司主页
        print('点击进入公司主页')
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/a/div/div[2]/div[2]/a/div/span').click()
        print('开始准备点击posts')
        time.sleep(float(int_time_2))
        # 点击posts
        for tag in driver.find_elements(By.XPATH, '//div[@class="mb4"]//ul[contains(@class, "org-page-navigation__items")]/li/a'):
            # print(tag.text)
            if tag.text.strip() == 'Posts':
                tag.click()
                break
            else:
                continue
        time.sleep(3)
        print('点击完成')
        # 为判断页面下拉距离设置一个初始值
        check_height = 0
        # 进入循环
        while True:
            # 页面无限下拉
            # print('开始页面下拉')
            js = 'window.scrollBy(0,300)'
            # 运行js代码
            driver.execute_script(js)
            # 沉睡，让滚动条有所反应
            time.sleep(0.5)
            # 测试出滚动条距离页面顶端的距离
            finally_height = driver.execute_script("return document.documentElement.scrollTop || document.body.scrollTop;")
            # 开始进行判断
            if check_height == finally_height:
                # 如果页面下拉距离与初始值相等，即退出下拉循环
                # print('页面下拉完成')
                break
            else:
                # 否则，将下拉值给初始值，为下一次下拉循环做准备
                check_height = finally_height
        self.parse_html(driver, str_company, int_time_3)

    def parse_html(self, driver, str_company, int_time_3):
        time.sleep(float(int_time_3))

        # 获取所有的信息
        buttons = driver.find_elements(By.XPATH, '//span[@class="comment feed-shared-social-action-bar__action-button"]//span[@class="artdeco-button__text"]')
        divs = driver.find_elements(By.XPATH, '//div[@class="scaffold-finite-scroll__content"]/div')
        if len(buttons) != len(divs):
            print('内容没有加载完成，请适当延长等待时间')
            print(f'div加载了{len(divs)}')
            print(f'comments加载了{len(buttons)}')
            time.sleep(5)
            driver.quit()
        else:
            print('内容加载完毕')
        # 完成数据提取
        for small_div, button in zip(divs, buttons):

            # 转换源代码格式
            html_data = small_div.get_attribute("outerHTML")
            xml_data = etree.HTML(html_data)
            list_total = []

            # 提取发布内容
            text_data = ' '.join(xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="feed-shared-update-v2__description-wrapper"]//span[@dir="ltr"]/text()'))
            text_url_data = ' '.join(xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="feed-shared-update-v2__description-wrapper"]//span[@dir="ltr"]/a/@href'))
            text_total_data = text_data.strip() + text_url_data.strip()
            print(text_total_data)
            list_total.append(emoji.emojize(text_total_data))

            # 获取发布内容的url
            if 'feed-shared-mini-update-v2 feed-shared-update-v2__update-content-wrapper artdeco-card' in html_data:
                # 如果是转发的链接
                for url_small_data in xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="feed-shared-mini-update-v2 feed-shared-update-v2__update-content-wrapper artdeco-card"]//a[@class="tap-target feed-shared-mini-update-v2__link-to-details-page text-body-medium ember-view"]/@href'):
                    url_data_1 = 'https://www.linkedin.com' + url_small_data
                    print(url_data_1)
                    list_total.append(url_data_1)
            elif 'media-player video-s-loader__video-container  ember-view' in html_data:
                # 如果是视频
                for url_video_data in xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="media-player video-s-loader__video-container  ember-view"]/div/video/@src'):
                    print(url_video_data)
                    list_total.append(url_video_data)
            elif 'feed-shared-article feed-shared-update-v2__content' in html_data:
                # 如果是小链接
                small_url_list = []
                for small_url_data in xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//article[@class="feed-shared-article feed-shared-update-v2__content"]//a/@href'):
                    print(small_url_data)
                    small_url_list.append(small_url_data)
                list_total.append(' '.join(small_url_list))
            elif 'feed-shared-image__container' in html_data:
                # 如果是图片
                img_list = []
                for url_data_2 in xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="feed-shared-image__container"]//img/@src'):
                    print(url_data_2)
                    img_list.append(url_data_2)
                list_total.append(','.join(img_list))
            else:
                # 如果以上情况都没有
                print('无相关所需内容')
                list_total.append(' ')

            # 获取发布时的点赞
            like_data = xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="social-details-social-activity update-v2-social-activity"]/ul/li[1]//span[@class="social-details-social-counts__reactions-count" or @class="social-details-social-counts__social-proof-fallback-number"]/text()')
            if len(like_data) == 0:
                like_data = 0
                print(like_data)
                list_total.append(list_total)
            else:
                print(like_data[0])
                list_total.append(like_data[0])

            # 获取发布时的转发量
            share_data = xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="social-details-social-activity update-v2-social-activity"]/ul/li/div[contains(@class, "t-black--light")]/span/text()')
            if len(share_data) == 0:
                share_data = '0 share'
                print(share_data)
                list_total.append(share_data)
            else:
                print(share_data[0])
                list_total.append(share_data[0])

            # 获取发布的时的评论数
            comment_count_data = xml_data.xpath('//div[@class="occludable-update ember-view"]/div/div//div[@class="social-details-social-activity update-v2-social-activity"]/ul/li[contains(@class, "social-details-social-counts__item social-details-social-counts__comments")]/button/span/text()')
            if len(comment_count_data) == 0:
                comment_count_data = '0 comment'
                print(comment_count_data)
                list_total.append(comment_count_data)
            else:
                print(comment_count_data[0].strip())
                list_total.append(comment_count_data[0].strip())

                # 点击评论
                webdriver.ActionChains(driver).move_to_element(button).click(button).perform()
                print('我点击了最基本的comments, 开始观察')
                time.sleep(2)
                while True:
                    print('我进入了循环')
                    if len(driver.find_elements(By.XPATH, '//button[@class="comments-comments-list__load-more-comments-button artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]/span[@class="artdeco-button__text"]')) != 0:
                        for more_button in driver.find_elements(By.XPATH, '//button[@class="comments-comments-list__load-more-comments-button artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]/span[@class="artdeco-button__text"]'):
                            webdriver.ActionChains(driver).move_to_element(more_button).click(more_button).perform()
                            time.sleep(4)
                            print('我点击了更多的comments')
                    else:
                        break

                # 获取评论当中的内容
                time.sleep(5)
                html_data = small_div.get_attribute("outerHTML")
                xml_data = etree.HTML(html_data)
                print('准备打印comments')
                for i in xml_data.xpath('//div[contains(@class, "comments-comments-list")]/div/article/div[3]//div[contains(@class, "feed-shared-inline-show-more-text")]'):
                    print(emoji.emojize(i.xpath('string(.)').strip()))
                    list_total.append(emoji.emojize(i.xpath('string(.)').strip()))

            # 保存数据到表格
            print('我已经完成了点击')
            self.save_excel(list_total, str_company)
            time.sleep(2)

    def save_excel(self, list_data, str_company):
        try:
            self.ws.append(list_data)
            self.wb.save(f'{str_company}数据.xlsx')
            print('该数据已加载')
        except:
            print('数据没加载出来')


if __name__ == '__main__':
    a = LingYing_Spider()
    a.login_html()
