import bs4 as bs
import urllib.request
from string import Template
import sys
import time

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(1,0,0);
while 1==1:
    time.sleep(second);
    sauce = urllib.request.urlopen('http://edition.cnn.com/specials/last-50-stories').read()
    #sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
    #sauce = urllib.request.urlopen('http://edition.cnn.com/specials/last-50-stories').read()
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
          print('http://edition.cnn.com'+data['link'])
          print (soup2.title.text)
 #新闻标题
          f = open(r'C:\Users\Administrator\Desktop\test2.txt','a',encoding='utf-8')   
          t1 = soup2.title.text
          f.write(t1)
          f.write('^')
          time1 = soup2.find('p',class_= 'update-time')
          while True:
                try:
                      print (time1.text)
                      t2 = time1.text
                      f.write(t2)
                      f.write('^')
                      break
                except:
                      break
#新闻发布时间
          for div2 in soup2.find_all('div',class_='zn-body__paragraph'):
                print(div2.text)
                t3 = div2.text
                f.write(t3)
#新闻文本内容
          f.write('\n')
          time.sleep(5)
      

