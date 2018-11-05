from flask_api import FlaskAPI
app = FlaskAPI(__name__)

# Routes
# /api/v1.0/precipitation
# Query for the dates and temperature observations from the last year.
# Convert the query results to a Dictionary using date as the key and 
# tobs as the value.
# Return the JSON representation of your dictionary.

# /api/v1.0/stations
# Return a JSON list of stations from the dataset.

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

@app.route("/")
def home():
    