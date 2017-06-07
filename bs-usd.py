from bs4 import BeautifulSoup
import urllib.request as req

url = "http://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
res = req.urlopen(url)

soup =BeautifulSoup(res, "html.parser")

price = soup.select_one(".stocksPrice")
price2 = soup.select(".stoksPrice")

print("usd/jpy=", price)
print(price2)
