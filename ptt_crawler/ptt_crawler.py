import requests
from bs4 import BeautifulSoup

def crawler(url):
    doc = requests.get(url).text
    soup = BeautifulSoup(doc, 'html.parser')
    if soup.find(class_='bbs-content').text == '404 - Not Found.':
        print("查無看板")
        return
    artlist = soup.find_all(class_='r-ent')
    for article in artlist:
        title = article.find(class_='title').text.strip()
        date = article.find(class_='date').text.strip()
        author = article.find(class_='author').text.strip()
        print(title, date, author)
        try:
            artUrl = 'https://www.ptt.cc' + article.find(class_='title').find('a')['href']
            artDoc = requests.get(artUrl).text
            artSoup = BeautifulSoup(artDoc, 'html.parser')
            content = artSoup.find(id='main-content')
            main_content = content.find(class_='article-metaline')
            print(main_content.findNextSibling(text=True))
        except Exception as e:
            print(e)
    try:
        nextUrl = ('https://www.ptt.cc' +
            soup.find(class_='btn-group-paging').find_all(class_='btn wide')[1]['href'])
        crawler(nextUrl)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    board = input("輸入看板：")
    crawler('https://www.ptt.cc/bbs/{}/index.html'.format(board))