from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req

url = "http://dev.craft-store.jp/products/redirect-test"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
print(soup)
