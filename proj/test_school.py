#!/usr/bin/python3
#-*- coding: utf-8 -*-
 
import sys
import codecs
import cgitb
cgitb.enable()
  
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("content-type: text/html; charset=UTF-8\n")

from bs4 import BeautifulSoup
from requests import get
import cgi, os, re

url = "https://uos.ac.kr/korNotice/list.do?list_id=FA2&epTicket=LOG#"
get_url = get(url)
soup = BeautifulSoup(get_url.content.decode('utf-8', 'replace'), "html.parser")

findCls = soup.find(class_ = "listType")
findBody = findCls.find_all('a')

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

addr_result = list()
title_strip = list()
final_result = list()

for addr in findBody:
    try:
        if re.match('fnView',addr['onclick']):
            addr_id = addr['onclick'][::-1]
            addr_id = addr_id[3:7]
            addr_id = addr_id[::-1]
            addr_result.append(addr_id)
    except:pass

for name in findBody:
        title_strip.append(name.text)
title_result = remove_values_from_list(title_strip,'\n\n')

for exam in range(len(title_result)-10, len(title_result)):
    title_result[exam] = title_result[exam][4:]

for i in range(0,len(title_result)):
    process = [addr_result[i], title_result[i]]
    final_result.append(process)

listStr = ''
for list in final_result:
    listStr += '<li class="list-group-item"><a href="/proj/test_desc_school.py?id={addr}">{title}</a></li>'.format(addr = list[0], title = list[1])

print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf=8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="http://localhost/smile/style_api.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <ul class="list-group list-group-flush">
        {listStr}
    </ul>
</body>
</html>
'''.format(listStr = listStr))
