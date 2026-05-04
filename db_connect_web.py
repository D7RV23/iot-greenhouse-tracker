import os
import io
import base64
import psycopg2
from dotenv import load_dotenv
from GreenhouseGraph import create_greenhouse_graph

load_dotenv()

def get_data():
    # Connect to db and get temperature and humidity data every 24 hours
    conn = psycopg2.connect(
        dbname=os.getenv("DBNAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )
    cur = conn.cursor()
    # (1440 minutes = 24 hours)
    cur.execute("SELECT temperature, humidity FROM dht11_data ORDER BY created_at DESC LIMIT 1440;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows # Return list of tuples (temp, hum)

def update_website():
    data = get_data() 
    
    fig = create_greenhouse_graph(data)
    
    # convert graph to base64 string
    img = io.BytesIO() 
    fig.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    
    with open("index.html", "r") as f:
        template = f.read()

    final_html = template.replace("{{TEMP}}", str(data[0][0]))
    final_html = template.replace("{{HUM}}", str(data[0][1]))
    final_html = template.replace("{{GRAPH_BASE64}}", graph_url)

    # push to apache
    with open("/var/www/html/index.html", "w") as f:
        f.write(final_html)

if __name__ == "__main__":
    update_website()
    print("Website updated successfully.")