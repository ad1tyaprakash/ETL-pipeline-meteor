import os
import sqlite3

DB_PATH = "data/processed/meteorites.db"


def load_to_db(df, table="meteorites"):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(table, conn, if_exists="replace", index=False)
    conn.close()
    print("Loaded to database:", table)