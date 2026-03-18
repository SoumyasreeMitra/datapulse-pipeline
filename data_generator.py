import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_transactions(n=1000):
    """
    Simulates a large-scale financial transaction dataset.
    Mimics real-world banking transaction data pipelines.
    """
    categories = ['Food', 'Transport', 'Shopping', 'Healthcare', 
                  'Entertainment', 'Utilities', 'Education', 'Travel']
    
    statuses = ['success', 'failed', 'pending']
    cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Pune', 'Chennai']

    data = []
    start_date = datetime(2024, 1, 1)

    for i in range(n):
        transaction = {
            'transaction_id': f'TXN{str(i+1).zfill(6)}',
            'user_id': f'USR{random.randint(1, 100):03d}',
            'amount': round(random.uniform(10, 50000), 2),
            'category': random.choice(categories),
            'status': random.choices(statuses, weights=[85, 10, 5])[0],
            'city': random.choice(cities),
            'timestamp': start_date + timedelta(
                days=random.randint(0, 364),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            )
        }
        data.append(transaction)

    df = pd.DataFrame(data)
    df.to_csv('transactions.csv', index=False)
    print(f"Generated {n} transactions -> transactions.csv")
    return df

if __name__ == '__main__':
    generate_transactions(1000)