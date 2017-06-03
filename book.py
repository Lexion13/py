import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 0:
    print("USAGE: hyakunin.py (keyword)")
    sys.exit()

API = "http://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt": "ini",
    "key": "日"
}
params = parse.urlencode(query)
url = API + "?" + params
print("url=", url)

with req.urlopen(url) as r:
    b = r.read
    print(b.decode("utf-8"))
