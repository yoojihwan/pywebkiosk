#!/usr/bin/python3
print("content-type:text/html; charset-UTF-8\n")

from bs4 import BeautifulSoup
from requests import get
import cgi

url="https://www.uos.ac.kr/food/placeList.do?epTicket=LOG"
r=get(url)
soup=BeautifulSoup(r.content.decode('utf-8', 'replace'), "html.parser")
findDiv = soup.find(id = "day")
findBody = findDiv.find_all('td')

pageId = '1'
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form['id'].value

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
      <li class="nav-item">''')

if pageId == '1':
    print('''
    <a class="nav-link active" href="./1.py?id=1">lunch</a>
    </li>
    <li class="nav-item">
    <a class="nav-link" href="./1.py?id=2">dinner</a>
    </li>
    </ul>
    </div>
    <div class="card-body">
    <p class="card-text">{menu}</p>'''.format(menu = findBody[1].encode('ascii')))

elif pageId == '2':
    print('''
    <a class="nav-link" href="./1.py?id=1">lunch</a>
    </li>
    <li class="nav-item">
    <a class="nav-link active" href="./1.py?id=2">dinner</a>
    </li>
    </ul>
    </div>
    <div class="card-body">
    <p class="card-text">{menu}</p>'''.format(menu = findBody[2].encode('ascii')))

print('''
  </div>
</div>
</div>
</div>
</body>
</html>
''')
