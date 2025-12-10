from extract import extract_data
from transform import clean_data
from load import load_to_db

RAW_PATH = "data/raw/meteorite.csv"

def run_pipeline():
    df = extract_data(RAW_PATH)
    df = clean_data(df)
    load_to_db(df)

if __name__ == "__main__":
    run_pipeline()