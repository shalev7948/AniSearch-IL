from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB = "anime.db"

def query(q, args=()):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(q, args)
    data = c.fetchall()
    conn.close()
    return data

@app.route("/api/latest")
def latest():
    rows = query("""
        SELECT e.id, a.title, e.episode, a.image
        FROM episodes e
        JOIN anime a ON e.anime_id = a.id
        ORDER BY e.id DESC
        LIMIT 16
    """)

    return jsonify([
        {
            "id": r[0],
            "title": r[1],
            "episode": r[2],
            "image": r[3]
        } for r in rows
    ])

if __name__ == "__main__":
    app.run(debug=True)
