import sqlite3
from backend.mal import get_image

def save(anime, episode, url):
    conn = sqlite3.connect("anime.db")
    c = conn.cursor()

    # anime
    c.execute("SELECT id FROM anime WHERE title=?", (anime,))
    row = c.fetchone()

    if row:
        anime_id = row[0]
    else:
        image = get_image(anime)
        c.execute("INSERT INTO anime(title, image) VALUES(?,?)", (anime, image))
        anime_id = c.lastrowid

    # episode
    c.execute("INSERT INTO episodes(anime_id, episode) VALUES(?,?)", (anime_id, episode))
    ep_id = c.lastrowid

    # source
    c.execute("INSERT INTO sources(episode_id, source_name, url) VALUES(?,?,?)",
              (ep_id, "source", url))

    conn.commit()
    conn.close()
