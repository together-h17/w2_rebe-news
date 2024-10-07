# -*- coding: utf-8 -*-
"""
Created on Wed May 15 01:10:17 2024

@author: vicky
"""

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
line_bot_api = LineBotApi('bot api')
import requests
from bs4 import BeautifulSoup
# import csv
import datetime
from pyshorteners import Shortener

today = datetime.date.today()
today_str = today.strftime('%Y-%m-%d')

news = False

url = 'http://www.rebe.ntpu.edu.tw/'
# 訪問權限+解析
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')


item = sp.find_all('div', class_ = 'w-annc__content-wrap')

for i in range(0, len(item)-1):
    list_ = []
    date = item[i].find('span', class_ = 'w-annc__postdate').text
    title = item[i].a.text.strip()
    href = "http://www.rebe.ntpu.edu.tw" + item[i].a.get("href")
    list_.append(date)
    list_.append(title)
    list_.append(href)

    if(date == " " + today_str):
        news = True
        #處理短網址
        shortener = Shortener('Tinyurl')
        shortener.timeout = 5
        short_href = shortener.short(href)
        
        message = "今日新消息！\n" + '發布時間' + date + "\n" + title + "\n" + short_href + "\n"
        print("今日新消息")
        print('發布時間' + date)
        print(title)
        print(short_href)
        print("\n")

        line_bot_api.push_message('要發送給的user id', TextSendMessage(text=message))

if(news == False):
    print("今日無消息，一切安好")
    line_bot_api.push_message('要發送給的user id', TextSendMessage(text="今日無消息，一切安好"))


