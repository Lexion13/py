from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req



url = "https://www.craft-store.jp/products?page=3"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
tag = soup.select(".craft-card-footer > .title")
for tags in tag:
	tagtext = tags.attrs["href"]
	print(tagtext,",")
