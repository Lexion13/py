from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import requests as req
import re
import sys

url = "http://next.craft-store.jp/"
user = "admin"
pw = "admin"

r = req.get(url,auth=('admin', 'admin'))
soup = BeautifulSoup(r.content, "html.parser")
meta_title = soup.title
print(meta_title)
