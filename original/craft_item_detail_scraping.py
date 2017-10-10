from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time

urls = [
"https://www.craft-store.jp/products/kimuraglass-waterglass",
"https://www.craft-store.jp/products/kimuraglass-karuta-1x1",
"https://www.craft-store.jp/products/kimuraglass-karuta-1x2",
"https://www.craft-store.jp/products/tasaki-sherry-8oz",
"https://www.craft-store.jp/products/tasaki-liqueur-3oz",
"https://www.craft-store.jp/products/tasaki-light-s-10oz",
"https://www.craft-store.jp/products/tasaki-young-s-12oz",
"https://www.craft-store.jp/products/kimuraglass-porceold",
"https://www.craft-store.jp/products/kimuraglass-lotus-goblet-10oz",
"https://www.craft-store.jp/products/tasaki-aging-20oz",
"https://www.craft-store.jp/products/kimuraglass-table-soysauce",
"https://www.craft-store.jp/products/kimuraglass-droplet",
"https://www.craft-store.jp/products/kimuraglass-crumple-wine-s-set",
"https://www.craft-store.jp/products/tasaki-cocktail-5oz",
"https://www.craft-store.jp/products/tasaki-sparkling-7oz",
"https://www.craft-store.jp/products/tasaki-prototype-s-12oz",
"https://www.craft-store.jp/products/tasaki-port-10oz",

]

print("href", end=",")
print("title", end=",")
print("brand", end=",")
print("price", end=",")
print("shippingdate", end=",")
print("indexstatus", end=",")
print("canonicalstatus", end=",")
print("metatitle", end=",")
print("metadescription", end=",")
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
        indexstatus = soup.find(attrs={"name": "robots"}).get('content')
    except:
        indexstatus = "index"
    try:
        canonicalstatus = soup.find(attrs={"rel": "canonical"}).get('href')
    except:
        canonicalstatus = "nothing"
    metatitle = soup.title
    metatitle = str(metatitle)
    metatitle = metatitle.replace(",", "")
    metadescription = soup.find(attrs={"name": "description"}).get('content')
    metadescription = str(metadescription)
    metadescription = metadescription.replace(",", "")

    metadescription = metadescription.replace(",", '')
    print(href, end=",")
    print(title, end=",")
    print(brand, end=",")
    print(price, end=",")
    print(shippingdate, end=",")
    print(indexstatus, end=",")
    print(canonicalstatus, end=",")
    print(metatitle, end=",")
    print(metadescription, end=",")
    print("")
    time.sleep(1)

'''
If you wanna get only url,
Please be commentout line 21.
'''
# like that
