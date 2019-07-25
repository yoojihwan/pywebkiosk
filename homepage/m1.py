#!/usr/bin/python3
print("content-type:text/html; charset-UTF-8\n")

import bs4
from requests import get
import sys

sys.stdout=open('./menu.txt', 'w')

url="https://www.uos.ac.kr/food/placeList.do?epTicket=LOG"

html=get(url)

bs_obj=bs4.BeautifulSoup(html.content.decode('utf-8', 'replace'), "html.parser")
div=bs_obj.find("div", {"id":"day"})
trs=div.findAll("tr")

print('<!DOCTYPE html>\n<meta charset="utf-8">')
for tr in trs:
    print(tr.encode('ascii'))
