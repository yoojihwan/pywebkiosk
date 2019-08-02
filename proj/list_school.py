#!/usr/bin/python3
#-*- coding: utf-8 -*-
print("content-type:text/html; charset=utf-8\r\n")

import cgi
from bs4 import BeautifulSoup
from requests import get
import sys
import codecs
import cgitb
import re

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
if 'pageIndex' in form:
    urlIndex = int(form['pageIndex'].value)
else:
    urlIndex = 1

url = "https://uos.ac.kr/korNotice/list.do?list_id=FA2&seq=0&sort=&pageIndex="+str(urlIndex)+"&searchCnd=&searchWrd=&cate_id=&viewAuth=Y&writeAuth=Y&board_list_num=10&lpageCount=10&epTicket=LOG"
get_url = get(url)
soup = BeautifulSoup(get_url.content.decode('utf-8', 'replace'), "html.parser")

findCls = soup.find(class_ = "listType")
findTot = soup.find(class_ = "mTot")
for span in findCls('span'):
    span.decompose()
for span in findTot('span'):
    span.decompose()
findBody = findCls.find_all('a')

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

addr_result = list()
title_strip = list()
final_result = list()

for addr in findBody:
    if re.match('fnView',addr['onclick']):
        addr_result.append(re.findall('\d+', addr['onclick'])[-1])

for name in findBody:
        title_strip.append(name.text)
title_result = remove_values_from_list(title_strip,'\n\n')

for i in range(0,len(title_result)):
    process = [addr_result[i], title_result[i]]
    final_result.append(process)

listStr = ''
for list in final_result:
    listStr += '<li class="list-group-item"><a href="/proj/desc_school.py?id={addr}">{title}</a></li>'.format(addr = list[0], title = list[1])

totalPage = int(findTot.text)
if urlIndex == 1:
    prevPage = totalPage
else:
    prevPage = urlIndex - 1
if urlIndex == totalPage:
    nextPage = 1
else:
    nextPage = urlIndex + 1

print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf=8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="/proj/design.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col">
                <a class='previous' href='?pageIndex={prevPage}'>
                    <img src="https://uos.ac.kr/images/kor2016/btn/btn_prev.png" class="rounded float-right mt-2" alt="Previous page">
                </a>
                <a class='first' href='?pageIndex=1'>
                    <img src="https://uos.ac.kr/images/kor2016/btn/btn_first.png" class="rounded float-right mt-2" alt="First page">
                </a>
            </div>
            <div class="col-3 mt-2">
                    <p class="text-center">{thisPage} / {lastpage}</p>
            </div>
            <div class="col">
                <a class='last' href='?pageIndex={nextPage}'>
                    <img src="https://uos.ac.kr/images/kor2016/btn/btn_next.png" class="rounded float-left mt-2" alt="next page">
                </a>
                <a class='last' href='?pageIndex={lastpage}'>
                    <img src="https://uos.ac.kr/images/kor2016/btn/btn_last.png" class="rounded float-left mt-2" alt="Last page">
                </a>
            </div>
        </div>
    </div>
    <ul class="list-group list-group-flush">
        {listStr}
    </ul>
</body>
</html>
'''.format(listStr = listStr, lastpage = totalPage, thisPage = urlIndex, prevPage = prevPage, nextPage = nextPage))
