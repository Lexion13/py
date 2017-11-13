from bs4 import BeautifulSoup
import requests as req
import re

urls = [
    'http://next.craft-store.jp/products/unilloy-22cm-shallow',
    'http://next.craft-store.jp/products/hirotagarasu-syouwamodernglass-cupsaucer'
]


print("href", end=",")
print("admin_url", end=",")
print("title", end=",")
print("brand", end=",")
print("item_name", end=",")
print("price")

for url in urls:
    res = req.get(url, auth=('admin', 'admin'))
    soup = BeautifulSoup(res.content, "html.parser")
    href = url
    admin_url = url.replace("/products", "/admin/products")
    title = soup.select_one(".product-main-info h1").string
    brand = soup.select_one(".product-main-info h2").string
    items = soup.find_all('form', attrs={'action': '/orders/populate'})

    for item in items:
        item = BeautifulSoup(item.content, "html.parser")
        item_name = item.select_one('.product-main-info-item-name')
        item_name = str(item_name)
        item_name = re.sub(r'<(.*?)>', '', item_name)
        price = item.select_one(".product-price")
        price = str(price)
        price = item.find_one('p', attrs={'data-hook': 'product_price'})
        if item_name != "None":
            print(href, admin_url, title, brand,end="")
            print(item_name,price)



'''

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

# like that

'''