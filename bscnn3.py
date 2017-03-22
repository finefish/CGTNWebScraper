import bs4 as bs
import urllib.request
import time
import os
from datetime import datetime

#日期文件夹
now = datetime.now()
print('job started', now, end=' ')

DateFolderName = '/data/'
DateFolderName += str(now.year) + '-' + str(now.month).zfill(2) + '-' + str(now.day).zfill(2)
if not os.path.exists(DateFolderName):
    os.makedirs(DateFolderName)
#文件名
FileName = DateFolderName + '/' + str(now.hour).zfill(2) + '.txt'

sauce = urllib.request.urlopen('http://edition.cnn.com/specials/last-50-stories').read()
soup = bs.BeautifulSoup(sauce,'lxml')
output = []

for div in soup.find_all('div',class_='media'):
    data = {}
    data['link'] = div.a['href']
    output.append(data)

#抓取CNN新闻链接
for data in output:
    sauce2 = urllib.request.urlopen('http://edition.cnn.com'+data['link']).read()
    soup2 = bs.BeautifulSoup(sauce2,'lxml')
    #print('http://edition.cnn.com'+data['link'])
    #print (soup2.title.text)
    #新闻标题
    f = open(FileName,'a',encoding='utf-8')
    t1 = soup2.title.text
    f.write(t1)
    f.write('^')
    time1 = soup2.find('p',class_= 'update-time')
    while True:
        try:
            #print (time1.text)
            t2 = time1.text
            f.write(t2)
            f.write('^')
            break
        except:
            break
#新闻发布时间
    for div2 in soup2.find_all('div',class_='zn-body__paragraph'):
        #print(div2.text)
        t3 = div2.text
        f.write(t3)
#新闻文本内容
    f.write('\n')
    time.sleep(5)

print('done')
