from db import init_db
from fetch_api import get_events
from insert_events import insert_events

def main():
    con, cur = init_db()
    events = get_events()
    insert_events(events, con, cur)
    con.close()
    print(f"Inserted {len(events)} events.")

if __name__ == "__main__":
    main()
