import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def insert_transaction(conn, transaction):
    sql = '''INSERT INTO transactions(type, category, amount, date)
             VALUES(?,?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, transaction)
    conn.commit()
    return cursor.lastrowid

def fetch_transactions(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    return cursor.fetchall()

if __name__ == "__main__":
    conn = create_connection("finance.db")
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")