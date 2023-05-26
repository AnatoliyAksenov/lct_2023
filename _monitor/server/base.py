import os

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.engine import Connection

conn:Connection = None

def connect():
    global conn
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST', '188.72.108.227')
    engine = create_engine(f'postgresql://{user}:{password}@{host}/postgres')
    conn = engine.connect()


async def get_event(timestamp):
    q = text("""
        select *
          from events
        where event_ts = :timestamp
    """)

    p = {"timestamp": timestamp}

    res = conn.execute(q, p)
    r = res.fetchall()
    cols = list(res.keys())

    return [{c[0]:c[1] for c in zip(cols, x)} for x in r ]


async def get_events_list():
    q = text("""
        select event_ts
          from events
    """)

    res = conn.execute(q)
    r = res.fetchall()
    cols = list(res.keys())

    return [{c[0]:c[1] for c in zip(cols, x)} for x in r ]    

       