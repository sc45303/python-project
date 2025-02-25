import pandas as pd
import sqlite3

def load_transactions():
    # Connect to SQLite database and fetch transactions
    conn = sqlite3.connect('data/transactions.db')
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return df
