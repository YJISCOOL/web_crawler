import urllib.request as req
# 抓取ptt Movie版的網頁原始碼
url_movie = 'https://www.ptt.cc/bbs/movie/index.html'

# 建立一個request物件，附加Request Headers的資訊，否則網頁會拒絕你讀取資料
# 利用這個request物件去打開網址
request = req.Request(url_movie, headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
})
with req.urlopen(request) as response:
    raw_data = response.read().decode('utf-8') # data就是該頁的原始碼內容

# 解析原始碼
import bs4
root = bs4.BeautifulSoup(raw_data, 'html.parser')
article_titles = root.find_all('div', class_='title') # article_titles會列出所有title的資訊
    # 整理資料
for title in article_titles:
    if title.a != None: # 若title底下a標籤裡的資料存在
        print(title.a.string) # 則印出title底下a標籤裡的字串