from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req

base_url = "https://www.craft-store.jp/products?page="

for i in range(10):
	if i > 0:
		access_url = base_url + str(i)
		res = req.urlopen(access_url)
		soup = BeautifulSoup(res, "html.parser")
		check404 = soup.select_one("#zero-search-results-title")
		if check404 != None:
			break
		items = soup.select("#relative-product .craft-card-in")
		for item in items:
			item = "<html><body>" + str(item) + "</body></html>"
			item = BeautifulSoup(item, "html.parser")
			try:
				image = item.find("img").get("src")
				href = item.find("a").get("href")
				print(href,",",image)

			except:
				print(" fuck you ! ")
