from divvy_api import app, db

import os 

from flask import render_template, jsonify

from divvy_api.models import Trip, trip_schema

from datetime import datetime

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ave_duration/<starttime>/<endtime>', methods = ['GET'])
def get_ave_duration(starttime, endtime):
    starttimed = datetime.strptime(starttime, "%m/%j/%y %H:%M").time()
    endtimed = datetime.strptime(endtime, "%m/%j/%y %H:%M").time()
    trip = Trip.query.filter_by(starttime > starttimed, endtime < endtimed).all()
    trip_mean = sum(trip) / len(trip)
    response = trip_schema.dump(trip_mean)
    return jsonify(response)
