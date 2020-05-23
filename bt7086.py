#!/user/bin/env/python3
# -*- coding: utf-8 -*-

'python study file'

__author__ = 'heyu<18781085152@163.com>'

import requests, re, time, os, random,threading
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class Bt7086(object):

    def __init__(self,name, startPage=1, endPage=1,number=0):
        self.headers = {
            'Referer': 'http://s1.pbnmdssb.club/pw/html_data/15/2005/4763406.html',
            'Sec-Fetch-Dest': 'image',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
        }
        self.proxies = {
            # 'http': '36.91.156.75:8080',
            # 'http': '46.118.33.132:36610',
            # 'http': '62.182.48.124:43686',
            # 'http': '200.112.204.2:8080',
            # 'http': '36.89.188.11:39507',
        }
        self.name = name
        self.startPage = startPage
        self.endPage = endPage
        self.number = number

    # 主程序
    def index(self):
        rootDir = 'bt7086'  # 下载根目录
        secondDir = rootDir + '/' + self.name  # 图片目录
        # url = 'http://s1.pbnmdssb.club/pw/thread.php?fid=15'
        # url = 'http://s1.pbnmdssb.club/pw/thread.php?fid=16'
        url = 'http://s1.pbnmdssb.club/pw/thread.php?fid=49'
        urlFix = 'http://s1.pbnmdssb.club/pw/'
        if int(self.startPage) < 1 or int(self.endPage) < 1:
            self.startPage = 1
            self.endPage = 2
        else:
            self.startPage = int(self.startPage)
            self.endPage = int(self.endPage)
        hot = 0
        for x in range(int(self.startPage), int(self.endPage)):
            pageUrl = ''
            if x > 1:
                pageUrl = url + '&page=' + str(x)
            else:
                pageUrl = url
            response = requests.get(url=pageUrl, headers=self.headers, proxies=self.proxies,timeout=30)
            response.encoding = 'utf-8'
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            for item in soup.select('tr.t_one.tr3 a'):
                if item.string.find(self.name) != -1:

                    # 创建图片保存目录
                    if not os.path.exists(rootDir):
                        os.mkdir(rootDir)
                    if not os.path.exists(secondDir):
                        os.mkdir(secondDir)

                    # 使用线程下载
                    threadName = threading.Thread(target=self.threads, args=(urlFix, item, secondDir))
                    threadName.start()
                else:
                    hot += 1

        if hot == 0:
            print('没有找到关于{}相关的信息'.format(self.name))
            exit()

    # 下载图片
    def downLoad(self,url, secondDir):
        url = list(map(lambda x: x.replace('"', ''), url))  # 去除正则返回数据多余的“符号
        try:
            for k, v in enumerate(url):
                imgHtmls = requests.get(url=v, headers=self.headers, proxies=self.proxies,timeout=30)
                data = imgHtmls.content  # 获取图片内容
                timeStr = time.strftime('%Y%M%D%H%M%S').replace('/', '')
                picName = secondDir + '/' + timeStr + str(random.randint(1000, 9999)) + '.jpg'  # 组装图片路径
                with open(picName, 'wb+') as f:
                    f.write(data)  # 下载文件
                    print(picName, '已经下载完成')
        except Exception as e:
            print('下载失败，原因是：', e)
            exit()

    # 创建线程下载
    def threads(self,urlFix, item, secondDir):
        imgHtml = requests.get(url=urlFix + item.get('href'), headers=self.headers,proxies=self.proxies,timeout=30)  # 获取对应页面url
        imgHtml.encoding = 'utf-8'
        returnList = re.findall(r'\"http+s?:\/\/.*?.jpg\"', imgHtml.text)  # 匹配图片地址
        self.downLoad(returnList, secondDir)  # 执行下载


if __name__ == '__main__':
    name = input('请输入搜索关键字： ')
    startPage = input('开始页码 ')
    endPage = input('结束页码 ')
    obj = Bt7086(name, startPage, endPage)
    obj.index()
    print('done')