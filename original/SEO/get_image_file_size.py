from bs4 import BeautifulSoup
import requests
import urllib.request as req
import urllib.parse
from urllib.parse import urlparse as urlparse
import urllib.request
from urllib.parse import urljoin
from os import makedirs
import os.path, time, re
from html.parser import HTMLParser

base_url = "https://www.craft-store.jp"
end_lists = []
url_lists = []

def get_img_size(url):
    soup = req.urlopen(url)
    soup = BeautifulSoup(soup,"html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        img_url = img.get("src")
        if img_url.find("http"):
            img_url = base_url + img_url
        else:
            img_url = img_url
        try:
            img_size = requests.head(img_url)
            img_size.headers
            img_size = int(img_size.headers['content-length'])
            img_size = img_size / 1024
            img_size = int(img_size)
            img_size = str(img_size) + "K"
            print(img_url,img_size)
        except:
            print("this image is not available")


def get_url(url):
    try:
        soup = req.urlopen(url)

        soup = BeautifulSoup(soup,"html.parser")
        links = soup.find_all("a")
        end_lists.append(url)
        for link in links:
            link = link.get("href")
            link = urljoin(base_url, link)
            url_lists.append(link)
            print(link)
            time.sleep(0.1)
    except:
        print("this url is not available")

get_url(base_url)

for url in url_lists:
    if url not in end_lists:
        get_url(url)

'''
for url in url_lists:
    try:
        get_img_size(url)
    except:
        print("Can't scraping")
'''