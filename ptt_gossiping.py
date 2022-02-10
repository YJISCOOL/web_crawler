import urllib.request as req

def geturldata(url):
    # 建立一個request物件，附加Request Headers的資訊，否則網頁會拒絕你讀取資料
    # 利用這個request物件去打開網址
    request = req.Request(url, headers={
        'cookie': 'over18=1', # 有cookie就得把他一起放進來
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    })
    with req.urlopen(request) as response:
        raw_data = response.read().decode('utf-8')  # data就是該頁的原始碼內容

    # 解析原始碼
    import bs4
    root = bs4.BeautifulSoup(raw_data, 'html.parser')
    article_titles = root.find_all('div', class_='title')  # article_titles會列出所有title的資訊
        # 整理資料
    for title in article_titles:
        if title.a != None:  # 若title底下a標籤裡的資料存在
            print(title.a.string)  # 則印出title底下a標籤裡的字串

        # 抓 上一頁 的連結
    nextLink = root.find('a', string='‹ 上頁')  # 去找內文a標籤裡字串為‘‹ 上頁’的資料
    return nextLink['href'] # 進到函式中，到此步會回傳上一頁的資料

urlpage = 'https://www.ptt.cc/bbs/Gossiping/index.html'
count_page = 0
while count_page<5:
    urlpage = 'https://www.ptt.cc'+geturldata(urlpage)
    count_page += 1
