import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import date

# Utility function to load transaction data from the database
def load_transactions():
    conn = sqlite3.connect('data/transactions.db')
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return df

# Utility function to calculate summary statistics
def calculate_summary(df):
    total_income = df[df['type'] == 'income']['amount'].sum()
    total_expenses = df[df['type'] == 'expense']['amount'].sum()
    savings = total_income - total_expenses
    return total_income, total_expenses, savings

def app():
    st.title("Personal Finance Dashboard")
    st.write("Welcome to your personalized finance dashboard. Here you can see a summary of your income, expenses, and savings, along with detailed visualizations and quick actions.")

    # Load transaction data
    df = load_transactions()
    
    if df.empty:
        st.info("No transactions recorded yet. Start by adding income and expenses.")
    else:
        # --- Summary Section ---
        total_income, total_expenses, savings = calculate_summary(df)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"${total_income:,.2f}")
        col2.metric("Total Expenses", f"${total_expenses:,.2f}")
        col3.metric("Savings", f"${savings:,.2f}")
        
        st.markdown("---")
        
        # --- Expense Breakdown Chart ---
        st.subheader("Expense Breakdown by Category")
        expense_df = df[df['type'] == 'expense']
        if not expense_df.empty:
            category_summary = expense_df.groupby('category')['amount'].sum().reset_index()
            fig = px.pie(category_summary, names='category', values='amount', title='Expenses by Category')
            st.plotly_chart(fig)
        else:
            st.info("No expense data to display chart.")
        
        st.markdown("---")
        
        # --- Recent Transactions ---
        st.subheader("Recent Transactions")
        recent_df = df.sort_values(by='date', ascending=False).head(10)
        st.dataframe(recent_df)
    
    st.markdown("---")
    
    # --- Quick Add Expense Form ---
    st.subheader("Quick Add Expense")
    with st.form("quick_add_expense", clear_on_submit=True):
        expense_date = st.date_input("Date", date.today())
        category = st.selectbox("Category", ["Food", "Transportation", "Entertainment", "Utilities", "Others"])
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        note = st.text_area("Note", height=68)
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            conn = sqlite3.connect('data/transactions.db')
            c = conn.cursor()
            c.execute(
                "INSERT INTO transactions (date, type, category, amount, note) VALUES (?, 'expense', ?, ?, ?)",
                (expense_date.strftime('%Y-%m-%d'), category, amount, note)
            )
            conn.commit()
            conn.close()
            st.success("Expense added successfully!")
            st.experimental_rerun()  # Refresh the page to update the dashboard

if __name__ == '__main__':
    app()
