from flask import Flask, jsonify
from data_generator import generate_transactions
from etl_pipeline import run_pipeline
from analytics import generate_insights
import pandas as pd
import os

app = Flask(__name__)

@app.route('/pipeline/run', methods=['POST'])
def run_full_pipeline():
    """Triggers the full ETL pipeline"""
    generate_transactions(1000)
    df = run_pipeline()
    return jsonify({
        "message": "Pipeline executed successfully",
        "records_processed": len(df)
    })

@app.route('/analytics', methods=['GET'])
def get_analytics():
    """Returns analytics insights from processed data"""
    if not os.path.exists('processed_transactions.csv'):
        return jsonify({"error": "Run pipeline first via POST /pipeline/run"}), 404
    df = pd.read_csv('processed_transactions.csv')
    df['is_high_value'] = df['amount'] > 10000
    insights = generate_insights(df)
    return jsonify(insights)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "DataPulse Pipeline is running"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)