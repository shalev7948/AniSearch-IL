from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

DB = "database/anime.db"


def query(q):
    try:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute(q)
        data = c.fetchall()
        conn.close()
        return data
    except Exception as e:
        print("DB ERROR:", e)
        return []


@app.route("/")
def home():
    return "API is running"


@app.route("/api/latest")
def latest():
    rows = query("""
        SELECT e.id, a.title, e.episode, a.image
        FROM episodes e
        JOIN anime a ON e.anime_id = a.id
        ORDER BY e.id DESC
        LIMIT 16
    """)

    # אם אין נתונים → נחזיר דמו
    if not rows:
        return jsonify([
            {
                "id": 1,
                "title": "Naruto",
                "episode": 1,
                "image": "https://via.placeholder.com/150"
            },
            {
                "id": 2,
                "title": "One Piece",
                "episode": 1070,
                "image": "https://via.placeholder.com/150"
            }
        ])

    return jsonify([
        {
            "id": r[0],
            "title": r[1],
            "episode": r[2],
            "image": r[3]
        } for r in rows
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
