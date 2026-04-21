import os
import time
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    time.sleep(5) # wait for the database to be ready
    return psycopg2.connect(
        dbname=os.getenv("DBNAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )

if __name__ == "__main__":
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                print("Connection successful!")
                # Testing retrieval from your dht11_data table
                cur.execute("SELECT * FROM dht11_data LIMIT 1;")
                row = cur.fetchone()
                print("Latest Sensor Reading:", row)
    except Exception as e:
        print("Connection failed:", e)
