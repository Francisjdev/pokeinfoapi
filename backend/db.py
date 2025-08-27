import sqlite3

def init_db():
    con = sqlite3.connect("events.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shop TEXT NOT NULL,
        type TEXT NOT NULL,
        name TEXT NOT NULL,
        address TEXT,
        city TEXT NOT NULL,
        date TEXT NOT NULL,
        url TEXT,
        UNIQUE(name, shop, date,address, url)
    );''')

    con.commit()
    return con, cur
