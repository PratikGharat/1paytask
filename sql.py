import pandas as pd
from sqlalchemy import create_engine

# Define connection to local MySQL 
engine = create_engine("mysql+pymysql://root:mysql123@localhost:3306/bank")

# Load CSV files
transactions_df = pd.read_csv("transactions_dirty.csv")
merchants_df = pd.read_csv("merchants.csv")

# Push to MySQL
transactions_df.to_sql(name='transactions', con=engine, if_exists='replace', index=False)
merchants_df.to_sql(name='merchants', con=engine, if_exists='replace', index=False)

print("Tables loaded successfully!")


