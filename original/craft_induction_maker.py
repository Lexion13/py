from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time
import datetime

urls = [
"https://www.craft-store.jp/products/gatomikio-waqwa-cup-s",
]

for url in urls:
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")

    href = url

    Brand = soup.select_one(".product-main-info h2").string
    ItemName = soup.select_one(".product-main-info h1").string
    ItemDetail = soup.select(".product-annotation p")
    ItemDetail = ItemDetail[1]



    print('''
    <div class="item-foreword-wrap">
        <h2 class="item-foreword-title">ご購入はこちら</h2>
        <div class="item-foreword-box">
            <div class="row">
                <div class="col-xs-4 col-sm-3">
                    <img src="" alt="{1}" class="img-responsive center-block">
                </div>
                <div class="col-xs-8 co-sm-9">
                    <h2>{1}</h2>
                    <h3>{0}</h3>
                    {2}
               </div>
               <a class="item-foreword-fixed-link" href="{3}">商品ページへ</a>
            </div>
        </div>
    </div>
    
    '''.format(Brand,ItemName,ItemDetail,url))

