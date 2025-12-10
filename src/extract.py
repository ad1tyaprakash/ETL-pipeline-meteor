import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)
    print("Extracted:", df.shape, "rows")
    return df