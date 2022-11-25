import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = 'http://www.boannews.com/media/o_list.asp'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')

now = datetime.now()
current = "hot_News_{}".format(now.date())

f = open('../data/hot/{}.txt'.format(current),'w')

def security_news(number):
    title = soup.select('div.news_list:nth-child({}) > a:nth-child(1) > span:nth-child(2)'.format(number))
    content = soup.select('div.news_list:nth-child({}) > a:nth-child(3)'.format(number))
    date = soup.select('div.news_list:nth-child({}) > span:nth-child(4)'.format(number))
    link = 'http://www.boannews.com/'+ soup.find(class_='news_content').get('href')
    # title
    for item in title:
        print("제목: " + item.get_text(), file=f)
    # content
    for item in content:
        print("내용: " + item.get_text(),file=f)
    # date
    for item in date:
        print("기자: " + item.get_text().replace("기자","").replace('|',"\n시간:"),file=f)
    print("링크:" + link,end="\n\n",file=f)

for a in range(1,21):
    security_news(a*2-1)
