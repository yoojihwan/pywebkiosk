#!/usr/bin/python3
#-*- coding: utf-8 -*-
 
import sys
import codecs
import cgitb
cgitb.enable()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

from bs4 import BeautifulSoup
from requests import get
import cgi, os, re

form = cgi.FieldStorage()#!/usr/bin/python3
print("content-type: text/html; charset=UTF-8\n")

from bs4 import BeautifulSoup
from requests import get
import cgi, os, re

form = cgi.FieldStorage()
if 'id' in form:
    urlId = form['id'].value

url = "https://uos.ac.kr/korNotice/view.do?list_id=FA2&seq="+str(urlId)+"&sort=1&pageIndex=1&searchCnd=&searchWrd=&cate_id=&viewAuth=Y&writeAuth=Y&board_list_num=10&lpageCount=10&epTicket=LOG"
get_url = get(url)
soup = BeautifulSoup(get_url.content.decode('utf-8', 'replace'), "html.parser")

findCls = soup.find(id = "view_content")
# findBody = findCls.find_all('')
print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf=8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="/proj/test_style.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <div class="description">
        {listText}
    </div>
</body>
</html>
'''.format(listText = findCls))
if 'id' in form:
    urlId = form['id'].value

url = "https://uos.ac.kr/korNotice/view.do?list_id=FA2&seq="+str(urlId)+"&sort=1&pageIndex=1&searchCnd=&searchWrd=&cate_id=&viewAuth=Y&writeAuth=Y&board_list_num=10&lpageCount=10&epTicket=LOG"
get_url = get(url)
soup = BeautifulSoup(get_url.content.decode('utf-8', 'replace'), "html.parser")

findCls = soup.find(id = "view_content")
# findBody = findCls.find_all('')
print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf=8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="/proj/test_style.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <div class="description">
        {listText}
    </div>
</body>
</html>
'''.format(listText = findCls))
