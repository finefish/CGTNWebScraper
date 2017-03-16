import bs4 as bs
import urllib.request
from string import Template
import sys
import os
from datetime import datetime

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

now = datetime.now()

DateFolderName = str(now.year) + '-' + str(now.month).zfill(2) + '-' + str(now.day).zfill(2)
if not os.path.exists(DateFolderName):
    os.makedirs(DateFolderName)

HourFolderName = DateFolderName + '/' + str(now.hour).zfill(2)
if not os.path.exists(HourFolderName):
    os.makedirs(HourFolderName)

for data in output:
    # print(data['time'],',',data['title'],',',data['link'])
    ArticleFileName = HourFolderName + '/' + data['title']
    with open(ArticleFileName, 'w') as f:
        f.write(data['time'])
