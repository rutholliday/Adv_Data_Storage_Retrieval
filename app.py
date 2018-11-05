import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Base.classes.keys()
# make reference to table
Measurement = Base.classes.measurement
Station = Base.classes.station

# session wrapper
session = Session(engine)

# Flask Setup
app = FlaskAPI(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/dates<br/>"
        f"/api/v1.0/temperature"

@app.route("/api/v1.0/precipitation")
def preciptation:
 """ Query for the dates and temperature observations from the last year.""" 
    results = session.query(Measurement.date, Measurement.temperature).all()

    # Convert the query results to a Dictionary using date as the key and tobs as the value.
    all_results = list(np.Measurement(results))
    # Return the JSON representation of your dictionary.
    return jsonify(all_results)

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for passenger in results:
        passenger_dict = {}
        passenger_dict["name"] = passenger.name
        passenger_dict["age"] = passenger.age
        passenger_dict["sex"] = passenger.sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)


# /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations:
    # Return a JSON list of stations from the dataset.
    return

# /api/v1.0/tobs
# Return a JSON list of Temperature Observations (tobs) 
# for the previous year.


# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average 
# temperature, and the max temperature for a given start or 
# start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX
# for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN,TAVG,
# and TMAX for dates between the start and end date inclusive.

# Hints
# You will need to join the station and measurement tables
# for some of the analysis queries.
# Use Flask jsonify to convert your API data into a valid 
# JSON response object.

