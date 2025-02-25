import sqlite3

# Connect to (or create) the database file in the 'data' folder.
conn = sqlite3.connect('data/transactions.db')
c = conn.cursor()

# Create a table named 'transactions' if it doesn't already exist.
c.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        note TEXT
    )
''')

# Save (commit) the changes and close the connection.
conn.commit()
conn.close()

print("Database and transactions table created successfully!")
