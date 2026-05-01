from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

# 🔥 זה הפתרון ל-CORS
CORS(app)

DB = "anime.db"

def query(q):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(q)
    data = c.fetchall()
    conn.close()
    return data

@app.route("/")
def home():
    return "API is running"

@app.route("/api/latest")
def latest():
    rows = query("""
        SELECT a.id, a.title, e.episode, a.image
        FROM episodes e
        JOIN anime a ON e.anime_id = a.id
        ORDER BY e.id DESC
        LIMIT 10
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
    app.run(host="0.0.0.0", port=5000)
