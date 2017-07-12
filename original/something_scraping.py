from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time

urls = [
	"http://www.azuma-web.co.jp/products/detail.php?product_id=433",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=432",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=430",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=429",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=427",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=425",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=424",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=423",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=421",
	"http://www.azuma-web.co.jp/products/detail.php?product_id=420"
]


for url in urls:
	res = req.urlopen(url)
	soup = BeautifulSoup(res, "html.parser")
	href = url
	price = soup.select_one(".sale_price").string.strip()
	price = price.replace("\n", '')
	price = price.replace("\r", '')
	id = soup.select_one(".product_info dd").string.strip()
	name = soup.select_one("#detailarea .title").string
	print(url, ",", end="")
	print(name, ",", end="")
	print(price, ",", end="")
	print(id, ",", end="")
	print("")
	time.sleep(1)
