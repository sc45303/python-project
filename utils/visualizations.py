import plotly.express as px

def expense_pie_chart(df):
    fig = px.pie(df, names='category', values='amount', title='Expenses by Category')
    return fig
