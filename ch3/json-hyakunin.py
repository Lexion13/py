import urllib.request as req
import os.path, random
import json

url = "http://api.aoikujira.com/hyakunin/get.php?fmt=json"
savename = "hyakunin.json"
if not os.path.exists(url):
	req.urlretrieve(url, savename)
print(os.path.exists(url))
data = json.load(open(savename, "r", encoding="UTF-8"))

r = random.choice(data)
print(r['kami'], r['simo'])

