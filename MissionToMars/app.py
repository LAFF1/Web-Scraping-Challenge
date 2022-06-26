#-----------------------------------------------
# MongoDB and Flask Application
#-----------------------------------------------

# Dependencies and Setup
from flask import Flask, render_template, redirect
from flask.helpers import url_for
import pymongo
import scrape

#-----------------------------------------------
# Flask Setup
#-----------------------------------------------
app = Flask(__name__)

#-----------------------------------------------
# PyMongo Connection Setup
#-----------------------------------------------
conn = "mongodb://localhost:27017"
mongo = pymongo.MongoClient(conn)
db = mongo.mars

#-----------------------------------------------
# Flask Routes
#-----------------------------------------------

# Home Route to query MongoDB & Pass Mars Data Into HTML Template
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Scrape Route call scrape function(s)
@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = scrape.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect(url_for('index'))

# Define Main Behavior
if __name__ == "__main__":
    app.run()