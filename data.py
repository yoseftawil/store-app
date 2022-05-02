import sqlite3


conn = sqlite3.connect('webapp.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS store")
c.execute("""CREATE TABLE store (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)""")

conn.commit()
conn.close()


# Fetch query. 
# Param: String 
def select(query):
    conn = sqlite3.connect('webapp.db')
    c = conn.cursor()

    if query is not None:
        c.execute("SELECT * FROM store WHERE name LIKE ? ORDER BY id DESC", ('%' + query + '%',))
    else:
        c.execute("SELECT * FROM store")

    results = c.fetchall()
    conn.close()

    return results

# Add product to DB.
# Param: Tuple with name and price
def insert(args):
    conn = sqlite3.connect('webapp.db')
    c = conn.cursor()

    c.execute("INSERT INTO store VALUES (?, ?, ?)", args)
    conn.commit()
    conn.close()

# Delete product to DB.
# Param: id of product
def delete(id):
    conn = sqlite3.connect('webapp.db')
    c = conn.cursor()

    c.execute("DELETE FROM store WHERE id=?", (id,))
    conn.commit()
    conn.close()

