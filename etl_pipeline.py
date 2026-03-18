import pandas as pd
import numpy as np

def extract(filepath='transactions.csv'):
    """
    EXTRACT: Load raw transaction data from CSV source.
    In production this would connect to a data warehouse or Kafka stream.
    """
    print("Extracting data...")
    df = pd.read_csv(filepath)
    print(f"Extracted {len(df)} records")
    return df

def transform(df):
    """
    TRANSFORM: Clean, validate and enrich the raw data.
    """
    print("Transforming data...")

    # 1. Parse timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # 2. Extract time features
    df['month'] = df['timestamp'].dt.month
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['hour'] = df['timestamp'].dt.hour

    # 3. Remove failed transactions for analytics
    df_clean = df[df['status'] == 'success'].copy()

    # 4. Flag high-value transactions
    df_clean['is_high_value'] = df_clean['amount'] > 10000

    # 5. Normalize amount (min-max scaling)
    min_amt = df_clean['amount'].min()
    max_amt = df_clean['amount'].max()
    df_clean['amount_normalized'] = (df_clean['amount'] - min_amt) / (max_amt - min_amt)

    print(f"Transformed: {len(df_clean)} valid records after cleaning")
    return df_clean

def load(df, output_path='processed_transactions.csv'):
    """
    LOAD: Store processed data to output sink.
    In production this would load into a data warehouse like Redshift or BigQuery.
    """
    print("Loading processed data...")
    df.to_csv(output_path, index=False)
    print(f"Loaded {len(df)} records -> {output_path}")
    return output_path

def run_pipeline():
    """
    Orchestrates the full ETL pipeline.
    """
    print("=" * 50)
    print("DataPulse ETL Pipeline Starting...")
    print("=" * 50)
    raw_df = extract()
    clean_df = transform(raw_df)
    load(clean_df)
    print("=" * 50)
    print("Pipeline completed successfully!")
    print("=" * 50)
    return clean_df

if __name__ == '__main__':
    run_pipeline()