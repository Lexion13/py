from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}
urls = [
"https://cryptocoincharts.info/coins/show/bch",
"https://cryptocoincharts.info/coins/show/btc",
"https://cryptocoincharts.info/coins/show/eth",
"https://cryptocoincharts.info/coins/show/dash",
"https://cryptocoincharts.info/coins/show/iot",
"https://cryptocoincharts.info/coins/show/bcc",
"https://cryptocoincharts.info/coins/show/omg",
"https://cryptocoincharts.info/coins/show/ybc",
"https://cryptocoincharts.info/coins/show/ltc",
"https://cryptocoincharts.info/coins/show/zec",
"https://cryptocoincharts.info/coins/show/neo",
"https://cryptocoincharts.info/coins/show/xrp",
"https://cryptocoincharts.info/coins/show/qtum",
"https://cryptocoincharts.info/coins/show/xmr",
"https://cryptocoincharts.info/coins/show/eos",
"https://cryptocoincharts.info/coins/show/etc",
"https://cryptocoincharts.info/coins/show/mco",
"https://cryptocoincharts.info/coins/show/pay",
"https://cryptocoincharts.info/coins/show/adx",
"https://cryptocoincharts.info/coins/show/lsk",
"https://cryptocoincharts.info/coins/show/snt",
"https://cryptocoincharts.info/coins/show/bts",
"https://cryptocoincharts.info/coins/show/ico",
"https://cryptocoincharts.info/coins/show/strat",
"https://cryptocoincharts.info/coins/show/cvc",
"https://cryptocoincharts.info/coins/show/waves",
"https://cryptocoincharts.info/coins/show/bat",
"https://cryptocoincharts.info/coins/show/mtl",
"https://cryptocoincharts.info/coins/show/xem",
"https://cryptocoincharts.info/coins/show/nxt",
"https://cryptocoincharts.info/coins/show/ark",
"https://cryptocoincharts.info/coins/show/synx",
"https://cryptocoincharts.info/coins/show/gnt",
"https://cryptocoincharts.info/coins/show/fct",
"https://cryptocoincharts.info/coins/show/sc",
"https://cryptocoincharts.info/coins/show/sys",
"https://cryptocoincharts.info/coins/show/dgb",
"https://cryptocoincharts.info/coins/show/exp",
"https://cryptocoincharts.info/coins/show/unb",
"https://cryptocoincharts.info/coins/show/edg",
"https://cryptocoincharts.info/coins/show/gbyte",
"https://cryptocoincharts.info/coins/show/qrl",
"https://cryptocoincharts.info/coins/show/pivx",
"https://cryptocoincharts.info/coins/show/safex",
"https://cryptocoincharts.info/coins/show/storj",
"https://cryptocoincharts.info/coins/show/ubq",
"https://cryptocoincharts.info/coins/show/doge",
"https://cryptocoincharts.info/coins/show/mue",
"https://cryptocoincharts.info/coins/show/geo",
"https://cryptocoincharts.info/coins/show/san",
"https://cryptocoincharts.info/coins/show/tkn",
"https://cryptocoincharts.info/coins/show/ardr",
"https://cryptocoincharts.info/coins/show/game",
"https://cryptocoincharts.info/coins/show/trust",
"https://cryptocoincharts.info/coins/show/tmc",
"https://cryptocoincharts.info/coins/show/xvg",
"https://cryptocoincharts.info/coins/show/fun",
"https://cryptocoincharts.info/coins/show/lbc",
"https://cryptocoincharts.info/coins/show/hmq",
"https://cryptocoincharts.info/coins/show/xel",
"https://cryptocoincharts.info/coins/show/qwark",
"https://cryptocoincharts.info/coins/show/crw",
"https://cryptocoincharts.info/coins/show/oax",
"https://cryptocoincharts.info/coins/show/xzc",
"https://cryptocoincharts.info/coins/show/ant",
"https://cryptocoincharts.info/coins/show/sngls",
"https://cryptocoincharts.info/coins/show/dcr",
"https://cryptocoincharts.info/coins/show/1st",
"https://cryptocoincharts.info/coins/show/bnt",
"https://cryptocoincharts.info/coins/show/ptoy",
"https://cryptocoincharts.info/coins/show/zcc",
"https://cryptocoincharts.info/coins/show/lun",
"https://cryptocoincharts.info/coins/show/nmr",
"https://cryptocoincharts.info/coins/show/bay",
"https://cryptocoincharts.info/coins/show/steem",
"https://cryptocoincharts.info/coins/show/dct",
"https://cryptocoincharts.info/coins/show/xlm",
"https://cryptocoincharts.info/coins/show/icn",
"https://cryptocoincharts.info/coins/show/cfi",
"https://cryptocoincharts.info/coins/show/sigma",
"https://cryptocoincharts.info/coins/show/vtc",
"https://cryptocoincharts.info/coins/show/snm",
"https://cryptocoincharts.info/coins/show/wings",
"https://cryptocoincharts.info/coins/show/maid",
"https://cryptocoincharts.info/coins/show/mcap",
"https://cryptocoincharts.info/coins/show/rdd",
"https://cryptocoincharts.info/coins/show/mgo",
"https://cryptocoincharts.info/coins/show/kore",
"https://cryptocoincharts.info/coins/show/stx",
"https://cryptocoincharts.info/coins/show/rlc",
"https://cryptocoincharts.info/coins/show/kmd",
"https://cryptocoincharts.info/coins/show/myst",
"https://cryptocoincharts.info/coins/show/draco",
"https://cryptocoincharts.info/coins/show/trig",
"https://cryptocoincharts.info/coins/show/xcp",
"https://cryptocoincharts.info/coins/show/rep",
"https://cryptocoincharts.info/coins/show/dgd",
"https://cryptocoincharts.info/coins/show/etp",
"https://cryptocoincharts.info/coins/show/round",
"https://cryptocoincharts.info/coins/show/blk"
]

print("url", end=",")
print("name", end=",")
print("symbol", end=",")
print("description", end=",")
print("algorithm", end=",")
print("website", end=",")
print("")

for url in urls:
	set = req.Request(url = url, headers = headers)
	res = req.urlopen(set)
	soup = BeautifulSoup(res, "html.parser")
	print(url, end=",")
	td = soup.select("td")
	for cel in td:
		print(cel.string, end=",")

	print("")
