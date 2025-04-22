import pandas as pd 

#load data
df =  pd.read_csv("transactions_dirty.csv")

df = df.dropna(subset=['transaction_id', 'txn_timestamp', 'txn_amount' ,'status'])# droping missing values

df['txn_timestamp'] = pd.to_datetime(df['txn_timestamp'], errors='coerce')#convert date and time 
df = df.dropna(subset=['txn_timestamp'])  # Drop invalid dates

#convert txt_amt to numeric
df['txn_amount'] = pd.to_numeric(df['txn_amount'], errors='coerce')

# Standardize status column (lowercase, strip spaces)
df["status"] = df["status"].str.strip().str.lower()



#Create a daily summary
# Create summary grouped by date
summary = df.groupby(df["txn_timestamp"].dt.date).agg(
    total_txns = ("transaction_id", "count"),
    successful_txns = ("status", lambda x: (x == "success").sum()),
    failed_txns = ("status", lambda x: (x == "failed").sum()),
    total_amount = ("txn_amount", "sum")
).reset_index()

#s
summary["success_rate"] = (summary["successful_txns"] / summary["total_txns"]) * 100
summary["rolling_avg_amount"] = summary["total_amount"].rolling(window=7).mean()
peak_day = summary.loc[summary["total_amount"].idxmax()]
print("Peak transaction day:\n", peak_day)



print(summary.head())
print(summary.tail())

#cleaned csv for download
#df.to_csv("transactions_cleaned.csv", index=False)

