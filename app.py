from flask import Flask, render_template, jsonify
import os
import pandas as pd
import json
import config
from sqlalchemy import create_engine
import requests

app = Flask(__name__)

@app.route("/")
def index():
    payload = requests.get("http://127.0.0.1:5000/api/v1.0/hbo-data").json()
    data = dict(payload)
    return render_template("base/index.html", data_for_front_end=data)


@app.route("/api/v1.0/hbo-data")
def justice_league():
    # Establish the PostgreSQL connection
    connection_string = f"{config.POSTGRES_UN}:{config.POSTGRES_PW}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB_NAME}"
    engine = create_engine(f'postgresql://{connection_string}')
    
    return jsonify(json.loads(pd.read_sql_query("SELECT * FROM hbo_final_data ORDER BY imdbvotes LIMIT 5", con=engine).to_json()))

@app.route("/api/v1.0/hbo-data/actors")
def actors_league():
    # Establish the PostgreSQL connection
    connection_string = f"{config.POSTGRES_UN}:{config.POSTGRES_PW}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB_NAME}"
    engine = create_engine(f'postgresql://{connection_string}')
    
    return jsonify(json.loads(pd.read_sql_query("SELECT actors FROM hbo_final_data ORDER BY imdbvotes LIMIT 5", con=engine).to_json()))


if __name__ == "__main__":
    app.run(debug=True)