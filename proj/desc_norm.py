#!/usr/bin/python3
#-*- coding: utf-8 -*-
print("content-type:text/html; charset=utf-8\r\n")

import cgi
from bs4 import BeautifulSoup
from requests import get
import sys
import codecs
import cgitb

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
urlId = form['id'].value

url = "https://uos.ac.kr/korNotice/view.do?list_id=FA1&seq="+str(urlId)+"&sort=1&pageIndex=1&searchCnd=&searchWrd=&cate_id=&viewAuth=Y&writeAuth=Y&board_list_num=10&lpageCount=10&epTicket=LOG"
get_url = get(url)
soup = BeautifulSoup(get_url.content.decode('utf-8', 'replace'), "html.parser")

findCls = soup.find(id = "view_content")
# findBody = findCls.find_all('')
print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf=8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="/proj/design.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <div class="description">
        {listText}
    </div>
</body>
</html>
'''.format(listText = findCls))
