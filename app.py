import os
from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_conn():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "rootpass"),
        database=os.getenv("DB_NAME", "praktikum"),
    )

@app.route('/')
def hello():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT 'Terhubung ke MySQL!'")
        row = cur.fetchone()
        conn.close()
        return f"Halo dari Flask + Docker + Jenkins! DB: {row[0]}"
    except Exception as e:
        return f"Gagal konek DB: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
