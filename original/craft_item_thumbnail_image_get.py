from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req



urls = [
	"https://www.craft-store.jp/products",
	"https://www.craft-store.jp/products?page=2",
	"https://www.craft-store.jp/products?page=3",
	"https://www.craft-store.jp/products?page=4"
]
for url in urls:
	res = req.urlopen(url)
	soup = BeautifulSoup(res, "html.parser")

	data_sets = soup.select("#relative-product .craft-card-body a")

	for data_set in data_sets:
		href = data_set.attrs["href"]
		image = data_set.string
		print(data_set)


'''
	images = soup.select("#relative-product .craft-card-body img")
	images = images.get('src')
	print(images)
'''
