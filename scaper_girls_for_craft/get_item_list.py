from bs4 import BeautifulSoup
import requests as req
import re

base_url = "http://next.craft-store.jp/products?page="

for i in range(100):
    i = str(i)
    url = base_url + i
    res = req.get(url, auth=('admin', 'admin'))
    soup = BeautifulSoup(res.content, "html.parser")
    check404 = soup.select_one("#zero-search-results-title")
    if check404 != None:
        break

    titles = soup.select(".craft-card-footer .title")
    print(type(titles))
    for title in titles:
        href = title.get("href", ",")
        href = href.replace(" ", "")
        href = '"' +href + '",'
        print(href)
