# import streamlit as st
# import sqlite3
# from datetime import date

# def app():
#     st.title("Income")
#     st.write("Enter your income details:")
#     income_date = st.date_input("Date", date.today())
#     source = st.text_input("Income Source", "Salary")
#     amount = st.number_input("Amount", min_value=0.0, format="%.2f")

#     if st.button("Add Income"):
#         conn = sqlite3.connect('data/transactions.db')
#         c = conn.cursor()
#         # Insert income with a positive amount
#         c.execute("INSERT INTO transactions (date, type, category, amount) VALUES (?, 'income', ?, ?)",
#                   (income_date.strftime('%Y-%m-%d'), source, amount))
#         conn.commit()
#         conn.close()
#         st.success("Income added successfully!")
