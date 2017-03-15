import bs4 as bs
import urllib.request
from string import Template
import sys

address = Template('https://www.cgtn.com/news/section.do?curPage=0&category=$category')
# print('Scraping Page: ', address.substitute(category=sys.argv[1]))

sauce = urllib.request.urlopen(address.substitute(category=sys.argv[1])).read()
soup = bs.BeautifulSoup(sauce,'lxml')

output = []

for div in soup.find_all('div',class_='title'):
    data = {}
    data['link'] = div.a['href']
    data['title'] = div.a['title']
    for child in div.parent.contents:
        if type(child).__name__ == 'Tag':
            if child['class'][0] == 'time':
                data['time'] = child.p.string
    output.append(data)

for data in output:
    print(data['time'],',',data['title'],',',data['link'])
