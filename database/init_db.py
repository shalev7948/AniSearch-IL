import sqlite3

conn = sqlite3.connect("anime.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS anime(
    id INTEGER PRIMARY KEY,
    title TEXT,
    image TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS episodes(
    id INTEGER PRIMARY KEY,
    anime_id INTEGER,
    episode INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS sources(
    id INTEGER PRIMARY KEY,
    episode_id INTEGER,
    source_name TEXT,
    url TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS notified(
    episode_id INTEGER UNIQUE
)
""")

conn.commit()
conn.close()

print("DB READY")
