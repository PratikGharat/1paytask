# 1paytask

1. Clone the Repository
  
2.Install Dependencies(pip install flask,streamlit,pandas.etc)

3.Run to utils for data summary(run command python utils.py)

4.Run the Flask API(python app.py)
API Endpoints
GET /summary?merchant_id=...&date=...
GET /failures?reseller_id=..

5.Run the Streamlit Dashboard(streamlit run app.py)

#uploaded sql.py to show how to connect to local database through python 
#for data(csv file) go to the data folder

# Part 4 – SQL Challenge 
Q1. List Top 5 Merchants by Transaction Amount in the ‘North’ Region

SELECT 
    m.merchant_id,
    m.merchant_name,
    SUM(t.txn_amount) AS total_amount
FROM 
    transactions t
JOIN 
    merchants m ON t.merchant_id = m.merchant_id
WHERE 
    m.region = 'North'
GROUP BY 
    m.merchant_id, m.merchant_name
ORDER BY 
    total_amount DESC
LIMIT 5;

![Screenshot 2025-04-22 164050](https://github.com/user-attachments/assets/8b8bcc13-a20c-4353-a1c5-64b9d59dba0a)

Q2. Find merchants who had more than 10 failed transactions in a single day.

SELECT 
    m.merchant_id, 
    m.merchant_name, 
    DATE(t.txn_timestamp) AS txn_date, 
    COUNT(*) AS failed_txns
FROM 
    transactions t
JOIN 
    merchants m ON t.merchant_id = m.merchant_id
WHERE 
    t.status = 'FAILED'
    AND DATE(txn_timestamp) = DATE(t.txn_timestamp)
GROUP BY 
    m.merchant_id, DATE(t.txn_timestamp)
HAVING 
    COUNT(*) > 10;
    
![image](https://github.com/user-attachments/assets/a3133f76-ec79-4376-a97a-193239008d9c)





