# -*- encoding: utf-8 -*-
from selenium import webdriver
import time
import threading

def login():

    # 设置登录连接
    url = "https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin"

    # 进入指定链接
    driver.get(url)

    # 点击微信登录
    print("请在30秒内登录。否则将会退出程序。")
    try:
        driver.find_element_by_class_name("signin-way-shjiaoyu").click()
    except:
        print("调用微信登录失败")
        driver.quit()

    for i in range(1, 30, 1):
        print("用时：" + str(i))
        time.sleep(1)
        if(i<30):
            try:
                driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div[2]/div[2]/div[1]/ul[1]/li[2]/p[1]").get_attribute("textContent")
                print("微信登录成功，计时退出")
                break
            except:
                pass
        else:
            driver.quit()


# 获取各种信息
class Obtain:

    # 获取姓名
    def obtain_name(self):
        name = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/p[1]").get_attribute("textContent")
        print("嗨！ " + name + " 你好。")

    # 获取课程数以及课程名
    def Course_number(self):
        print("获取课程中……")
        time.sleep(3)
        # 获取几门课程

        number = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div[2]/div[2]/div[1]/ul[1]/li[2]/p[1]").get_attribute("textContent")
        print("您一共选择了：" + number + "门课程。")

        # 获取课程名称
        for i in range(1, int(number)+1):
            path = "//*[@id='sharingClassed']/div[2]/ul[" + str(i) + "]/div[1]/dl[1]/dt[1]/div[1]"
            Course_name = driver.find_element_by_xpath(path).get_attribute("textContent")
            print(str(i) + " " + Course_name)
            print("-"*25)
        print("\n")


# 进入视频页
def into(num):
    print("进入视频中")
    try:
        driver.find_element_by_xpath("//*[@id='sharingClassed']/div[2]/ul["+str(num)+"]/div[1]/dl[1]/dt[1]/div[1]").click()
    except:
        print("进入失败，正在重新进入")

    try:
        time.sleep(3)
        driver.get("https://onlineh5.zhihuishu.com/onlineWeb.html#/studentIndex")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='sharingClassed']/div[2]/ul[" + str(num) + "]/div[1]/dl[1]/dt[1]/div[1]").click()
    except:
        print("第二次进入失败")
        driver.quit()


# 关闭课前提示
def close():

    try:
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div[1]/button').click()
        print("关闭我知道了成功")
    except:
        pass

    # 关闭学前须知
    try:
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[7]/div[2]/div[1]/i').click()
        print("关闭学前须知成功")
    except:
        pass


# 设置基础
def set():

    # 设置画面质量
    try:
        time.sleep(1)
        driver.execute_script('document.querySelector("#vjs_container > div.controlsBar > div.definiBox > div > b.line1bq.switchLine").click()')  # 设置流畅
        print("设置流畅成功")
    except:
        print("设置流畅失败")

    # 设置倍速
    try:
        time.sleep(1)
        driver.execute_script('document.querySelector("#vjs_container > div.controlsBar > div.speedBox > div > div.speedTab.speedTab10").click()')  # 1.25倍
        print("设置1.25倍成功")
    except:
        print("设置1.25倍失败")


    # 设置静音
    try:
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[6]').click()
        print("设置静音成功")
    except:
        print("设置静音失败")


# 关闭弹窗
def Close_Popup():
    print("弹窗检测中")

    while(True):
        try:
            time.sleep(5)
            driver.find_element_by_class_name("topic-item").click()  # 点击第一个答案
            driver.find_element_by_xpath('/html/body/div[1]/div/div[7]/div/div[3]/span/div').click()  # 点击关闭
            time.sleep(2)
            driver.execute_script('document.querySelector("#playButton").click()')  # 点击播放
            print("关闭弹窗成功")
        except:
            pass


# 跳转下一节
def play_next():
    print("下一集检测中")
    time.sleep(5)
    # 总时间
    total_time = driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[4]/span[2]').get_attribute('textContent')
    # 章节
    chapter = driver.find_element_by_id("lessonOrder").get_attribute('textContent')
    print("正在观看：" + chapter + " 本节视频总时长：" + total_time)
    while(True):
        time.sleep(5)
        total_time = driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[4]/span[2]').get_attribute('textContent')
        current_time = driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[4]/span[1]').get_attribute('textContent')
        print(current_time)
        if current_time == total_time:
            print('本节视频播放完成，正在播放下一节')
            try:
                driver.execute_script("document.querySelector('#nextBtn').click()")  # 当前视频播放结束，点击下一节
                time.sleep(3)
                set()
            except:
                print("切换下一节失败，正在重试")
                time.sleep(2)
                driver.execute_script("document.querySelector('#nextBtn').click()")  # 当前视频播放结束，点击下一节


if __name__ == '__main__':

    print("智慧树自动看课系统V1.3启动成功")
    driver = webdriver.Chrome()
    print("浏览器启动")

    # 登录
    login()

    # 创建类实例
    obtain = Obtain()

    # 调用姓名，课程号
    obtain.obtain_name()
    obtain.Course_number()

    # 输入编号
    num = input("请输入序号进行刷课：")
    into(num)

    # 关闭我知道了
    close()

    # 设置流畅
    set()

    # 关闭弹窗
    poput = threading.Thread(target=Close_Popup)

    # 跳转下一节
    next = threading.Thread(target=play_next)

    poput.start()
    next.start()