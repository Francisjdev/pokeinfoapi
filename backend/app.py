from fastapi import FastAPI
import sqlite3
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://127.0.0.1:5500",
    "https://francisjdev.github.io"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




def fetch_events(query, params=()):
    """Helper function to fetch events from the DB and return as list of dicts."""
    conn = sqlite3.connect("events.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    stores = [dict(row) for row in rows]
    conn.close()
    status = "empty" if not stores else "ok"
    return {"status": status, "events": stores}


@app.get("/events")
def read_root():
    today = date.today().isoformat()
    query = "SELECT shop, type, date, city, address, url FROM events WHERE date >= ?;"
    return fetch_events(query, (today,))


@app.get("/events/porfecha")
def read_by_date(user_date: str = None):
    date_to_use = user_date or date.today().isoformat()
    query = "SELECT shop, type, date, city, address, url FROM events WHERE date = ?;"
    return fetch_events(query, (date_to_use,))


@app.get("/events/porcomuna")
def read_by_city(city: str):
    today = date.today().isoformat()
    query = """
        SELECT shop, type, date, city, address, url
        FROM events
        WHERE city = ? COLLATE NOCASE AND date >= ?;
    """
    return fetch_events(query, (city, today))

@app.get("/events/porcomuna_fecha")
def read_by_city_and_date(city: str = None, user_date: str = None):
    conn = sqlite3.connect("events.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if city ==None and user_date ==None:
        return read_root()
    if city ==None:
        return read_by_date(user_date)
    if user_date is None:
        return read_by_city(city)
    
    query = """
        SELECT shop, type, date, city, address, url
        FROM events
        WHERE city = ? COLLATE NOCASE AND date = ?;
    """
    cur.execute(query, (city, user_date))
    rows = cur.fetchall()
    stores = [dict(row) for row in rows]
    conn.close()

    status = "ok" if stores else "empty"
    return {"status": status, "events": stores}

# handling load up requests from front end
@app.get("/comunas")
def get_comunas():
    conn = sqlite3.connect("events.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    query="SELECT DISTINCT city FROM events;"
    cur.execute(query)
    rows = cur.fetchall()
    cities = [str(row[0]) for row in rows]
    conn.close()
    status = "empty" if not cities else "ok"
    return {"status": status, "comunas": cities}