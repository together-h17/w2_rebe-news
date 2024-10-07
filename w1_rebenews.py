import requests
from bs4 import BeautifulSoup
import csv
import datetime


today = datetime.date.today()
today_str = today.strftime('%Y-%m-%d')

news = False

# 開個csv
with open('rebenews.csv', 'w+', newline = '')as f:
    writer = csv.writer(f)

    url = 'http://www.rebe.ntpu.edu.tw/'
    # 訪問權限+解析
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    
   
    item = sp.find_all('div', class_ = 'w-annc__content-wrap')
    writer.writerow(['發布時間', '標題', '網址'])
    for i in range(0, len(item)-1):
        list_ = []
        date = item[i].find('span', class_ = 'w-annc__postdate').text
        title = item[i].a.text.strip()
        href = "http://www.rebe.ntpu.edu.tw" + item[i].a.get("href")

        if(date == " " + today_str):
            news = True
            print("今日新消息")
            print('發布時間' + date)
            print(title)
            print(href)
            print("\n")
            list_.append(date)
            list_.append(title)
            list_.append(href)
            writer.writerow(list_)

    if(news == False):
        print("今日無消息，一切安好")
        


    