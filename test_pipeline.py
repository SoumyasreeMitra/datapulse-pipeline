import pandas as pd
from data_generator import generate_transactions
from etl_pipeline import extract, transform, load
from analytics import generate_insights

def test_data_generation():
    df = generate_transactions(100)
    assert len(df) == 100
    assert 'transaction_id' in df.columns
    assert 'amount' in df.columns

def test_transform():
    df = generate_transactions(100)
    df.to_csv('test_transactions.csv', index=False)
    raw = extract('test_transactions.csv')
    clean = transform(raw)
    assert len(clean) > 0
    assert 'month' in clean.columns
    assert 'is_high_value' in clean.columns

def test_analytics():
    df = generate_transactions(100)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df[df['status'] == 'success'].copy()
    df['is_high_value'] = df['amount'] > 10000
    df['hour'] = df['timestamp'].dt.hour
    df['month'] = df['timestamp'].dt.month
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['amount_normalized'] = 0.5
    insights = generate_insights(df)
    assert 'total_transactions' in insights
    assert 'by_category' in insights