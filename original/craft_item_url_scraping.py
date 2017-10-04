from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req

print("href", end=",")
print("title")
urls = []
base_url = "https://www.craft-store.jp/products?keywords=&utf8=%E2%9C%93&page="
for i in range(100):
	if i != 0:
		i = str(i)
		url = base_url + i
		res = req.urlopen(url)
		soup = BeautifulSoup(res, "html.parser")
		check404 = soup.select_one("#zero-search-results-title")
		if check404 != None:
			break
		titles = soup.select(".craft-card-footer .title")
		for title in titles:
			href = title.get("href", ",")
			href = href.replace(" ", "")
#			print(href, end=",")
#			print(title.string, end=",")
#			print(" ")
			urls.append(href)
print(len(urls))

already_fin = []
products_links = []
operand = "products/"
for url in urls:
	if url not in already_fin:
		res = req.urlopen(url)
		soup = BeautifulSoup(res, "html.parser")
		anchors = soup.find_all("a")
		for anchor in anchors:
			anchor = anchor.get("href")
			anchor = str(anchor)
			if operand in anchor:
				products_links.append(anchor)
		already_fin.append(url)

products_links.extend(urls)
link_unique = []

for link in products_links:
	if link not in link_unique:
		link_unique.append(link)
print(link_unique)
print(len(link_unique))

'''
If you wanna get only url,
Please be commentout line 21.
'''
# like that
