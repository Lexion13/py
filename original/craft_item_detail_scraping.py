from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re


urls = [
	"https://www.craft-store.jp/products/nagae-form-bamboo-set",
	"https://www.craft-store.jp/products/nagae-ratio-square-l",
	"https://www.craft-store.jp/products/nagae-ratio-square-m",
	"https://www.craft-store.jp/products/nagae-ratio-square-s",
	"https://www.craft-store.jp/products/siwa-clutchbag-l",
	"https://www.craft-store.jp/products/siwa-clutchbag-m",
	"https://www.craft-store.jp/products/siwa-lunchibag",
	"https://www.craft-store.jp/products/siwa-shoulderbag",
	"https://www.craft-store.jp/products/siwa-slipper-l",
	"https://www.craft-store.jp/products/siwa-slipper-s",
	"https://www.craft-store.jp/products/tsuki-bowl-120",
	"https://www.craft-store.jp/products/tsuki-bowl-170",
	"https://www.craft-store.jp/products/tsuki-flatplate-190",
	"https://www.craft-store.jp/products/tsuki-flatplate-230"
]

print("href", ",", end="")
print("title", ",", end="")
print("brand", ",", end="")
print("price", ",", end="")
print("shippingdate", ",", end="")
print("indexstatus", ",", end="")
print("canonicalstatus", ",", end="")
print("metatitle", ",", end="")
print("metadescription", ",", end="")
print("")

for url in urls:
	res = req.urlopen(url)
	soup = BeautifulSoup(res, "html.parser")
	'''
	get list
	href
	title
	brand
	price
	shipping date
	index status
	canonical status
	meta title
	meta description
	
	'''
	href = url
	title = soup.select_one(".product-main-info h1").string
	brand = soup.select_one(".product-main-info h2").string
	price = soup.select_one(".product-main-info .product-price").text
	price = re.split(r'円', price)
	price = price[0]
	price = price.strip()
	price = price.replace(",", "")
	shippingdate = soup.select_one("#product-shipping-time").text
	shippingdate = shippingdate.strip()
	try:
		indexstatus = soup.find(attrs={"name":"robots"}).get('content')
	except:
		indexstatus = "index"
	try:
		canonicalstatus = soup.find(attrs={"rel":"canonical"}).get('href')
	except:
		canonicalstatus = "nothing"
	metatitle = soup.select_one("title")
	metadescription = soup.find(attrs={"name": "description"}).get('content')

	print(href, ",", end="")
	print(title, ",", end="")
	print(brand, ",", end="")
	print(price, ",", end="")
	print(shippingdate, ",", end="")
	print(indexstatus, ",", end="")
	print(canonicalstatus, ",", end="")
	print(metatitle, ",", end="")
	print(metadescription, ",", end="")
	print("")



'''
If you wanna get only url,
Please be commentout line 21.
'''
# like that
