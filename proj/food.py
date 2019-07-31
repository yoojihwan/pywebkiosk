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

#학생회관1층 메뉴 크롤링
url = "https://www.uos.ac.kr/food/placeList.do?epTicket=LOG"
r = get(url)
soup = BeautifulSoup(r.content.decode('utf-8','replace'), "html.parser")

findDiv = soup.find(id = "day")
findBody = findDiv.find_all('td')

#양식당 메뉴 크롤링
r2 = get("https://www.uos.ac.kr/food/placeList.do?rstcde=030&epTicket=LOG")
soup2 = BeautifulSoup(r2.content.decode('utf-8', 'replace'), "html.parser")

Div = soup2.find(id = "day")
Td = Div.find_all('td')

pageId = '1'
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form['id'].value

if pageId == '1':
    menu = findBody[1]
    a = 'active'
    b = ''
    c = ''
elif pageId == '2':
    menu = findBody[2]
    a = ''
    b = 'active'
    c = ''
elif pageId == '3':
    menu = Td[1]
    a = ''
    b = ''
    c = 'active'

print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf=8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="http://localhost/smile/style_api.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
<div class="card">
  <div class="card-header">
    <ul class="nav nav-tabs card-header-tabs">
      <li class="nav-item">
    <a class="nav-link {p1}" href="./food.py?id=1">학생회관1층(중식)</a>
    </li>
    <li class="nav-item">
    <a class="nav-link {p2}" href="./food.py?id=2">학생회관1층(석식)</a>
    </li>
    <li class="nav-item">
    <a class="nav-link {p3}" href="./food.py?id=3">양식당(중식)</a>
    </li>
    </ul>
    </div>
    <div class="card-body">
    <p class="card-text">{menu}</p>'''.format(p1 = a, p2 = b, p3 = c, menu = menu))

print('''
    </div>
    </div>
    </body>
    </html>
    ''')
