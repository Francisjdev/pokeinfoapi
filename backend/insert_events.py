def insert_events(events, con, cur):
    for e in events:
        cur.execute('''
            INSERT OR IGNORE INTO events (shop, type, name, address, city, date, url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            e["shop"],
            e["type"],
            e["name"],
            e["street_address"],
            e["city"],
            e["date"],
            e["pokemon_url"]
        ))
    con.commit()
