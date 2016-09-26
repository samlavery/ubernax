from app import db
from sqlalchemy.dialects.postgresql import JSON

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    provider_id = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    event_received = db.Column(db.Integer)
    event_began    = db.Column(db.Integer)
    status         = db.Column(db.String)
    last_update    = db.Column(db.Integer)

    def __init__(self, user_id, provider_id, latitude, longitude, event_received, event_began, last_update):
        self.user_id = user_id
        self.provider_id = provider_id
        self.latitude = latitude
        self.longitude = longitude
        self.event_received = event_received
        self.event_began = event_began
        self.status = status
        self.last_update = last_update

    def __repr__(self):
        return '<id {}>'.format(self.id)
