import pandas as pd 

#load data
df =  pd.read_csv("transactions_dirty.csv")

df = df.dropna(subset=['transaction_id','txn_amount' ,'status'])# droping missing values 

df['txn_timestamp'] = pd.to_datetime(df['txn_timestamp'], errors='coerce')#convert date and time 
df = df.dropna(subset=['txn_timestamp'])  # Drop invalid dates

#convert txt_amt to numeric
df['txn_amount'] = pd.to_numeric(df['txn_amount'], errors='coerce')

# Standardize status column (lowercase, strip spaces)
df["status"] = df["status"].str.strip().str.lower()

#Create a daily summary
summary = df.groupby(df["txn_timestamp"].dt.date).agg(
    total_txns = ("transaction_id", "count"),
    successful_txns = ("status", lambda x: (x == "success").sum()),
    failed_txns = ("status", lambda x: (x == "failed").sum()),
    total_amount = ("txn_amount", "sum")
).reset_index()

#success_rate on daily transaction
summary["success_rate"] = (summary["successful_txns"] / summary["total_txns"]) * 100

print(summary.head())

#cleaned csv for download
#df.to_csv("transactions_cleaned.csv", index=False)

