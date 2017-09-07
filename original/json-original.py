import urllib.request as req
import os.path, random
import json

file = open("cryptocurrency_list.json", 'r', encoding='UTF-8').read()
data = json.loads(file)

data = data['Data']

print("Symbol", end=",")
print("ImageURL", end=",")
print("Algorithm", end=",")
print("ProofType", end=",")
print("Api_id", end=",")
print("")
for d in data:

    print(data[d]['Name'], end=",")
    try:
        print(data[d]['ImageUrl'], end=",")
    except:
        print("noimageURL", end=",")
    print(data[d]['CoinName'], end=",")
    print(data[d]['Algorithm'], end=",")
    print(data[d]['ProofType'], end=",")
    print(data[d]['Id'], end=",")
    print("")


