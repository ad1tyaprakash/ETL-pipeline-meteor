import sqlite3

def load_to_db(df, table="meteorites"):
    conn = sqlite3.connect("etl.db")
    df.to_sql(table, conn, if_exists="replace", index=False)
    conn.close()
    print("Loaded to database:", table)