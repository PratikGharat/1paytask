from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load and clean data function
def load_data():
    df = pd.read_csv("transactions_dirty.csv")
    df = df.dropna(subset=['txn_amount', 'status'])#droping txt_amnt and status some values are missing
    df['txn_timestamp'] = pd.to_datetime(df['txn_timestamp'], errors='coerce', infer_datetime_format=True)#converting date and time 
    df = df.dropna(subset=['txn_timestamp'])#droping invalid date and time
    df = df[df['txn_amount'] > 0] #will fetch only positive transactions
    df['date'] = df['txn_timestamp'].dt.date   #extracting only the date 
    return df


# Initial load
data = load_data()

@app.route("/summary", methods=['GET'])
def get_summary():
    merchant_id = request.args.get("merchant_id")
    date_str = request.args.get("date")

    if not merchant_id or not date_str:
        return jsonify({"error": "merchant_id and date are required"}), 400

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    filtered = data[(data['merchant_id'] == merchant_id) & (data['date'] == date_obj)]
    total_txns = len(filtered)
    successful_txns = (filtered['status'] == 'SUCCESS').sum()
    failed_txns = (filtered['status'] == 'FAILED').sum()
    total_amount = filtered['txn_amount'].sum()

    return jsonify({
    "merchant_id": merchant_id,
    "date": str(date_obj),
    "total_txns": int(total_txns),
    "successful_txns": int(successful_txns),
    "failed_txns": int(failed_txns),
    "total_amount": total_amount
    })

@app.route("/failures", methods=['GET'])
def get_failures():
    reseller_id = request.args.get("reseller_id")
    if not reseller_id:
        return jsonify({"error": "reseller_id is required"}), 400

    failed_txns = data[(data['reseller_id'] == reseller_id) & (data['status'] == 'FAILED')]

    """To convert GMT to IST
    failed_txns['txn_timestamp'] = failed_txns['txn_timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S IST')
    failed_txns['date'] = pd.to_datetime(failed_txns['date']).dt.strftime('%Y-%m-%d')
    """

    return jsonify(failed_txns.to_dict(orient="records"))

@app.route("/reload", methods=['POST'])
def reload_data():
    global data
    data = load_data()
    return jsonify({"status": "Data reloaded successfully"})

if __name__ == '__main__':
    app.run(debug=True)


