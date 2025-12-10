import pandas as pd
import numpy as np

def clean_data(df):
    df.columns = [c.lower().strip() for c in df.columns]
    df['mass'] = pd.to_numeric(df['mass'], errors='coerce')
    df['reclat'] = pd.to_numeric(df['reclat'], errors='coerce')
    df['reclong'] = pd.to_numeric(df['reclong'], errors='coerce')
    df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
    df.loc[df['year'] > 2025, 'year'] = None
    df = df.dropna(subset=['reclat', 'reclong'])
    df = df.drop_duplicates(subset=['name'])
    print("After cleaning:", df.shape, "rows")
    return df