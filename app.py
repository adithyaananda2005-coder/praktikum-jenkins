import os
import time
from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_conn():
    last_err = None
    for _ in range(10):
        try:
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "db"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "rootpass"),
                database=os.getenv("DB_NAME", "praktikum"),
            )
        except Exception as e:
            last_err = e
            time.sleep(3)
    raise last_err

@app.route('/')
def index():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS kunjungan (id INT AUTO_INCREMENT PRIMARY KEY, waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cur.execute("INSERT INTO kunjungan () VALUES ()")
        conn.commit()
        cur.execute("SELECT COUNT(*) FROM kunjungan")
        total = cur.fetchone()[0]
        conn.close()
        return f"Halo dari Flask + Docker + Jenkins! Terhubung ke MySQL. Total kunjungan tersimpan di database: {total}"
    except Exception as e:
        return f"Gagal konek DB: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
