#!/usr/bin/python3
print("content-type:text/html; charset-UTF-8\n")

from bs4 import BeautifulSoup
from requests import get

url="https://www.uos.ac.kr/food/placeList.do?epTicket=LOG"
r=get(url)
soup=BeautifulSoup(r.content.decode('utf-8','replace'), "html.parser")

findDiv = soup.find(id = "day")
findBody = findDiv.find_all('tr')

print('''
        <meta http-equiv="Content-Type" content="text/html" charset="utf-8" />
    ''')

for menu in findBody:
    print(menu.encode('ascii'))
