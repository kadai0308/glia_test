
from collections import Counter

urls = [
    "http://www.aa.com/a.txt",
    "http://www.bb.com/a.txt",
    "http://www.cc.com/c.jpg",
    "http://www.ss.com/a.txt",
    "http://www.ff.com/b.txt",
    "http://www.xx.com/b.txt",
    "http://www.ee.com/c.jpg",
    "http://www.ww.com/haha.png",
]

def urlsG(urls):
  for url in urls:
    yield url.split('/')[-1]

urls_count = Counter(urlsG(urls))

top_three = urls_count.most_common(3)

top_three.sort(key=lambda s: s[0])

for i in top_three:
    print(i[0], i[1])
