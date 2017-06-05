
from collections import Counter

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com/a.txt",
    "http://www.google.com/c.jpg",
    "http://www.google.com/a.txt",
    "http://www.google.com/b.txt",
    "http://www.google.com/b.txt",
    "http://www.google.com/c.jpg",
    "http://www.google.com/haha.png",
]

urls_count = Counter(urls)

top_three = urls_count.most_common(3)

top_three.sort(key=lambda s: s[0].split('/')[-1])

for i in top_three:
    print(i[0].split('/')[-1], i[1])
