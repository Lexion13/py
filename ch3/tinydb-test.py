from tinydb import TinyDB, Query

filepath = "test-tynydb.json"
db = TinyDB(filepath)

db.purge_table('fruits')

table = db.table('fruits')

table.insert( {'name': 'Banana', 'price': 600} )
table.insert( {'name': 'Fuck', 'price':9999} )
table.insert( {'name': 'Fuck me', 'price':1234} )

print(table.all())

Item = Query()
res = table.search(Item.name == "Fuck me")
print('Fuck me is...', res[0]['price'])

print("price ?")
res = table.search(Item.price >= 1000)
for it in res:
    print("-", it['name'])
