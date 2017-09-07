from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time
import datetime

urls = [
"https://www.craft-store.jp/products/ha-65-indigo",
"https://www.craft-store.jp/t/teburuuea",
"https://www.craft-store.jp/products/nosaku_kago_square_m",
"https://www.craft-store.jp/products/unilloy-22cm?taxon_id=1",
"https://www.craft-store.jp/products/g1208-fuji?taxon_id=1",
"https://www.craft-store.jp/products/suzuko_mug",
"https://www.craft-store.jp/products/unilloy-20cm?taxon_id=1",
"https://www.craft-store.jp/features-tags/%E4%BE%BF%E5%88%A9",
"https://www.craft-store.jp/features-tags/%E9%8C%AB%E5%99%A8",
"https://www.craft-store.jp/features-tags/%E6%99%A9%E9%85%8C",
"https://www.craft-store.jp/features-tags/%E7%99%BA%E8%A6%8B",
"https://www.craft-store.jp/products/ha-65?taxon_id=1",
"https://www.craft-store.jp/features-tags/%E9%99%B6%E7%A3%81%E5%99%A8",
"https://www.craft-store.jp/features-tags/%E6%B3%A2%E4%BD%90%E8%A6%8B%E7%84%BC",
"https://www.craft-store.jp/products/nosaku_kago_square_m?taxon_id=1",
"https://www.craft-store.jp/t/za-huo-slash-xiao-wu",
"https://www.craft-store.jp/features-tags/HASAMI",
"https://www.craft-store.jp/products/ha-65",
"https://www.craft-store.jp/products/suzuko_old?taxon_id=1",
"https://www.craft-store.jp/products/5091903",
"https://www.craft-store.jp/features-tags/%E3%82%A2%E3%82%A4%E3%83%87%E3%82%A2",
"https://www.craft-store.jp/t/ge-zhi-pin",
"https://www.craft-store.jp/products/g1208-fuji",
"https://www.craft-store.jp/products/16-1-1?taxon_id=1",
"https://www.craft-store.jp/products/rice-wine-glass-for-sake?taxon_id=1",
"https://www.craft-store.jp/products/16-1-1",
"https://www.craft-store.jp/t/dining"

]

print("href,", end="")
print("404 status")

for url in urls:
    '''
    get list
        href
        404 status
    '''
    href = url
    try:
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        soup.select_one(".error-title")
        status_404 = "available"

    except:
        status_404 = "404 or something error"


    print(href, end=",")
    print(status_404,)
