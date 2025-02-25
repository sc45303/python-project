import streamlit as st
import sqlite3

def app():
    st.title("Budgeting")
    st.write("Set your monthly budget for each category:")

    # Example form for budget input
    category = st.selectbox("Select Category", ["Food", "Transportation", "Entertainment", "Utilities", "Others"])
    budget_amount = st.number_input("Budget Amount", min_value=0.0, format="%.2f")

    if st.button("Set Budget"):
        # For simplicity, save budgets to a local file or database table
        st.success(f"Budget of {budget_amount} set for {category}!")
        # (Implement saving functionality as needed)
