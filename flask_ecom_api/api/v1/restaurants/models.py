from flask_ecom_api import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(length=140),
        index=True,
        unique=True,
        nullable=False,
    )
    address = db.Column(db.String(length=140), index=True, unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    contact_phone = db.Column(db.String(10))
