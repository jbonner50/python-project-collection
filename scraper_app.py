# amazon_scraper_app.py

from flask import Flask, jsonify
from scraping import scrape

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(Products=scrape())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
