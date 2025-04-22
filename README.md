# 1paytask



#uploaded sql.py to show how to connect to local database through python 
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
    t.status = 'failed'
GROUP BY 
    m.merchant_id, txn_date
HAVING 
    failed_txns > 10;
![image](https://github.com/user-attachments/assets/8abc6f66-301b-4b6d-a3a9-dc7ebc00cc56)



