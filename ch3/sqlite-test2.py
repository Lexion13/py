import sqlite3
#connect database
filepath = "test2sqlite"
conn = sqlite3.connect(filepath)

#create table
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )
''')
cur = conn.cursor()
data = [("Mango", 700), ("Kiwi", 400), ("Grape", 800), ("Peach", 940), ("Persimmon", 700), ("Banana", 400)]
cur.executemany(
    "INSERT INTO items(name, price) VALUES (?,?)",
    data
)
conn.commit()

cur = conn.cursor()
price_range = (400, 700)
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?",
    price_range
)

fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)
