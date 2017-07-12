from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req


urls = [
	"https://www.craft-store.jp/products",
	"https://www.craft-store.jp/products?page=2",
	"https://www.craft-store.jp/products?page=3",
	"https://www.craft-store.jp/products?page=4",
	"https://www.craft-store.jp/products?page=5",
	"https://www.craft-store.jp/products?page=6",
	"https://www.craft-store.jp/products?page=7",
]
for url in urls:
	res = req.urlopen(url)
	soup = BeautifulSoup(res, "html.parser")
	titles = soup.select(".craft-card-footer .title")
	for title in titles:
#		print(title.string, ",", end="")
		print(title.get("href"), ",")

'''
If you wanna get only url,
Please be commentout line 21.
'''
# like that
