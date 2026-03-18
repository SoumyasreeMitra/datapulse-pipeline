import pandas as pd
import numpy as np

def generate_insights(df):
    """
    Synthesizes key business insights from processed transaction data.
    Mimics real-world financial analytics used in banking systems.
    """
    insights = {}

    # 1. Total transaction volume
    insights['total_transactions'] = len(df)
    insights['total_volume'] = round(df['amount'].sum(), 2)
    insights['average_transaction'] = round(df['amount'].mean(), 2)

    # 2. Category breakdown
    category_stats = df.groupby('category')['amount'].agg([
        ('total', 'sum'),
        ('count', 'count'),
        ('average', 'mean')
    ]).round(2)
    insights['by_category'] = category_stats.to_dict()

    # 3. City-wise spending
    city_stats = df.groupby('city')['amount'].sum().round(2)
    insights['by_city'] = city_stats.to_dict()

    # 4. Peak transaction hours
    hourly = df.groupby('hour')['amount'].count()
    insights['peak_hour'] = int(hourly.idxmax())
    insights['peak_hour_count'] = int(hourly.max())

    # 5. High value transaction rate
    high_value_count = df['is_high_value'].sum()
    insights['high_value_transactions'] = int(high_value_count)
    insights['high_value_percentage'] = round(
        (high_value_count / len(df)) * 100, 2
    )

    # 6. Top spending users
    top_users = df.groupby('user_id')['amount'].sum().nlargest(5).round(2)
    insights['top_5_users'] = top_users.to_dict()

    return insights

def print_report(insights):
    print("\n" + "="*50)
    print("DATAPULSE ANALYTICS REPORT")
    print("="*50)
    print(f"Total Transactions : {insights['total_transactions']}")
    print(f"Total Volume       : ₹{insights['total_volume']:,.2f}")
    print(f"Average Transaction: ₹{insights['average_transaction']:,.2f}")
    print(f"Peak Hour          : {insights['peak_hour']}:00")
    print(f"High Value Txns    : {insights['high_value_transactions']} ({insights['high_value_percentage']}%)")
    print("\nTop 5 Users by Spend:")
    for user, amount in insights['top_5_users'].items():
        print(f"  {user}: ₹{amount:,.2f}")
    print("="*50)

if __name__ == '__main__':
    df = pd.read_csv('processed_transactions.csv')
    df['is_high_value'] = df['amount'] > 10000
    insights = generate_insights(df)
    print_report(insights)