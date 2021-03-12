from divvy_api import app, db, ma
from datetime import datetime

class Trip(db.Model):
    trip_id = db.Column(db.Integer, primary_key = True)
    starttime = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    stoptime = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    bikeid = db.Column(db.Integer, nullable = False, default=0)
    from_station_id = db.Column(db.Integer, nullable = False, default=0)
    from_station_name = db.Column(db.String(150), nullable = False, default = '')
    to_station_id = db.Column(db.Integer, nullable = False, default = 0)
    to_station_name = db.Column(db.String(150), nullable = False, default='')
    user_type = db.Column(db.String(150), nullable = False, default='')
    gender = db.Column(db.String(150), nullable = True, default='')
    birthday = db.Column(db.String(150), nullable = True, default='')
    trip_duration = db.Column(db.Integer, nullable = False, default = 0)

    def __init__(self,starttime,stoptime,bikeid,from_station_id,from_station_name,
                 to_station_id,to_station_name, user_type, gender, birthday, trip_duration):
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.user_type = user_type
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration

    def __repr__(self):
        return self.current_alias

    def to_dict(self):
        return {
            "trip_id": self.trip_id,
            "starttime": self.starttime,
            "stoptime": self.stoptime,
            "bikeid": self.bikeid,
            "from_station_id": self.from_station_id,
            "from_station_name": self.from_station_name,
            "to_station_id": self.to_station_id,
            "to_station_name": self.to_station_name,
            "user_type": self.user_type,
            "gender": self.gender,
            "birthday": self.birthday,
            "trip_duration": self.trip_duration,
        }

class TripSchema(ma.Schema):
    class Meta:
        fields = ['trip_id', 'starttime', 'stoptime', 'bikeid', 'from_station_id', 'from_station_name', 
            'to_station_id', 'to_station_name', 'user_type', 'gender', 'birthday', 'trip_duration']

trip_schema = TripSchema()
