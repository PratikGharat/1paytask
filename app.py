import streamlit as st
import pandas as pd


# Load and clean data
def load_data():
    df = pd.read_csv("transactions_dirty.csv")
    df = df.dropna(subset=['txn_amount', 'status'])
    df['txn_timestamp'] = pd.to_datetime(df['txn_timestamp'], errors='coerce', infer_datetime_format=True)
    df = df.dropna(subset=['txn_timestamp'])
    df = df[df['txn_amount'] > 0]
    df['date'] = df['txn_timestamp'].dt.date
    return df

data = load_data()

st.title("Transaction Dashboard")

# Sidebar filters
selected_date = st.date_input("Select Date", value=pd.to_datetime("2024-04-01").date())

"""#want start and end date 
start_date = st.sidebar.date_input("Start Date", value=data['date'].min())
end_date = st.sidebar.date_input("End Date", value=data['date'].max())
"""
merchant_ids = sorted(data['merchant_id'].unique())
selected_merchant = st.selectbox("Select Merchant", merchant_ids)

# Filtered data
filtered = data[(data['merchant_id'] == selected_merchant) & (data['date'] == selected_date)]

"""#if you want start and end date run this code and comment above line
filtered = data[
    (data['merchant_id'] == selected_merchant) &
    (data['date'] >= start_date) &
    (data['date'] <= end_date)
]
"""
# Transaction volume over time (line chart)
daily_counts = data[data['merchant_id'] == selected_merchant].groupby('date')['transaction_id'].count()
st.subheader("Daily Transaction Volume")
st.line_chart(daily_counts)

# Success vs Failure (bar chart)
st.subheader("Success vs Failure on Selected Date")
status_counts = filtered['status'].value_counts()
st.bar_chart(status_counts)

# Optional: Download button
st.subheader("Download Filtered Data")
st.download_button(
    label="Download CSV",
    data=filtered.to_csv(index=False),
    file_name=f"transactions_{selected_merchant}_{selected_date}.csv",
    mime='text/csv'
)

"""
# Optional: Download button
st.subheader("Download Filtered Data")
csv_data = filtered.to_csv(index=False)
file_name = f"transactions_{selected_merchant}_{start_date}_to_{end_date}.csv"

st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name=file_name,
    mime='text/csv'
)
"""
