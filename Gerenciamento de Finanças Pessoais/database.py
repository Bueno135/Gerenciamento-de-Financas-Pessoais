import sqlite3
import os

def create_connection(db_file):
    """Cria uma conexão com o banco de dados SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexão com o banco de dados '{db_file}' estabelecida.")  # Debug
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def create_table(conn):
    """Cria a tabela 'transactions' se ela não existir."""
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
        print("Tabela 'transactions' criada com sucesso.")  # Debug
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")

def insert_transaction(conn, transaction):
    """Insere uma nova transação na tabela 'transactions'."""
    sql = '''INSERT INTO transactions(type, category, amount, date)
             VALUES(?,?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, transaction)
    conn.commit()
    return cursor.lastrowid

def fetch_transactions(conn):
    """Busca todas as transações da tabela 'transactions'."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    return cursor.fetchall()

if __name__ == "__main__":
    # Cria o banco de dados e a tabela se não existirem
    db_file = "finance.db"
    conn = create_connection(db_file)
    if conn is not None:
        create_table(conn)
    else:
        print("Erro! Não foi possível estabelecer a conexão com o banco de dados.")