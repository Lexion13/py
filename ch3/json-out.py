import json

price = {
	"date": "2017-05-10",
	"price": {
		"apple": 80,
		"fuck":  122,
		"shit": 1212
	}
}
s = json.dumps(price)
print(s)

s = json.loads(s)
print(s)