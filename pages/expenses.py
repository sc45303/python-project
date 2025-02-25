import streamlit as st
import sqlite3
from datetime import date

def app():
    st.title("Expenses")
    st.write("Log your expenses:")
    expense_date = st.date_input("Date", date.today())
    category = st.selectbox("Category", ["Food", "Transportation", "Entertainment", "Utilities", "Others"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    note = st.text_area("Note")

    if st.button("Add Expense"):
        conn = sqlite3.connect('data/transactions.db')
        c = conn.cursor()
        # Insert expense with a negative amount (or store type as 'expense')
        c.execute("INSERT INTO transactions (date, type, category, amount, note) VALUES (?, 'expense', ?, ?, ?)",
                  (expense_date.strftime('%Y-%m-%d'), category, amount, note))
        conn.commit()
        conn.close()
        st.success("Expense added successfully!")
