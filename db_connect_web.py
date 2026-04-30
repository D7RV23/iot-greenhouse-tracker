import os
import io
import base64
from flask import Flask, render_template
import psycopg2
from dotenv import load_dotenv
from GreenhouseGraph import create_greenhouse_graph

load_dotenv()
flask_app = Flask(__name__)

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

@flask_app.route('/')
def index():
    data = get_data()
    
    fig = create_greenhouse_graph(data)

    # Convert plot to PNG image for HTML
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html', graph=graph_url, temp=data[0][0], hum=data[0][1])