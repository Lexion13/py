import MySQLdb

conn = MySQLdb.connect(
    user = 'root',
    passwd= '',
    host = 'localhost',
    db = 'test')
    
cur = conn.cursor()

cur.execute('DROP TABLE items')
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
''')

data = [('BANANA', 300),('Mango', 640),('fuck', 1200)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES(%s,%s)", i)
    
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)
