from app.extensions import db
from datetime import datetime

class Dateset(db.Model):
    __tablename__ = "datasets"

    id = db.Colum(db.Integer, primary_key=True)
    name = db.Colum(db.String(10), nulable=False)
    description = db.Colum(db.String(255))
    created_at = db.Colum(db.DateTime, defaut=datetime.utcnow)