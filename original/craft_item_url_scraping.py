from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req

print("href", end=",")
print("ttle")

base_url = "https://www.craft-store.jp/products/"
for i in range(100):
	if i != 0:
		i = str(i)
		url = base_url + "?page=" + i
		res = req.urlopen(url)
		soup = BeautifulSoup(res, "html.parser")
		check404 = soup.select_one("#zero-search-results-title")
		if check404 != None:
			break
		titles = soup.select(".craft-card-footer .title")
		for title in titles:
			href = title.get("href", ",")
			href = href.replace(" ", "")
			print(href, end=",")
			print(title.string, end=",")
			print(" ")

'''
If you wanna get only url,
Please be commentout line 21.
'''
# like that
