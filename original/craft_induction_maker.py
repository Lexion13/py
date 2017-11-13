from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time
import datetime

urls = [
"https://www.craft-store.jp/products/2016-bg-coffee-dripper",
]

for url in urls:
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")

    href = url

    Brand = soup.select_one(".product-main-info h2").string
    ItemName = soup.select_one(".product-main-info h1").string
    ItemDetail = soup.select(".product-annotation p")
    ItemDetail = ItemDetail[1]
    ItemPrice = soup.select_one(".product-price").text



    print('''
<div class="row item-foreword2-wrap">
    <div class="col-xs-12 col-sm-5 col-md-5">
        <div class="row">
            <div class="col-xs-5 item-foreword2-image">
                <img src="" class="img-responsive">
            </div>
            <div class="col-xs-7">
                <p class="item-foreword2-brand">{0}</p>
                <p class="item-foreword2-item-name">{1}</p>
                <p class="item-foreword2-price">{4}</p>
            </div>
            <div class="col-xs-12">
                <a class="item-foreword2-btn" href="{3}">ご購入はこちら</a>
            </div>
        </div>
    </div>

</div>

    
    '''.format(Brand,ItemName,ItemDetail,url,ItemPrice))

