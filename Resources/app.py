# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def index():
    return "Hello, world!"

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

#Precipitation#####################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all precipitation in the last year
    lastDate = session.query(measurement.date).order_by(measurement.date.desc()).first()
    preYear = dt.datetime.strptime(lastDate,'%Y-%m-%d').date() - dt.timedelta(365)
    results = session.query(measurement.date,measurement.prcp).\
    filter(measurement.date >= preYear).order_by(measurement.date).all()     

    session.close()


    # Create a dictionary from the row data and append to a list of dates within last year
    lyear_precipitation = []
    for precipitation in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict.append(precipitation_dict)


    return jsonify(precipitation_dict)

#@app.route("/precipitation_jsonified")
#def precipitation_jsonified():
#    return jsonify(prep_dict)




@app.route("/about")
def about():
    name = "Hanbin"
    location = "Zerose Heart"

    return f"My name is {name}, and I live in {location}."


@app.route("/contact")
def contact():
    email = "peleke@example.com"

    return f"Questions? Comments? Complaints? Shoot an email to {email}."

@app.route("/")
def welcome():
    return (
        f"Welcome to the Justice League API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league"
    )

# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)

