import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = "http://www.boannews.com/search/news_hash.asp?search=key_word&find=%BB%E7%B0%C7%BB%E7%B0%ED"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')

# url = 'https://www.boannews.com' 

now = datetime.now()

current = "security_News_{}".format(now.date())
f = open('../data/sec/{}.txt'.format(current),'w')

def security_news(number):
    title = soup.select('div.news_list:nth-child({}) > a > span'.format(number))
    link = 'http://www.boannews.com/'+ soup.find(class_='news_list').find('a').get('href')
    content = soup.select('div.news_list:nth-child({}) > a:nth-child(3)'.format(number))
    date = soup.select('div.news_list:nth-child({}) > span'.format(number))
    # title
    for item in title:
        print("제목: " + item.get_text(), file=f)
    # content
    for item in content:
        print("내용: " + item.get_text(), file=f)
    # date
    for item in date:
        print("기자: " +item.get_text().replace("기자","").replace('|',"\n시간:"),file=f)
    # link
    print("링크:",url,end="\n\n",file=f)

for a in range(1,21):
    security_news(a*2-1)
f.close()
