import sqlite3


def create_db():
    DB_FILE = 'database.db'
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # создаем таблицу, если она еще не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS audio (
                        id INTEGER PRIMARY KEY,
                        name_audio TEXT,
                        hash_audio TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                            id INTEGER PRIMARY KEY,
                            result TEXT,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        )''')
    conn.commit()
    conn.close()
